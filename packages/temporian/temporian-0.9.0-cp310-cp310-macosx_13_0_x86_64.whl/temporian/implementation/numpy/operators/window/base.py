# Copyright 2021 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import abstractmethod
import logging
from typing import Dict, Optional, List, Any, Union

import numpy as np
from temporian.core.data.duration_utils import NormalizedDuration

from temporian.core.operators.window.base import BaseWindowOperator
from temporian.implementation.numpy.data.event_set import IndexData
from temporian.implementation.numpy.data.event_set import (
    EventSet,
)
from temporian.implementation.numpy.operators.base import OperatorImplementation
from temporian.implementation.numpy.data.dtype_normalization import (
    tp_dtype_to_np_dtype,
)


class BaseWindowNumpyImplementation(OperatorImplementation):
    """Interface definition and common logic for numpy implementation of
    window operators."""

    def __init__(self, operator: BaseWindowOperator) -> None:
        super().__init__(operator)
        assert isinstance(operator, BaseWindowOperator)

    def __call__(
        self,
        input: EventSet,
        sampling: Optional[EventSet] = None,
        window_length: Optional[EventSet] = None,
    ) -> Dict[str, EventSet]:
        assert isinstance(self.operator, BaseWindowOperator)

        # pick effective sampling
        effective_sampling = input
        if self.operator.has_variable_winlen:
            assert window_length is not None
            effective_sampling = window_length
        elif self.operator.has_sampling:
            assert sampling is not None
            effective_sampling = sampling

        # check that sampling isn't the input's, in which case we don't pass it
        # to cpp impl to use the more efficient sampling-less version
        has_sampling = (
            effective_sampling.node().sampling_node
            is not input.node().sampling_node
        )

        # create destination evset
        output_schema = self.operator.outputs["output"].schema
        output_evset = EventSet(data={}, schema=output_schema)

        # For each index
        for index_key, sampling_data in effective_sampling.data.items():
            output_data = IndexData(
                features=[],
                timestamps=sampling_data.timestamps,
                schema=None,  # Checking is done later
            )

            if window_length is not None:
                effective_window_length = window_length.data[
                    index_key
                ].features[0]
                # Warn if not all window length values are positive
                if not np.all(effective_window_length > 0):
                    logging.warning(
                        "`window_length`'s values should be strictly"
                        " positive. 0, NaN and negative window lengths will"
                        " output missing values."
                    )
            else:
                assert self.operator.window_length is not None
                effective_window_length = self.operator.window_length

            sampling_timestamps = (
                sampling_data.timestamps if has_sampling else None
            )

            if index_key in input.data:
                input_data = input.data[index_key]

                self._compute(
                    src_timestamps=input_data.timestamps,
                    src_features=input_data.features,
                    sampling_timestamps=sampling_timestamps,
                    dst_features=output_data.features,
                    window_length=effective_window_length,
                )
            else:
                # Sets the feature data as missing.
                empty_features = [
                    np.empty((0,), dtype=tp_dtype_to_np_dtype(f.dtype))
                    for f in output_schema.features
                ]
                empty_timestamps = np.empty((0,), dtype=np.float64)
                self._compute(
                    src_timestamps=empty_timestamps,
                    src_features=empty_features,
                    sampling_timestamps=sampling_timestamps,
                    dst_features=output_data.features,
                    window_length=effective_window_length,
                )

            output_data.check_schema(output_schema)
            output_evset.set_index_value(
                index_key, output_data, normalize=False
            )

        return {"output": output_evset}

    @abstractmethod
    def _implementation(self) -> Any:
        pass

    def _compute(
        self,
        src_timestamps: np.ndarray,
        src_features: List[np.ndarray],
        sampling_timestamps: Optional[np.ndarray],
        dst_features: List[np.ndarray],
        window_length: Union[NormalizedDuration, np.ndarray],
    ) -> None:
        assert isinstance(self.operator, BaseWindowOperator)

        implementation = self._implementation()
        for src_ts in src_features:
            kwargs = {
                "evset_timestamps": src_timestamps,
                "evset_values": src_ts,
                "window_length": window_length,
            }
            if sampling_timestamps is not None:
                kwargs["sampling_timestamps"] = sampling_timestamps
            dst_feature = implementation(**kwargs)
            dst_features.append(dst_feature)

    def apply_feature_wise(
        self,
        src_timestamps: np.ndarray,
        src_feature: np.ndarray,
        feature_idx: int,
    ) -> np.ndarray:
        """Applies the operator on a single feature."""
        assert isinstance(self.operator, BaseWindowOperator)

        implementation = self._implementation()
        kwargs = {
            "evset_timestamps": src_timestamps,
            "evset_values": src_feature,
            "window_length": self.operator.window_length,
        }
        return implementation(**kwargs)

    def apply_feature_wise_with_sampling(
        self,
        src_timestamps: Optional[np.ndarray],
        src_feature: Optional[np.ndarray],
        sampling_timestamps: np.ndarray,
        feature_idx: int,
    ) -> np.ndarray:
        """Applies the operator on a single feature with a sampling."""

        assert isinstance(self.operator, BaseWindowOperator)
        implementation = self._implementation()

        if src_feature is not None:
            kwargs = {
                "evset_timestamps": src_timestamps,
                "evset_values": src_feature,
                "window_length": self.operator.window_length,
                "sampling_timestamps": sampling_timestamps,
            }
            return implementation(**kwargs)
        else:
            # Sets the feature data as missing.
            output_schema = self.operator.outputs["output"].schema
            output_dtype = output_schema.features[feature_idx].dtype
            empty_features = np.empty(
                (0,), dtype=tp_dtype_to_np_dtype(output_dtype)
            )
            empty_timestamps = np.empty((0,), dtype=np.float64)
            kwargs = {
                "evset_timestamps": empty_timestamps,
                "evset_values": empty_features,
                "window_length": self.operator.window_length,
                "sampling_timestamps": sampling_timestamps,
            }
            return implementation(**kwargs)
