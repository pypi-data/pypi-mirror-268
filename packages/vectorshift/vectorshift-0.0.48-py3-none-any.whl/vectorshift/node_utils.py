# functionality defining the shape and properties of computation nodes, and how
# they connect to each other in pipelines
from abc import ABC, abstractclassmethod
import json
import random
import re 
import string

from vectorshift.pipeline_data_types import *

# A parent class for all nodes. Shouldn't be initialized by the user directly.
# Each node subclasses NodeTemplate and takes in class-specific parameters 
# depending on what the node does. Node classes below are organized by their
# order and structure of appearance in the no-code editor.
class NodeTemplate(ABC):
    def __init__(self):
        # Each node has a certain type, also called an "ID" in Mongo. The _id
        # of the node is formed by appending a counter to the node type.
        self._id:str = None
        # The backend functionality executed by each node is given by three
        # string parameters stored in Mongo.
        self.node_type:str = None
        self.category:str = None 
        self.task_name:str = None
        # Every node has zero or more inputs or outputs. Each output itself 
        # is a list (in case one input takes in/aggregates multiple outputs).
        # In some cases, nodes may take in either NodeOutputs *or* strings as
        # inputs (e.g. for string parameters). In that case, the current 
        # pattern is to designate an additional dictionary self._input_strs.
        self._inputs:dict[str, list[NodeOutput]] = {}
        
    # Dump the JSON
    def __repr__(self): 
        return f'<{self.__class__.__name__} with JSON representation\n\
            {json.dumps(self.to_json_rep())}\n>'
    
    # Print the node in a style mimicking how you could construct the node
    # using the class. Indicate the ID in parentheses.
    def __str__(self):
        args_strs = self.init_args_strs(indicate_id=False)
        args_strs = [s for s in args_strs if s is not None]
        init_args_str = ',\n\t'.join(args_strs)
        return f'(node id {self._id})={self.__class__.__name__}(\n\
\t{init_args_str}\n)'
    
    # Essentially the same as __str__, but printed in such a way that it can
    # be run as Python code.
    def construction_strs(self):
        # the variable for the node is a snake case'd-version of the node ID
        var_name = (re.sub('(?!^)([A-Z]+)', r'_\1', self._id)) \
            .replace('-', '_').lower()
        # filter out Nones if any exist 
        args_strs = self.init_args_strs(indicate_id=False)
        args_strs = [s for s in args_strs if s is not None]
        init_args_str = ',\n\t'.join([
            s.replace('\n', '\\n') for s in args_strs
        ])
        return var_name, f'{self.__class__.__name__}(\n\
\t{init_args_str}\n)'
        
    def init_args_strs(self, indicate_id=False) -> list[str]: 
        raise NotImplementedError('Subclasses should implement this!')

    # Inputs are a dictionary of NodeOutputs keyed by input fields (the in-edge 
    # labels in the no-code graph/the target handle for the node's in-edge).
    def inputs(self) -> dict[str, list['NodeOutput']]: return self._inputs

    def set_input(self, input_name:str, input:'NodeOutput'):
        if input_name not in self._inputs.keys():
            # this shouldn't actually be reached currently, because missing 
            # inputs should cause the typechecker function to throw errors 
            print(f'WARNING: {input_name} not currently in node\'s inputs.')
        self._inputs[input_name] = input
    
    # Outputs should be a dictionary of NodeOutputs keyed by output fields (the
    # out-edge labels/the source handle for the node's out-edge). Invariant: 
    # a key should equal the corresponding value's output_field.
    # For syntactic sugar, class-specific methods can also return specific 
    # outputs rather than the entire dict, e.g. the method "output()" that 
    # directly gives the NodeOutput object for nodes that only have one output.
    def outputs(self) -> dict[str, 'NodeOutput']: 
        raise NotImplementedError('Subclasses should implement this!')

    # The dictionary that corresponds with the 'data' field in the JSON 
    # serialization of the node. Should return a subset of how a node object 
    # is stored as part of a pipeline in Mongo, specifically, the fields within 
    # the 'data' field specific to the node. 
    # Fields common to all nodes are inserted in to_json_rep.
    # For both _to_json_rep and to_json_rep, the 'generic' flag indicates 
    # whether or not to return a "generic" version of JSONs for user-created 
    # objects, e.g. IntegrationNodes, which have user-specific information
    # stripped. (On the no-code editor, this would provoke the user to setup.)
    @abstractclassmethod
    def _to_json_rep(self, generic:bool=False) -> dict:
        # If the node references a user-defined object that lives on the VS
        # platform (other pipelines, integrations, files, vectorstores,
        # transformations), calling this function will involve an API call
        # to get the details of that user-defined object.
        raise NotImplementedError('Subclasses should implement this!')
    
    # This should only be called after an id has been assigned to the node.
    def to_json_rep(self, generic:bool=False) -> dict: 
        json_data = self._to_json_rep(generic=generic) 
        return {
            'id': self._id, 
            'type': self.node_type, 
            'data': {
                'id': self._id, 
                'nodeType': self.node_type,
                'category': self.category, 
                'task_name': self.task_name,
                **json_data
            }
        }
    
    # From a Python dict representing how a node is stored in JSON, create a
    # node object. The json_data argument passed in here only contains the
    # fields within the 'data' field in the node's JSON representation 
    # (symmetric with the functionality of _to_json_rep).
    # IMPORTANTLY, this does NOT initialize the _inputs param with NodeOutput
    # values (and thus doesn't perform typechecks); we expect NodeOutputs to
    # be inserted post_hoc, and assume they're valid.
    @staticmethod
    @abstractclassmethod
    def _from_json_rep(json_data:dict) -> 'NodeTemplate':
        raise NotImplementedError('Subclasses should implement this!')
    
    @classmethod 
    def from_json_rep(cls, json_data: dict) -> 'NodeTemplate':
        n:NodeTemplate = cls._from_json_rep(json_data['data'])
        n._id = json_data['id']
        # Clear the dummy entries in _inputs
        n._inputs = {}
        return n

# A wrapper class for outputs from nodes, for basic "type"-checks and to figure
# out how nodes connect to each other. NOT the same as OutputNode, which is 
# a node that represents the final result of a pipeline.
class NodeOutput:
    def __init__(self, source:NodeTemplate, output_field:str, 
            output_data_type:PipelineDataType):
        # The Node object producing this output.
        self.source = source
        # The specific output field from the source node (the node handle).
        self.output_field = output_field
        # A string roughly corresponding to the output type. (Strings are 
        # flimsy, but they will do the job.)
        self.output_data_type = output_data_type

    def __repr__(self):
        return f'<NodeOutput of type {self.output_data_type} from \
            {self.source.__class__.__name__} (node id {self.source._id}), \
            output field {self.output_field}>'
    
    def __str__(self):
        return f'<NodeOutput {format_node_output(self)}>'

# indicate_id throughout this code is a flag determining how to format IDs.
# If set to True, the ID is in camelCase as stored in Mongo, and the text
# (node id ... ) is added. 
# If False, the id is in snake_case with hyphens replaced with underscores.
def format_node_output(output:NodeOutput, indicate_id:bool=True) -> str:
    id_str = f'(node id {output.source._id})' if indicate_id \
        else re.sub('(?!^)([A-Z]+)', r'_\1', output.source._id).replace('-', '_').lower()
    return f"{id_str}.outputs()['{output.output_field}']"

# Helper functions for printing out NodeOutput sources in init arg strings
def format_node_output_with_name (output_name:str, output:NodeOutput, indicate_id=False) -> str: 
    return f"{output_name}={format_node_output(output, indicate_id)}"

def format_node_output_dict (outputs:dict[str, list[NodeOutput]], indicate_id=False) -> str:
    d = {}
    for k, v in outputs.items():
        output_str = '['
        for o in v:
           output_str += f"{format_node_output(o, indicate_id)}, "
        if len(output_str) > 2:
            output_str = output_str[:-2]
        output_str += ']'
        d[k] = output_str
    return d.__str__().replace('"', '')

# Check the data type of an output. The output should either be a NodeOutput,
# in which case we check its output data type. Else it should be a string.
def check_type(name:str, output:str|NodeOutput, expected_t:PipelineDataType, str_ok:bool=False):
    if type(output) == NodeOutput:
        t = output.output_data_type
        if not t.intersects(expected_t):
            raise ValueError(f'Invalid input type to {name}: expected {expected_t}, got {t}')
        elif not t.is_subset(expected_t):
            print(f'WARNING: {name} received input type {t}, which may be incompatible with expected type {expected_t}')
        return
    else:
        if not str_ok:
            raise ValueError(f'Invalid input to {name}: Not a NodeOutput.')
        if type(output) != str:
            raise ValueError(f'Invalid input to {name}: Not a string or NodeOutput.')

# Helper function to extract text variables
def find_text_vars(text:str):
    text_var_instances = re.findall(r'\{\{([^{}]+)\}\}', text)
    text_var_instances = [v.strip() for v in text_var_instances]
    text_vars = []
    # remove duplicates while preserving order
    for v in text_var_instances:
        if v not in text_vars:
            text_vars.append(v)
    return text_vars

# Helper function to check text variables; ensures given_vars is a superset 
# of actual_vars
def check_text_vars(actual_vars:list[str], given_vars:list[str]):
    for text_var in actual_vars:
        if text_var not in given_vars:
            raise ValueError(f'TextNode: no input provided for text variable {text_var}.')

# Helper function for printing possibly None string values. Not currently 
# needed, but use in init_args_strs if None can be passed as a non-default 
# argument
def nullable_str(s:str): 
    return f"'{s}'" if s else None

def gen_str_id(l:int=20):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(l))