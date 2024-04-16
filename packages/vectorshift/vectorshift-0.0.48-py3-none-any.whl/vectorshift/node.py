# definitions of all particular node classes
from copy import deepcopy
import requests

import vectorshift
from vectorshift.consts import *
from vectorshift.pipeline_data_types import *
from vectorshift.node_utils import * 

# To add a new node class:
# - define the class (using subclassing as appropriate), ensuring the functions
#   indicated in NodeTemplate are satisfied 
# - add appropriate typechecking for any constructor inputs that are 
#   NodeOutputs
# - add any necessary details in pipeline.py

###############################################################################
# HOME                                                                        #
###############################################################################

class InputNode(NodeTemplate):
    '''
    Represents the inputs (start points) to a pipeline. Your pipelines should always start with these.

    Inputs: None. This node represents what is passed into the pipeline when it is run.

    Parameters:
    - name: A string representing the input name, e.g. "text_input". Should consist of alphanumeric characters and underscores.
    - input_type: A string representing the input type. Each input type corresponds with a specific data type for the outputs of the node. The string must be one of the following, and an error is thrown otherwise: 
        - "text": The input to the pipeline should be (one or more pieces of) text; Corresponds to the Text data type (List[Text] for multiple inputs);
        - "file": The input to the pipeline should be one or more files. Corresponds to the File data type (List[File] for multiple inputs).
    - process_files: If the input_type is 'file', sets whether or not to automatically process the files into text. (If set to True, this node essentially also includes the functionality of FileLoaderNode.)

    Outputs:
    - value: The NodeOutput representing the pipeline's input. The output data type is specified by the input_type parameter above.
    '''

    def __init__(self, name:str, input_type:str, 
            process_files:bool=True, **kwargs):
        super().__init__()
        self.node_type = 'customInput'
        self.category = self.task_name = 'input'
        # Text or File
        if input_type not in INPUT_NODE_TYPES:
            raise ValueError(f'InputNode: input type {input_type} not supported.')
        if not all(ch.isalnum() or ch == '_' for ch in name):
            raise ValueError(f'InputNode: Name must contain only alphanumeric characters or underscores.')
        if len(name) < 3 or len(name) > 50:
            raise ValueError(f'InputNode: Name must be between 3 and 50 characters in length.')
        self.name = name
        self.input_type = input_type
        self.process_files = process_files

    def set_name(self, name:str): 
        if not all(ch.isalnum() or ch == '_' for ch in name):
            raise ValueError(f'InputNode: Name must contain only alphanumeric characters or underscores.')
        if len(name) < 3 or len(name) > 50:
            raise ValueError(f'InputNode: Name must be 3-50 characters.')
        self.name = name
    
    def set_input_type(self, input_type:str):
        if input_type not in INPUT_NODE_TYPES:
            raise ValueError(f'InputNode: input type {input_type} not supported.')
        self.input_type = input_type 

    def set_process_files(self, process_files:bool): 
        self.process_files = process_files

    def init_args_strs(self, indicate_id=False):
        return [
            f"name='{self.name}'", 
            f"input_type='{self.input_type}'",
            f'process_files={self.process_files}' if not self.process_files else None
        ]
        
    def output(self) -> NodeOutput:
        # Input nodes can only return files or text for now
        output_data_type = FILE_TYPE if self.input_type == 'file' and not self.process_files else TEXT_TYPE
        return NodeOutput(
            source=self, 
            output_field='value', 
            output_data_type=output_data_type
        )
    
    def outputs(self):
        o = self.output()
        return {o.output_field: o}
        
    def _to_json_rep(self, generic:bool=False):
        json_rep = {
            'inputName': self.name,
            'inputType': self.input_type.capitalize(),
        }
        if self.input_type == 'file':
            json_rep['processFiles'] = self.process_files
        return json_rep
    
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'InputNode':
        return InputNode(
            name=json_data['inputName'], 
            input_type=json_data['inputType'].lower(),
            process_files=json_data.get('processFiles', True),
            skip_typecheck=True
        )

class OutputNode(NodeTemplate):
    '''
    Represents the outputs (end points) to a pipeline. Your pipelines should always end with these.

    Inputs: 
    - input: The NodeOutput to be used as the pipeline output, whose data type should match input_type (Text or File).

    Parameters:
    - name: A string representing the name of the pipeline's overall output, e.g. "text_output". Should consist of alphanumeric characters and underscores.
    - input_type: A string representing the input type. Each input type corresponds with a specific output data type for the outputs of the node.The string must be one of the following, and an error is thrown otherwise:
        - "text": The input to the pipeline should be (one or more pieces of) text. Corresponds to the Text data type (List[Text] for multiple inputs).
        - "file": The input to the pipeline should be one or more files. Corresponds to the File data type (List[File] for multiple inputs).

    Outputs: None. This node represents what the pipeline produces when it is run.
    '''
    def typecheck_inputs(self):
        if self.output_type == 'file':
            check_type('OutputNode', self._inputs['value'][0], FILE_TYPE)
        elif self.output_type in ['text', 'formatted_text']:
            check_type('OutputNode', self._inputs['value'][0], UnionType(TEXT_TYPE, ListType(TEXT_TYPE)))
        else:
            check_type('OutputNode', self._inputs['value'][0], UnionType(IMAGE_FILE_TYPE, ListType(IMAGE_FILE_TYPE)))

    def __init__(self, name:str, output_type:str, input:NodeOutput, **kwargs):
        super().__init__()
        self.node_type = 'customOutput'
        self.category = self.task_name = 'output'
        # Text or File
        if not output_type.lower() in OUTPUT_NODE_TYPES:
            raise ValueError(f'OutputNode: output type {output_type} not supported.')
        if not all(ch.isalnum() or ch == '_' for ch in name):
            raise ValueError(f'InputNode: Name must contain only alphanumeric characters or underscores.')
        if len(name) < 3 or len(name) > 50:
            raise ValueError(f'InputNode: Name must be 3-50 characters.')
        self.name = name
        self.output_type = output_type
        self._inputs = {'value': [input]}
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            self.typecheck_inputs()

    def set_name(self, name:str): 
        if not all(ch.isalnum() or ch == '_' for ch in name):
            raise ValueError(f'InputNode: Name must contain only alphanumeric characters or underscores.')
        if len(name) < 3 or len(name) > 50:
            raise ValueError(f'InputNode: Name must be 3-50 characters.')
        self.name = name
    
    def set_output_type(self, output_type:str):
        if output_type not in OUTPUT_NODE_TYPES:
            raise ValueError(f'InputNode: input type {output_type} not supported.')
        self.output_type = output_type 
    
    def set_input(self, input:NodeOutput):
        old_input = self._inputs['value']
        self._inputs['value'] = [input]
        try:
            self.typecheck_inputs()
        except ValueError as err:
            self._inputs['value'] = old_input
            raise err

    def init_args_strs(self, indicate_id=False):
        input = self._inputs['value'][0]
        return [
            f"name='{self.name}'", 
            f"output_type='{self.output_type}'",
            format_node_output_with_name('input', input, indicate_id)
        ]

    def outputs(self): return None
    
    def _to_json_rep(self, generic:bool=False):
        return {
            'outputName': self.name,
            'outputType': self.output_type.capitalize(),
        }
        
    @staticmethod 
    def _from_json_rep(json_data:dict) -> 'OutputNode':
        return OutputNode(
            name=json_data['outputName'], 
            output_type=json_data['outputType'].lower().replace(' ', '_'),
            input=None,
            skip_typecheck=True
        )

class TextNode(NodeTemplate):
    '''
    Represents a block of text. The text may include text variables, which are placeholders for text produced earlier on expected to be supplied as additional inputs, and notated using double curly brackets {{}}. For instance, the text block

    Here is our response: {{response}}

    would expect one text variable, response. When the pipeline is run, the earlier output is substituted into the place of {{response}} to create the actual text.

    Inputs:
    - text_inputs: A map of text variable names to NodeOutputs expected to produce the text for the variables. Each NodeOutput should have data type Text. text_inputs may contain a superset of the variables in text. However, each text variable in text should be included as a key in text_inputs. When the pipeline is run, each NodeOutput's contents are interpreted as text and substituted into the variable's places. If text contains no text variables, this can be empty.

    Parameters:
    - text: The string representing the text block, wrapping text variables with double brackets. The same variable can be used in more than one place.
    - format_text: A flag for whether or not to auto-format text.

    Outputs:
    - output: The NodeOutput representing the text, of data type Text. 
    '''
    def __init__(self, text:str, text_inputs:dict[str, NodeOutput]={},
            format_text:bool=True, **kwargs):
        super().__init__()
        self.node_type = 'text'
        self.category = 'task'
        self.task_name = 'text'
        self.text = text
        # if there are required inputs, they should be of the form {{}} - each
        # of them is a text variable
        self.text_vars = find_text_vars(self.text)
        self.format_text = format_text
        # wrap each NodeOutput into a singleton list to fit the type. 
        # if there are variables, we expect them to be matched with inputs
        # they should be passed in a dictionary with the
        # arg name text_inputs. E.g. {"Context": ..., "Task": ...}
        # make it possible for the user to supply extraneous inputs, but
        # only store NodeOutputs corresponding to text vars in self._inputs
        self.all_inputs = {k: [v] for k, v in text_inputs.items()}
        check_text_vars(self.text_vars, self.all_inputs.keys())
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            for var_name, var_input in text_inputs.items():
                check_type(f'TextNode input {var_name}', var_input, TEXT_TYPE)
        self._inputs = {
            k: v for k, v in self.all_inputs.items() if k in self.text_vars
        }
    
    # if the new text adds variables, the proper pattern of usage is to first 
    # add an input for that variable, then calling set_text
    def set_text(self, text:str):
        self.text = text 
        self.text_vars = find_text_vars(self.text)
        check_text_vars(self.text_vars, self.all_inputs.keys())
        # the actual text variables used may have changed
        self._inputs = {
            k: v for k, v in self.all_inputs if k in self.text_vars
        }

    def set_format_text(self, format_text:bool): self.format_text = format_text
    
    def set_text_input(self, text_var:str, input:NodeOutput):
        check_type(f'TextNode input {text_var}', input, TEXT_TYPE)
        self.all_inputs[text_var] = [input]

    def remove_text_input(self, text_var:str):
        if text_var in self.text_vars:
            raise ValueError(f'TextNode: text variable {text_var} is being used.')
        del self.all_inputs[text_var]
    
    def set_text_inputs(self, text_inputs:dict[str, NodeOutput]):
        check_text_vars(self.text_vars, text_inputs.keys())
        for k, v in text_inputs.items():
            check_type(f'TextNode input {k}', v, TEXT_TYPE)
        self.all_inputs = {k: [v] for k, v in text_inputs}
        self._inputs = {
            k: v for k, v in self.all_inputs if k in self.text_vars
        }
            
    def init_args_strs(self, indicate_id=False):
        return [
            f"text='{self.text}'".replace('\n', '\\n'),
            f"text_inputs={format_node_output_dict(self._inputs, indicate_id)}"
        ]
            
    def output(self) -> NodeOutput: 
        return NodeOutput(
            source=self, 
            output_field='output', 
            output_data_type=TEXT_TYPE
        )
    
    def outputs(self):
        o = self.output()
        return {o.output_field: o}
        
    def _to_json_rep(self, generic:bool=False):
        input_names = self.text_vars if len(self.text_vars) > 0 else None
        return {
            'text': self.text,
            'inputNames': input_names,
            'formatText': self.format_text,
        }
        
    def _from_json_rep(json_data:dict) -> 'TextNode':
        text_inputs = {}
        input_names = json_data.get('inputNames', [])
        if not input_names: input_names = []
        for name in input_names:
            text_inputs[name] = None
        return TextNode(
            text=json_data['text'],
            text_inputs=text_inputs,
            format_text=json_data.get('formatText', False),
            skip_typecheck=True
        )

# User-created object
class FileNode(NodeTemplate):
    '''
    Represents one or more files in a pipeline. Files should already be stored within the VectorShift platform. An API call is made upon initialization to retrieve relevant file data, so an API key is required. 

    Inputs: None. This node expects to retrieve files via an API call to the VectorShift platform.

    Parameters:
    - file_names: A list of file names stored on the VectorShift platform to be loaded by this node.
    - process_files: Whether or not to automatically process the files into text. (If set to True, this node essentially also includes the functionality of FileLoaderNode.)
    - chunk_size, chunk_overlap: How files should be loaded if process_files is True. Resulting strings will be of length at most chunk_size and overlap with chunk_overlap.
    - public_key, private_key: The VectorShift API key to make calls to retrieve the file data.

    Outputs:
    - files: The NodeOutput representing the files, of data type List[File] if process_files is set to False, and List[Document] otherwise.
    '''
    def __init__(
        self,
        file_names:list[str]=[],
        process_files:bool=True,
        chunk_size:int=DEFAULT_CHUNK_SIZE,
        chunk_overlap:int=DEFAULT_CHUNK_OVERLAP,
        api_key:str=None,
        public_key:str=None,
        private_key:str=None,
        **kwargs
    ):
        super().__init__()
        self.node_type = 'file'
        self.category = 'task'
        self.task_name = 'file'
        self.file_names = file_names
        self.process_files = process_files
        if chunk_size < 1 or chunk_size > 4096:
            raise ValueError(f'FileNode: invalid chunk_size value.')
        if chunk_overlap < 0: raise ValueError('FileNode: invalid chunk_overlap value.')
        if chunk_overlap >= chunk_size:
            raise ValueError(f'FileNode: chunk_overlap must be smaller than chunk_size.')
        self.chunk_size, self.chunk_overlap = chunk_size, chunk_overlap
        self._api_key = api_key or vectorshift.api_key
        self._public_key = public_key or vectorshift.public_key
        self._private_key = private_key or vectorshift.private_key

    def set_file_names(self, file_names:list[str]):
        self.file_names = file_names
    
    def set_process_files(self, process_files:bool):
        self.process_files = process_files 

    def set_chunk_size(self, chunk_size:int):
        if chunk_size < 1 or chunk_size > 4096:
            raise ValueError(f'FileNode: invalid chunk_size value.')
        self.chunk_size = chunk_size 

    def set_chunk_overlap(self, chunk_overlap:int):
        if chunk_overlap < 0: raise ValueError('FileNode: invalid chunk_overlap value.')
        if chunk_overlap >= self.chunk_size:
            raise ValueError(f'FileNode: chunk_overlap must be smaller than chunk_size.')
        self.chunk_overlap = chunk_overlap
    
    def set_api_key(self, api_key: str = None, public_key: str = None, private_key: str = None) -> None:
        self._api_key = api_key
        self._public_key = public_key
        self._private_key = private_key

    def init_args_strs(self, indicate_id=False):
        return [
            f'file_names={self.file_names}',
            f'process_files={self.process_files}' \
                if not self.process_files else None, 
            f'chunkSize={self.chunk_size}' \
                if self.chunk_size != DEFAULT_CHUNK_SIZE else None,
            f'chunkOverlap={self.chunk_overlap}' \
                if self.chunk_overlap != DEFAULT_CHUNK_OVERLAP else None
        ]

    def output(self) -> NodeOutput:
        output_data_type = ListType(DOCUMENT_TYPE) if self.process_files else ListType(FILE_TYPE)
        return NodeOutput(
            source=self,
            output_field='files',
            output_data_type=output_data_type
        )

    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self, generic:bool=False):
        files_json = []
        if not generic and len(self.file_names) > 0:
            if self._api_key is None and (self._public_key is None or self._private_key is None):
                raise ValueError('FileNode: API key required to fetch files.')
            # Note: there's currently no way in the API to get files owned
            # by another user, nor is there a way to get files by their ID.
            response = requests.get(
                API_FILE_FETCH_ENDPOINT,
                data={
                    'file_names': self.file_names,
                },
                headers={
                    'Api-Key': self._api_key or vectorshift.api_key,
                    'Public-Key': self._public_key,
                    'Private-Key': self._private_key
                }
            )
            if response.status_code != 200:
                raise Exception(f'Error fetching files: {response.text}')
            # list of JSONs for each file
            files_json = response.json()
        return {
            'selectedFiles': files_json, 
            'processFiles': self.process_files,
            'chunkSize': self.chunk_size,
            'chunkOverlap': self.chunk_overlap,
        }

    @staticmethod 
    def _from_json_rep(json_data:dict) -> 'FileNode':
        file_names = [
            file_data['name'] for file_data in json_data.get('selectedFiles', [])
        ]
        return FileNode(
            file_names=file_names,
            process_files=json_data.get('processFiles', True),
            chunk_size=int(json_data.get('chunkSize', DEFAULT_CHUNK_SIZE)),
            chunk_overlap=int(json_data.get('chunkOverlap', DEFAULT_CHUNK_OVERLAP)),
            skip_typecheck=True
        )

# User-created object
class PipelineNode(NodeTemplate):
    '''
    Represent a nested Pipeline, which will be run as a part of the overall Pipeline. When the node is executed, the pipeline it represents is executed with the supplied inputs, and the overall pipeline's output becomes the node's output. The Pipeline must already exist on the VectorShift platform, so that it can be referenced by its ID or name. An API call is made upon initialization to retrieve relevant Pipeline data, meaning an API key is required.

    Inputs:
    - inputs: A map of input names to NodeOutputs, which depends on the specific Pipeline. In essence, the NodeOutputs passed in are interpreted as inputs to the Pipeline represented by the PipelineNode. They should match up with the expected input names of the pipeline. For instance, if the Pipeline has input names input_1 and input_2, then the dictionary should contain those strings as keys.

    Parameters:
    - pipeline_id: The ID of the Pipeline being represented.
    - pipeline_name: The name of the Pipeline being represented. At least one of pipeline_id and pipeline_name should be provided. If both are provided, pipeline_id is used to search for the Pipeline.
    - username: The username of the user owning the Pipeline.
    - org_name: The organization name of the user owning the Pipeline, if applicable.
    - batch_mode: A flag to set whether or not the pipeline can run batched inputs.
    - public_key, private_key: The VectorShift API key to make calls to retrieve the Pipeline data.

    Outputs: Outputs are determined from the pipeline represented. Since each pipeline returns one or more named outputs that are either of File or Text data type, the keys of the outputs dictionary are the named outputs of the pipeline, with the values given the appropriate data type.
    '''
    def typecheck_inputs(self):
        for i in self.pipeline_inputs:
            input_name = i['name']
            node_input = self._inputs[input_name][0]
            if i['type'] == 'Text':
                check_type(f'PipelineNode input {input_name}', node_input, TEXT_TYPE)
            elif i['type'] == 'File':
                check_type(f'PipelineNode input {input_name}', node_input, FILE_TYPE)
            else:
                raise ValueError(f"PipelineNode: invalid input type for {input_name}: {i['type']}") 

    def setup_pipeline_data(self, 
            pipeline_id:str=None, pipeline_name:str=None, 
            username:str=None, org_name:str=None, 
            inputs:dict[str, NodeOutput]={}):
        # We'd like to know what the input and output names are upon 
        # initialization so we can validate that the inputs dict matches up.
        # So the API call to get the pipeline JSON is located in the
        # constructor here (compare to other nodes, where it's in _to_json_rep)
        if self._api_key is None and (self._public_key is None or self._private_key is None):
            raise ValueError('PipelineNode: API key required to fetch pipeline. If you are getting this error while loading a pipeline from the platform, set the environment variables vectorshift.public_key and vectorshift.private_key.')
        response = requests.get(
            API_PIPELINE_FETCH_ENDPOINT,
            data={
                'pipeline_id': pipeline_id,
                'pipeline_name': pipeline_name,
                'username': username,
                'org_name': org_name,
            },
            headers={
                'Api-Key': self._api_key or vectorshift.api_key,
                'Public-Key': self._public_key or vectorshift.public_key,
                'Private-Key': self._private_key or vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(response.text)
        self.pipeline_json = response.json()
        self.pipeline_id = self.pipeline_json['id']
        self.pipeline_name = self.pipeline_json['name']
        # The list of inputs provided should have keys matching the input names
        # defined by the pipeline
        self.pipeline_inputs = self.pipeline_json.get('inputs', {}).values()
        self.input_names = [i['name'] for i in self.pipeline_inputs]
        if sorted(list(inputs.keys())) != sorted(self.input_names):
            raise ValueError(f'PipelineNode: inputs do not match expected input names: expected f{self.input_names}')

    def __init__(self, pipeline_id:str=None, pipeline_name:str=None, 
            inputs:dict[str, NodeOutput]={},
            username:str=None, org_name:str=None,
            api_key:str=None,
            public_key:str=None, private_key:str=None, 
            batch_mode:bool=False, **kwargs):
        super().__init__()
        self.node_type = 'pipeline'
        self.category = self.task_name = 'pipeline'
        self.pipeline_id = pipeline_id 
        self.pipeline_name = pipeline_name 
        self.username = username
        self.org_name = org_name 
        self._api_key = api_key or vectorshift.api_key
        self._public_key = public_key or vectorshift.public_key
        self._private_key = private_key or vectorshift.private_key
        self.batch_mode = batch_mode 
        # set the inputs and outputs
        self.pipeline_json = {}
        if pipeline_id or pipeline_name:
            self.setup_pipeline_data(pipeline_id, pipeline_name, username, org_name, inputs)
        self._inputs = {
            input_name: [inputs[input_name]] for input_name in self.input_names
        }
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            self.typecheck_inputs()

    def set_pipeline(self, pipeline_id:str=None, pipeline_name:str=None, 
            inputs:dict[str, NodeOutput]={},
            username:str=None, org_name:str=None):
        old_id, old_name = self.pipeline_id, self.pipeline_name
        old_username, old_org_name = self.username, self.org_name 
        old_inputs = self._inputs
        self.pipeline_id = pipeline_id 
        self.pipeline_name = pipeline_name 
        self.username = username
        self.org_name = org_name 
        self.setup_pipeline_data(pipeline_id, pipeline_name, username, org_name, inputs)
        self._inputs = {
            input_name: [inputs[input_name]] for input_name in self.input_names
        }
        try:
            self.typecheck_inputs()
        except ValueError as err:
            self.pipeline_id, self.pipeline_name, = old_id, old_name 
            self.username, self.org_name = old_username, old_org_name 
            self._inputs = old_inputs
            raise err

    def set_batch_mode(self, batch_mode:bool):
        self.batch_mode = batch_mode

    def set_input(self, input_name:str, input:NodeOutput):
        if input_name not in self._inputs.keys():
            raise ValueError(f'PipelineNode: Invalid input name {input_name}.')
        old_input = self._inputs[input_name]
        self._inputs[input_name] = [input] 
        try:
            self.typecheck_inputs()
        except ValueError as err:
            self._inputs[input_name] = old_input
            raise err

    def set_inputs(self, inputs:dict[str, NodeOutput]):
        if sorted(inputs.keys()) != sorted(self._inputs.keys()):
            raise ValueError(f'PipelineNode: Invalid input names provided.')
        old_inputs = self._inputs.copy()
        self._inputs = {
            k: [v] for k, v in inputs.items()
        } 
        try:
            self.typecheck_inputs()
        except ValueError as err:
            self._inputs = old_inputs
            raise err

    @staticmethod
    def from_pipeline_obj(pipeline_obj, 
            inputs:dict[str, NodeOutput],
            api_key=None,
            public_key=None, private_key=None) -> 'PipelineNode':
        if not pipeline_obj.id:
            print('PipelineNode.from_pipeline_obj: Pipeline object does not contain a required ID, which likely means that the pipeline has not yet been saved. Attempting to save the pipeline...')
            pipeline_obj.save(api_key, public_key, private_key)
            print('PipelineNode: Pipeline object successfully saved.')
        # This is inefficient right now, since we save (write to Mongo) and 
        # then immediately query the object (read from Mongo) in the 
        # constructor.
        return PipelineNode(
            pipeline_id=pipeline_obj.id,
            pipeline_name=pipeline_obj.name,
            inputs=inputs,
            api_key=api_key,
            public_key=public_key, 
            private_key=private_key
        )

    def init_args_strs(self, indicate_id=False):
        return [
            f"pipeline_id='{self.pipeline_id}'" \
                if self.pipeline_id else None,
            f"pipeline_name='{self.pipeline_name}'" \
                if self.pipeline_name else None,
            f'inputs={format_node_output_dict(self._inputs, indicate_id)}',
            f"username='{self.username}" if self.username else None,
            f"org_name='{self.org_name}'" if self.org_name else None,
            f'batch_mode={self.batch_mode}' if self.batch_mode else None
        ]

    def set_api_key(self, api_key: str = None, public_key: str = None, private_key: str = None) -> None:
        self._api_key = api_key
        self._public_key = public_key
        self._private_key = private_key

    def outputs(self):
        os = {}
        for o in self.pipeline_json.get('outputs', {}).values():
            output_field = o['name']
            # Pipelines can only return files or text for now
            # note: these correspond with how the output type for an OutputNode
            # is stored in Mongo, which is capitalized 
            output_data_type = None
            if o['type'] == 'File':
                output_data_type = FILE_TYPE 
            elif o['type'] in ['Text', 'Formatted Text']:
                output_data_type = TEXT_TYPE 
            else:
                raise ValueError(f"PipelineNode: invalid pipeline output type {o['type']}")
            os[output_field] = NodeOutput(
                source=self, 
                output_field=output_field, 
                output_data_type=output_data_type
            )
        return os

    def _to_json_rep(self, generic:bool=False):
        if generic or self.pipeline_json == {}:
            return { 'batchMode': self.batch_mode }
        pipeline_field_json = {
            'id': self.pipeline_json['id'],
            'name': self.pipeline_json['name'],
            'inputs': self.pipeline_json['inputs'],
            'outputs': self.pipeline_json['outputs'],
            # TODO: we just use the name as a placeholder; if this field is 
            # important we'll have to figure out a way to determine whether or
            # not the user/org name in this pipeline is different from the 
            # user/org name of whoever is writing this code (perhaps through
            # the Config class?). Same issue in TransformationNode.
            'displayName': self.pipeline_json['name']
        }
        return {
            'pipeline': pipeline_field_json,
            'batchMode': self.batch_mode,
        }

    @staticmethod
    def _from_json_rep(json_data:dict) -> 'PipelineNode':
        pipeline_json = json_data.get('pipeline', {})
        inputs = {}
        for i in pipeline_json.get('inputs', {}).values():
            inputs[i['name']] = None
        return PipelineNode(
            pipeline_id=pipeline_json.get('id', None),
            pipeline_name=pipeline_json.get('name', None),
            # We don't have a way to recover the username/org name, or the 
            # API key
            inputs=inputs,
            skip_typecheck=True
        )

# User-created object.
class TransformationNode(NodeTemplate):
    '''
    Represent a user-created transformation. The transformation must already exist on the VectorShift platform, so that it can be referenced by its name. An API call is made upon initialization to retrieve relevant transformation data, meaning an API key is required. 

    Inputs:
    - inputs: A map of input names to strings of NodeOutputs, which depends on the specific transformation. The inputs should match the expected names and data types of the specific integration and function. There are currently no checks on the input, so it is up to your discretion to ensure that the NodeOutputs you provide to the transformation node are compatible with the transformation.

    Parameters:
    - transformation_name: The name of the user-created transformation being represented.
    - public_key, private_key: API keys to be used when retrieving information about the transformation from the VectorShift platform.

    Outputs: Outputs are determined from the specific transformation. They are currently given data type Any. 
    '''
    def __init__(self, transformation_name:str, inputs:dict[str, NodeOutput],
            api_key:str=None, public_key:str=None, private_key:str=None, **kwargs):
        super().__init__()
        self.node_type = 'transformation'
        self.category = self.task_name = 'transformation'
        self._api_key = api_key or vectorshift.api_key
        self._public_key = public_key or vectorshift.public_key
        self._private_key = private_key or vectorshift.private_key
        if not transformation_name:
            raise ValueError('TransformationNode: transformation_name must be provided.')
        self.transformation_name = transformation_name
        # We make an API call to get the transformation JSON here to get the
        # desired outputs - see PipelineNode
        if self._api_key is None and (self._public_key is None or self._private_key is None):
            raise ValueError('TransformationNode: API key required to fetch transformation. If you are getting this error while loading a pipeline from the platform, set the environment variables vectorshift.public_key and vectorshift.private_key.')
        # Note: there's currently no way in the API code to get files owned 
        # by another user, nor is there a way to get files by their ID.
        response = requests.get(
            API_TRANSFORMATION_FETCH_ENDPOINT,
            data={
                'transformation_name': self.transformation_name
            },
            headers={
                'Api-Key': self._api_key,
                'Public-Key': self._public_key,
                'Private-Key': self._private_key
            }
        )
        if response.status_code != 200:
            raise Exception(f'Error fetching transformation: {response.text}')
        self.transformation_json = response.json()
        input_names = self.transformation_json['inputs']
        # The list of inputs provided should have keys matching the input names
        # defined by the transformation
        if sorted(list(inputs.keys())) != sorted(input_names):
            raise ValueError(f'TransformationNode: inputs do not match expected input names: expected f{input_names}')
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            # TODO: add typechecking
            pass
        self._inputs = {
            input_name: [inputs[input_name]] for input_name in input_names
        } 

    def set_input(self, input_name:str, input:NodeOutput):
        if input_name not in self._inputs.keys():
            raise ValueError(f'Invalid input name {input_name}.')
        old_input = self._inputs[input_name]
        self._inputs[input_name] = [input] 
        try: pass
        except ValueError as err:
            self._inputs[input_name] = old_input
            raise err

    def set_inputs(self, inputs:dict[str, NodeOutput]):
        if sorted(inputs.keys()) != sorted(self._inputs.keys()):
            raise ValueError(f'Invalid input names provided.')
        old_inputs = self._inputs.copy()
        self._inputs = {
            k: [v] for k, v in inputs.items()
        } 
        try: pass
        except ValueError as err:
            self._inputs = old_inputs
            raise err
    
    def set_api_key(self, api_key: str = None, public_key: str = None, private_key: str = None) -> None:
        self._api_key = api_key
        self._public_key = public_key
        self._private_key = private_key

    def init_args_strs(self, indicate_id=False):
        return [
            f"transformation_name='{self.transformation_name}'",
            f'inputs={format_node_output_dict(self._inputs, indicate_id)}'
        ]
    
    def outputs(self):
        os = {}
        for output_field in self.transformation_json['outputs'].keys():
            os[output_field] = NodeOutput(
                source=self,
                output_field=output_field,
                # TODO: start storing types with transformations
                # Using AnyType() for now
                output_data_type=AnyType()
            )
        return os
    
    # "Generic" transformations are currently not supported
    def _to_json_rep(self, generic:bool=False):
        transformation_field_json = {
            'id': self.transformation_json['id'],
            'name': self.transformation_json['name'],
            'description': self.transformation_json['description'],
            'inputs': self.transformation_json['inputs'],
            'outputs': self.transformation_json['outputs'],
            # In the app repo this calls a helper function to format pipeline
            # names. For the time being this will be the same as the name as
            # the only case in which it isn't the name are if it's owned by the
            # user (which is impossible right now). TODO: may need to fix. Same
            # issue in PipelineNode.
            'displayName': self.transformation_json['name'],
        }
        return {
            'transformation': transformation_field_json,
        }
    
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'TransformationNode':
        return TransformationNode(
            transformation_name=json_data['transformation']['name'],
            inputs={
                input_name: None
                for input_name in json_data['transformation'].get('inputs', [])
            },
            skip_typecheck=True
        )

class FileSaveNode(NodeTemplate):
    '''
    Represent the saving of one or more files to the VectorShift platform.

    Inputs:
    - name_input: A NodeOutput representing the name under which the file should be saved. The output of a TextNode can be used if the desired file name is known and fixed. Should have data type String.
    - files_input : One or more NodeOutputs representing files to be saved. They should have output data type File.

    Parameters: None.

    Outputs: None. This node represents saving files.
    '''
    def __init__(self, name_input:NodeOutput, files_input:list[NodeOutput], 
            **kwargs):
        super().__init__()
        self.node_type = 'fileSave'
        self.category = 'task'
        self.task_name = 'save_file'
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            check_type('FileSaveNode input name', name_input, TEXT_TYPE)
            for file_input in files_input:
                check_type('FileSaveNode input files', file_input, UnionType(FILE_TYPE, ListType(FILE_TYPE)))
        self._inputs = {
            'name': [name_input],
            # files aggregates one or more node outputs
            'files': files_input
        }

    def init_args_strs(self, indicate_id=False):
        name_input = self._inputs['name'][0]
        files_input_strs = [
            format_node_output(i, indicate_id)
            for i in self._inputs['files']
        ]
        return [
            format_node_output_with_name('name_input', name_input, indicate_id),
            f'files_input={files_input_strs}'
        ]
    
    def set_name_input(self, name_input:NodeOutput):
        check_type('FileSaveNode input name', name_input, TEXT_TYPE)
        self._inputs['name'] = [name_input]
    
    def set_files_input(self, files_input:list[NodeOutput]):
        for o in files_input:
             check_type('FileSaveNode input files', o, UnionType(FILE_TYPE, ListType(FILE_TYPE)))
        self._inputs['files'] = files_input
    
    def outputs(self): return None
    
    def _to_json_rep(self, generic:bool=False):
        return {
            'outputName': self._id.replace('-', '_')
        }
        
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'FileSaveNode':
        _ = json_data 
        return FileSaveNode(
            name_input=None,
            files_input=[],
            skip_typecheck=True
        )

# SDK users shouldn't really have a use for this given that Python comments 
# exist. Included for compatibility.
# Note: in the no-code editor, this is named a 'Note'.
class StickyNoteNode(NodeTemplate):
    '''
    A sticky note with no functionality.

    Inputs: None.

    Parameters:
    - text: The text in the sticky note.

    Outputs: None.
    '''
    def __init__(self, text:str, **kwargs):
        super().__init__()
        self.node_type = 'stickyNote'
        self.category = 'comment'
        self.task_name = 'none'
        self.text = text 
        # no typechecking needed

    def set_text(self, text:str): self.text = text 

    def init_args_strs(self, indicate_id=False):
        return [f"text='{self.text}'"]
    
    def outputs(self): return None 

    def _to_json_rep(self, generic:bool=False):
        return {'text': self.text}
    
    @staticmethod 
    def _from_json_rep(json_data:dict) -> 'StickyNoteNode':
        return StickyNoteNode(
            text=json_data.get('text', ''),
            skip_typecheck=True
        )

###############################################################################
# INTEGRATIONS                                                                #
###############################################################################

# User-created object.
class IntegrationNode(NodeTemplate):
    '''
    Represents a particular action taken from a VectorShift integration (e.g. the "save files" action from a Google Drive integration). The integration should already exist on the VectorShift platform, so that it can be referenced by its name. The particular actions available depend on the integration. An API call is made when a pipeline containing this node is saved to retrieve relevant integration data, meaning an API key is required. 

    Inputs:
    - inputs: A map of input names to lists of NodeOutputs, which depends on the specific integration. (If there is only one NodeOutput, a singleton list should be used as the value.) The inputs should match the expected names and data types of the specific integration and action. 

    Parameters:
    - integration_type: A string denoting the type of integration. 
    - integration_id: The ID of the integration object being represented.
    - action: The name of the specific action to be used with the integration.
    - public_key, private_key: API keys to be used when retrieving integration data from the VectorShift platform.

    Outputs: Outputs are determined from the specific integration action. They are currently given data type Any. 
    '''
    def setup_integration_action(self, inputs, **kwargs):
        self.task_name = self.action_params['taskName']
        # The list of inputs provided should have keys matching the input names
        # defined by the integration action. 
        # Note: each input to an integration node could be a list of 
        # NodeOutputs (multiple in-edges to a node's input field, e.g. saving
        # multiple files to Drive at once). This is different from the input
        # structure for pipeline and transformation nodes.
        self.input_names = [i['name'] for i in self.action_params['inputs']]
        self.integration_specific_params = {}
        # Add a list of given fields as expected inputs, if they have to be
        # found from constructor arguments.
        def handle_dynamic_inputs(fields):
            # add dynamic inputs to input list
            dynamic_inputs = []
            for field in fields:
                dynamic_inputs.append({
                    'name': field,
                    'displayName': field,
                    'multiInput': False,
                })
            self.action_params['inputs'] = dynamic_inputs
            input_names = [
                i['name'] for i in self.action_params['inputs']
            ]
            return input_names
        if self.integration_type == 'Airtable' and self.action == 'read_tables':
            # Expects a list of dicts with base and table IDs and names for each
            # table to load from
            if not ('airtable_tables' in kwargs):
                print('IntegrationNode: missing airtable_tables input in Airtable integration. Integration is incomplete. Expecting a list of dictionaries including base_id, base_name, and table_id keys.')
            for t in kwargs.get('airtable_tables', []):
                if 'base_id' not in t or 'base_name' not in t or 'table_id' not in t:
                    raise ValueError('IntegrationNode: missing base_id, base_name, or table_id keys in airtable_tables input item in Airtable integration.') 
            self.integration_specific_params['selectedTables'] = kwargs.get('airtable_tables', [])
        elif self.integration_type == 'Airtable' and self.action == 'new_record':
            # Expects a base ID, table ID, and a list of table fields to write to
            if not ('base_id' in kwargs) or not ('table_id' in kwargs) or not ('table_fields' in kwargs):
                print('IntegrationNode: missing base_id, table_id, or table_fields inputs in Airtable integration. Integration is incomplete.')
            self.integration_specific_params['base_id'] = kwargs.get('base_id', None)
            self.integration_specific_params['table_id'] = kwargs.get('table_id', None)
            self.integration_specific_params['input_names'] = kwargs.get('table_fields', None)
            self.integration_specific_params['selectedDynamicHandleNames'] = kwargs.get('table_fields', None)
            self.input_names = handle_dynamic_inputs(kwargs.get('table_fields', []))
            for field in kwargs.get('table_fields', []):
                if field not in list(inputs.keys()):
                    raise ValueError(f'IntegrationNode: Airtable inputs do not match expected input names: expected {self.input_names}')
        elif self.integration_type == 'Notion' and self.action == 'write_to_database':
            # Expects a string containing the database_id to write to
            # Expects a list of strings which contain the fields of the database we will write to
            if not 'database_id' in kwargs or not 'database_fields' in kwargs:
                print('IntegrationNode: missing database_id or database_fields inputs in Notion integration. Integration is incomplete.')
            self.integration_specific_params['database_id'] = kwargs.get('database_id', None)
            self.integration_specific_params['database_fields'] = kwargs.get('database_fields', [])
            self.integration_specific_params['selectedDynamicHandleNames'] = kwargs.get('database_fields', [])
            self.input_names = handle_dynamic_inputs(kwargs.get('database_fields', []))
            # Validate that we receive an input for each database field
            for field in kwargs.get('database_fields', []):
                if field not in list(inputs.keys()):
                    raise ValueError(f'IntegrationNode: Notion inputs do not match expected input names: expected {self.input_names}')
        elif self.integration_type == 'Google Sheets' and self.action == 'write_to_sheet':
            if not ('file_id' in kwargs) or not ('sheet_id' in kwargs) or not ('sheet_fields' in kwargs):
                print('IntegrationNode: missing file_id, sheet_id, or sheet_fields inputs in Google Sheets integration. Integration is incomplete.')
            self.integration_specific_params['file_id'] = kwargs.get('file_id', None)
            self.integration_specific_params['sheet_id'] = kwargs.get('sheet_id', None)
            self.integration_specific_params['selectedDynamicHandleNames'] = kwargs.get('sheet_fields', [])
            self.input_names = handle_dynamic_inputs(kwargs['sheet_fields'])
            for field in kwargs['sheet_fields']:
                if field not in list(inputs.keys()):
                    raise ValueError(f'IntegrationNode: Google Sheets inputs do not match expected input names: expected {self.input_names}')
        # Check that the inputs supplied match the inputs expected
        if sorted(list(inputs.keys())) != sorted(self.input_names):
            raise ValueError(f'IntegrationNode: inputs do not match expected input names: expected {self.input_names}')

    # Note: actions are referred to as functions in Mongo.
    # If integration_id is left None, then the node represents a generic
    # integration that needs to be set up before the pipeline is run
    # If action is left None, the node represents a generic integration whose
    # action should be later specified
    def __init__(self, integration_type:str, integration_id:str=None, 
            action:str=None, inputs:dict[str, list[NodeOutput]]={},
            api_key:str=None, public_key:str=None, private_key:str=None, **kwargs):
        super().__init__()
        self.node_type = 'integration'
        self.category = 'integration'
        self.task_name = ''
        # task_name is retrieved from the specific integration parameters
        self._api_key = api_key or vectorshift.api_key
        self._public_key = public_key or vectorshift.public_key
        self._private_key = private_key or vectorshift.private_key
        # The specific integration is stored in two sub-fields under the 
        # data field in the node's JSON representation. One field contains 
        # details of the integration itself, which requires an API call to
        # retrieve the integration object from Mongo. The other contains 
        # details of the action to run with the integration, which defines
        # the inputs/outputs of the node and can be deduced from the 
        # constructor arguments provided.
        if integration_type not in INTEGRATION_PARAMS.keys():
            raise ValueError(f'IntegrationNode: invalid integration {integration_type}.')
        self.integration_type = integration_type 
        self.integration_id = integration_id
        # Each integration action has some list of inputs and outputs.
        self.action = action
        self.action_params = {}
        # Specific integration actions require additional argument parameters 
        # passed in via the constructor rather than as NodeOutputs in the 
        # inputs arg.
        self.integration_specific_params = {}
        # The overall list of expected NodeOutput input names.
        self.input_names = []
        if self.action:
            if self.action not in INTEGRATION_PARAMS[integration_type].keys():
                raise ValueError(f'IntegrationNode: invalid action {self.action} for integration {integration_type}.')
            self.action_params = INTEGRATION_PARAMS[self.integration_type][self.action]
            # add the action name to the action params
            self.action_params['name'] = self.action
            self.setup_integration_action(inputs, **kwargs)
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            # TODO: add typechecking for integrations
            pass
        self._inputs = {
            input_name: inputs[input_name] for input_name in self.input_names 
        }

    def set_integration(self, integration_type:str, 
            action:str, inputs:dict[str, list[NodeOutput]], **kwargs):
        self.integration_type = integration_type
        self.action = action 
        if self.action not in INTEGRATION_PARAMS[integration_type].keys():
            raise ValueError(f'IntegrationNode: invalid action {self.action} for integration {integration_type}.')
        self.action_params = INTEGRATION_PARAMS[self.integration_type][self.action]
        # add the action name to the action params
        self.action_params['name'] = self.action
        self.setup_integration_action(inputs, **kwargs)
        self._inputs = {
            input_name: inputs[input_name] for input_name in self.input_names 
        }
        
    def set_integration_id(self, integration_id:str):
        self.integration_id = integration_id

    def set_input(self, input_name:str, input:list[NodeOutput]):
        if input_name not in self._inputs.keys():
            raise ValueError(f'Invalid input name {input_name}.')
        old_input = self._inputs[input_name]
        self._inputs[input_name] = input
        try: pass
        except ValueError as err:
            self._inputs[input_name] = old_input
            raise err

    def set_inputs(self, inputs:dict[str, list[NodeOutput]]):
        if sorted(inputs.keys()) != sorted(self._inputs.keys()):
            raise ValueError(f'Invalid input names provided.')
        old_inputs = self._inputs.copy()
        self.input_names = [i['name'] for i in self.action_params['inputs']]
        self._inputs = {
            input_name: inputs[input_name] for input_name in self.input_names 
        }
        try: pass
        except ValueError as err:
            self._inputs = old_inputs
            raise err

    def set_api_key(self, api_key: str = None, public_key: str = None, private_key: str = None) -> None:
        self._api_key = api_key
        self._public_key = public_key
        self._private_key = private_key

    def init_args_strs(self, indicate_id=False):
        args_strs = [
            f"integration_type='{self.integration_type}'",
            f"integration_id='{self.integration_id}'",
            f"action='{self.action}'",
            f"inputs={format_node_output_dict(self._inputs, indicate_id)}"
        ] 
        for k, v in self.integration_specific_params.items():
            args_strs.append(f"{k}={v}")
        return args_strs

    def outputs(self):
        os = {}
        for o in self.action_params.get('outputs', []):
            output_field = o['name']
            os[output_field] = NodeOutput(
                source=self, 
                output_field=output_field,
                # TODO: start storing types with integration actions on frontend
                # Using AnyType() for now
                output_data_type=AnyType()
            )
        return os
    
    def _to_json_rep(self, generic:bool=False):
        integration_json = {}
        # Get integration information from the given ID
        if self.integration_id and not generic:
            if self._api_key is None and (self._public_key is None or self._private_key is None):
                raise ValueError('IntegrationNode: API key required to fetch integration.')
            # Even if we constructed this IntegrationNode from JSON and have
            # information for an integration object, we'll still make an API 
            # call since integration information may have changed.
            response = requests.get(
                API_INTEGRATION_FETCH_ENDPOINT,
                data={
                    'integration_id': self.integration_id
                },
                headers={
                    'Api-Key': self._api_key,
                    'Public-Key': self._public_key,
                    'Private-Key': self._private_key
                }
            )
            if response.status_code != 200:
                raise Exception(f"Error fetching integration: {response.text}")
            integration_json = response.json()
            if integration_json['type'] != self.integration_type:
                raise ValueError(f"IntegrationNode: Mismatching integration type (expected {self.integration_type}, got {integration_json['type']}). You may want to double-check your integration ID.")
            # don't need to store integration parameters in node's JSON
            if 'params' in integration_json:
                del integration_json['params']

        return {
            'integration': integration_json,
            'integrationType': self.integration_type,
            'function': self.action_params,
            # I'm duplicating these specific parameters because who knows when
            # the JSON structure will change at this point
            **self.integration_specific_params,
            'integrationFields': self.integration_specific_params
        }
    
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'IntegrationNode':
        input_names = json_data.get('function', {}).get('inputs', [])
        if not input_names: input_names = []
        integration_type = json_data.get('integrationType', None)
        integration_id = None
        integration_json = json_data.get('integration', None)
        if integration_json is not None:
            integration_type = integration_json.get('type', integration_type)
            integration_id = integration_json.get('id', None)
        return IntegrationNode(
            integration_type=integration_type,
            integration_id=integration_id,
            action=json_data.get('function', {}).get('name', None),
            # For IntegrationNodes, we must pass in the input names to the 
            # constructor, as they will be validated against the integration 
            # and action upon initialization.
            inputs={ 
                i['name']: [None] 
                for i in input_names
            },
            # any integration-specific parameters
            **{k: v for k, v in json_data.items()
               if k not in 
               ['id', 'nodeType', 'category', 'task_name', 'integration', 'function']},
            **{k: v for k, v in json_data.get('integrationFields', {}).items()},
            skip_typecheck=True
        )

class PineconeIntegrationNode(IntegrationNode):
    '''Akin to an IntegrationNode with integration_type = 'Pinecone'.'''
    def __init__(self, integration_id:str, action:str, 
            inputs:dict[str, list[NodeOutput]], 
            api_key:str=None, public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Pinecone',
            integration_id=integration_id,
            action=action,
            inputs=inputs,
            api_key=api_key,
            public_key=public_key,
            private_key=private_key,
            **kwargs
        )

class SalesforceIntegrationNode(IntegrationNode):
    '''Akin to an IntegrationNode with integration_type = 'Salesforce'.'''
    def __init__(self, integration_id:str, action:str, 
            inputs:dict[str, list[NodeOutput]], 
            api_key:str=None, public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Salesforce',
            integration_id=integration_id,
            action=action,
            inputs=inputs,
            api_key=api_key,
            public_key=public_key,
            private_key=private_key,
            **kwargs
        )

class GoogleDriveIntegrationNode(IntegrationNode):
    '''Akin to an IntegrationNode with integration_type = 'Google Drive'.'''
    def __init__(self, integration_id:str, action:str, 
            inputs:dict[str, list[NodeOutput]], 
            api_key:str=None, public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Google Drive',
            integration_id=integration_id,
            action=action,
            inputs=inputs,
            api_key=api_key,
            public_key=public_key,
            private_key=private_key,
            **kwargs
        )

class GmailIntegrationNode(IntegrationNode):
    '''Akin to an IntegrationNode with integration_type = 'Gmail'.'''
    def __init__(self, integration_id:str, action:str, 
            inputs:dict[str, list[NodeOutput]], 
            api_key:str=None, public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Gmail',
            integration_id=integration_id,
            action=action,
            inputs=inputs,
            api_key=api_key,
            public_key=public_key,
            private_key=private_key,
            **kwargs
        )

class NotionIntegrationNode(IntegrationNode):
    def __init__(self, integration_id:str, action:str,
            inputs:dict[str, list[NodeOutput]],
            database_id:str=None,
            database_fields:list[str]=None,
            api_key:str=None, public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Notion',
            integration_id=integration_id,
            action=action,
            inputs=inputs,
            api_key=api_key,
            public_key=public_key,
            private_key=private_key,
            database_id=database_id,
            database_fields=database_fields,
            **kwargs
        )

class AirtableIntegrationNode(IntegrationNode):
    '''Akin to an IntegrationNode with integration_type = 'Airtable'.'''
    def __init__(self, integration_id:str, action:str, 
            inputs:dict[str, list[NodeOutput]],
            airtable_tables:list[dict]=None,
            api_key:str=None, public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Airtable',
            integration_id=integration_id,
            action=action,
            inputs=inputs,
            api_key=api_key,
            public_key=public_key,
            private_key=private_key,
            airtable_tables=airtable_tables,
            **kwargs
        )

class HubSpotIntegrationNode(IntegrationNode):
    '''Akin to an IntegrationNode with integration_type = 'Hubspot'.'''
    def __init__(self, integration_id:str, action:str, 
            inputs:dict[str, list[NodeOutput]], 
            api_key:str=None, public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Hubspot',
            integration_id=integration_id,
            action=action,
            inputs=inputs,
            api_key=api_key,
            public_key=public_key,
            private_key=private_key,
            **kwargs
        )

class SugarCRMIntegrationNode(IntegrationNode):
    '''Akin to an IntegrationNode with integration_type = 'SugarCRM'.'''
    def __init__(self, integration_id:str, action:str, 
            inputs:dict[str, list[NodeOutput]], 
            api_key:str=None, public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='SugarCRM',
            integration_id=integration_id,
            action=action,
            inputs=inputs,
            api_key=api_key,
            public_key=public_key,
            private_key=private_key,
            **kwargs
        )

class LinearIntegrationNode(IntegrationNode):
    '''Akin to an IntegrationNode with integration_type = 'Linear'.'''
    def __init__(self, integration_id:str, action:str, 
            inputs:dict[str, list[NodeOutput]], 
            api_key:str=None, public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Linear',
            integration_id=integration_id,
            action=action,
            inputs=inputs,
            api_key=api_key,
            public_key=public_key,
            private_key=private_key,
            **kwargs
        )

class SlackIntegrationNode(IntegrationNode):
    '''Akin to an IntegrationNode with integration_type = 'Slack'.'''
    def __init__(self, integration_id:str, action:str, 
            inputs:dict[str, list[NodeOutput]], 
            api_key:str=None, public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Slack',
            integration_id=integration_id,
            action=action,
            inputs=inputs,
            api_key=api_key,
            public_key=public_key,
            private_key=private_key,
            **kwargs
        )

class DiscordIntegrationNode(IntegrationNode):
    '''Akin to an IntegrationNode with integration_type = 'Discord'.'''
    def __init__(self, integration_id:str, action:str, 
            inputs:dict[str, list[NodeOutput]], 
            api_key:str=None, public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Discord',
            integration_id=integration_id,
            action=action,
            inputs=inputs,
            api_key=api_key,
            public_key=public_key,
            private_key=private_key,
            **kwargs
        )

class CopperIntegrationNode(IntegrationNode):
    '''Akin to an IntegrationNode with integration_type = 'Copper'.'''
    def __init__(self, integration_id:str, action:str, 
            inputs:dict[str, list[NodeOutput]], 
            api_key:str=None, public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Copper',
            integration_id=integration_id,
            action=action,
            inputs=inputs,
            api_key=api_key,
            public_key=public_key,
            private_key=private_key,
            **kwargs
        )

class GoogleSheetsIntegrationNode(IntegrationNode):
    '''Akin to an IntegrationNode with integration_type = 'Google Sheets'.'''
    def __init__(self, integration_id:str, action:str, 
            inputs:dict[str, list[NodeOutput]], 
            api_key:str=None, public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Google Sheets',
            integration_id=integration_id,
            action=action,
            inputs=inputs,
            api_key=api_key,
            public_key=public_key,
            private_key=private_key,
            **kwargs
        )

class GoogleDocsIntegrationNode(IntegrationNode):
    '''Akin to an IntegrationNode with integration_type = 'Google Docs'.'''
    def __init__(self, integration_id:str, action:str, 
            inputs:dict[str, list[NodeOutput]], 
            api_key:str=None, public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Google Docs',
            integration_id=integration_id,
            action=action,
            inputs=inputs,
            api_key=api_key,
            public_key=public_key,
            private_key=private_key,
            **kwargs
        )

class GoogleCalendarIntegrationNode(IntegrationNode):
    '''Akin to an IntegrationNode with integration_type = 'Google Calendar'.'''
    def __init__(self, integration_id:str, action:str, 
            inputs:dict[str, list[NodeOutput]], 
            api_key:str=None, public_key:str=None, private_key:str=None, **kwargs):
        super().__init__(
            integration_type='Google Calendar',
            integration_id=integration_id,
            action=action,
            inputs=inputs,
            api_key=api_key,
            public_key=public_key,
            private_key=private_key,
            **kwargs
        )

###############################################################################
# LLMS                                                                        #
###############################################################################

class OpenAILLMNode(NodeTemplate):
    '''
    Represents an OpenAI LLM. These models take in two main inputs: one "system" input that describes the background or context for generating the text, and one input for the prompt itself. For instance, the system input could be used for telling the model that it is an assistant for a specific task, and the prompt input could be a task-related question. Optionally, text variables can be inserted into the system and prompt in an analogous manner to TextNode.

    Inputs:
    - system_input: The output corresponding to the system prompt. Should have data type Text. Can also be a string.
    - prompt_input: The output corresponding to the prompt. Should have data type Text. Can also be a string.
    - text_inputs: A map of text variable names to NodeOutputs expected to produce the text for the system and prompt, if they are strings containing text variables. Each NodeOutput should have data type Text. Each text variable in system_input and prompt_input, if they are strings, should be included as a key in text_inputs. When the pipeline is run, each NodeOutput's contents are interpreted as text and substituted into the variable's places. 

    Parameters:
    - model: The specific OpenAI model to use.
    - max_tokens: How many tokens the model should generate at most. Note that the number of tokens in the provided system and prompt are included in this number.
    - temperature: The temperature used by the model for text generation. Higher temperatures generate more diverse but possibly irregular text.
    - top_p: If top-p sampling is used, controls the threshold probability. Under standard text generation, only the most probable next token is used to generate text; under top-p sampling, the choice is made randomly among all tokens (if they exist) with predicted probability greater than the provided parameter p. Should be between 0 and 1.
    - stream_response:  A flag setting whether or not to return the model output as a stream or one response.
    - json_response: A flag setting whether or not to return the model output in JSON format.
    - personal_api_key: An optional parameter to provide if you have a personal OpenAI account and wish to use your API key.

    Outputs:
    - response: The generated text, with data type Text. 
    '''
    def __init__(self, model:str, 
            system_input:str|NodeOutput, prompt_input:str|NodeOutput,
            text_inputs:dict[str, NodeOutput]={},
            max_tokens:int=DEFAULT_MAX_TOKENS, 
            temperature:float=DEFAULT_TEMPERATURE,
            top_p:float=DEFAULT_TOP_P,
            stream_response:bool = False, json_response:bool = False, 
            personal_api_key:str = None, **kwargs):
        super().__init__()
        self.node_type = 'llmOpenAI'
        self.category = 'task'
        self.task_name = 'llm_openai'
        if model not in SUPPORTED_OPENAI_LLMS.keys():
            raise ValueError(f'OpenAILLMNode: invalid model {model}.')
        self.model = model 
        self.stream_response = stream_response 
        self.json_response = json_response
        # assume if a personal API key is provided, it's being used
        self.personal_api_key = "" 
        if personal_api_key:
            self.personal_api_key = personal_api_key
        self.max_tokens, self.temp, self.top_p = max_tokens, temperature, top_p
        if self.max_tokens < 0:
            raise ValueError(f'OpenAILLMNode: invalid max_tokens value.')
        if self.max_tokens > SUPPORTED_OPENAI_LLMS[self.model]:
            raise ValueError(f'OpenAILLMNode: max_tokens {self.max_tokens} is too large for model {self.model}.')
        if self.temp < 0. or self.temp > 1.:
            raise ValueError(f'OpenAILLMNode: invalid temperature value.')
        if self.top_p <= 0.:
            raise ValueError(f'OpenAILLMNode: invalid top_p value.')
        # Store the inputs that are NodeOutputs vs. those that are strings
        # in separate dicts. For those that are strings, find text variables
        # which should be provided in text_inputs. See comments in TextNode
        self._inputs = {}
        self.all_text_inputs : dict[str, list[NodeOutput]] = {
            k: [v] for k, v in text_inputs.items()
        }
        self.system_text, self.prompt_text = '', ''
        self.system_text_vars, self.prompt_text_vars = [], []
        if type(system_input) == str:
            self.system_text = system_input
            self.system_text_vars = find_text_vars(self.system_text)
        else:
            self._inputs['system'] = [system_input]
        if type(prompt_input) == str:
            self.prompt_text = prompt_input 
            self.prompt_text_vars = find_text_vars(self.prompt_text)
        else:
            self._inputs['prompt'] = [prompt_input]
        check_text_vars(
            self.system_text_vars + self.prompt_text_vars, 
            self.all_text_inputs.keys()
        )
        # the _inputs keys are 'system', 'prompt', and any text var names
        for k, v in self.all_text_inputs.items():
            if k in self.system_text_vars or k in self.prompt_text_vars:
                self._inputs[k] = v
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            for k, v in self._inputs.items():
                check_type(f'OpenAILLMNode input {k}', v[0], TEXT_TYPE)

    def set_system(self, system_input:str|NodeOutput):
        if type(system_input) == NodeOutput:
            check_type('OpenAILLMNode input system', system_input, TEXT_TYPE)
            self.system_text, self.system_text_vars = '', []
            # update _inputs to remove any potential unused text vars
            self._inputs['system'] = [system_input]
            for k in list(self._inputs.keys()):
                if k not in ['system', 'prompt'] + self.prompt_text_vars:
                    del self._inputs[k]
        else:
            self.system_text = system_input
            self.system_text_vars = find_text_vars(self.system_text)
            check_text_vars(
                self.system_text_vars, 
                self.all_text_inputs.keys()
            )
            new_inputs = {
                k: v for k, v in self.all_text_inputs if k in self.system_text_vars + self.prompt_text_vars
            }
            if 'prompt' in self._inputs.keys(): 
                new_inputs['prompt'] = self._inputs['prompt']
            self._inputs = new_inputs

    def set_prompt(self, prompt_input:str|NodeOutput):
        if type(prompt_input) == NodeOutput:
            check_type('OpenAILLMNode input prompt', prompt_input, TEXT_TYPE)
            self.prompt_text, self.prompt_text_vars = '', []
            # update _inputs to remove any potential unused text vars
            self._inputs['prompt'] = [prompt_input]
            for k in list(self._inputs.keys()):
                if k not in ['system', 'prompt'] + self.system_text_vars:
                    del self._inputs[k]
        else:
            self.prompt_text = prompt_input
            self.prompt_text_vars = find_text_vars(self.prompt_text)
            check_text_vars(
                self.prompt_text_vars, 
                self.all_text_inputs.keys()
            )
            new_inputs = {
                k: v for k, v in self.all_text_inputs if k in self.system_text_vars + self.prompt_text_vars
            }
            if 'system' in self._inputs.keys():
                new_inputs['system'] = self._inputs['system']
            self._inputs = new_inputs

    def set_text_input(self, text_var:str, input:NodeOutput):
        check_type(f'OpenAILLMNode text input {text_var}', input, TEXT_TYPE)
        self.all_text_inputs[text_var] = [input]

    def remove_text_input(self, text_var:str):
        if text_var in self.system_text_vars + self.prompt_text_vars:
            raise ValueError(f'OpenAILLMNode: text variable {text_var} is being used.')
        del self.all_text_inputs[text_var]

    def set_text_inputs(self, text_inputs:dict[str, NodeOutput]):
        check_text_vars(self.system_text_vars + self.prompt_text_vars, text_inputs.keys())
        for k, v in text_inputs.items():
            check_type(f'OpenAILLMNode text input {k}', v, TEXT_TYPE)
        self.all_text_inputs = {k: [v] for k, v in text_inputs}
        for k in self._inputs.keys():
            if k in self.all_text_inputs.keys():
                self._inputs[k] = self.all_text_inputs[k]

    def set_model(self, model:str):
        if model not in SUPPORTED_OPENAI_LLMS.keys():
            raise ValueError(f'OpenAILLMNode: invalid model {model}.')
        self.model = model 

    def set_max_tokens(self, max_tokens:int):
        if max_tokens < 0:
            raise ValueError(f'OpenAILLMNode: invalid max_tokens value.')
        if max_tokens > SUPPORTED_OPENAI_LLMS[self.model]:
            raise ValueError(f'OpenAILLMNode: max_tokens {self.max_tokens} is too large for model {self.model}.')
        self.max_tokens = max_tokens
    
    def set_temperature(self, temp:float):
        if temp < 0. or temp > 1.:
            raise ValueError(f'OpenAILLMNode: invalid temperature value.')
        self.temp = temp

    def set_top_p(self, top_p:float):
        if top_p <= 0.:
            raise ValueError(f'OpenAILLMNode: invalid top_p value.')
        self.top_p = top_p
    
    def init_args_strs(self, indicate_id=False):
        system_arg_str = f"system_input='{self.system_text}'"
        prompt_arg_str = f"prompt_input='{self.prompt_text}'"
        if 'system' in self._inputs: 
            system_arg_str = format_node_output_with_name('system_input', self._inputs['system'][0], indicate_id)
        if 'prompt' in self._inputs: 
            prompt_arg_str = format_node_output_with_name('prompt_input', self._inputs['prompt'][0], indicate_id)
        # only prints any variables that are actually used
        text_inputs_arg_dict = {
            k: format_node_output(v[0], indicate_id) \
                for k, v in self._inputs.items() \
                    if k not in ['system', 'prompt']
        }
        args_strs = [
            f"model='{self.model}'",
            system_arg_str,
            prompt_arg_str,
            f'max_tokens={self.max_tokens}' \
                if self.max_tokens != DEFAULT_MAX_TOKENS else None,
            f'temperature={self.temp}' \
                if self.temp != DEFAULT_TEMPERATURE else None,
            f'top_p={self.top_p}' \
                if self.top_p != DEFAULT_TOP_P else None
        ]
        if text_inputs_arg_dict != {}:
            text_inputs_arg_dict_str = text_inputs_arg_dict.__str__().replace('"', '')
            args_strs.append(f'text_inputs={text_inputs_arg_dict_str}')
        return args_strs

    def output(self) -> NodeOutput: 
        return NodeOutput(
            source=self,
            output_field='response', 
            output_data_type=TEXT_TYPE
        )
    
    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self, generic:bool=False):
        json_rep = {
            'model': self.model,
            'system': self.system_text,
            'prompt': self.prompt_text,
            'maxTokens': self.max_tokens,
            'temperature': str(round(self.temp, 2)),
            'topP': str(round(self.top_p, 2)),
            'stream': self.stream_response,
            'jsonResponse': self.json_response,
            'usePersonalAPIKey': self.personal_api_key != '',
            'apiKey': self.personal_api_key,
        }
        if self.system_text_vars:
            json_rep['systemInputNames'] = self.system_text_vars
        if self.prompt_text_vars:
            json_rep['promptInputNames'] = self.prompt_text_vars
        return json_rep
       
    @staticmethod 
    def _from_json_rep(json_data:dict) -> 'OpenAILLMNode':
        text_inputs = {}
        system_input_names = json_data.get('systemInputNames', [])
        prompt_input_names = json_data.get('promptInputNames', [])
        if not system_input_names: system_input_names = []
        if not prompt_input_names: prompt_input_names = []
        for name in system_input_names:
            text_inputs[name] = None
        for name in prompt_input_names:
            text_inputs[name] = None
        return OpenAILLMNode(
            model=json_data['model'],
            system_input=json_data.get('system', None),
            prompt_input=json_data.get('prompt', None),
            text_inputs=text_inputs,
            max_tokens=int(json_data['maxTokens']),
            temperature=float(json_data['temperature']),
            top_p=float(json_data['topP']),
            stream_response=json_data.get('stream', False),
            json_response=json_data.get('jsonResponse', False),
            personal_api_key=json_data['apiKey'] if json_data.get('usePersonalAPIKey', False) else None,
            skip_typecheck=True
        )

# Abstraction of shared methods for node classes representing LLMs which take
# in a single prompt. OpenAILLMNode does not follow this, as it supports both
# a system and a prompt input.
class PromptLLMNode(NodeTemplate):
    '''
    A general class for LLMs which take in a single text prompt input (unlike OpenAILLMNode, which expects two inputs). Optionally, text variables can be inserted into the prompt input in an analogous manner to TextNode. We categorize LLMs into families (e.g. by Anthropic, Meta, etc.), denoted by the llm_family parameter. Each family comes with different models. Each specific model has its own max_tokens limit. 

    Inputs:
    - prompt_input: The output corresponding to the prompt. Should have data type Text. Can also be a string.
    - text_inputs: A map of text variable names to NodeOutputs expected to produce the text for the variables. Each NodeOutput should have data type Text. Each text variables in text should be included as a key in text_inputs. When the pipeline is run, the NodeOutput's contents are interpreted as text and substituted into the variable's places. If text contains no text variables, this can be empty.

    Parameters:
    - llm_family: The overall family of LLMs to use. 
    - model: The specific model within the family of models to use. 
    - max_tokens: How many tokens the model should generate at most. Note that the number of tokens in the provided system and prompt are included in this number. 
    - temperature: The temperature used by the model for text generation. Higher temperatures generate more diverse but possibly irregular text.
    - top_p: If top-p sampling is used, controls the threshold probability. Under standard text generation, only the most probable next token is used to generate text; under top-p sampling, the choice is made randomly among all tokens (if they exist) with predicted probability greater than the provided parameter p. Should be between 0 and 1.

    Outputs:
    - response: The generated text, with data type Text.
    '''
    def __init__(self, llm_family:str, model:str, 
            prompt_input:str|NodeOutput, 
            text_inputs:dict[str, NodeOutput]={}, 
            max_tokens:int=DEFAULT_MAX_TOKENS, 
            temperature:float=DEFAULT_TEMPERATURE, 
            top_p:float=DEFAULT_TOP_P,
            **kwargs):
        super().__init__()
        if llm_family not in PROMPT_LLM_FAMILIES.keys():
            raise ValueError(f'PromptLLMNode: Invalid LLM type {llm_family}.')
        llm_details = PROMPT_LLM_FAMILIES[llm_family]
        self.node_type = llm_details['node_type']
        self.category = 'task'
        self.task_name = llm_details['task_name']
        self.class_name = llm_details['node_class_name']
        # corresponds to a const SUPPORTED_*_LLMS
        self.models:dict[str, int] = llm_details['models']
        if model not in self.models.keys():
            raise ValueError(f'{self.class_name}: invalid model {model}.')
        self.model = model 
        if max_tokens < 0:
            raise ValueError(f'{self.class_name}: invalid max_tokens value {max_tokens}.')
        if max_tokens > self.models[self.model]:
            raise ValueError(f'{self.class_name}: max_tokens {max_tokens} is too large for model {self.model}.')
        if temperature < 0. or temperature > 1.:
            raise ValueError(f'{self.class_name}: invalid temperature value {temperature}.')
        if top_p <= 0.:
            raise ValueError(f'{self.class_name}: invalid top_p value {top_p}.')
        self.max_tokens, self.temp, self.top_p = max_tokens, temperature, top_p
        # these nodes support text variables
        self._inputs = {}
        self.all_text_inputs = {
            k: [v] for k, v in text_inputs.items()
        }
        self.prompt_text, self.prompt_text_vars = '', []
        if type(prompt_input) == str:
            self.prompt_text = prompt_input 
            self.prompt_text_vars = find_text_vars(self.prompt_text)
        else:
            self._inputs['prompt'] = [prompt_input]
        check_text_vars(self.prompt_text_vars, self.all_text_inputs.keys())
        for k, v in self.all_text_inputs.items():
            if k in self.prompt_text_vars:
                self._inputs[k] = v
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            for k, v in self._inputs.items():
                check_type(f'PromptLLMNode input {k}', v[0], TEXT_TYPE)

    def set_prompt(self, prompt_input:str|NodeOutput):
        if type(prompt_input) == NodeOutput:
            check_type(f'{self.class_name} input prompt', prompt_input, TEXT_TYPE)
            # no text variables if the prompt is a NodeOutput
            self._inputs = {'prompt': [prompt_input]}
        else:
            self.prompt_text = prompt_input 
            self.prompt_text_vars = find_text_vars(self.prompt_text)
            check_text_vars(
                self.prompt_text_vars, 
                self.all_text_inputs.keys()
            )
            self._inputs = {
                k: v for k, v in self.all_text_inputs if k in self.prompt_text_vars
            }

    def set_text_input(self, text_var:str, input:NodeOutput):
        check_type(f'{self.class_name} text input {text_var}', input, TEXT_TYPE)
        self.all_text_inputs[text_var] = [input]

    def remove_text_input(self, text_var:str):
        if text_var in self.prompt_text_vars:
            raise ValueError(f'{self.class_name}: text variable {text_var} is being used.')
        del self.all_text_inputs[text_var]

    def set_text_inputs(self, text_inputs:dict[str, NodeOutput]):
        check_text_vars(self.prompt_text_vars, text_inputs.keys())
        for k, v in text_inputs.items():
            check_type(f'{self.class_name} text input {k}', v, TEXT_TYPE)
        self.all_text_inputs = {k: [v] for k, v in text_inputs}
        for k in self._inputs.keys():
            if k in self.all_text_inputs.keys():
                self._inputs[k] = self.all_text_inputs[k]

    def set_model(self, model:str):
        if model not in self.models.keys():
            raise ValueError(f'{self.class_name}: invalid model {model}.')
        self.model = model 

    def set_max_tokens(self, max_tokens:int):
        if max_tokens < 0:
            raise ValueError(f'{self.class_name}: invalid max_tokens value {max_tokens}.')
        if max_tokens > SUPPORTED_ANTHROPIC_LLMS[self.model]:
            raise ValueError(f'{self.class_name}: max_tokens {self.max_tokens} is too large for model {self.model}.')
        self.max_tokens = max_tokens
    
    def set_temperature(self, temperature:float):
        if temperature < 0. or temperature > 1.:
            raise ValueError(f'{self.class_name}: invalid temperature value {temperature}.')
        self.temp = temperature

    def set_top_p(self, top_p:float):
        if top_p <= 0.:
            raise ValueError(f'{self.class_name}: invalid top_p value {top_p}.')
        self.top_p = top_p

    def init_args_strs(self, indicate_id=False):
        prompt_arg_str = f"prompt_input='{self.prompt_text}'"
        if 'prompt' in self._inputs and type(self._inputs['prompt'][0]) == NodeOutput:
            prompt_arg_str = format_node_output_with_name('prompt_input', self._inputs['prompt'][0], indicate_id)
        # only prints any variables that are actually used
        text_inputs_arg_dict = {
            k: format_node_output(v[0], indicate_id) \
                for k, v in self._inputs.items() \
                    if k not in ['system', 'prompt']
        }
        args_strs = [
            f"model='{self.model}'",
            prompt_arg_str, 
            f'max_tokens={self.max_tokens}' \
                if self.max_tokens != DEFAULT_MAX_TOKENS else None,
            f'temperature={self.temp}' \
                if self.temp != DEFAULT_TEMPERATURE else None,
            f'top_p={self.top_p}' if self.top_p != DEFAULT_TOP_P else None
        ]
        if text_inputs_arg_dict != {}:
            text_inputs_arg_dict_str = text_inputs_arg_dict.__str__().replace('"', '')
            args_strs.append(f'text_inputs={text_inputs_arg_dict_str}')
        return args_strs
    
    def output(self) -> NodeOutput:
        return NodeOutput(
            source=self, 
            output_field='response', 
            output_data_type=TEXT_TYPE
        )
    
    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self, generic:bool=False):
        json_rep = {
            'model': self.model,
            'prompt': self.prompt_text,
            'maxTokens': self.max_tokens,
            'temperature': str(round(self.temp, 2)),
            'topP': str(round(self.top_p, 2)),
        }
        if self.prompt_text_vars:
            json_rep['promptInputNames'] = self.prompt_text_vars
        return json_rep
    
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'PromptLLMNode':
        text_inputs = {}
        prompt_input_names = json_data.get('promptInputNames', [])
        if not prompt_input_names: prompt_input_names = []
        for name in prompt_input_names:
            text_inputs[name] = None
        llm_family = ''
        for family, details in PROMPT_LLM_FAMILIES.items():
            if details['task_name'] == json_data['task_name']:
                llm_family = family
        return PromptLLMNode(
            llm_family=llm_family,
            model=json_data['model'],
            prompt_input=json_data.get('prompt', None),
            text_inputs=text_inputs,
            max_tokens=int(json_data['maxTokens']),
            temperature=float(json_data['temperature']),
            top_p=float(json_data['topP']),
            skip_typecheck=True
        )

class AnthropicLLMNode(PromptLLMNode):
    '''Akin to a PromptLLMNode with llm_family = 'anthropic'.'''
    def __init__(self, model:str, 
            prompt_input:str|NodeOutput, 
            text_inputs:dict[str, NodeOutput]={}, 
            max_tokens:int=DEFAULT_MAX_TOKENS, 
            temperature:float=DEFAULT_TEMPERATURE, 
            top_p:float=DEFAULT_TOP_P,
            **kwargs):
        super().__init__(
            llm_family='anthropic',
            model=model, 
            prompt_input=prompt_input,
            text_inputs=text_inputs,
            max_tokens=max_tokens, 
            temperature=temperature, 
            top_p=top_p, 
            **kwargs
        )
        
class CohereLLMNode(PromptLLMNode):
    '''Akin to a PromptLLMNode with llm_family = 'cohere'.'''
    def __init__(self, model:str, 
            prompt_input:str|NodeOutput, 
            text_inputs:dict[str, NodeOutput]={}, 
            max_tokens:int=DEFAULT_MAX_TOKENS, 
            temperature:float=DEFAULT_TEMPERATURE, 
            top_p:float=DEFAULT_TOP_P,
            **kwargs):
        super().__init__(
            llm_family='cohere',
            model=model, 
            prompt_input=prompt_input,
            text_inputs=text_inputs,
            max_tokens=max_tokens, 
            temperature=temperature, 
            top_p=top_p, 
            **kwargs
        )

class AWSLLMNode(PromptLLMNode):
    '''Akin to a PromptLLMNode with llm_family = 'aws'.'''
    def __init__(self, model:str, 
            prompt_input:str|NodeOutput, 
            text_inputs:dict[str, NodeOutput]={}, 
            max_tokens:int=DEFAULT_MAX_TOKENS, 
            temperature:float=DEFAULT_TEMPERATURE, 
            top_p:float=DEFAULT_TOP_P,
            **kwargs):
        super().__init__(
            llm_family='aws',
            model=model, 
            prompt_input=prompt_input,
            text_inputs=text_inputs,
            max_tokens=max_tokens, 
            temperature=temperature, 
            top_p=top_p, 
            **kwargs
        )
    
class MetaLLMNode(PromptLLMNode):
    '''Akin to a PromptLLMNode with llm_family = 'meta'.'''
    def __init__(self, model:str, 
            prompt_input:str|NodeOutput, 
            text_inputs:dict[str, NodeOutput]={}, 
            max_tokens:int=DEFAULT_MAX_TOKENS, 
            temperature:float=DEFAULT_TEMPERATURE, 
            top_p:float=DEFAULT_TOP_P,
            **kwargs):
        super().__init__(
            llm_family='meta',
            model=model, 
            prompt_input=prompt_input,
            text_inputs=text_inputs,
            max_tokens=max_tokens, 
            temperature=temperature, 
            top_p=top_p, 
            **kwargs
        )

class OpenSourceLLMNode(PromptLLMNode):
    '''Akin to a PromptLLMNode with llm_family = 'open_source'.'''
    def __init__(self, model:str, 
            prompt_input:str|NodeOutput, 
            text_inputs:dict[str, NodeOutput]={}, 
            max_tokens:int=DEFAULT_MAX_TOKENS, 
            temperature:float=DEFAULT_TEMPERATURE, 
            top_p:float=DEFAULT_TOP_P,
            **kwargs):
        super().__init__(
            llm_family='open_source',
            model=model, 
            prompt_input=prompt_input,
            text_inputs=text_inputs,
            max_tokens=max_tokens, 
            temperature=temperature, 
            top_p=top_p, 
            **kwargs
        )

class GoogleLLMNode(PromptLLMNode):
    '''Akin to a PromptLLMNode with llm_family = 'google'.'''
    def __init__(self, model:str, 
            prompt_input:str|NodeOutput, 
            text_inputs:dict[str, NodeOutput]={}, 
            max_tokens:int=DEFAULT_MAX_TOKENS, 
            temperature:float=DEFAULT_TEMPERATURE,
            top_p:float=DEFAULT_TOP_P,
            **kwargs):
        super().__init__(
            llm_family='google',
            model=model, 
            prompt_input=prompt_input,
            text_inputs=text_inputs,
            max_tokens=max_tokens, 
            temperature=temperature, 
            top_p=top_p, 
            **kwargs
        )

###############################################################################
# MULTIMODAL                                                                  #
###############################################################################

class ImageGenNode(NodeTemplate):
    '''
    Represents a text-to-image generative model.

    Inputs:
    - prompt_input: The text prompt for generating the image(s). Should have data type Text.

    Parameters:
    - model: The specific text-to-image model used.
    - image_size: The size of the image (e.g. if this is set to 512, then 512 x 512 images will be generated; if set to a tuple (a, b), then a x b images will be generated). Must be one of the valid sizes for the model as listed above.
    - num_images: The number of images to generate.  Must be one of the valid numbers for the model as listed above.

    Outputs:
    - images: The generated image(s), with data type List[ImageFile].
    '''
    def __init__(self, model:str, 
            image_size:int|tuple[int,int], num_images:int, 
            prompt_input:str|NodeOutput, 
            text_inputs:dict[str, NodeOutput]={}, **kwargs):
        super().__init__()
        self.node_type = 'imageGen'
        self.category = 'task'
        self.task_name = 'generate_image'
        if model not in SUPPORTED_IMAGE_GEN_MODELS.keys():
            raise ValueError(f'ImageGenNode: invalid model {model}.')
        # models like DALL-E are represented with dots in the database
        self.model = model
        if image_size not in SUPPORTED_IMAGE_GEN_MODELS[self.model][0]:
            raise ValueError(f'ImageGenNode: Invalid image size {image_size}.')
        if num_images not in SUPPORTED_IMAGE_GEN_MODELS[self.model][1]:
            raise ValueError(f'ImageGenNode: Invalid number of images {num_images}.')
        self.image_size = image_size 
        self.num_images = num_images 
        # this node also supports text vars
        self._inputs = {}
        self.all_text_inputs = {
            k: [v] for k, v in text_inputs.items()
        }
        self.prompt_text, self.prompt_str_vars = '', []
        if type(prompt_input) == NodeOutput or prompt_input is None:
            self._inputs['prompt'] = [prompt_input]
        else:
            self.prompt_text = prompt_input 
            self.prompt_text_vars = find_text_vars(self.prompt_text)
            check_text_vars(self.prompt_text_vars, self.all_text_inputs.keys())
            for k, v in self.all_text_inputs.items():
                if k in self.prompt_text_vars:
                    self._inputs[k] = v
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            for k, v in self._inputs.items():
                check_type(f'ImageGenNode input {k}', v[0], TEXT_TYPE)

    def set_prompt(self, prompt_input:str|NodeOutput):
        if type(prompt_input) == NodeOutput:
            check_type('ImageGenNode input prompt', prompt_input, TEXT_TYPE)
            # no text variables if the prompt is a NodeOutput
            self._inputs = {'prompt': [prompt_input]}
        else:
            self.prompt_text = prompt_input 
            self.prompt_text_vars = find_text_vars(self.prompt_text)
            check_text_vars(
                self.prompt_text_vars, 
                self.all_text_inputs.keys()
            )
            self._inputs = {
                k: v for k, v in self.all_text_inputs if k in self.prompt_text_vars
            }

    def set_text_input(self, text_var:str, input:NodeOutput):
        check_type(f'ImageGenNode text input {text_var}', input, TEXT_TYPE)
        self.all_text_inputs[text_var] = [input]

    def remove_text_input(self, text_var:str):
        if text_var in self.prompt_text_vars:
            raise ValueError(f'ImageGenNode: text variable {text_var} is being used.')
        del self.all_text_inputs[text_var]

    def set_text_inputs(self, text_inputs:dict[str, NodeOutput]):
        check_text_vars(self.prompt_text_vars, text_inputs.keys())
        for k, v in text_inputs.items():
            check_type(f'ImageGenNode text input {k}', v, TEXT_TYPE)
        self.all_text_inputs = {k: [v] for k, v in text_inputs}
        for k in self._inputs.keys():
            if k in self.all_text_inputs.keys():
                self._inputs[k] = self.all_text_inputs[k]

    def set_model_params(self, model:str, image_size:int|tuple[int,int], num_images:int):
        if model not in SUPPORTED_IMAGE_GEN_MODELS.keys():
            raise ValueError(f'AnthropicLLMNode: invalid model {model}.')
        self.model = model 
        if image_size not in SUPPORTED_IMAGE_GEN_MODELS[self.model][0]:
            raise ValueError(f'ImageGenNode: Invalid image size {image_size}.')
        if num_images not in SUPPORTED_IMAGE_GEN_MODELS[self.model][1]:
            raise ValueError(f'ImageGenNode: Invalid number of images {num_images}.')
        self.image_size = image_size 
        self.num_images = num_images 
    
    def init_args_strs(self, indicate_id=False):
        prompt_arg_str = f"prompt_input='{self.prompt_text}'"
        if 'prompt' in self._inputs and type(self._inputs['prompt'][0]) == NodeOutput:
            prompt_arg_str = format_node_output_with_name('prompt_input', self._inputs['prompt'][0], indicate_id)
        # only prints any variables that are actually used
        text_inputs_arg_dict = {
            k: format_node_output(v[0], indicate_id) \
                for k, v in self._inputs.items() \
                    if k not in ['system', 'prompt']
        }
        args_strs = [
            f"model='{self.model}'",
            f'image_size={self.image_size}',
            f'num_images={self.num_images}',
            prompt_arg_str
        ]
        if text_inputs_arg_dict != {}:
            text_inputs_arg_dict_str = text_inputs_arg_dict.__str__().replace('"', '')
            args_strs.append(f'text_inputs={text_inputs_arg_dict_str}')
        return args_strs

    def output(self) -> NodeOutput:
        return NodeOutput(
            source=self, 
            output_field='images', 
            output_data_type=ListType(IMAGE_FILE_TYPE)
        )
    
    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self, generic:bool=False):
        size = f'{self.image_size}x{self.image_size}' \
            if type(self.image_size) == int \
            else f'{self.image_size[0]}x{self.image_size[1]}'
        json_rep = {
            'model': self.model.replace('DALL-E', 'DALL·E'),
            'prompt': self.prompt_text,
            'size': size,
            'imageCount': self.num_images,
        }
        if self.prompt_text_vars:
            json_rep['promptInputNames'] = self.prompt_text_vars
        return json_rep
        
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'ImageGenNode':
        image_size_str = json_data['size']
        x_coord = image_size_str.index('x')
        image_size = (
            int(image_size_str[:x_coord]), 
            int(image_size_str[x_coord+1:])
        )
        if image_size[0] == image_size[1]:
            image_size = image_size[0]
        text_inputs = {}
        prompt_input_names = json_data.get('promptInputNames', [])
        if not prompt_input_names: prompt_input_names = []
        for name in prompt_input_names:
            text_inputs[name] = None
        return ImageGenNode(
            model=json_data['model'].replace('DALL·E', 'DALL-E'),
            image_size=image_size,
            num_images=int(json_data['imageCount']),
            prompt_input=json_data.get('prompt', None),
            text_inputs=text_inputs,
            skip_typecheck=True
        )
    
class SpeechToTextNode(NodeTemplate):
    '''
    Represents a speech-to-text generative model.

    Inputs:
    - audio_input: The audio file to be converted to text. Should have data type AudioFile.

    Parameters:
    - model: The specific speech-to-text model to use. We currently only support the model OpenAI Whisper.

    Outputs:
    - text: The transcribed text, with data type Text.
    '''
    def __init__(self, model:str, audio_input:NodeOutput, **kwargs):
        super().__init__()
        self.node_type = 'speechToText'
        self.category = 'task'
        self.task_name = 'speech_to_text'
        if model not in SUPPORTED_SPEECH_TO_TEXT_MODELS:
            raise ValueError(f'SpeechToTextNode: invalid model {model}.')
        self.model = model
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            check_type('ImageGenNode input audio', audio_input, AUDIO_FILE_TYPE)
        self._inputs = {'audio': [audio_input]}

    def set_model(self, model:str):
        if model not in SUPPORTED_SPEECH_TO_TEXT_MODELS:
            raise ValueError(f'SpeechToTextNode: invalid model {model}.')
        self.model = model

    def set_audio_input(self, audio_input:NodeOutput):
        check_type('ImageGenNode input audio', audio_input, AUDIO_FILE_TYPE)
        self._inputs['audio'] = [audio_input]
    
    def init_args_strs(self, indicate_id=False):
        audio_input = self._inputs['audio'][0]
        return [
            f"model='{self.model}'",
            format_node_output_with_name('audio_input', audio_input, indicate_id)
        ]

    def output(self) -> NodeOutput:
        return NodeOutput(
            source=self, 
            output_field='output', 
            output_data_type=TEXT_TYPE
        )
    
    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self, generic:bool=False):
        return {'model': self.model}
        
    @staticmethod 
    def _from_json_rep(json_data:dict) -> 'SpeechToTextNode':
        return SpeechToTextNode(
            model=json_data['model'],
            audio_input=None,
            skip_typecheck=True
        )

# Currently, ImageToText has a structure very similar to OpenAILLMNode, so
# we just subclass.
class ImageToTextNode(OpenAILLMNode):
    '''
    Represents an (OpenAI) image-to-text LLM. These models take in three main inputs: a system and prompt input analogous to OpenAILLMNode, and an image input. Text variables can be optionally inserted.

    Inputs:
    - system_input: The output corresponding to the system prompt. Should have data type Text. Can also be a string.
    - prompt_input: The output corresponding to the prompt. Should have data type Text. Can also be a string.
    - text_inputs: A map of text variable names to NodeOutputs expected to produce the text for the system and prompt, if they are strings containing text variables. Each NodeOutput should have data type Text. Each text variable in system_input and prompt_input, if they are strings, should be included as a key in text_inputs. When the pipeline is run, each NodeOutput's contents are interpreted as text and substituted into the variable's places.
    - image_input: The output corresponding to the image. Should have data type ImageFile.

    Parameters:
    - model: The specific OpenAI model to use.
    - max_tokens: How many tokens the model should generate at most. Note that the number of tokens in the provided system and prompt are included in this number.
    - temperature: The temperature used by the model for text generation. Higher temperatures generate more diverse but possibly irregular text.
    - top_p: If top-p sampling is used, controls the threshold probability. Under standard text generation, only the most probable next token is used to generate text; under top-p sampling, the choice is made randomly among all tokens (if they exist) with predicted probability greater than the provided parameter p. Should be between 0 and 1.
    - stream_response:  A flag setting whether or not to return the model output as a stream or one response.
    - json_response: A flag setting whether or not to return the model output in JSON format.
    - personal_api_key: An optional parameter to provide if you have a personal OpenAI account and wish to use your API key.

    Outputs:
    - response: The generated text, with data type Text. 
    '''
    def __init__(self, model:str, 
        system_input:str|NodeOutput, prompt_input:str|NodeOutput,
        image_input:NodeOutput,
        text_inputs:dict[str, NodeOutput]={},
        max_tokens:int=DEFAULT_MAX_TOKENS, 
        temperature:float=DEFAULT_TEMPERATURE,
        top_p:float=DEFAULT_TOP_P,
        stream_response:bool = False, json_response:bool = False, 
        personal_api_key:str = None, **kwargs):
        super().__init__(model, system_input, prompt_input, text_inputs, max_tokens, temperature, top_p, stream_response, json_response, personal_api_key)
        self.node_type = 'llmOpenAIVision'
        self.task_name = 'image_to_text'
        if model not in SUPPORTED_IMAGE_TO_TEXT_MODELS:
            raise ValueError(f'OpenAILLMNode (ImageToTextNode): invalid model {model}.')
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            check_type(f'OpenAILLMNode (ImageToTextNode) input image', image_input, IMAGE_FILE_TYPE)
        self._inputs['image'] = [image_input]

    def set_image(self, image_input:NodeOutput):
        check_type(f'OpenAILLMNode (ImageToTextNode) input image', image_input, IMAGE_FILE_TYPE)
        self._inputs['image'] = [image_input]

    def set_model(self, model:str):
        if model not in SUPPORTED_IMAGE_TO_TEXT_MODELS:
            raise ValueError(f'OpenAILLMNode (ImageToTextNode): invalid model {model}.')
        self.model = model

    def init_args_strs(self, indicate_id=False):
        args_strs = super().init_args_strs(indicate_id)
        image_input_arg_str = format_node_output_with_name('image_input', self._inputs['image'][0], indicate_id)
        return args_strs[:3] + [image_input_arg_str] + args_strs[3:]

    def output(self) -> NodeOutput:
        return NodeOutput(
            source=self,
            output_field='response',
            output_data_type=TEXT_TYPE
        )
    
    def outputs(self):
        o = self.output()
        return {o.output_field: o}

    @staticmethod 
    def _from_json_rep(json_data:dict) -> 'ImageToTextNode':
        text_inputs = {}
        system_input_names = json_data.get('systemInputNames', [])
        prompt_input_names = json_data.get('promptInputNames', [])
        if not system_input_names: system_input_names = []
        if not prompt_input_names: prompt_input_names = []
        for name in system_input_names:
            text_inputs[name] = None
        for name in prompt_input_names:
            text_inputs[name] = None
        return ImageToTextNode(
            model=json_data['model'],
            system_input=json_data.get('system', None),
            prompt_input=json_data.get('prompt', None),
            image_input=None,
            text_inputs=text_inputs,
            max_tokens=int(json_data['maxTokens']),
            temperature=float(json_data['temperature']),
            top_p=float(json_data['topP']),
            stream_response=json_data.get('stream', False),
            json_response=json_data.get('jsonResponse', False),
            personal_api_key=json_data['apiKey'] if json_data.get('usePersonalAPIKey', False) else None,
            skip_typecheck=True
        )

###############################################################################
# DATALOADERS                                                                #
###############################################################################

class DataLoaderNode(NodeTemplate):
    '''
    A general-purpose node representing the retrieval of data from a third-party source. The names and data types of inputs and outputs are dependent on the specific loader (the loader type). Inputs can either be string parameters or NodeOutputs from earlier nodes.

    For most Data Loaders, the output is a list of documents. The optional parameters chunk_size and chunk_overlap then determine how those documents are formed, specifying the size and stride in tokens of each document. 

    Inputs:
    - inputs: A map of input names to lists of either strings or NodeOutputs, which depends on the specific loader. (If the input field is known, a string can directly be supplied.) Currently each input name maps to a single string or NodeOutput, so only singleton lists are expected. 

    Parameters:
    - loader_type: The specific Data Loader. Should be one of the valid Data Loader types listed below.
    - chunk_size: The maximum size of each document in tokens, if the node returns a List[Document]. 
    - chunk_overlap: The amount of overlap between documents in tokens, if the node returns a [List[Document].

    Outputs:
    - output: The data loaded by the node. The data type depends on the specific loader.
    '''
    def typecheck_inputs(self):
        inputs = {**self._inputs, **self._input_strs}
        match self.loader_type:
            case 'File':
                for f_input in inputs['file']:
                    check_type(
                        'File DataLoader node', 
                        f_input, 
                        UnionType(
                            FILE_TYPE, ListType(FILE_TYPE), 
                            TEXT_TYPE, ListType(TEXT_TYPE)
                        )
                    )
            case 'CSV Query':
                check_type(
                    'CSV Query DataLoader node input query', 
                    inputs['query'][0], TEXT_TYPE, 
                    str_ok=True
                )
                check_type(
                    'CSV Query DataLoader node input csv',
                    inputs['csv'][0], CSV_FILE_TYPE
                )
            case 'URL':
                check_type(
                    'URL DataLoader node input url',
                    inputs['url'][0], URL_TYPE,
                    str_ok=True
                )
            case 'Wikipedia':
                check_type(
                    'Wikipedia DataLoader node input query', 
                    inputs['query'][0], TEXT_TYPE,
                    str_ok=True
                )
            case 'YouTube':
                check_type(
                    'YouTube DataLoader node input url',
                    inputs['url'][0],
                    UnionType(URL_TYPE, ListType(URL_TYPE)),
                    str_ok=True
                )
            case 'Arxiv':
                check_type(
                    'Arxiv DataLoader node input query', 
                    inputs['query'][0], TEXT_TYPE,
                    str_ok=True
                )
            case 'SerpAPI':
                check_type(
                    'SerpAPI DataLoader node input apiKey', 
                    inputs['apiKey'][0], TEXT_TYPE,
                    str_ok=True
                )
                check_type(
                    'SerpAPI DataLoader node input query',
                    inputs['query'][0], TEXT_TYPE
                )
            case 'Git':
                check_type(
                    'Git DataLoader node input repo',
                    inputs['repo'][0], URL_TYPE,
                    str_ok=True
                )
            case 'YOU_DOT_COM', 'YOU_DOT_COM_NEWS':
                check_type(
                    'You.com DataLoader node input query',
                    inputs['query'][0], TEXT_TYPE, 
                    str_ok=True
                )
            case 'EXA_AI_SEARCH', 'EXA_AI_SEARCH_COMPANIES', 'EXA_AI_SEARCH_RESEARCH_PAPERS':
                check_type(
                    'Exa AI DataLoader node input query',
                    inputs['query'][0], TEXT_TYPE, 
                    str_ok=True
                )
            # DEPRECATED
            case 'Notion':
                check_type(
                    'Notion DataLoader node input token', 
                    inputs['token'][0], TEXT_TYPE
                )
                check_type(
                    'Notion DataLoader node input database',
                    inputs['database'][0], TEXT_TYPE
                )
            # DEPRECATED
            case 'Confluence':
                check_type(
                    'Confluence DataLoader node input username', 
                    inputs['username'][0], TEXT_TYPE
                )
                check_type(
                    'Confluence DataLoader node input apiKey',
                    inputs['apiKey'][0], TEXT_TYPE
                )
                check_type(
                    'Confluence DataLoader node input url', 
                    inputs['url'][0], TEXT_TYPE
                )
            case _:
                raise ValueError(f'DataLoaderNode: Unrecognized loader type {self.loader_type}.')

    # inputs can either be NodeOutputs or strings, so inputs is a dictionary of
    # input names to a list of NodeOutputs or a singleton list of strings. 
    def __init__(self, loader_type:str, 
            inputs:dict[str, list[str|NodeOutput]], 
            chunk_size:int=DEFAULT_CHUNK_SIZE, 
            chunk_overlap:int=DEFAULT_CHUNK_OVERLAP, 
            func:str=DEFAULT_LOADER_FUNC, **kwargs):
        super().__init__()
        self.node_type = 'dataLoader'
        self.category = 'task'
        if loader_type not in DATALOADER_PARAMS.keys():
            raise ValueError(f'DataLoaderNode: invalid dataloader type {loader_type}.')
        input_names = DATALOADER_PARAMS[loader_type]['input_names']
        if sorted(list(inputs.keys())) != sorted(input_names):
            raise ValueError(f'DataLoaderNode: inputs do not match expected input names: expected {input_names}')
        self.loader_type = loader_type
        self.task_name = DATALOADER_PARAMS[loader_type]['task_name']
        if chunk_size < 1 or chunk_size > 4096:
            raise ValueError(f'DataLoaderNode: invalid chunk_size value.')
        if chunk_overlap < 0: raise ValueError('DataLoaderNode: invalid chunk_overlap value.')
        if chunk_overlap >= chunk_size:
            raise ValueError(f'DataLoaderNode: chunk_overlap must be smaller than chunk_size.')
        self.chunk_size, self.chunk_overlap, self.func = chunk_size, chunk_overlap, func
        # Store the inputs that are NodeOutputs vs. those that are strings
        # in separate dicts
        self._inputs = {}
        self._input_strs:dict[str, list[str]] = {}
        # only the inputs that are NodeOutputs should be added to _inputs
        if inputs:
            for k, v in inputs.items():
                if len(v) == 0:
                    raise ValueError(f'DataLoaderNode: received no inputs for input name {k}.')
                if type(v[0]) == NodeOutput or v[0] is None:
                    self._inputs[k] = v
                elif type(v[0]) == str:
                    if len(v) != 1:
                        raise ValueError('DataLoaderNode: string inputs should be singleton lists.')
                    self._input_strs[k] = v
                else:
                    raise ValueError(f'DataLoaderNode: input name {k} must be a NodeOutput or a string.')
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            self.typecheck_inputs()

    def set_chunk_size(self, chunk_size:int):
        if chunk_size < 1 or chunk_size > 4096:
            raise ValueError(f'DataLoaderNode: invalid chunk_size value.')
        self.chunk_size = chunk_size 

    def set_chunk_overlap(self, chunk_overlap:int):
        if chunk_overlap < 0: raise ValueError('DataLoaderNode: invalid chunk_overlap value.')
        if chunk_overlap >= self.chunk_size:
            raise ValueError(f'DataLoaderNode: chunk_overlap must be smaller than chunk_size.')
        self.chunk_overlap = chunk_overlap

    def set_func(self, func:str): self.func = func

    def set_input(self, input_name:str, input:str|list[NodeOutput]):
        if type(input) == str:
            if input_name in self._inputs.keys(): 
                del self._inputs[input_name]
            self._input_strs[input_name] = [input]
        else:
            old_input = self._inputs[input_name]
            self._inputs[input_name] = [input]
            try:
                self.typecheck_inputs()
            except ValueError as err:
                self._inputs['value'] = old_input
                raise err

    def set_inputs(self, inputs:dict[str, list[str|NodeOutput]]):
        if sorted(inputs.keys()) != sorted(self._inputs.keys()):
            raise ValueError(f'Invalid input names provided.')
        old_inputs = self._inputs.copy()
        self._inputs = inputs 
        try:
            self.typecheck_inputs()
        except ValueError as err:
            self._inputs = old_inputs
            raise err

    def init_args_strs(self, indicate_id=False):
        inputs_strs = {}
        for k, v in self._inputs.items():
            inputs_strs[k] = format_node_output(v[0], indicate_id)
        for k, v in self._input_strs.items():
            inputs_strs[k] = v
        return [
            f"loader_type='{self.loader_type}'",
            f'inputs={inputs_strs}',
            f'chunk_size={self.chunk_size}' \
                if self.chunk_size != DEFAULT_CHUNK_SIZE else None,
            f'chunk_overlap={self.chunk_overlap}' \
                if self.chunk_overlap != DEFAULT_CHUNK_OVERLAP else None,
            f"func='{self.func}'" if self.func != DEFAULT_LOADER_FUNC else None
        ]

    def output(self) -> NodeOutput: 
        # for most dataloaders the data returned is a document list
        output_data_type = ListType(DOCUMENT_TYPE)
        if self.loader_type in ['CSV Query', 'SerpAPI']:
            output_data_type = TEXT_TYPE
        return NodeOutput(
            source=self,
            output_field='output',
            output_data_type=output_data_type
        )

    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self, generic:bool=False):
        input_strs = {k: v[0] for k, v in self._input_strs}
        return {
            'loaderType': self.loader_type,
            'function': self.func,
            'chunkSize': self.chunk_size,
            'chunkOverlap': self.chunk_overlap,
            # add in string params if they were passed into the constructor
            **input_strs
        }
    
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'DataLoaderNode':
        inputs = {}
        # inputs that were explicitly initialized with strings take the form
        # of additional fields in the JSON, rather than edges
        for k in DATALOADER_PARAMS[json_data['loaderType']]['input_names']:
            if k in json_data.keys():
                inputs[k] = [json_data[k]]
            else:
                inputs[k] = [None]
        return DataLoaderNode(
            loader_type=json_data['loaderType'],
            inputs=inputs,
            chunk_size=int(json_data.get('chunkSize', DEFAULT_CHUNK_SIZE)),
            chunk_overlap=int(json_data.get('chunkOverlap', DEFAULT_CHUNK_OVERLAP)),
            func=json_data['function'],
            skip_typecheck=True
        )

# An API node's implementation is substantially different from other data 
# Data Loaders, so we don't subclass
class ApiLoaderNode(NodeTemplate):
    '''
    A node which executes an API call and returns its results. Constructor inputs essentially defines the parameters of the API call and should all be strings.

    Inputs: None.

    Parameters:
    - method: The API method.
    - url: The API endpoint to call.
    - headers: A list of tuples of strings, representing the headers as key-value pairs.
    - param_type: The types of API parameters, either 'Body' or 'Query'.
    - params: A list of tuples of strings, representing the parameters as key-value pairs.

    Outputs:
    - output: The data returned from the API call, of data type Text. 
    '''
    def __init__(self, method:str, url:str, 
                 headers:list[tuple[str, str]], 
                 param_type:str, params:list[tuple[str, str]], 
                 **kwargs):
        super().__init__()
        self.node_type = 'dataLoader'
        self.category = 'task'
        self.loader_type = 'Api'
        self.task_name = 'load_api'
        if method not in API_LOADER_METHODS:
            raise ValueError(f'ApiLoaderNode: Invalid API endpoint {method}.')
        if param_type not in API_LOADER_PARAM_TYPES:
            raise ValueError(f'ApiLoaderNode: Invalid parameter type {param_type}.')
        self.method = method
        self.param_type = param_type
        self.url = url
        self.headers = headers
        self.params = params
        self._inputs = {}

    def set_url(self, url:str): self.url = url

    def set_method(self, method:str): 
        if method not in API_LOADER_METHODS:
            raise ValueError(f'ApiLoaderNode: Invalid API endpoint {method}.')
        self.method = method 

    def set_param_type(self, param_type:str):
        if param_type not in API_LOADER_PARAM_TYPES:
            raise ValueError(f'ApiLoaderNode: Invalid parameter type {param_type}.')
        self.param_type = param_type
    
    def set_headers(self, headers:list[tuple[str, str]]): 
        self.headers = headers
    
    def set_params(self, params:list[tuple[str, str]]): self.params = params

    def init_args_strs(self, indicate_id=False):
        return [
            f"method='{self.method}'",
            f"url='{self.url}'",
            f'headers={self.headers}',
            f"param_type='{self.param_type}'",
            f'params={self.params}',
        ]
    
    def output(self) -> NodeOutput: 
        return NodeOutput(
            source=self,
            output_field='output',
            output_data_type=TEXT_TYPE
        )

    def outputs(self):
        o = self.output()
        return {o.output_field: o}

    def _to_json_rep(self, generic:bool=False):
        return {
            'loaderType': self.loader_type,
            'method': self.method,
            'url': self.url,
            'headers': [{'key': h[0], 'value': h[1]} for h in self.headers],
            'params': [{'key': p[0], 'value': p[1]} for p in self.params],
            'param': self.param_type,
        }
    
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'ApiLoaderNode':
        return ApiLoaderNode(
            method=json_data['method'],
            url=json_data['url'],
            headers=[(h['key'], h['value']) for h in json_data.get('headers', [])],
            param_type=json_data['param'],
            params=[(p['key'], p['value']) for p in json_data.get('params', [])],
            skip_typecheck=True
        )

class FileLoaderNode(DataLoaderNode):
    '''Akin to a DataLoaderNode with loader_type = 'File' and inputs being {'file': files_input}.'''
    def __init__(self, files_input:list[NodeOutput], **kwargs):
        super().__init__(
            loader_type='File',
            inputs={'file': files_input},
            **kwargs
        )

class CSVQueryLoaderNode(DataLoaderNode):
    '''Akin to a DataLoaderNode with loader_type = 'CSV Query' and inputs being {'query': [query_input], 'csv': [csv_input]}.'''
    def __init__(self, query_input:str|NodeOutput, csv_input:NodeOutput, 
            **kwargs):
        super().__init__(
            loader_type='CSV Query',
            inputs={'query':[query_input], 'csv':[csv_input]},
            **kwargs
        )

class URLLoaderNode(DataLoaderNode):
    '''Akin to instantiating a DataLoaderNode with loader_type = 'URL' and inputs being {'url': [url_input]}.'''
    def __init__(self, url_input:str|NodeOutput, **kwargs):
        super().__init__(
            loader_type='URL',
            inputs={'url':[url_input]},
            **kwargs
        )
        
class WikipediaLoaderNode(DataLoaderNode):
    '''Akin to instantiating a WikipediaLoaderNode with loader_type = 'Wikipedia' and inputs being {'query': [query_input]}.'''
    def __init__(self, query_input:str|NodeOutput, **kwargs):
        super().__init__(
            loader_type='Wikipedia',
            inputs={'query':[query_input]},
            **kwargs
        )

class YouTubeLoaderNode(DataLoaderNode):
    '''Akin to instantiating a DataLoaderNode with loader_type = 'YouTube' and inputs being {'url': [url_input]}.'''
    def __init__(self, url_input:str|NodeOutput, **kwargs):
        super().__init__(
            loader_type='YouTube',
            inputs={'url':[url_input]},
            **kwargs
        )
    
class ArXivLoaderNode(DataLoaderNode):
    '''Akin to a DataLoaderNode with loader_type = 'Arxiv' and inputs being {'query': [query_input]}.'''
    def __init__(self, query_input:str|NodeOutput, **kwargs):
        super().__init__(
            loader_type='Arxiv',
            inputs={'query':[query_input]},
            **kwargs
        )

class SerpAPILoaderNode(DataLoaderNode):
    '''Akin to a DataLoaderNode with loader_type = 'SerpAPI' and inputs being {'apiKey': [api_key_input], 'query': [query_input]}.'''
    def __init__(self, api_key_input:str|NodeOutput, query_input:NodeOutput, **kwargs):
        super().__init__(
            loader_type='SerpAPI',
            inputs={'apiKey':[api_key_input], 'query':[query_input]},
            **kwargs
        )

class GitLoaderNode(DataLoaderNode):
    '''Akin to a DataLoaderNode with loader_type = 'Git' and inputs being {'repo': [repo_input]}.'''
    def __init__(self, repo_input:str|NodeOutput, **kwargs):
        super().__init__(
            loader_type='Git',
            inputs={'repo':[repo_input]},
            **kwargs
        )

class YouDotComLoaderNode(DataLoaderNode):
    '''
    Akin to a DataLoaderNode loading You.com search, with loader_type determined by the search type and inputs being {'query': [query_input]}.
    
    Params: 
    - loader_type: If None, corresponds to 'YOU_DOT_COM'. If 'news', corresponds to 'YOU_DOT_COM_NEWS'.
    '''
    def __init__(self, loader_type:str, query_input:str|NodeOutput, **kwargs):
        loader_type_map = {
            None: 'YOU_DOT_COM',
            'news': 'YOU_DOT_COM_NEWS'
        }
        super().__init__(
            loader_type=loader_type_map[loader_type],
            inputs={'query':[query_input]},
            **kwargs
        )

class ExaAILoaderNode(DataLoaderNode):
    '''
    Akin to a DataLoaderNode loading from Exa AI, with loader_type determined by the search type and inputs being {'query': [query_input]}.
    
    Params: 
    - loader_type: If None, corresponds to 'EXA_AI_SEARCH'. If 'companies', corresponds to 'EXA_AI_SEARCH_COMPANIES'. If 'papers', corresponds to 'EXA_AI_SEARCH_RESEARCH_PAPERS'.
    '''
    def __init__(self, loader_type:str, query_input:str|NodeOutput, **kwargs):
        loader_type_map = {
            None: 'EXA_AI_SEARCH',
            'companies': 'EXA_AI_SEARCH_COMPANIES',
            'papers': 'EXA_AI_SEARCH_RESEARCH_PAPERS'
        }
        super().__init__(
            loader_type=loader_type_map[loader_type],
            inputs={'query':[query_input]},
            **kwargs
        )

# DEPRECATED
class NotionLoaderNode(DataLoaderNode):
    def __init__(self, token_input, database_input, **kwargs):
        super().__init__(
            loader_type='Notion',
            inputs={'token':[token_input], 'database':[database_input]},
            **kwargs
        )

# DEPRECATED
class ConfluenceLoaderNode(DataLoaderNode):
    def __init__(self, username_input, api_key_input, url_input:NodeOutput, **kwargs):
        super().__init__(
            loader_type='Confluence',
            inputs={
                'username':[username_input],
                'apiKey':[api_key_input],
                'url':[url_input]
            },
            **kwargs
        )

###############################################################################
# VECTORDB                                                                    #
###############################################################################

# The implementation of this is akin to that of dataloader nodes.
# DEPRECATED.
class VectorDBLoaderNode(NodeTemplate):
    def __init__(self, documents_input:list[NodeOutput], 
            chunk_size:int=DEFAULT_CHUNK_SIZE, 
            chunk_overlap:int=DEFAULT_CHUNK_OVERLAP, 
            func:str=DEFAULT_LOADER_FUNC, **kwargs):
        super().__init__()
        self.node_type = 'vectorDBLoader'
        self.category = 'task'
        self.task_name = 'load_vector_db'
        if chunk_size < 1 or chunk_size > 4096:
            raise ValueError(f'VectorDBLoaderNode: invalid chunk_size value.')
        if chunk_overlap < 0: raise ValueError('FileNode: invalid chunk_overlap value.')
        if chunk_overlap >= chunk_size:
            raise ValueError(f'VectorDBLoaderNode: chunk_overlap must be smaller than chunk_size.')
        self.chunk_size, self.chunk_overlap, self.func = chunk_size, chunk_overlap, func
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            for d_input in documents_input:
                check_type('VectorDBLoaderNode input documents', d_input, TEXT_TYPE)
        self._inputs = {'documents': documents_input}
    
    def set_chunk_size(self, chunk_size:int):
        if chunk_size < 1 or chunk_size > 4096:
            raise ValueError(f'VectorDBLoaderNode: invalid chunk_size value.')
        self.chunk_size = chunk_size 

    def set_chunk_overlap(self, chunk_overlap:int):
        if chunk_overlap < 0: raise ValueError('DataLoaderNode: invalid chunk_overlap value.')
        if chunk_overlap >= self.chunk_size:
            raise ValueError(f'VectorDBLoaderNode: chunk_overlap must be smaller than chunk_size.')
        self.chunk_overlap = chunk_overlap

    def set_func(self, func:str): self.func = func

    def init_args_strs(self, indicate_id=False):
        documents_input_strs = [
            format_node_output(i, indicate_id)
            for i in self._inputs['documents']
        ]
        return [f'documents_input={documents_input_strs}']

    def output(self) -> NodeOutput:
        return NodeOutput(
            source=self, 
            output_field='database', 
            output_data_type=VECTOR_DB_TYPE
        )

    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self, generic:bool=False):
        return {'function': self.func}
        
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'VectorDBLoaderNode':
        return VectorDBLoaderNode(
            documents_input=None,
            chunk_size=int(json_data.get('chunkSize', DEFAULT_CHUNK_SIZE)),
            chunk_overlap=int(json_data.get('chunkOverlap', DEFAULT_CHUNK_OVERLAP)),
            func=json_data['function'],
            skip_typecheck=True
        )

# DEPRECATED.
class VectorDBReaderNode(NodeTemplate):
    def __init__(self, query_input:NodeOutput, database_input:NodeOutput, 
            func:str=DEFAULT_LOADER_FUNC, 
            max_docs_per_query:int=DEFAULT_MAX_DOCS,
            **kwargs):
        super().__init__()
        self.node_type = 'vectorDBReader'
        self.category = 'task'
        self.task_name = 'query_vector_db'
        self.func = func
        self.max_docs_per_query = max_docs_per_query
        if self.max_docs_per_query < 1:
            raise ValueError('VectorDBReaderNode: Invalid max_docs_per_query value.')
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            check_type('VectorDBReaderNode input query', query_input, TEXT_TYPE)
            check_type('VectorDBReaderNode input database', database_input, VECTOR_DB_TYPE)
        self._inputs = {'query': [query_input], 'database': [database_input]}
    
    def init_args_strs(self, indicate_id=False):
        query_input = self._inputs['query'][0]
        database_input = self._inputs['database'][0]
        return [
            format_node_output_with_name('query_input', query_input, indicate_id),
            format_node_output_with_name('database_input', database_input, indicate_id)
        ]

    def output(self) -> NodeOutput:
        # assume the reader returns the query result post-processed back into text
        return NodeOutput(
            source=self, 
            output_field='results', 
            output_data_type=ListType(DOCUMENT_TYPE)
        )
    
    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self, generic:bool=False):
        return {
            'function': self.func,
            'maxDocsPerQuery': self.max_docs_per_query
        }
        
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'VectorDBReaderNode':
        return VectorDBReaderNode(
            query_input=None,
            database_input=None,
            func=json_data['function'],
            max_docs_per_query=int(json_data['maxDocsPerQuery']),
            skip_typecheck=True
        )

# Akin to chaining together a VectorDBLoaderNode and VectorDBReaderNode.
class SemanticSearchNode(NodeTemplate):
    '''
    Create a new temporary vector database, load documents into it, run one or more queries to perform semantic search, and return the results. Once the pipeline finishes running, the database is deleted.
    
    Inputs:
    - query_input: The query/queries to the semantic search on the vector database. Each NodeOutput should have data type Text. 
    - documents_input: A list of one or more NodeOutputs to be loaded into the vector database. Each NodeOutput should have data type Text.
    - max_docs_per_query: The maximum number of documents from the vector database to return from the query.
    - enable_filter: Flag for whether or not to add an additional filter to query results.
    - filter_input: The additional filter for results if enable_filter is True. Should be a NodeOutput of type Text or a string.
    - rerank_documents: Flag for whether or not to rerank documents.

    Outputs:
    - result: The documents returned from the semantic search, with data type List[Document].
    '''
    def __init__(self, query_input:list[NodeOutput], 
            documents_input:list[NodeOutput], 
            max_docs_per_query:int=DEFAULT_MAX_DOCS, 
            func:str=DEFAULT_LOADER_FUNC, 
            enable_filter:bool=False, filter_input:str|NodeOutput=None, 
            rerank_documents:bool=False, **kwargs):
        super().__init__()
        self.node_type = 'vectorQuery'
        self.category = 'task'
        self.task_name = 'load_and_query_vector_db'
        if max_docs_per_query < 1: 
            raise ValueError('SemanticSearchNode: invalid max_docs_per_query value.')
        self.max_docs_per_query, self.func = max_docs_per_query, func
        self.enable_filter, self.rerank_documents = enable_filter, rerank_documents
        self._inputs = {'query-0': query_input, 'documents': documents_input}
        self.filter_text = None
        if type(filter_input) == str:
            self.filter_text = filter_input
        elif filter_input is not None:
            self._inputs['filter'] = [filter_input]
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            for o in query_input:
                check_type('SemanticSearchNode input query', o, TEXT_TYPE)
            for o in documents_input:
                check_type('SemanticSearchNode input documents', o, TEXT_TYPE)
            if filter_input:
                check_type('SemanticSearchNode input filter', filter_input, TEXT_TYPE)

    def set_enable_filter(self, enable_filter:bool): 
        self.enable_filter = enable_filter

    def set_rerank_documents(self, rerank_documents:bool):
        self.rerank_documents = rerank_documents

    def set_max_docs_per_query(self, max_docs_per_query:int):
        if max_docs_per_query < 1: 
            raise ValueError('SemanticSearchNode: invalid max_docs_per_query value.')
        self.max_docs_per_query = max_docs_per_query
    
    def set_query_input(self, query_input:list[NodeOutput]):
        if len(query_input) < 1:
            raise ValueError('SemanticSearchNode: documents_input is empty.')
        for o in query_input:
            check_type('SemanticSearchNode input query', o, TEXT_TYPE)
        self._inputs['query-0'] = query_input
    
    def set_documents_input(self, documents_input:list[NodeOutput]):
        if len(documents_input) < 1:
            raise ValueError('SemanticSearchNode: documents_input is empty.')
        for o in documents_input:
            check_type('SemanticSearchNode input documents', o, TEXT_TYPE)
        self._inputs['documents'] = documents_input

    def set_filter_input(self, filter_input:str|NodeOutput):
        if type(filter_input) == NodeOutput:
            check_type('SemanticSearchNode input filter', filter_input, TEXT_TYPE)
            self._inputs['filter'] = [filter_input]
            self.filter_text = None
        else:
            self.filter_text = filter_input 
            del self._inputs['filter']

    def init_args_strs(self, indicate_id=False):
        query_input_strs = [
            format_node_output(i, indicate_id)
            for i in self._inputs['query-0']
        ]
        documents_input_strs = [
            format_node_output(i, indicate_id)
            for i in self._inputs['documents']
        ]
        filter_arg_str = f"filter_input='{self.filter_text}'" \
            if self.filter_text else None
        if 'filter' in self._inputs:
            filter_arg_str = format_node_output_with_name('filter_input', self._inputs['filter'][0], indicate_id)
        return [
            f'query_input={query_input_strs}',
            f'documents_input={documents_input_strs}'
            f'max_docs_per_query={self.max_docs_per_query}' \
                if self.max_docs_per_query != DEFAULT_MAX_DOCS else None,
            f'func={self.func}' if self.func != DEFAULT_LOADER_FUNC else None,
            f'enable_filter={self.enable_filter}' \
                if self.enable_filter else None,
            filter_arg_str,
            f'rerank_documents={self.rerank_documents}' \
                if self.rerank_documents else None
        ]

    def output(self) -> NodeOutput:
        # assume the reader returns the query result post-processed back into text
        return NodeOutput(
            source=self, 
            output_field='query-result-0', 
            output_data_type=ListType(DOCUMENT_TYPE)
        )

    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self, generic:bool=False):
        return {
            'function': self.func,
            'maxDocsPerQuery': self.max_docs_per_query,
            'numQueries': len(self._inputs['query-0']),
            'enableFilter': self.enable_filter, 
            'filter': self.filter_text,
            'rerankDocuments': self.rerank_documents
        }
        
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'SemanticSearchNode':
        return SemanticSearchNode(
            query_input=None,
            documents_input=None,
            func=json_data['function'],
            max_docs_per_query=int(json_data['maxDocsPerQuery']),
            enable_filter=json_data.get('enableFilter', False),
            filter_input=json_data.get('filter', ''),
            rerank_documents=json_data.get('rerankDocuments', False),
            skip_typecheck=True
        )

VectorQueryNode = SemanticSearchNode

# User-created object.
class KnowledgeBaseNode(NodeTemplate):
    '''
    References a particular permanent Knowledge Base (a Knowledge Base), queries it, and returns the results. The Knowledge Base should already exist on the VectorShift platform, so that it can be referenced by its ID or name. An API call is made when a pipeline containing this node is saved to retrieve relevant data, meaning an API key is required. It is also possible to construct nodes from Knowledge Base (Vector Store) objects.
    
    Inputs:
    - query_input: The query to the Knowledge Base, which should have data type Text. 

    Parameters:
    - id: The ID of the Knowledge Base being represented.
    - name: The name of the Knowledge Base being represented. At least one of base_id and base_name should be provided. If both are provided, base_id is used to search for the Knowledge Base object. Otherwise, the node represents a generic Knowledge Base that needs to be set up before being run.
    - username: The username of the user owning the Knowledge Base.
    - org_name: The organization name of the user owning the Knowledge Base, if applicable.
    - max_docs_per_query: The maximum number of documents from the Knowledge Base to return from the query.
    - enable_filter: Flag for whether or not to add an additional filter to query results.
    - filter_input: The additional filter for results if enable_filter is True. Should be a NodeOutput of type Text or a string.
    - rerank_documents: Flag for whether or not to rerank documents.
    - alpha: The value of alpha for performing searches (weighting between dense and sparse indices). Ignored if the Knowledge Base is not hybrid.
    - public_key, private_key: API keys to be used when retrieving information about the Knowledge Base from the VectorShift platform.

    Outputs:
    - results: The documents returned from the Knowledge Base, with data type List[Document].
    '''
    def __init__(self, query_input:NodeOutput, 
                 base_id=None, base_name=None, 
                 username=None, org_name=None, 
                 max_docs_per_query=DEFAULT_MAX_DOCS, 
                 enable_filter:bool=False, filter_input:str|NodeOutput=None, 
                 rerank_documents:bool=False, alpha:float=DEFAULT_ALPHA,
                 api_key:str=None, public_key:str=None, private_key:str=None,
                 **kwargs):
        super().__init__()
        self.node_type = 'vectorStore'
        self.category = 'task'
        self.task_name = 'query_vectorstore'
        self.vectorstore_id = base_id
        self.vectorstore_name = base_name
        self.username = username 
        self.org_name = org_name
        self.max_docs_per_query = max_docs_per_query
        if self.max_docs_per_query < 1:
            raise ValueError('KnowledgeBaseNode: Invalid max_docs_per_query value.')
        self.enable_filter, self.rerank_documents = enable_filter, rerank_documents
        # note: alpha only means something to hybrid vectorstores
        if alpha < 0. or alpha > 1.:
            raise ValueError(f'KnowledgeBaseNode: Invalid value of alpha {alpha}.')
        self.alpha = alpha
        self._inputs = {'query': [query_input]}
        self.filter_text = None
        if type(filter_input) == str:
            self.filter_text = filter_input
        elif filter_input is not None:
            self._inputs['filter'] = [filter_input]
        # we'll need to use the API key when fetching the user-defined 
        # vectorstore
        self._api_key = api_key or vectorshift.api_key
        self._public_key = public_key or vectorshift.public_key
        self._private_key = private_key or vectorshift.private_key
        # we don't store vectorstore-specific params like chunk params, since 
        # that is a property of the vectorstore and not the node
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            check_type('KnowledgeBaseNode input query', query_input, TEXT_TYPE)
            if filter_input:
                check_type('KnowledgeBaseNode input filter', filter_input, TEXT_TYPE, str_ok=True)
    
    @staticmethod
    def from_obj(obj, 
            query_input:NodeOutput, 
            api_key:str=None, public_key:str=None, private_key:str=None):
        if not obj.id:
            print('KnowledgeBaseNode.from_obj: object does not contain a required ID, which likely means that the Knowledge Base has not yet been saved. Attempting to save the pipeline...')
            obj.save(api_key, public_key, private_key)
            print('KnowledgeBaseNode: Knowledge Base successfully saved.')
        # This is inefficient right now, since we save (write to Mongo) and 
        # then immediately query the object (read from Mongo) in the 
        # constructor.
        return KnowledgeBaseNode(
            query_input=query_input, 
            id=obj.id, 
            name=obj.name,
            api_key=api_key,
            public_key=public_key, 
            private_key=private_key
        )

    from_vectorstore_obj = from_obj 
    from_knowledge_base_obj = from_obj

    def set_knowledge_base(self, base_id:str, base_name:str, 
            username: str, org_name: str): 
        self.vectorstore_id = base_id
        self.vectorstore_name = base_name
        self.username = username
        self.org_name = org_name
    
    set_vectorstore = set_knowledge_base

    def set_enable_filter(self, enable_filter:bool): 
        self.enable_filter = enable_filter

    def set_rerank_documents(self, rerank_documents:bool):
        self.rerank_documents = rerank_documents

    def set_max_docs_per_query(self, max_docs_per_query:int):
        if max_docs_per_query < 1: 
            raise ValueError('KnowledgeBaseNode: invalid max_docs_per_query value.')
        self.max_docs_per_query = max_docs_per_query

    def set_query_input(self, query_input:NodeOutput):
        check_type('KnowledgeBaseNode input query', query_input, TEXT_TYPE)
        self._inputs['query'] = [query_input]

    def set_filter_input(self, filter_input:str|NodeOutput):
        if type(filter_input) == NodeOutput:
            check_type('KnowledgeBaseNode input filter', filter_input, TEXT_TYPE)
            self._inputs['filter'] = [filter_input]
            self.filter_text = None
        else:
            self.filter_text = filter_input 
            del self._inputs['filter']

    def set_alpha(self, alpha:float):
        if alpha < 0. or alpha > 1.:
            raise ValueError(f'KnowledgeBaseNode: Invalid value of alpha {alpha}.')
        self.alpha = alpha
    
    # If this node was loaded from JSON and changed to reference another
    # vectorstore object, we need to use the API key to query the new object.
    # This setter provides an explicit way to make sure the API key is in the 
    # node (if the key weren't initialized globally).
    def set_api_key(self, api_key: str = None, public_key: str = None, private_key: str = None) -> None:
        self._api_key = api_key
        self._public_key = public_key
        self._private_key = private_key

    def init_args_strs(self, indicate_id=False):
        query_input = self._inputs['query'][0]
        filter_arg_str = f"filter_input='{self.filter_text}'" \
            if self.filter_text else None
        if 'filter' in self._inputs:
            filter_arg_str = format_node_output_with_name('filter_input', self._inputs['filter'][0], indicate_id)
        return [
            format_node_output_with_name('query_input', query_input, indicate_id),
            f"base_id='{self.vectorstore_id}'" \
                if self.vectorstore_id else None,
            f"base_name='{self.vectorstore_name}'" \
                if self.vectorstore_name else None,
            f"username='{self.username}'" if self.username else None,
            f"org_name='{self.org_name}'" if self.org_name else None,
            f'max_docs_per_query={self.max_docs_per_query}' \
                if self.max_docs_per_query != DEFAULT_MAX_DOCS else None,
            f'enable_filter={self.enable_filter}' \
                if self.enable_filter else None,
            filter_arg_str,
            f'rerank_documents={self.rerank_documents}' \
                if self.rerank_documents else None,
            f'alpha={self.alpha}' if self.alpha != DEFAULT_ALPHA else None
        ]

    def output(self) -> NodeOutput:
        return NodeOutput(
            source=self, 
            output_field='results', 
            output_data_type=ListType(DOCUMENT_TYPE)
        )
    
    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self, generic:bool=False):
        # There's currently no notion of "sharing" vectorstores (so username
        # and org_name aren't required right now), but there probably will be 
        # one in the future.
        json_rep = {
            'maxDocsPerQuery': self.max_docs_per_query,
            'enableFilter': self.enable_filter, 
            'filter': self.filter_text, 
            'rerankDocuments': self.rerank_documents,
            'alpha': self.alpha
        }
        vectorstore_json = {}
        if (self.vectorstore_id or self.vectorstore_name) and not generic:
            if self._api_key is None and (self._public_key is None or self._private_key is None):
                raise ValueError('KnowledgeBaseNode: API key required to fetch Knowledge Base.')
            response = requests.get(
                API_VECTORSTORE_FETCH_ENDPOINT,
                data={
                    'vectorstore_id': self.vectorstore_id,
                    'vectorstore_name': self.vectorstore_name,
                    'username': self.username,
                    'org_name': self.org_name
                },
                headers={
                    'Api-Key': self._api_key,
                    'Public-Key': self._public_key,
                    'Private-Key': self._private_key
                }
            )
            if response.status_code != 200:
                raise Exception(f"Error fetching Knowledge Base: {response.text}")
            vectorstore_json = response.json()
            # we just copy everything over, including the vectors (if any)
            json_rep['vectorStore'] = vectorstore_json
        return json_rep

    @staticmethod 
    def _from_json_rep(json_data:dict) -> 'KnowledgeBaseNode':
        # there isn't a way to recover the API key from the JSON rep; it can
        # be set with set_api_key; also as mentioned above, (author) username
        # and org name data isn't currently saved in Mongo
        vectorstore_json = json_data.get('vectorStore', {})
        return KnowledgeBaseNode(
            query_input=None,
            id=vectorstore_json.get('id', None),
            name=vectorstore_json.get('name', None),
            max_docs_per_query=json_data['maxDocsPerQuery'],
            enable_filter=json_data.get('enableFilter', False),
            filter_input=json_data.get('filter', ''),
            rerank_documents=json_data.get('rerankDocuments', False),
            alpha=json_data.get('alpha', DEFAULT_ALPHA),
            skip_typecheck=True
        )

VectorStoreNode = KnowledgeBaseNode

###############################################################################
# LOGIC                                                                       #
###############################################################################

class LogicConditionNode(NodeTemplate):
    '''
    This node allows for simple control flow. It takes in one or more inputs, which are given labels (akin to variable names). It also takes in a list of conditions. Each condition is a tuple of two strings, a predicate that can reference the labels and a resulting label to be outputted by the node if the predicate is True. The predicate must be a string representing a boolean statement in Python; more information on predicates is located here.

    The node has multiple outputs: one output corresponding to each of the conditions, along with an else output. If a predicate evaluates to True then that condition's output will emit the NodeOutput whose label is given by the predicate's corresponding label. If a predicate has evaluated to True, further predicates are not evaluated (i.e. the node only activates the first path that evaluates to True.) Otherwise, the output is not produced and downstream nodes from that output will not be executed. The outputs are labeled output-0, output-1, etc. for each of the conditions, and output_else.

    Inputs:
    - inputs: A map of output labels to NodeOutputs. Identifies each NodeOutput with a label. Can have any data type.

    Parameters:
    - conditions: A list of conditions. As explained above, each condition is comprised of a predicate, which should be a string expressing a Python boolean statement, and output label. The predicates are evaluated in order of the list. The first predicate that evaluates to True will return the NodeOutput identified by the associated label. If no predicates evaluate to True, the NodeOutput identified by else_value is returned.
    - else_value: The label of the NodeOutput to emit in the else case.

    Outputs: 
    - Outputs named output-0, output-1, ..., output-n where n is one less than the total number of conditions. output-i equals the NodeOutput identified by the label in the ith (0-indexed) condition in the list, and is only produced if the ith predicate evaluates to True. The data type is the same as the original NodeOutput's data type.
    - An output named output-else, which emits the NodeOutput whose label is given by else_value. The data type is the same as the original NodeOutput's data type.
    '''
    def typecheck_inputs(self):
        # For now, we just mandate that any input names that appear in a 
        # condition are text.
        input_names = self._inputs.keys()
        conditional_input_names = set()
        for c in self.conditions:
            for n in list(input_names):
                if n in c[0]:
                    conditional_input_names.add(n)
        for cnd_input_name in list(conditional_input_names):
            check_type(f'LogicConditionNode input {cnd_input_name}', self._inputs[cnd_input_name][0], TEXT_TYPE)

    # inputs should comprise all in-edges, which are the names of all conditions 
    # and values along with the NodeOutputs they correspond to.
    # conditions is a list of (cond, val), where if cond is True the node 
    # returns val (where val is an input name).
    # default is what the node returns in the (final) else case.
    def __init__(self, inputs:dict[str, NodeOutput], 
            conditions:list[tuple[str, str]], else_value:str,
            **kwargs):
        super().__init__()
        self.node_type = 'condition'
        # task_name is not used
        self.category = self.task_name = 'condition' 
        input_names = list(inputs.keys())
        if len(set(input_names)) != len(input_names):
            raise ValueError('LogicConditionNode: duplicate input names.')
        for cond in conditions:
            if cond[1] not in input_names:
                raise ValueError(f'LogicConditionNode: Returned value {cond[1]} of condition {cond[0]} was not specified in inputs.')
        if else_value not in input_names:
            raise ValueError(f'LogicConditionNode: Returned value {else_value} of else condition was not specified in inputs.')
        self.input_names = input_names
        self.conditions = conditions
        # NB: self.predicates maps to the JSON "conditions" field. The result
        # of the corresponding predicate in the input argument conditions is
        # the same-indexed element in self.output_names.
        self.predicates = [cond[0] for cond in conditions]
        self.output_names = [cond[1] for cond in conditions] + [else_value]
        # each separate input is an in-edge to the node, with the input name
        # being the user-provided name
        self._inputs = {k: [v] for k, v in inputs.items()}
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            self.typecheck_inputs()

    def set_input(self, input_name:str, input:NodeOutput):
        if input_name not in self._inputs.keys():
            raise ValueError(f'LogicConditionNode: invalid input name {input_name}.')
        old_input = self._inputs[input_name]
        self._inputs[input_name] = [input]
        try:
            self.typecheck_inputs()
        except ValueError as err:
            self._inputs[input_name] = [old_input]
            raise err
    
    # Pragmatically speaking it might be easier to just create a new node
    # rather than fiddling around with these methods
    def set_conditions(self, conditions:list[tuple[str, str]]):
        old_conditions = self.conditions
        self.conditions = conditions
        self.predicates = [cond[0] for cond in conditions]
        self.output_names = [cond[1] for cond in conditions] \
            + self.output_names[-1]
        try:
            self.typecheck_inputs()
        except ValueError as err:
            self.conditions = old_conditions 
            self.predicates = [cond[0] for cond in self.conditions]
            self.output_names = [cond[1] for cond in self.conditions] \
                + self.output_names[-1]
            raise err

    def set_else_value(self, else_value:str):
        if else_value not in self.input_names:
            raise ValueError(f'LogicConditionNode: Returned value {else_value} of else condition is not specified in inputs.')
        self.output_names[-1] = else_value
    
    def init_args_strs(self, indicate_id=False):
        input_dict = {
            k: format_node_output(v[0], indicate_id)
            for k, v in self._inputs.items()
        }
        input_dict_str = input_dict.__str__().replace('"', '')
        return [
            f'inputs={input_dict_str}',
            f'conditions={self.conditions}',
            f"else_value='{self.output_names[-1]}'"
        ]

    # Unlike most other nodes, this node has several outputs, corresponding to
    # each of the specified conditions (and the else case).
    def outputs(self):
        # the outputs are labelled "output-0", "output-1", etc. followed by
        # "output-else"
        os = {}
        # We can do better than the API code since we still have access to the
        # NodeOutputs in each conditional output (and thus the type)
        for ind in range(len(self.predicates)):
            output_source_name = self.output_names[ind]
            output_data_type = self._inputs[output_source_name][0].output_data_type
            o = NodeOutput(
                source=self, 
                output_field=f'output-{ind}', 
                output_data_type=output_data_type)
            os[o.output_field] = o
        else_output_source_name = self.output_names[-1]
        else_o = NodeOutput(
            source=self, 
            output_field='output-else', 
            output_data_type=self._inputs[else_output_source_name][0].output_data_type
        )
        os[else_o.output_field] = else_o
        return os
    
    # If a user currently wants to index into a specific output, they need to 
    # call the outputs() method and then index into it by name (e.g. 
    # "output-2", "output-else"), or use the helper functions below.
    def output_index(self, i:int) -> NodeOutput:
        if i < 0 or i >= len(self.predicates):
            raise ValueError('LogicConditionNode: index out of range.')
        os = self.outputs()
        return os[f'output-{i}']
    
    def output_else(self) -> NodeOutput: 
        os = self.outputs()
        return os['output-else']
    
    def _to_json_rep(self, generic:bool=False):
        return {
            'conditions': self.predicates,
            'inputNames': self.input_names,
            'outputs': self.output_names,
        }

    @staticmethod
    def _from_json_rep(json_data:dict) -> 'LogicConditionNode':
        predicates = json_data['conditions']
        output_names = json_data['outputs']
        input_names = json_data.get('inputNames', [])
        if not input_names: input_names = []
        return LogicConditionNode(
            inputs={name: None for name in input_names},
            conditions=[(predicates[i], output_names[i]) for i in range(len(predicates))],
            else_value=output_names[-1],
            skip_typecheck=True
        )
    
class LogicMergeNode(NodeTemplate):
    '''
    This node merges together conditional branches that may have been produced by a LogicConditionNode, returning the output that is the first in the list to have been computed. As above, the documentation on conditional logic may provide helpful context. 

    Inputs:
    - inputs: Different outputs from conditional branches to combine.

    Parameters: None.

    Outputs:
    - output: The merged output, of data type Union[ts], where ts represent the data types of all input NodeOutputs. 
    '''
    def __init__(self, inputs:list[NodeOutput], **kwargs):
        super().__init__()
        self.node_type = 'merge'
        # task_name is not used
        self.category = self.task_name = 'merge'
        self._inputs = {
            # The JSON name for the in-edge is "input", although the displayed
            # name is "inputs".
            'input': inputs
        }

    def set_inputs(self, inputs:list[NodeOutput]):
        self._inputs['input'] = inputs 
        
    def init_args_strs(self, indicate_id=False):
        input_strs = [
            format_node_output(i, indicate_id)
            for i in self._inputs['input']
        ]
        return [f'inputs={input_strs}'.replace('"', '')]

    def output(self) -> NodeOutput:
        output_data_types = set([o.output_data_type for o in self._inputs['input']])
        return NodeOutput(
            source=self, 
            output_field='output', 
            output_data_type=UnionType(*output_data_types)
        )
    
    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self, generic:bool=False):
        # only one function is currently supported
        return {'function': 'default'}
    
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'LogicMergeNode':
        _ = json_data
        return LogicMergeNode(
            inputs=[],
            skip_typecheck=True
        )

class SplitTextNode(NodeTemplate):
    '''
    Splits text into multiple strings based on a delimiter.

    Inputs:
    - text_input: An output containing text to split, which should have data type Text.

    Parameters:
    - delimiter: The string on which to split the text. If the text is 'foo, bar, baz' and delimiter is ',', then the result corresponds to the strings 'foo', ' bar', and ' baz'.

    Outputs:
    - output: All the split strings, of data type List[Text].
    '''
    def __init__(self, delimiter:str, text_input:NodeOutput, **kwargs):
        super().__init__()
        self.node_type = 'splitText'
        self.category = 'task'
        self.task_name = 'split_text'
        if not delimiter:
            raise ValueError('SplitTextNode: delimiter cannot be an empty string.')
        self.delimiter_chars = delimiter
        self.delimiter_name = 'character(s)'
        if delimiter in TEXT_SPLIT_DELIMITER_NAMES:
            self.delimiter_name = TEXT_SPLIT_DELIMITER_NAMES[delimiter]
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            check_type('SplitTextNode input text', text_input, TEXT_TYPE)
        self._inputs = {'text': [text_input]}

    def set_delimiter(self, delimiter:str):
        self.delimiter_chars = delimiter
        self.delimiter_name = 'character(s)'
        if delimiter in TEXT_SPLIT_DELIMITER_NAMES:
            self.delimiter_name = TEXT_SPLIT_DELIMITER_NAMES[delimiter]

    def set_text_input(self, text_input:NodeOutput):
        check_type('SplitTextNode input text', text_input, TEXT_TYPE)
        self._inputs['text'] = [text_input]
    
    def init_args_strs(self, indicate_id=False):
        text_input = self._inputs['text'][0]
        return [
            f"delimiter='{self.delimiter_chars}'",
            format_node_output_with_name('text_input', text_input, indicate_id)
        ]
    
    def output(self) -> NodeOutput:
        return NodeOutput(
            source=self,
            output_field='output',
            output_data_type=ListType(TEXT_TYPE)
        )

    def outputs(self):
        o = self.output()
        return {o.output_field: o}

    def _to_json_rep(self, generic:bool=False):
        character = None if self.delimiter_name != 'character(s)' else self.delimiter_chars
        return {
            'delimiter': self.delimiter_name,
            'character': character,
        }
    
    @staticmethod 
    def _from_json_rep(json_data:dict) -> 'SplitTextNode':
        delimiter_name = json_data.get('delimiter', '')
        delimiter_chars = json_data.get('character', '')
        if delimiter_name == 'space':
            delimiter_chars = ' '
        if delimiter_name == 'newline':
            delimiter_chars = '\n'
        return SplitTextNode(
            delimiter=delimiter_chars,
            skip_typecheck=True
        )

class TimeNode(NodeTemplate):
    '''
    Outputs a time in text form given a time zone and optional offset.

    Inputs: None.

    Parameters:
    - timezone: The timezone, which should be in pytz.
    - delta: The value of a time offset.
    - delta_unit: The units of a time offset.
    - output_format: The string format in which to output the time.

    Outputs:
    - output: The string representing the time.
    '''
    def __init__(self, timezone:str, 
                 delta:float, delta_unit:str, output_format:str, **kwargs):
        super().__init__()
        self.node_type = 'timeNode'
        self.category = 'timeNode'
        self.task_name = 'time_node'
        if timezone not in TIMEZONES:
            raise ValueError(f'TimeNode: invalid timezone {timezone}.')
        if delta_unit not in TIME_UNITS:
            raise ValueError(f'TimeNode: invalid delta unit {delta_unit}.')
        if output_format not in TIME_OUTPUT_FORMATS:
            raise ValueError(f'TimeNode: invalid output format {output_format}.')
        self.timezone = timezone 
        self.delta = delta 
        self.delta_unit = delta_unit 
        self.output_format = output_format 
        self._inputs = {}

    def set_timezone(self, timezone:str): 
        if timezone not in TIMEZONES:
            raise ValueError(f'TimeNode: invalid timezone {timezone}.')
        self.timezone = timezone

    def set_delta(self, delta:float): self.delta = delta 

    def set_delta_unit(self, delta_unit:str): 
        if delta_unit not in TIME_UNITS:
            raise ValueError(f'TimeNode: invalid delta unit {delta_unit}.')
        self.delta_unit = delta_unit
    
    def set_output_format(self, output_format:str):
        if output_format not in TIME_OUTPUT_FORMATS:
            raise ValueError(f'TimeNode: invalid output format {output_format}.')
        self.output_format = output_format

    def init_args_str(self, indicate_id=False):
        return [
            f"timezone='{self.timezone}'",
            f'delta={self.delta}',
            f"delta_unit='{self.delta_unit}'",
            f"output_format='{self.output_format}'"
        ]
    
    def output(self) -> NodeOutput:
        return NodeOutput(
            source=self, 
            output_field='output', 
            output_data_type=TEXT_TYPE
        )
    
    def outputs(self):
        o = self.output()
        return {o.output_field: o}

    def _to_json_rep(self, generic:bool=False):
        return {
            'timeNodeZone': self.timezone,
            'isPositiveDelta': self.delta >= 0.,
            'deltaValue': str(self.delta),
            'deltaTimeUnit': self.delta_unit,
            'outputFormat': self.output_format
        }
    
    @staticmethod 
    def _from_json_rep(json_data:dict) -> 'TimeNode':
        return TimeNode(
            timezone=json_data['timeNodeZone'],
            delta=float(json_data['deltaValue']),
            delta_unit=json_data['deltaTimeUnit'],
            output_format=json_data['outputFormat'],
            skip_typecheck=True
        )

###############################################################################
# CHAT                                                                        #
###############################################################################

class ChatMemoryNode(NodeTemplate):
    '''
    Represents the chat memory for chatbots, i.e. the chat history that the chatbot can reference when generating messages.

    Inputs: None.

    Parameters:
    - memory_type: The particular type of chat memory to use. 
    - memory_window: The access to memory; whether or not this should be given depends on the value of memory_type.

    Outputs:
    - value: The chat history, of data type Text if memory_type is 'Full - Formatted' and List[Dict] otherwise.
    '''
    def __init__(self, memory_type:str, memory_window:int=None, **kwargs):
        super().__init__()
        self.node_type = 'chatMemory'
        self.category = 'memory'
        self.task_name = 'load_memory'
        if memory_type not in CHAT_MEMORY_TYPES.keys():
            raise ValueError(f'ChatMemoryNode: invalid chat memory type {memory_type}.')
        self.memory_type = memory_type
        # self.memory_window is set to the value corresponding to 
        # self.memory_type's entry in memory_window_values, which may be 
        # overridden by the constructor arg memory_window
        self.memory_window = CHAT_MEMORY_TYPES[self.memory_type]
        if memory_window is not None:
            if memory_window <= 0: 
                raise ValueError(f'ChatMemoryNode: invalid memory_window value {memory_window}.')
            if CHAT_MEMORY_TYPES[self.memory_type] == 0:
                raise ValueError('ChatMemoryNode: memory window should not be specified if the chat memory is the full text.')
        self.memory_window = memory_window

    def set_memory_type(self, memory_type:str):
        if memory_type not in CHAT_MEMORY_TYPES.keys():
            raise ValueError(f'ChatMemoryNode: invalid chat memory type {memory_type}.')
        self.memory_type = memory_type

    def set_memory_window(self, memory_window:int):
        if memory_window <= 0: 
            raise ValueError(f'ChatMemoryNode: invalid memory_window value {memory_window}.')
        if CHAT_MEMORY_TYPES[self.memory_type] == 0:
            raise ValueError("ChatMemoryNode: memory window shouldn't be specified if the chat memory is the full text.")
        self.memory_window = memory_window
    
    def init_args_strs(self, indicate_id=False):
        return [f"memory_type='{self.memory_type}'"]

    def output(self) -> NodeOutput:
        output_data_type = TEXT_TYPE if self.memory_type == 'Full - Formatted' else ListType(DICT_TYPE)
        return NodeOutput(
            source=self, 
            output_field='value', 
            output_data_type=output_data_type
        )

    def outputs(self):
        o = self.output()
        return {o.output_field: o}
    
    def _to_json_rep(self, generic:bool=False):
        return {
            'memoryType': self.memory_type,
            'memoryWindow': self.memory_window,
            'memoryWindowValues': CHAT_MEMORY_TYPES,
        }
    
    @staticmethod
    def _from_json_rep(json_data:dict) -> 'ChatMemoryNode':
        n = ChatMemoryNode(
            memory_type=json_data['memoryType'],
            skip_typecheck=True
        )
        # overwrite with JSON window (not passed in constructor to handle edge case of 0)
        n.memory_window = int(json_data['memoryWindow'])
        return n

class DataCollectorNode(NodeTemplate):
    '''
    Prompts a LLM to search the chat history based on a prompt and one or more example fields, returning a summary of the relevant information.

    Inputs:
    - input: A NodeOutput which should represent the chat memory. Should be of data type Text or List[Dict] (coming from a ChatMemoryNode).

    Parameters:
    - prompt: The string prompt to guide the kind of data from the chat history to collect.
    - fields: A list of dictionaries, each indicating a data field to collect. Each dictionary should contain the following fields: field, containing the name of the field; description, describing the field; and example, giving a text example of what to search for.

    Outputs:
    - output: A selection of relevant information from the chat history, of data type Text.
    '''
    def __init__(self, input:NodeOutput, prompt:str='', 
                 fields:list[dict[str, str]]=[], **kwargs):
        super().__init__()
        self.node_type = 'dataCollector'
        self.category = 'dataCollector'
        self.task_name = 'data_collector'
        self.fields = []
        for f in fields:
            for field_name in ['field', 'description', 'example']:
                if field_name not in f.keys():
                    raise ValueError(f'DataCollectorNode: missing key {field_name}.')
            # generate random IDs for new fields
            if 'id' not in f.keys():
                f['id'] = gen_str_id()
        for f in fields:
            self.fields.append(f)
        self.prompt = prompt
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            check_type('DataCollectorNode input', input, TEXT_TYPE)
        self._inputs = {'input': [input]}
        
    def set_prompt(self, prompt:str): self.prompt = prompt 

    def add_field(self, field:dict[str, str]):
        for field_name in ['field', 'description', 'example']:
            if field_name not in field.keys():
                raise ValueError(f'DataCollectorNode: missing key {field_name}.')
        if 'id' not in field.keys():
            field['id'] = gen_str_id()
        self.fields.append(field)

    def set_fields(self, fields:list[dict[str, str]]):
        self.fields = []
        for f in fields:
            for field_name in ['field', 'description', 'example']:
                if field_name not in f.keys():
                    raise ValueError(f'DataCollectorNode: missing key {field_name}.')
            # generate random IDs for new fields
            if 'id' not in f.keys():
                f['id'] = gen_str_id()
        for f in fields:
            self.fields.append(f)

    def set_input(self, input:NodeOutput):
        check_type('DataCollectorNode input', input, TEXT_TYPE)
        self._inputs['input'] = [input]

    def init_args_strs(self, indicate_id:bool=False):
        fields = deepcopy(self.fields)
        for f in fields: del f['id']
        input = self._inputs['input'][0]
        return [
            format_node_output_with_name('input', input, indicate_id),
            f"prompt='{self.prompt}'",
            f'fields={fields}'
        ]
    
    def output(self) -> NodeOutput:
        return NodeOutput(
            source=self, 
            output_field='output',
            output_data_type=TEXT_TYPE
        )
    
    def outputs(self):
        o = self.output() 
        return {o.output_field: o}
    
    def _to_json_rep(self, generic:bool=False):
        return {
            'fields': self.fields,
            'dataCollectorNodeId': self._id, 
            'prompt': self.prompt,
            # hard coded for now
            'autoGenerate': True,
            'llm': 'OpenAI',
            'model': 'gpt-4-1106-preview'
        }
    
    @staticmethod 
    def _from_json_rep(json_data:dict) -> 'DataCollectorNode':
        return DataCollectorNode(
            input=None,
            prompt=json_data['prompt'],
            fields=json_data['fields'],
            skip_typecheck=True
        )

###############################################################################
# AGENTS                                                                       
###############################################################################

# User created object
# as a user create object Agent Node just references an existing agent by ID 
# Start with user created object implementation
# Maybe agent node is analagous to a pipeline node and we have an Agent class that as analogous to a pipeline class and alllows defining the agent with various tools
class AgentNode(NodeTemplate):
    '''
    Represent an agent. The agent must already exist on the VectorShift platform, so that it can be referenced by its ID or name. An API call is made upon initialization to retrieve relevant agent data, meaning an API key is required.

    Inputs:
    - inputs: A map of input names to NodeOutputs, which depends on the specific agent. In essence, the NodeOutputs passed in are interpreted as inputs to the pipeline represented by the AgentNode. They should match up with the expected input names of the agent. For instance, if the agent has input names input_1 and input_2, then the dictionary should contain those strings as keys.

    Parameters:
    - agent_id: The ID of the agent being represented.
    - agent_name: The name of the agent being represented. At least one of agent_id and agent_name should be provided. If both are provided, agent_id is used to search for the agent object.
    - username: The username of the user owning the agent.
    - org_name: The organization name of the user owning the agent, if applicable.
    - public_key, private_key: The VectorShift API key to make calls to retrieve the agent data.

    Outputs: Outputs are determined from the agent represented. Since each agent returns one or more named outputs that are either of File or Text data type, the keys of the outputs dictionary are the named outputs of the agent, with the values given the appropriate data type.
    '''
    def typecheck_inputs(self):
        agent_inputs = self.agent_json['inputs'].values()
        for input in agent_inputs:
            input_name = input['name']
            if input_name not in self._inputs.keys():
                raise ValueError(f'AgentNode missing input {input_name}.')
            node_input = self._inputs[input_name][0]
            if input['type'] == 'Text':
                check_type(f'AgentNode input {input_name}', node_input, TEXT_TYPE)
            elif input['type'] == 'File':
                check_type(f'AgentNode input {input_name}', node_input, FILE_TYPE)
            else:
                raise ValueError(f"Invalid input type to AgentNode input {input_name}: {input['type']}")
    
    def __init__(self, agent_id:str=None, agent_name:str=None,
        inputs:dict[str, NodeOutput]={},
        username:str=None, org_name:str=None,
        api_key:str=None, public_key:str=None, private_key:str=None, **kwargs):      
        super().__init__()
        self.node_type = 'agent'
        # task_name is not used
        self.category = self.task_name = 'agent'
        if agent_id is None and agent_name is None:
            raise ValueError('AgentNode: either the agent ID or name should be specified.')
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.username = username
        self.org_name = org_name
        self._api_key = api_key or vectorshift.api_key
        self._public_key = public_key or vectorshift.public_key
        self._private_key = private_key or vectorshift.private_key
        if self._api_key is None and (self._public_key is None or self._private_key is None):
            raise ValueError('AgentNode: API key required to fetch Agent. If you are getting this error while loading a pipeline from the platform, set the environment variables vectorshift.public_key and vectorshift.private_key.')
        response = requests.get(
            API_AGENT_FETCH_ENDPOINT,
            data={
                'agent_id': self.agent_id,
                'agent_name': self.agent_name,
                'username': self.username,
                'org_name': self.org_name
            },
            headers={
                'Api-Key': self._api_key,
                'Public-Key': self._public_key,
                'Private-Key': self._private_key
            }
        )
        if response.status_code != 200:
            raise Exception(f"Error fetching agent: {response.text}")
        self.agent_json = response.json()
        self.agent_id = self.agent_json['id']
        self.agent_name = self.agent_json['name']
        input_names = [
            i['name'] for i in self.agent_json['inputs'].values()
        ]
        if sorted(list(inputs.keys())) != sorted(input_names):
            raise ValueError(f'AgentNode: pipeline node inputs do not match expected input names: expected f{input_names}')
        self._inputs = {
            input_name: [inputs[input_name]] for input_name in input_names
        }
        if not 'skip_typecheck' in kwargs or not kwargs['skip_typecheck']:
            self.typecheck_inputs()

    @staticmethod 
    def from_agent_obj(agent_obj, 
                       inputs:dict[str, NodeOutput],
                       api_key:str=None, public_key:str=None, private_key:str=None):
        if not agent_obj.id:
            print('AgentNode.from_agent_obj: object does not contain a required ID, which likely means that the agent has not yet been saved. Attempting to save...')
            agent_obj.save(api_key, public_key, private_key)
            print('Agent object successfully saved.')
        # This is inefficient right now, since we save (write to Mongo) and 
        # then immediately query the object (read from Mongo) in the 
        # constructor.
        return AgentNode(
            agent_id=agent_obj.id,
            agent_name=agent_obj.name,
            inputs=inputs,
            api_key=api_key,
            public_key=public_key, 
            private_key=private_key
        )

    def set_input(self, input_name:str, input:NodeOutput):
        if input_name not in self._inputs.keys():
            raise ValueError(f'AgentNode: Invalid input name {input_name}.')
        old_input = self._inputs[input_name]
        self._inputs[input_name] = [input] 
        try:
            self.typecheck_inputs()
        except ValueError as err:
            self._inputs[input_name] = old_input
            raise err

    def set_inputs(self, inputs:dict[str, NodeOutput]):
        if sorted(inputs.keys()) != sorted(self._inputs.keys()):
            raise ValueError(f'AgentNode: Invalid input names provided.')
        old_inputs = self._inputs.copy()
        self._inputs = {
            k: [v] for k, v in inputs.items()
        } 
        try:
            self.typecheck_inputs()
        except ValueError as err:
            self._inputs = old_inputs
            raise err

    def init_args_strs(self, indicate_id=False):
        return [
            f"agent_id='{self.agent_id}'" if self.agent_id else None,
            f"agent_name='{self.agent_name}'" if self.agent_name else None,
            f'inputs={format_node_output_dict(self._inputs, indicate_id)}',
            f"username='{self.username}'" if self.username else None,
            f"org_name='{self.org_name}'" if self.org_name else None,
        ]

    def set_api_key(self, api_key: str = None, public_key: str = None, private_key: str = None) -> None:
        self._api_key = api_key
        self._public_key = public_key
        self._private_key = private_key

    def outputs(self) -> dict[str, NodeOutput]:
        os = {}
        for o in self.agent_json['outputs'].values():
            output_field = o['name']
            if o['type'] in ['Text', 'Formatted Text']:
                output_data_type = TEXT_TYPE
            elif o['type'] == 'File':
                output_data_type = FILE_TYPE
            else:
                raise ValueError(f'AgentNode: unsupported output type {o["type"]}')
            os[output_field] = NodeOutput(
                source=self, 
                output_field=output_field, 
                output_data_type=output_data_type
            )
        return os
    
    def output(self) -> NodeOutput:
        return NodeOutput(
            source=self, 
            output_field='output',
            output_data_type=None
        )
    
    def _to_json_rep(self, generic:bool=False):
        return {'agentDefinition': self.agent_json}

    @staticmethod
    def _from_json_rep(json_data:dict) -> 'AgentNode':
        inputs = {}
        for input_name in json_data['agentDefinition'].get('inputs', {}).keys():
            inputs[input_name] = None
        return AgentNode(
            agent_id=json_data['agentDefinition']['id'],
            agent_name=json_data['agentDefinition']['name'],
            inputs=inputs,
            skip_typecheck=True
        )
