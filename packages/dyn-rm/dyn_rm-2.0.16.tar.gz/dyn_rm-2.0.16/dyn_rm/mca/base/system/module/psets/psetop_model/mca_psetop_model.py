from dyn_rm.mca.base.graph.module.edge_model import MCAEdgeModelModule

class MCAPSetOpModelModule(MCAEdgeModelModule):
    def __init__(self, parent = None, parent_dir = ".", verbosity = 0, enable_output = False):
        super().__init__(parent = parent, parent_dir = parent_dir, verbosity = verbosity, enable_output = enable_output)