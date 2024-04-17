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

import numpy as np
from absl.testing import absltest

from temporian.implementation.numpy.data.io import event_set

from temporian.test.utils import f32, f64, assertOperatorResult


class ArithmeticTest(absltest.TestCase):
    """Test arithmetic operators between two event-sets
    using a two-level index and disordered rows."""

    def setUp(self):
        # 2 index columns, 2 feature columns (float64 and float32)
        self.evset_1 = event_set(
            timestamps=[0, 1, 2, 1, 1, 2, 0, 1],
            features={
                "store_id": [1, 1, 1, 1, 2, 2, 2, 2],
                "product_id": [1, 1, 1, 2, 2, 2, 3, 3],
                "f1": f64([-14.0, 15.0, 16.0, 10.0, 0.0, 8.0, 3.0, 4.0]),
                "f2": f32([1.0, 2.0, 3, 4, 5, 6, 7, 8]),
            },
            indexes=["store_id", "product_id"],
        )

        # 2 index columns, 2 feature columns (float64 and float32)
        self.evset_2 = event_set(
            timestamps=[0, 1, 2, 1, 1, 2, 0, 1],
            features={
                "store_id": [1, 1, 1, 1, 2, 2, 2, 2],
                "product_id": [1, 1, 1, 2, 2, 2, 3, 3],
                "f3": f64([4.5, -5.5, 16, 0, 3, -8, 3, 5]),
                "f4": f32([5, 3, 1, 2, -8, 2, 4, 3]),
            },
            indexes=["store_id", "product_id"],
            same_sampling_as=self.evset_1,
        )

    def test_addition(self) -> None:
        # Expected result after addition
        expected_evset = event_set(
            timestamps=[0, 1, 2, 1, 1, 2, 0, 1],
            features={
                "store_id": [1, 1, 1, 1, 2, 2, 2, 2],
                "product_id": [1, 1, 1, 2, 2, 2, 3, 3],
                "f1": f64([-9.5, 9.5, 32, 10, 3, 0, 6, 9]),
                "f2": f32([6, 5, 4, 6, -3, 8, 11, 11]),
            },
            indexes=["store_id", "product_id"],
            same_sampling_as=self.evset_1,
        )
        assertOperatorResult(self, self.evset_1 + self.evset_2, expected_evset)

    def test_subtraction(self) -> None:
        expected_evset = event_set(
            timestamps=[0, 1, 2, 1, 1, 2, 0, 1],
            features={
                "store_id": [1, 1, 1, 1, 2, 2, 2, 2],
                "product_id": [1, 1, 1, 2, 2, 2, 3, 3],
                "f1": f64([-18.5, 20.5, 0, 10, -3, 16, 0, -1]),
                "f2": f32([-4, -1, 2, 2, 13, 4, 3, 5]),
            },
            indexes=["store_id", "product_id"],
            same_sampling_as=self.evset_1,
        )
        assertOperatorResult(self, self.evset_1 - self.evset_2, expected_evset)

    def test_multiplication(self) -> None:
        expected_evset = event_set(
            timestamps=[0, 1, 2, 1, 1, 2, 0, 1],
            features={
                "store_id": [1, 1, 1, 1, 2, 2, 2, 2],
                "product_id": [1, 1, 1, 2, 2, 2, 3, 3],
                "f1": f64([-63, -82.5, 256, 0, 0, -64, 9, 20]),
                "f2": f32([5, 6, 3, 8, -40, 12, 28, 24]),
            },
            indexes=["store_id", "product_id"],
            same_sampling_as=self.evset_1,
        )
        assertOperatorResult(self, self.evset_1 * self.evset_2, expected_evset)

    def test_division(self) -> None:
        expected_evset = event_set(
            timestamps=[0, 1, 2, 1, 1, 2, 0, 1],
            features={
                "store_id": [1, 1, 1, 1, 2, 2, 2, 2],
                "product_id": [1, 1, 1, 2, 2, 2, 3, 3],
                "f1": f64([-14 / 4.5, -15 / 5.5, 1, np.inf, 0, -1, 1, 0.8]),
                "f2": f32([0.2, 2 / 3, 3, 2, -0.625, 3, 1.75, 8 / 3]),
            },
            indexes=["store_id", "product_id"],
            same_sampling_as=self.evset_1,
        )
        assertOperatorResult(self, self.evset_1 / self.evset_2, expected_evset)

    def test_floordiv(self) -> None:
        expected_evset = event_set(
            timestamps=[0, 1, 2, 1, 1, 2, 0, 1],
            features={
                "store_id": [1, 1, 1, 1, 2, 2, 2, 2],
                "product_id": [1, 1, 1, 2, 2, 2, 3, 3],
                "f1": f64([-4, -3, 1, np.inf, 0, -1, 1, 0]),
                "f2": f32([0, 0, 3, 2, -1, 3, 1, 2]),
            },
            indexes=["store_id", "product_id"],
            same_sampling_as=self.evset_1,
        )
        assertOperatorResult(self, self.evset_1 // self.evset_2, expected_evset)

    def test_noindex_unsorted(self) -> None:
        evset_1 = event_set(
            timestamps=[2, 1, 0, 3],
            features={
                "f1": [2, 1, 0, 3],
                "f2": [20, 10, 0, 30],
            },
        )
        evset_2 = event_set(
            timestamps=[3, 2, 1, 0],
            features={
                "f2": [30, 20, 10, 0],
                "f1": [-3, -2, -1, 0],
            },
            same_sampling_as=evset_1,
        )
        expected = event_set(
            timestamps=[0, 1, 2, 3],
            features={
                "f1": [0, 11, 22, 33],
                "f2": [0, 9, 18, 27],
            },
            same_sampling_as=evset_1,
        )
        assertOperatorResult(self, evset_1 + evset_2, expected)


if __name__ == "__main__":
    absltest.main()
