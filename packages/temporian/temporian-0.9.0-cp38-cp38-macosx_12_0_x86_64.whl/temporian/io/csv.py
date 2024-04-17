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

"""Utilities for reading and saving EventSets from/to disk."""

from typing import List, Optional
from temporian.implementation.numpy.data.event_set import EventSet
from temporian.io.pandas import from_pandas, to_pandas
from temporian.utils.typecheck import typecheck


@typecheck
def from_csv(
    path: str,
    timestamps: str = "timestamp",
    indexes: Optional[List[str]] = None,
    sep: str = ",",
) -> EventSet:
    """Reads an [`EventSet`][temporian.EventSet] from a CSV file.

    Example:
        ```python
        >>> # Example CSV
        >>> temp_file = str(tmp_dir / "temporal_data.csv")
        >>> _ = open(temp_file, "w").write(
        ...     "date,feature_1,feature_2\n"
        ...     "2023-01-01,10.0,3.0\n"
        ...     "2023-01-02,20.0,4.0\n"
        ...     "2023-02-01,30.0,5.0"
        ... )
        >>> # Load CSV
        >>> evset = tp.from_csv(temp_file, timestamps="date")
        >>> evset
        indexes: []
        features: [('feature_1', float64), ('feature_2', float64)]
        events:
            (3 events):
                timestamps: ['2023-01-01T00:00:00' '2023-01-02T00:00:00'
                             '2023-02-01T00:00:00']
                'feature_1': [10. 20. 30.]
                'feature_2': [3. 4. 5.]
        ...

        ```

    Args:
        path: Path to the file.
        timestamps: Name of the column to be used as timestamps for the
            EventSet.
        indexes: Names of the columns to be used as indexes for the EventSet.
            If None, a flat EventSet will be created.
        sep: Separator to use.

    Returns:
        EventSet read from file.
    """

    import pandas as pd

    if indexes is None:
        indexes = []

    df = pd.read_csv(path, sep=sep)
    return from_pandas(df, indexes=indexes, timestamps=timestamps)


@typecheck
def to_csv(
    evset: EventSet,
    path: str,
    sep: str = ",",
    na_rep: Optional[str] = None,
    columns: Optional[List[str]] = None,
):
    """Saves an [`EventSet`][temporian.EventSet] to a CSV file.

    Example:
        ```python
        >>> output_path = str(tmp_dir / "output_data.csv")
        >>> evset = tp.event_set(timestamps=[1,], features={"f1": [0.1]})
        >>> tp.to_csv(evset, output_path)

        ```

    Args:
        evset: EventSet to save.
        path: Path to the file.
        sep: Separator to use.
        na_rep: Representation to use for missing values.
        columns: Columns to save. If `None`, saves all columns.
    """
    df = to_pandas(evset)
    df.to_csv(path, index=False, sep=sep, na_rep=na_rep, columns=columns)
