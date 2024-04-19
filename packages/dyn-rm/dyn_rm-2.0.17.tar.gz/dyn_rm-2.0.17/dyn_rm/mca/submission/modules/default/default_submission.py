from dyn_rm.mca.base.submission.module import MCASubmissionModule

from dyn_rm.mca.base.event_loop.component import MCAEventLoopComponent
#from dyn_rm.mca.components.base.system.system import MCASystemComponent
#from dyn_rm.mca.components.base.set_model import MCASetModelComponent
#from dyn_rm.mca.components.base.setop_model import MCASetopModelComponent
from dyn_rm.mca.event_loop.modules.asyncio import AsyncioEventLoopModule
#from dyn_rm.mca.modules.setop_model.add.default import DefaultAddModel
#from dyn_rm.mca.modules.set_model import *


from dyn_rm.util.constants import *
from dyn_rm.util.functions import *


import asyncio
#import yaml

class DefaultSubmissionModule(MCASubmissionModule):

    def __init__(self, parent=None, parent_dir=".", verbosity=0, enable_output=False):
        super().__init__(parent, parent_dir, verbosity, enable_output)
        self.event_loop = MCAEventLoopComponent()
        self.event_loop.register_module(AsyncioEventLoopModule())
    
    '''
    def submit_object_function(self, object_file, system, params):
        object = None
        with open(object_file, "r") as stream:
            try:
                object = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                return DYNRM_ERR_BAD_PARAM
        print(object)
        node = [node for node in object["graph"]["nodes"].values()][0]
        job_id = MCASystemComponent.generate_new_job_id(),
        setop_id = MCASystemComponent.generate_new_setop_id()

        setop = MCASystemComponent.create_setop(
            setop_id,
            job_id,
            MCASystemComponent.SetOp.OP_ADD,
            [""],
            [],
            None,
            None,
            DefaultAddModel,
            None,
            {"input0" : NullSetModel, "output0": globals()[node["model_name"]]},
            {"output0": node["model_params"]},
            {"input0" : MCASetModelComponent.SetState(0, {"nodes": []}, None, {"executable": node["cmd"]})},
            {"output0" : MCASetopModelComponent.SetStateSpace(contraints = node["constraints"], mappings = node["mappings"])},
            verbosity=5
        )

        system.add_setop(setop)

        job = MCASystemComponent.Job(job_id, [],[],[""],setop_id)

        system.add_job(job)

        return DYNRM_MCA_SUCCESS

    
    def submit_mix_function(self, mix_file, system, params, loop_name):
        with open(mix_file, "r") as stream:
            try:
                object = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                return DYNRM_ERR_BAD_PARAM
        
        for submission in object["submissions"]:
            self.event_loop.call_soon_threadsafe(self.event_loop.call_later, submission["arrival"], self.run_service, "SUBMIT", "OBJECT", submission["object"],  system, params, loop_name)
        
        return DYNRM_MCA_SUCCESS
    '''
