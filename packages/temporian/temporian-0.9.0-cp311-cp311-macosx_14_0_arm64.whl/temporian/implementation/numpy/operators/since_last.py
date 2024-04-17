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

from typing import Dict, Optional

import numpy as np

from temporian.core.operators.since_last import SinceLast
from temporian.implementation.numpy import implementation_lib
from temporian.implementation.numpy.data.event_set import IndexData, EventSet
from temporian.implementation.numpy.operators.base import OperatorImplementation
from temporian.implementation.numpy_cc.operators import operators_cc


class SinceLastNumpyImplementation(OperatorImplementation):
    """Numpy implementation of the since last operator."""

    def __init__(self, operator: SinceLast) -> None:
        super().__init__(operator)
        assert isinstance(operator, SinceLast)

    def __call__(
        self, input: EventSet, sampling: Optional[EventSet] = None
    ) -> Dict[str, EventSet]:
        assert isinstance(self.operator, SinceLast)

        assert self.operator.has_sampling == (sampling is not None)
        steps = self.operator.steps

        output_schema = self.output_schema("output")
        output_evset = EventSet(data={}, schema=output_schema)

        for index_key, index_data in input.data.items():
            if sampling is not None:
                sampling_timestamps = sampling.data[index_key].timestamps
                feature_values = operators_cc.since_last(
                    index_data.timestamps, sampling_timestamps, steps
                )
                output_evset.set_index_value(
                    index_key,
                    IndexData(
                        [feature_values],
                        sampling_timestamps,
                        schema=output_schema,
                    ),
                    normalize=False,
                )
            else:
                t = index_data.timestamps
                diffs = np.full_like(t, np.nan)
                diffs[steps:] = t[steps:] - t[:-steps]  # ok if steps >= len(t)
                output_evset.set_index_value(
                    index_key,
                    IndexData(
                        [diffs],
                        index_data.timestamps,
                        schema=output_schema,
                    ),
                    normalize=False,
                )

        return {"output": output_evset}


implementation_lib.register_operator_implementation(
    SinceLast, SinceLastNumpyImplementation
)
