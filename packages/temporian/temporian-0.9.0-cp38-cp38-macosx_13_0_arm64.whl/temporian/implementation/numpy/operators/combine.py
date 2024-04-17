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


"""Implementation for the Combine operator."""


from typing import Dict, List
import numpy as np

from temporian.implementation.numpy.data.event_set import (
    IndexData,
    EventSet,
)
from temporian.core.operators.combine import Combine
from temporian.core.operators.combine import How
from temporian.implementation.numpy import implementation_lib
from temporian.implementation.numpy.operators.base import OperatorImplementation


class CombineNumpyImplementation(OperatorImplementation):
    def __init__(self, operator: Combine) -> None:
        assert isinstance(operator, Combine)
        super().__init__(operator)

    def __call__(self, **inputs: EventSet) -> Dict[str, EventSet]:
        assert isinstance(self.operator, Combine)
        output_schema = self.output_schema("output")
        output_evset = EventSet(data={}, schema=output_schema)
        how = self.operator.how

        input_evsets = list(inputs.values())
        first_input = input_evsets[0]
        first_features = first_input.schema.feature_names()

        # What index values to use
        if how == How.left:
            combined_keys = first_input.data.keys()
        elif how == How.outer:
            combined_keys = set()
            for evset in input_evsets:
                combined_keys |= set(evset.data.keys())
        elif how == How.inner:
            combined_keys = set(first_input.data.keys())
            for evset in input_evsets[1:]:
                combined_keys &= set(evset.data.keys())
        else:
            raise ValueError(f"Unknown parameter for combine: {how=}")

        # Concatenate timestamps and features for each index, and sort
        for index_key in combined_keys:
            all_timestamps: List[np.ndarray] = []
            # Outer list contains each feature, inner list each evset
            all_feats: List[List[np.ndarray]] = [[] for _ in first_features]

            # Get timestamps and features from all input EventSets
            for evset in input_evsets:
                if index_key not in evset.data:
                    continue
                index_data = evset.get_index_value(index_key, normalize=False)
                all_timestamps.append(index_data.timestamps)

                # Find features by name and put them in the right position
                source_feats = evset.schema.feature_names()
                for target_idx, feat in enumerate(first_features):
                    source_idx = source_feats.index(feat)
                    all_feats[target_idx].append(
                        index_data.features[source_idx]
                    )

            # Concatenate and sort timestamps
            timestamps: np.ndarray = np.concatenate(all_timestamps)
            time_position = np.argsort(timestamps, kind="mergesort")
            timestamps = timestamps[time_position]

            # Concatenate features and sort based on timestamps
            features: List[np.ndarray] = []
            for idx in range(len(first_features)):
                feat = np.concatenate(all_feats[idx])
                features.append(feat[time_position])

            # Fill IndexData
            output_evset.set_index_value(
                index_key,
                IndexData(
                    features=features,
                    timestamps=timestamps,
                    schema=output_schema,
                ),
                normalize=False,
            )

        return {"output": output_evset}


implementation_lib.register_operator_implementation(
    Combine, CombineNumpyImplementation
)
