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

from temporian.core import graph
from temporian.core.test import utils


class GraphTest(absltest.TestCase):
    def setUp(self):
        utils.register_test_operators()

    def tearDown(self):
        utils.unregister_test_operators()

    def test_infer_graph_no_names(self):
        """Lists all the objects in a graph."""

        i1 = utils.create_input_node()
        o2 = utils.OpI1O1(i1)
        i3 = utils.create_input_node()
        o4 = utils.OpI2O1(o2.outputs["output"], i3)
        o5 = utils.OpI1O2(o4.outputs["output"])
        output_1 = o5.outputs["output_1"]
        output_2 = o4.outputs["output"]

        g = graph.infer_graph({i1, i3}, {output_1, output_2})

        self.assertLen(g.operators, 3)
        self.assertLen(g.samplings, 3)
        self.assertLen(g.nodes, 6)
        self.assertLen(g.features, 10)
        self.assertSetEqual(g.inputs, {i1, i3})
        self.assertSetEqual(g.outputs, {output_1, output_2})
        self.assertIsNone(g.named_inputs)
        self.assertIsNone(g.named_outputs)

        with self.assertRaisesRegex(ValueError, "All the input nodes and only"):
            g.set_input_node_names({"io_input_1": i1})

        with self.assertRaisesRegex(ValueError, "All the input nodes and only"):
            g.set_input_node_names(
                {"io_input_1": o2.outputs["output"], "io_input_2": i3}
            )

        g.set_input_node_names({"io_input_1": i1, "io_input_2": i3})
        g.set_output_node_names(
            {"io_output_1": output_1, "io_output_2": output_2}
        )

    def test_infer_graph_with_names(self):
        """Lists all the objects in a graph."""

        i1 = utils.create_input_node()
        o2 = utils.OpI1O1(i1)
        i3 = utils.create_input_node()
        o4 = utils.OpI2O1(o2.outputs["output"], i3)
        o5 = utils.OpI1O2(o4.outputs["output"])
        output_1 = o5.outputs["output_1"]
        output_2 = o4.outputs["output"]

        g = graph.infer_graph_named_nodes(
            {"io_input_1": i1, "io_input_2": i3},
            {"io_output_1": output_1, "io_output_2": output_2},
        )

        self.assertLen(g.operators, 3)
        self.assertLen(g.samplings, 3)
        self.assertLen(g.nodes, 6)
        self.assertLen(g.features, 10)
        self.assertSetEqual(g.inputs, {i1, i3})
        self.assertSetEqual(g.outputs, {output_1, output_2})
        g.set_input_node_names({"io_input_1": i1, "io_input_2": i3})
        g.set_output_node_names(
            {"io_output_1": output_1, "io_output_2": output_2}
        )

    def test_infer_graph_with_node_names(self):
        """Lists all the objects in a graph."""

        i1 = utils.create_input_node("io_input_1")
        o2 = utils.OpI1O1(i1)
        i3 = utils.create_input_node("io_input_2")
        o4 = utils.OpI2O1(o2.outputs["output"], i3)
        o5 = utils.OpI1O2(o4.outputs["output"])
        output_1 = o5.outputs["output_1"]
        output_2 = o4.outputs["output"]
        output_1.name = "io_output_1"
        output_2.name = "io_output_2"

        g = graph.infer_graph_named_nodes([i1, i3], [output_1, output_2])

        self.assertLen(g.operators, 3)
        self.assertLen(g.samplings, 3)
        self.assertLen(g.nodes, 6)
        self.assertLen(g.features, 10)
        self.assertSetEqual(g.inputs, {i1, i3})
        self.assertSetEqual(g.outputs, {output_1, output_2})
        g.set_input_node_names({"io_input_1": i1, "io_input_2": i3})
        g.set_output_node_names(
            {"io_output_1": output_1, "io_output_2": output_2}
        )

    def test_infer_graph_noop(self):
        """With an opt that just passes features."""

        a = utils.create_input_node()
        b = utils.OpI1O1NotCreator(a)
        c = utils.OpI1O1(b.outputs["output"])

        g = graph.infer_graph({a}, {c.outputs["output"]})

        self.assertLen(g.operators, 2)
        self.assertLen(g.samplings, 2)
        self.assertLen(g.nodes, 3)
        self.assertLen(g.features, 4)

    def test_infer_graph_input_is_not_feature_creator(self):
        """When the user input is not the feature creator."""

        a = utils.create_input_node()
        b = utils.OpI1O1NotCreator(a)
        c = utils.OpI1O1(b.outputs["output"])

        g = graph.infer_graph(
            {b.outputs["output"]},
            {c.outputs["output"]},
        )

        self.assertLen(g.operators, 1)
        self.assertLen(g.samplings, 2)
        self.assertLen(g.nodes, 2)
        self.assertLen(g.features, 4)

    def test_infer_graph_missing_input(self):
        """The input is missing."""

        i = utils.create_input_node("missing_node")
        o2 = utils.OpI1O1(i)

        with self.assertRaisesRegex(ValueError, " but not provided as input"):
            graph.infer_graph(set(), {o2.outputs["output"]})

    def test_infer_graph_automatic_input(self):
        """Infer automatically the input."""

        i1 = utils.create_input_node()
        i1.name = "io_input_1"
        o2 = utils.OpI1O1(i1)
        i3 = utils.create_input_node()
        i3.name = "io_input_2"
        o4 = utils.OpI2O1(o2.outputs["output"], i3)
        o5 = utils.OpI1O2(o4.outputs["output"])

        g = graph.infer_graph(
            None,
            {o5.outputs["output_1"], o4.outputs["output"]},
        )

        self.assertLen(g.operators, 3)
        self.assertLen(g.samplings, 3)
        self.assertLen(g.nodes, 6)
        self.assertLen(g.features, 10)

    def test_automatic_input_equality_graph(self):
        """Automated inference when the input is the same as the output."""

        i1 = utils.create_input_node()
        g = graph.infer_graph(None, {i1})

        self.assertLen(g.operators, 0)
        self.assertLen(g.nodes, 1)
        self.assertLen(g.samplings, 1)
        self.assertLen(g.inputs, 1)
        self.assertLen(g.outputs, 1)
        self.assertEqual(g.inputs, g.outputs)

    def test_apply_on_inputs(self):
        """Ensures applying a graph on inputs works and doesn't cause repeated
        ordered internal op ids when infer_graph is called again on the outputs.
        """
        i1 = utils.create_input_node("io_input_1")
        o2 = utils.OpI1O1(i1)
        i3 = utils.create_input_node("io_input_2")
        o4 = utils.OpI2O1(o2.outputs["output"], i3)
        o5 = utils.OpI1O2(o4.outputs["output"])

        output_1 = o5.outputs["output_1"]
        output_2 = o4.outputs["output"]
        output_1.name = "io_output_1"
        output_2.name = "io_output_2"

        g = graph.infer_graph_named_nodes([i1, i3], [output_1, output_2])

        # Apply same graph again to its own outputs
        outputs = g.apply_on_inputs(
            {"io_input_1": output_1, "io_input_2": output_2}
        )
        new_output_1 = outputs["io_output_1"]
        new_output_2 = outputs["io_output_2"]
        new_g = graph.infer_graph_named_nodes(
            [i1, i3], [new_output_1, new_output_2]
        )

        self.assertLen(new_g.operators, 6)
        self.assertLen(new_g.nodes, 10)  # 6 in the original graph + 4
        # 2 in inputs + 2 * OpI101 which creates a new one
        self.assertLen(new_g.samplings, 4)
        # 4 in inputs + 2 created by each operator
        self.assertLen(new_g.features, 16)

        self.assertSetEqual(new_g.inputs, {i1, i3})
        self.assertSetEqual(new_g.outputs, {new_output_1, new_output_2})

        internal_ids = [op._internal_ordered_id for op in new_g.operators]
        self.assertEqual(len(internal_ids), len(set(internal_ids)))


if __name__ == "__main__":
    absltest.main()
