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

"""Prefix operator class and public API function definition."""

from temporian.core import operator_lib
from temporian.core.compilation import compile
from temporian.core.data.node import (
    EventSetNode,
    create_node_new_features_existing_sampling,
)
from temporian.core.operators.base import Operator
from temporian.core.typing import EventSetOrNode
from temporian.proto import core_pb2 as pb


class Prefix(Operator):
    def __init__(
        self,
        input: EventSetNode,
        prefix: str,
    ):
        super().__init__()

        self.add_attribute("prefix", prefix)
        self.add_input("input", input)

        # TODO: When supported, re-use existing feature instead of creating a
        # new one.

        self.add_output(
            "output",
            create_node_new_features_existing_sampling(
                features=[
                    (prefix + f.name, f.dtype) for f in input.schema.features
                ],
                sampling_node=input,
                creator=self,
            ),
        )
        self.check()

    @property
    def prefix(self):
        return self.attributes["prefix"]

    @classmethod
    def build_op_definition(cls) -> pb.OperatorDef:
        return pb.OperatorDef(
            key="PREFIX",
            attributes=[
                pb.OperatorDef.Attribute(
                    key="prefix",
                    type=pb.OperatorDef.Attribute.Type.STRING,
                )
            ],
            inputs=[pb.OperatorDef.Input(key="input")],
            outputs=[pb.OperatorDef.Output(key="output")],
        )


operator_lib.register_operator(Prefix)


@compile
def prefix(
    input: EventSetOrNode,
    prefix: str,
) -> EventSetOrNode:
    assert isinstance(input, EventSetNode)

    return Prefix(input=input, prefix=prefix).outputs["output"]
