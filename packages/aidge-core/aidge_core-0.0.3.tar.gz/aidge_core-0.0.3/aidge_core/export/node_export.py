import aidge_core

from abc import ABC, abstractmethod


class ExportNode(ABC):
    """Abstract class to interface node with export generation.
    """

    @abstractmethod
    def __init__(self, aidge_node: aidge_core.Node) -> None:
        """Create ExportNode and retieve attirubtes from ``aidge_node``:

        - name: aidge Node name
        - attributes: dictionnary of attributes of the aidge Operator linked to the node, attributes name follow aidge naming convention
        - parameters: List of parameters node, order in the list is the same as the one defined by the aidge operator

        """
        super().__init__()
        self.node = aidge_node
        self.operator = aidge_node.get_operator()
        self.name = self.node.name()
        self.attributes = {} # Attributes are auto fetched from aidge operators
        if isinstance(self.operator, aidge_core.Attributes):
            for attr_name in self.operator.get_attrs_name():
                self.attributes[attr_name] = self.operator.get_attr(attr_name)

        # rename is_leaf ?
        self.is_last = len(self.node.get_children()) == 0


        self.inputs = []
        self.outputs = []
        self.inputs_dims = []
        self.outputs_dims = []

        for idx, parent_node in enumerate(self.node.get_parents()):
            self.inputs.append(parent_node)
            if parent_node is not None:
                self.inputs_dims.append(self.operator.get_input(idx).dims())
            else:
                print(self.operator.get_input(idx))
                if self.operator.get_input(idx) is not None:
                    self.inputs_dims.append(self.operator.get_input(idx).dims())
                else:
                    self.inputs_dims.append(None)

        for idx, child_node in enumerate(self.node.get_children()):
            self.outputs.append(child_node)

        # Dirty hot fix, change it quickly
        self.outputs_dims.append(self.operator.get_output(0).dims())

    @abstractmethod
    def export(self, export_folder:str, list_configs:list):
        """Define how to export the node definition.
        """
        pass

    @abstractmethod
    def forward(self, list_actions:list):
        """Define how to generate code to perform a forward pass.
        """
        pass

