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

import re
from functools import partial
import os
import pydoc
import tempfile
from typing import Dict

from absl import logging
from absl.testing import absltest
import temporian as tp
from temporian.core import serialization
from temporian.core import graph
from temporian.core.data.dtype import DType
from temporian.core.test import utils
from temporian.core.typing import EventSetOrNode
from temporian.implementation.numpy.data.io import event_set


class SerializationTest(absltest.TestCase):
    def setUp(self):
        utils.register_test_operators()
        self.evset = tp.event_set(
            timestamps=[1, 2, 3],
            features={
                "x": [1.0, 2.0, 3.0],
                "y": [4.0, 5.0, 6.0],
            },
        )

    def tearDown(self):
        utils.unregister_test_operators()

    def test_serialize(self):
        i1 = utils.create_input_node()
        o2 = utils.OpI1O1(i1)
        i3 = utils.create_input_node()
        o4 = utils.OpI2O1(o2.outputs["output"], i3)
        o5 = utils.OpI1O2(o4.outputs["output"])

        original = graph.infer_graph_named_nodes(
            {"io_input_1": i1, "io_input_2": i3},
            {
                "io_output_1": o5.outputs["output_1"],
                "io_output_2": o4.outputs["output"],
            },
        )
        logging.info("original:\n%s", original)

        proto = serialization._serialize(original)
        logging.info("proto:\n%s", proto)

        restored = serialization._unserialize(proto)
        logging.info("restored:\n%s", restored)

        self.assertEqual(len(original.samplings), len(restored.samplings))
        self.assertEqual(len(original.features), len(restored.features))
        self.assertEqual(len(original.operators), len(restored.operators))
        self.assertEqual(len(original.nodes), len(restored.nodes))
        self.assertEqual(
            original.named_inputs.keys(), restored.named_inputs.keys()
        )
        self.assertEqual(
            original.named_outputs.keys(), restored.named_outputs.keys()
        )
        # TODO: Deep equality tests.

        # Ensures that "original" and "restored" don't link to the same objects.
        self.assertFalse(
            serialization._all_identifiers(original.samplings)
            & serialization._all_identifiers(restored.samplings)
        )
        self.assertFalse(
            serialization._all_identifiers(original.features)
            & serialization._all_identifiers(restored.features)
        )
        self.assertFalse(
            serialization._all_identifiers(original.operators)
            & serialization._all_identifiers(restored.operators)
        )
        self.assertFalse(
            serialization._all_identifiers(original.nodes)
            & serialization._all_identifiers(restored.nodes)
        )
        self.assertFalse(
            serialization._all_identifiers(original.named_inputs.values())
            & serialization._all_identifiers(restored.named_inputs.values())
        )
        self.assertFalse(
            serialization._all_identifiers(original.named_outputs.values())
            & serialization._all_identifiers(restored.named_outputs.values())
        )

    def test_serialize_with_key_prefix(self):
        i1 = utils.create_simple_input_node()
        i2 = utils.create_simple_input_node()
        i3 = utils.create_simple_input_node()
        o2 = utils.OpMultiIO1(input_1=i1, input_2=i2, input_3=i3)

        original = graph.infer_graph_named_nodes(
            {"io_input_1": i1, "io_input_2": i2, "io_input_3": i3},
            {"io_output": o2.outputs["output"]},
        )
        logging.info("original:\n%s", original)

        proto = serialization._serialize(original)
        logging.info("proto:\n%s", proto)

        restored = serialization._unserialize(proto)
        logging.info("restored:\n%s", restored)

        self.assertEqual(len(original.samplings), len(restored.samplings))
        self.assertEqual(len(original.features), len(restored.features))
        self.assertEqual(len(original.operators), len(restored.operators))
        self.assertEqual(len(original.nodes), len(restored.nodes))
        self.assertEqual(
            original.named_inputs.keys(), restored.named_inputs.keys()
        )
        self.assertEqual(
            original.named_outputs.keys(), restored.named_outputs.keys()
        )
        # TODO: Deep equality tests.

        # Ensures that "original" and "restored" don't link to the same objects.
        self.assertFalse(
            serialization._all_identifiers(original.samplings)
            & serialization._all_identifiers(restored.samplings)
        )
        self.assertFalse(
            serialization._all_identifiers(original.features)
            & serialization._all_identifiers(restored.features)
        )
        self.assertFalse(
            serialization._all_identifiers(original.operators)
            & serialization._all_identifiers(restored.operators)
        )
        self.assertFalse(
            serialization._all_identifiers(original.nodes)
            & serialization._all_identifiers(restored.nodes)
        )
        self.assertFalse(
            serialization._all_identifiers(original.named_inputs.values())
            & serialization._all_identifiers(restored.named_inputs.values())
        )
        self.assertFalse(
            serialization._all_identifiers(original.named_outputs.values())
            & serialization._all_identifiers(restored.named_outputs.values())
        )

    def test_serialize_autonode(self):
        input_data = event_set(
            timestamps=[1, 2, 3, 4],
            features={
                "f1": [5, 6, 7, 8],
                "x": [1, 1, 2, 2],
            },
            indexes=["x"],
        )

        input_node = input_data.node()
        output_node = input_node.moving_sum(2.0)

        original = graph.infer_graph_named_nodes(
            {"i": input_node},
            {"o": output_node},
        )
        logging.info("original:\n%s", original)

        proto = serialization._serialize(original)
        logging.info("proto:\n%s", proto)

        restored = serialization._unserialize(proto)
        logging.info("restored:\n%s", restored)

    def test_serialize_attributes(self):
        """Test serialization with different types of operator attributes."""
        attributes = {
            "attr_int": 1,
            "attr_str": "hello",
            "attr_list": ["temporian", "rocks"],
            "attr_float": 5.0,
            "attr_bool": True,
            "attr_map": {"good": "bye", "nice": "to", "meet": "you"},
            "attr_list_dtypes": [DType.FLOAT32, DType.STRING],
        }
        i_event = utils.create_input_node()
        operator = utils.OpWithAttributes(i_event, **attributes)

        original = graph.infer_graph_named_nodes(
            inputs={"i_event": i_event},
            outputs={"output": operator.outputs["output"]},
        )
        logging.info("original:\n%s", original)

        proto = serialization._serialize(original)
        logging.info("proto:\n%s", proto)

        restored = serialization._unserialize(proto)
        logging.info("restored:\n%s", restored)

        self.assertEqual(len(original.operators), len(restored.operators))
        self.assertEqual(
            original.named_inputs.keys(), restored.named_inputs.keys()
        )
        self.assertEqual(
            original.named_outputs.keys(), restored.named_outputs.keys()
        )

        # Check all restored attributes for the only operator
        restored_attributes = list(restored.operators)[0].attributes
        for attr_name, attr_value in attributes.items():
            self.assertEqual(attr_value, restored_attributes[attr_name])

        self.assertFalse(
            serialization._all_identifiers(original.operators)
            & serialization._all_identifiers(restored.operators)
        )
        self.assertFalse(
            serialization._all_identifiers(original.named_inputs.values())
            & serialization._all_identifiers(restored.named_inputs.values())
        )
        self.assertFalse(
            serialization._all_identifiers(original.named_outputs.values())
            & serialization._all_identifiers(restored.named_outputs.values())
        )

    def test_save_graph_and_load_graph(self):
        input_node = self.evset.node()
        x = input_node
        x = x.cast(float)
        x = x["x"]
        x = 2 * x
        output_node = x

        result = tp.run(output_node, {input_node: self.evset})

        with tempfile.TemporaryDirectory() as tempdir:
            path = os.path.join(tempdir, "my_graph.tem")
            tp.save_graph(
                inputs={"a": input_node}, outputs={"b": output_node}, path=path
            )
            loaded_inputs, loaded_outputs = tp.load_graph(
                path=path, squeeze=True
            )

        loaded_results = tp.run(loaded_outputs, {loaded_inputs: self.evset})

        self.assertEqual(result, loaded_results)

    def test_save(self):
        @tp.compile
        def f(x: EventSetOrNode) -> Dict[str, EventSetOrNode]:
            return {"output": x.prefix("a_")}

        result = f(self.evset)

        with tempfile.TemporaryDirectory() as tempdir:
            path = os.path.join(tempdir, "my_fn.tem")
            tp.save(f, path, x=self.evset)
            inputs, outputs = tp.load_graph(path=path)

        self.assertEqual(list(inputs.keys()), ["x"])
        self.assertEqual(list(outputs.keys()), ["output"])

        loaded_result = tp.run(outputs, {inputs["x"]: self.evset})

        self.assertEqual(result, loaded_result)

    def test_save_and_load_node_input(self):
        @tp.compile
        def f(x: EventSetOrNode):
            return {"output": x.prefix("a_")}

        node = self.evset.node()
        result = tp.run(f(node), {node: self.evset})

        with tempfile.TemporaryDirectory() as tempdir:
            path = os.path.join(tempdir, "my_fn.tem")
            tp.save(f, path, x=node)
            inputs, outputs = tp.load_graph(path=path)

        loaded_result = tp.run(outputs, {inputs["x"]: self.evset})

        self.assertEqual(result, loaded_result)

    def test_save_and_load_schema_input(self):
        @tp.compile
        def f(x: EventSetOrNode):
            return {"output": x.prefix("a_")}

        result = f(self.evset)

        with tempfile.TemporaryDirectory() as tempdir:
            path = os.path.join(tempdir, "my_fn.tem")
            tp.save(f, path, x=self.evset.schema)
            inputs, outputs = tp.load_graph(path=path)

        loaded_result = tp.run(outputs, {inputs["x"]: self.evset})

        self.assertEqual(result, loaded_result)

    def test_save_and_load_many_inputs(self):
        @tp.compile
        def f(x: EventSetOrNode, y: EventSetOrNode, z: EventSetOrNode):
            return {"output": tp.glue(x, y, z)}

        x = tp.event_set(
            timestamps=[1.0, 2.0, 3.0],
            features={"f1": [100.0, 200.0, 300.0]},
        )
        y = tp.event_set(
            timestamps=[1.0, 2.0, 3.0],
            features={"f2": [1.0, 2.0, 3.0]},
            same_sampling_as=x,
        )
        z = tp.event_set(
            timestamps=[1.0, 2.0, 3.0],
            features={"f3": [3.0, 5.0, 2.0]},
            same_sampling_as=x,
        )
        result = f(x, y, z)

        with tempfile.TemporaryDirectory() as tempdir:
            path = os.path.join(tempdir, "my_fn.tem")
            tp.save(f, path, x, y, z=z)
            inputs, outputs = tp.load_graph(path=path)

        self.assertEqual(list(inputs.keys()), ["x", "y", "z"])

        loaded_result = tp.run(
            outputs, {inputs["x"]: x, inputs["y"]: y, inputs["z"]: z}
        )

        self.assertEqual(result, loaded_result)

    def test_save_not_compiled(self):
        def f(x: EventSetOrNode):
            return {"output": x.prefix("a_")}

        with tempfile.TemporaryDirectory() as tempdir:
            path = os.path.join(tempdir, "my_fn.tem")
            with self.assertRaisesRegex(
                ValueError, "Can only save a function that has been compiled"
            ):
                tp.save(f, path, x=self.evset)

    def test_save_wrong_input_types(self):
        def f(x: EventSetOrNode, y: int):
            return {"output": x.prefix("a_")}

        setattr(f, "is_tp_compiled", True)  # hack to pass compiled check

        with tempfile.TemporaryDirectory() as tempdir:
            path = os.path.join(tempdir, "my_fn.tem")
            with self.assertRaisesRegex(
                ValueError, "The function's parameters can only be"
            ):
                tp.save(f, path, self.evset, 3)

    def test_load(self):
        @tp.compile
        def f(x: EventSetOrNode) -> Dict[str, EventSetOrNode]:
            return {"output": x.prefix("a_")}

        result = f(self.evset)

        with tempfile.TemporaryDirectory() as tempdir:
            path = os.path.join(tempdir, "my_fn.tem")
            tp.save(f, path, x=self.evset)
            loaded_f = tp.load(path=path)

        loaded_result = loaded_f(x=self.evset)

        self.assertEqual(result, loaded_result)

    def test_load_use_twice(self):
        """Tests that the loaded fn can be used more than once, since the graph
        is only loaded once but used on each call."""

        @tp.compile
        def f(x: EventSetOrNode):
            return {"output": x.prefix("a_")}

        other_evset = tp.event_set(
            timestamps=[1, 2, 3],
            features={
                "x": [10.0, 20.0, 30.0],
                "y": [40.0, 50.0, 60.0],
            },
        )

        result = f(self.evset)
        other_result = f(other_evset)

        with tempfile.TemporaryDirectory() as tempdir:
            path = os.path.join(tempdir, "my_fn.tem")
            tp.save(f, path, x=self.evset)
            loaded_f = tp.load(path=path)

        loaded_result = loaded_f(x=self.evset)
        loaded_other_result = loaded_f(x=other_evset)

        self.assertEqual(result, loaded_result)
        self.assertEqual(other_result, loaded_other_result)

    def test_load_many_kwargs(self):
        @tp.compile
        def f(x: EventSetOrNode, y: EventSetOrNode, z: EventSetOrNode):
            return {"output": tp.glue(x, y, z)}

        x = tp.event_set(
            timestamps=[1.0, 2.0, 3.0],
            features={"f1": [100.0, 200.0, 300.0]},
        )
        y = tp.event_set(
            timestamps=[1.0, 2.0, 3.0],
            features={"f2": [1.0, 2.0, 3.0]},
            same_sampling_as=x,
        )
        z = tp.event_set(
            timestamps=[1.0, 2.0, 3.0],
            features={"f3": [3.0, 5.0, 2.0]},
            same_sampling_as=x,
        )

        result = f(x, y, z)

        with tempfile.TemporaryDirectory() as tempdir:
            path = os.path.join(tempdir, "my_fn.tem")
            tp.save(f, path, x=x, y=y, z=z)
            loaded_f = tp.load(path=path)

        loaded_result = loaded_f(x=x, y=y, z=z)

        self.assertEqual(result, loaded_result)

    def test_load_args_and_kwargs(self):
        @tp.compile
        def f(x: EventSetOrNode, y: EventSetOrNode, z: EventSetOrNode):
            return {"output": tp.glue(x, y, z)}

        x = tp.event_set(
            timestamps=[1.0, 2.0, 3.0],
            features={"f1": [100.0, 200.0, 300.0]},
        )
        y = tp.event_set(
            timestamps=[1.0, 2.0, 3.0],
            features={"f2": [1.0, 2.0, 3.0]},
            same_sampling_as=x,
        )
        z = tp.event_set(
            timestamps=[1.0, 2.0, 3.0],
            features={"f3": [3.0, 5.0, 2.0]},
            same_sampling_as=x,
        )

        result = f(x, y, z)

        with tempfile.TemporaryDirectory() as tempdir:
            path = os.path.join(tempdir, "my_fn.tem")
            tp.save(f, path, x=x, y=y, z=z)
            loaded_f = tp.load(path=path)

        loaded_result = loaded_f(x, y, z)

        self.assertEqual(result, loaded_result)

    def test_load_signature(self):
        """Checks that help(loaded_f) shows the correct param spec."""

        @tp.compile
        def f(x: EventSetOrNode, y: EventSetOrNode, z: EventSetOrNode):
            return {"output": x.prefix("a_")}

        with tempfile.TemporaryDirectory() as tempdir:
            path = os.path.join(tempdir, "my_fn.tem")
            tp.save(f, path, x=self.evset, y=self.evset, z=self.evset)
            loaded_f = tp.load(path=path)

        doc = pydoc.render_doc(loaded_f)
        self.assertIsNotNone(
            re.search(r"x: \S*temporian\.core\.data\.node\.EventSetNode", doc)
        )
        self.assertIsNotNone(
            re.search(r"y: \S*temporian\.core\.data\.node\.EventSetNode", doc)
        )
        self.assertIsNotNone(
            re.search(r"z: \S*temporian\.core\.data\.node\.EventSetNode", doc)
        )
        self.assertIsNotNone(
            re.search(
                r"-> Dict[str, \S*temporian.core.data.node.EventSetNode]", doc
            )
        )

    def test_save_function_composition(self):
        @tp.compile
        def f(x: EventSetOrNode):
            return {"output": x.prefix("f_")}

        @tp.compile
        def g(x: EventSetOrNode):
            return {"output": x.prefix("g_")}

        @tp.compile
        def h(x: EventSetOrNode):
            return f(g(x)["output"])

        result = h(self.evset)

        with tempfile.TemporaryDirectory() as tempdir:
            path = os.path.join(tempdir, "my_fn.tem")
            tp.save(h, path, x=self.evset)
            loaded_f = tp.load(path=path)

        loaded_result = loaded_f(self.evset)

        self.assertEqual(result, loaded_result)

    def test_save_partial_function(self):
        @tp.compile
        def f(x: EventSetOrNode, b: bool):
            if b:
                return {"output": x.prefix("true_")}
            else:
                return {"output": x.prefix("false_")}

        result = f(self.evset, b=True)
        self.assertEqual(result["output"].schema.feature_names()[0], "true_x")

        with tempfile.TemporaryDirectory() as tempdir:
            path = os.path.join(tempdir, "my_fn.tem")
            tp.save(tp.compile(partial(f, b=True)), path, x=self.evset)
            loaded_f = tp.load(path=path)

        loaded_result = loaded_f(self.evset)

        self.assertEqual(result, loaded_result)

        result = f(self.evset, b=False)
        self.assertEqual(result["output"].schema.feature_names()[0], "false_x")

        with tempfile.TemporaryDirectory() as tempdir:
            path = os.path.join(tempdir, "my_fn.tem")
            tp.save(tp.compile(partial(f, b=False)), path, x=self.evset)
            loaded_f = tp.load(path=path)

        loaded_result = loaded_f(self.evset)

        self.assertEqual(result, loaded_result)

    def test_save_recursive_function(self):
        @tp.compile
        def f(x: EventSetOrNode, n: int):
            if n > 0:
                return f(x.prefix(f"{n}_"), n=n - 1)
            else:
                return {"output": x}

        result = f(self.evset, n=5)
        self.assertEqual(
            result["output"].schema.feature_names()[0], "1_2_3_4_5_x"
        )

        with tempfile.TemporaryDirectory() as tempdir:
            path = os.path.join(tempdir, "my_fn.tem")
            tp.save(tp.compile(partial(f, n=5)), path, x=self.evset)
            loaded_f = tp.load(path=path)

        loaded_result = loaded_f(self.evset)

        self.assertEqual(result, loaded_result)


if __name__ == "__main__":
    absltest.main()
