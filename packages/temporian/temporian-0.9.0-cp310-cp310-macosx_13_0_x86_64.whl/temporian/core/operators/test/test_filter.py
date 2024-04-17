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

from absl.testing import absltest
from absl.testing.parameterized import TestCase

from temporian.implementation.numpy.data.io import event_set
from temporian.test.utils import assertOperatorResult


class FilterTest(TestCase):
    def test_basic(self):
        evset = event_set(
            timestamps=[1, 2, 3], features={"x": [4, 5, 6], "y": [7, 8, 9]}
        )
        condition = event_set(
            timestamps=[1, 2, 3],
            features={"c": [True, True, False]},
            same_sampling_as=evset,
        )

        result = evset.filter(condition)

        expected = event_set(
            timestamps=[1, 2],
            features={"x": [4, 5], "y": [7, 8]},
        )

        assertOperatorResult(self, result, expected, check_sampling=False)

    def test_no_condition(self):
        evset = event_set([0, 1, 2], features={"cond": [True, False, True]})

        result = evset.filter()

        expected = event_set([0, 2], features={"cond": [True, True]})

        assertOperatorResult(self, result, expected, check_sampling=False)

    def test_condition_many_features(self):
        evset = event_set([])
        condition = event_set(
            [], features={"a": [], "b": []}, same_sampling_as=evset
        )
        with self.assertRaisesRegex(
            ValueError, "Condition must be a single feature. Got"
        ):
            evset.filter(condition)

    def test_condition_not_boolean(self):
        evset = event_set([])
        condition = event_set([0], features={"a": [3]}, same_sampling_as=evset)
        with self.assertRaisesRegex(
            ValueError, "Condition must be a boolean feature. Got"
        ):
            evset.filter(condition)


if __name__ == "__main__":
    absltest.main()
