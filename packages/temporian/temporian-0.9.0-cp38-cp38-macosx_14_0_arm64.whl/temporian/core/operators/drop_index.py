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

"""Drop index operator class and public API function definition."""

from typing import List, Optional, Union

from temporian.core import operator_lib
from temporian.core.compilation import compile
from temporian.core.data.node import (
    EventSetNode,
    create_node_new_features_new_sampling,
)
from temporian.core.data.schema import FeatureSchema, IndexSchema
from temporian.core.operators.base import Operator
from temporian.core.typing import EventSetOrNode
from temporian.proto import core_pb2 as pb


class DropIndexOperator(Operator):
    def __init__(
        self,
        input: EventSetNode,
        indexes: List[str],
        keep: bool,
    ) -> None:
        super().__init__()

        # `indexes`` is the list of indexes in `input` to drop. If
        # `keep` is true, those indexes will be converted into features.
        self._indexes = indexes
        self._keep = keep

        self.add_input("input", input)
        self.add_attribute("indexes", indexes)
        self.add_attribute("keep", keep)

        self._output_feature_schemas = self._get_output_feature_schemas(
            input, indexes, keep
        )

        output_indexes = [
            index_level
            for index_level in input.schema.indexes
            if index_level.name not in indexes
        ]

        self.add_output(
            "output",
            create_node_new_features_new_sampling(
                features=self._output_feature_schemas,
                indexes=output_indexes,
                is_unix_timestamp=input.schema.is_unix_timestamp,
                creator=self,
            ),
        )
        self.check()

    def _get_output_feature_schemas(
        self, input: EventSetNode, indexes: List[str], keep: bool
    ) -> List[FeatureSchema]:
        if not keep:
            return input.schema.features

        index_dict = input.schema.index_name_to_dtype()

        new_features: List[FeatureSchema] = []
        for index in indexes:
            new_features.append(
                FeatureSchema(name=index, dtype=index_dict[index])
            )

        # Note: The new features are added after the existing features.
        return input.schema.features + new_features

    @property
    def output_feature_schemas(self) -> List[FeatureSchema]:
        return self._output_feature_schemas

    @property
    def indexes(self) -> List[str]:
        return self._indexes

    @property
    def keep(self) -> bool:
        return self._keep

    @classmethod
    def build_op_definition(cls) -> pb.OperatorDef:
        return pb.OperatorDef(
            key="DROP_INDEX",
            attributes=[
                pb.OperatorDef.Attribute(
                    key="indexes",
                    type=pb.OperatorDef.Attribute.Type.LIST_STRING,
                ),
                pb.OperatorDef.Attribute(
                    key="keep",
                    type=pb.OperatorDef.Attribute.Type.BOOL,
                ),
            ],
            inputs=[pb.OperatorDef.Input(key="input")],
            outputs=[pb.OperatorDef.Output(key="output")],
        )


operator_lib.register_operator(DropIndexOperator)


def _normalize_indexes(
    input: EventSetNode,
    indexes: Optional[Union[List[str], str]],
) -> List[str]:
    if indexes is None:
        # Drop all the indexes
        return input.schema.index_names()

    if isinstance(indexes, str):
        indexes = [indexes]

    if len(indexes) == 0:
        raise ValueError("Cannot specify empty list as `indexes` argument.")

    # Check that requested indexes exist
    index_dict = input.schema.index_name_to_dtype()
    for index in indexes:
        if index not in index_dict:
            raise ValueError(
                f"{index} is not an index in {input.schema.indexes}."
            )

    return indexes


@compile
def drop_index(
    input: EventSetOrNode,
    indexes: Optional[Union[str, List[str]]] = None,
    keep: bool = True,
) -> EventSetOrNode:
    assert isinstance(input, EventSetNode)

    indexes = _normalize_indexes(input, indexes)
    return DropIndexOperator(input, indexes, keep).outputs["output"]
