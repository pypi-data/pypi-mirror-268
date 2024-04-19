import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from requests_toolbelt.multipart.encoder import MultipartEncoder
from get_file_type import get_mime_type
import requests
import json

class Client:
    def __init__(self, api_key, **kwargs):
        self.ptr_id = kwargs.get('id', None)
        self.model_name = kwargs.get('name', None)
        self.api_key = api_key
        self.api_url = 'https://n4kh6hh8p3.execute-api.us-east-1.amazonaws.com/rilaas_client_get_metadata'
        self.endpoint_params = None
        self.model_predictor = None
        self.selected_endpoint = None
        self.response_metadata = None

    def get_endpoints(self):
        if self.ptr_id is not None:
            if self.endpoint_params:
                return self.endpoint_params
            
            request_type = 'endpoints'
            
            headers = {
                'Content-Type': 'application/json',
                'API_KEY': self.api_key
            }

            data = {
                'ptr_id': self.ptr_id,
                'request_type': request_type
            }

            try:
                response = requests.post(self.api_url, headers=headers, json=data)
                self.response_metadata = response.json()
                self.endpoint_params = self.response_metadata[0]
                return self.endpoint_params
        
            except requests.RequestException as e:
                print(f"Error during request: {e}")
                return None
        else:
            return None
        
    def get_ptr_id(self):
        if self.ptr_id is None:
            if self.model_name is not None:
                request_type = 'get_ptr_id'
                
                headers = {
                    'Content-Type': 'application/json',
                    'API_KEY': self.api_key
                }

                data = {
                    'name': self.model_name,
                    'request_type': request_type
                }

                try:
                    response = requests.post(self.api_url, headers=headers, json=data)
                    self.ptr_id = response.text
                    return response.text
            
                except requests.RequestException as e:
                    print(f"Error during request: {e}")
                    return None
            else:
                return None
        else:
            return self.ptr_id
        
    def get_parameters(self, endpoint):
        if self.endpoint_params and endpoint in self.endpoint_params:
            self.selected_endpoint = endpoint
            return self.endpoint_params[endpoint]
        else:
            print(f"Endpoint '{endpoint}' not found or failed to fetch endpoints.")
            return None
    
    def init_model_predictor(self):
        if self.response_metadata[2].lower() in 'yolov5':
            self.model_predictor = Yolov5_Client(self.ptr_id, self.api_key, self.selected_endpoint)
        elif self.response_metadata[2].lower() in ["diffusers_sd", "diffusers_sdxl", "sdxl_turbo"]:
            self.model_predictor = Diffusers_Client(self.ptr_id, self.api_key, self.selected_endpoint)
        elif self.response_metadata[2].lower() in 'llms':
            self.model_predictor = Llms_Client(self.ptr_id, self.api_key, self.selected_endpoint)
        elif self.response_metadata[2].lower() in 'transformers':
            self.model_predictor = Transformers_Client(self.ptr_id, self.api_key, self.selected_endpoint, self.response_metadata[3])
        else:
            print ("Wrong Model Input")
            
    def predict(self, **kwargs):
        if not self.model_predictor:
            self.init_model_predictor()

        return self.model_predictor.predict(**kwargs)
        

class Yolov5_Client():
    def __init__(self, ptr_id, api_key, selected_endpoint):
        self.initial_url = 'https://n4kh6hh8p3.execute-api.us-east-1.amazonaws.com/'
        self.ptr_id = ptr_id
        self.api_key = api_key 
        self.selected_endpoint = selected_endpoint
    
    def predict(self, **kwargs):
        url = os.path.join(self.initial_url, self.ptr_id, "inference", self.selected_endpoint)
        
        payload = {}
        img_path = kwargs.get('image_path', None)
        files=[('img',(os.path.basename(img_path),open(img_path,'rb'),'image/jpeg'))]
        headers = {
        'API_KEY': self.api_key
        }
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        return response

class Diffusers_Client():
    def __init__(self, ptr_id, api_key, selected_endpoint):
        self.initial_url = 'https://n4kh6hh8p3.execute-api.us-east-1.amazonaws.com/'
        self.ptr_id = ptr_id
        self.api_key = api_key
        self.selected_endpoint = selected_endpoint
    
    def predict(self, **kwargs):
        url = os.path.join(self.initial_url, self.ptr_id, "inference", self.selected_endpoint)
        
        if "txt2img" == self.selected_endpoint.lower():
            
            data = {
                "prompt": kwargs.get('prompt', None),
                "negative_prompt": kwargs.get('negative_prompt', None),
                "height": kwargs.get('height', None),
                "width": kwargs.get('width', None),
                "num_inference_steps": kwargs.get('num_inference_steps', None),
                "guidance_scale": kwargs.get('guidance_scale', None),
                "eta": kwargs.get('eta', None)
            }
            fields = {
                'data': json.dumps(data)
            }
            multipart_encoder = MultipartEncoder(fields=fields)
    
            headers = {
                'accept': 'image/jpeg',
                'Content-Type': multipart_encoder.content_type,
                'API_KEY': self.api_key
            }
            
            response = requests.request(
                method="POST",
                url=url,
                headers=headers,
                data=multipart_encoder.to_string()
            )
            return response
            
        elif "img2img" == self.selected_endpoint.lower():
            
            data = {
                "prompt": kwargs.get('prompt', None),
                "negative_prompt": kwargs.get('negative_prompt', None),
                "height": kwargs.get('height', None),
                "width": kwargs.get('width', None),
                "num_inference_steps": kwargs.get('num_inference_steps', None),
                "guidance_scale": kwargs.get('guidance_scale', None),
                "eta": kwargs.get('eta', None)
            }
            fields = {
                'data': json.dumps(data),
                'img': ('image.jpg', open(kwargs.get('img', None), 'rb'), 'image/jpeg') 
            }
            multipart_encoder = MultipartEncoder(fields=fields)
    
            headers = {
                'accept': 'image/jpeg',
                'Content-Type': multipart_encoder.content_type,
                'API_KEY': self.api_key
            }
            
            response = requests.request(
                method="POST",
                url=url,
                headers=headers,
                data=multipart_encoder.to_string()
            )
            return response
            
        elif "inpaint" == self.selected_endpoint.lower():
            
            data = {
                "prompt": kwargs.get('prompt', None),
                "negative_prompt": kwargs.get('negative_prompt', None),
                "height": kwargs.get('height', None),
                "width": kwargs.get('width', None),
                "num_inference_steps": kwargs.get('num_inference_steps', None),
                "guidance_scale": kwargs.get('guidance_scale', None),
                "eta": kwargs.get('eta', None)
            }
            fields = {
                'data': json.dumps(data),
                'img': ('image.jpg', open(kwargs.get('img', None), 'rb'), 'image/jpeg'),
                'img_mask': ('image_mask.jpg', open(kwargs.get('img_mask', None), 'rb'), 'image/jpeg') 
            }
            multipart_encoder = MultipartEncoder(fields=fields)
    
            headers = {
                'accept': 'image/jpeg',
                'Content-Type': multipart_encoder.content_type,
                'API_KEY': self.api_key
            }
            
            response = requests.request(
                method="POST",
                url=url,
                headers=headers,
                data=multipart_encoder.to_string()
            )
            return response
            
        else:
            return "Endpoint does not exists"
        
class Llms_Client():
    # need to fix the payload input
    def __init__(self, ptr_id, api_key, selected_endpoint):
        self.initial_url = 'https://n4kh6hh8p3.execute-api.us-east-1.amazonaws.com/'
        self.ptr_id = ptr_id
        self.api_key = api_key 
        self.selected_endpoint = selected_endpoint
    
    def predict(self, **kwargs):
        url = os.path.join(self.initial_url, self.ptr_id, "inference", self.selected_endpoint)
        
        sampling_params = {
            "temperature": kwargs.get("sampling_params", {}).get("temperature"),
            "logprobs": kwargs.get("sampling_params", {}).get("logprobs")
        }
        data = {
            "prompt": kwargs.get("prompt",None),
            "stream": kwargs.get("stream",None),
            "sampling_params":sampling_params
        }

        fields = {
                'data': json.dumps(data)
            }
        multipart_encoder = MultipartEncoder(fields=fields)
        headers = {
                'accept': 'image/jpeg',
                'Content-Type': multipart_encoder.content_type,
                'API_KEY': self.api_key
            }
        
        response = requests.request(
                method="POST",
                url=url,
                headers=headers,
                data=multipart_encoder.to_string()
            )
        return response
    
class Transformers_Client():
    def __init__(self, ptr_id, api_key, selected_endpoint, model_sub_category):
        self.initial_url = 'https://n4kh6hh8p3.execute-api.us-east-1.amazonaws.com/'
        self.ptr_id = ptr_id
        self.api_key = api_key 
        self.selected_endpoint = selected_endpoint
        self.model_sub_category = model_sub_category
    
    def predict(self, **kwargs):
        url = os.path.join(self.initial_url, self.ptr_id, "inference", self.selected_endpoint)
        if self.model_sub_category.lower() == "summarization" or self.model_sub_category.lower() == "token-classification" or self.model_sub_category.lower() == "text-classification" or self.model_sub_category.lower() == "text2text-generation":
            data = {
                    "inputs": kwargs.get('inputs', None)
                }
            fields = {
                    'data': json.dumps(data)
                }
            multipart_encoder = MultipartEncoder(fields=fields)
            headers = {
                    'accept': 'image/jpeg',
                    'Content-Type': multipart_encoder.content_type,
                    'API_KEY': self.api_key
                }
            
            response = requests.request(
                    method="POST",
                    url=url,
                    headers=headers,
                    data=multipart_encoder.to_string()
                )
            return response
        
        elif self.model_sub_category.lower() == "question-answering":
            data = {
                    "question": kwargs.get("question",None),
                    "context": kwargs.get("context",None),
                }
            fields = {
                    'data': json.dumps(data)
                }
            multipart_encoder = MultipartEncoder(fields=fields)
            headers = {
                    'accept': 'image/jpeg',
                    'Content-Type': multipart_encoder.content_type,
                    'API_KEY': self.api_key
                }
            
            response = requests.request(
                    method="POST",
                    url=url,
                    headers=headers,
                    data=multipart_encoder.to_string()
                )
            return response
        
        elif self.model_sub_category.lower() == "translation":
            data = {
                    "inputs": kwargs.get("inputs",None),
                    "src_lang": kwargs.get("src_lang",None),
                    "tgt_lang": kwargs.get("tgt_lang",None)
                }
            fields = {
                    'data': json.dumps(data)
                }
            multipart_encoder = MultipartEncoder(fields=fields)
            headers = {
                    'accept': 'image/jpeg',
                    'Content-Type': multipart_encoder.content_type,
                    'API_KEY': self.api_key
                }
            
            response = requests.request(
                    method="POST",
                    url=url,
                    headers=headers,
                    data=multipart_encoder.to_string()
                )
            return response
        elif self.model_sub_category.lower() == "table-question-answering":
            inputs = {
                    "query": kwargs.get("inputs", {}).get("query"),
                    "table": kwargs.get("inputs", {}).get("table"),
                }
            payload = {
                "inputs": inputs
            }
            fields = {
                    'data': json.dumps(payload)
                }
            multipart_encoder = MultipartEncoder(fields=fields)
            headers = {
                    'accept': 'image/jpeg',
                    'Content-Type': multipart_encoder.content_type,
                    'API_KEY': self.api_key
                }
            
            response = requests.request(
                    method="POST",
                    url=url,
                    headers=headers,
                    data=multipart_encoder.to_string()
                )
            return response
        elif self.model_sub_category.lower() == "zero-shot-classification":
            data = {
                    "inputs": kwargs.get("inputs",None),
                    "candidate_labels": kwargs.get("candidate_labels",None)
                }
            fields = {
                    'data': json.dumps(data)
                }
            multipart_encoder = MultipartEncoder(fields=fields)
            headers = {
                    'accept': 'image/jpeg',
                    'Content-Type': multipart_encoder.content_type,
                    'API_KEY': self.api_key
                }
            
            response = requests.request(
                    method="POST",
                    url=url,
                    headers=headers,
                    data=multipart_encoder.to_string()
                )
            return response
        
class CustomModel_Client():
    def __init__(self, ptr_id, api_key, selected_endpoint):
        self.initial_url = 'https://n4kh6hh8p3.execute-api.us-east-1.amazonaws.com/'
        self.ptr_id = ptr_id
        self.api_key = api_key
        self.selected_endpoint = selected_endpoint
    
    def predict(self, **kwargs):
        url = os.path.join(self.initial_url, self.ptr_id, "inference", self.selected_endpoint)
        fields = {}
    
        if 'text' in kwargs:
            fields['text'] = json.dumps(kwargs['text'])
        
        if 'json' in kwargs:
            fields['json'] = kwargs['json']
        
        if 'dataframe' in kwargs:
            fields['dataframe'] = kwargs['dataframe']
        
        if 'numpy' in kwargs:
            fields['numpy'] = kwargs['numpy']
        
        if 'input_img' in kwargs:
            fields['input_img'] = ('image.jpg', open(kwargs['input_img'], 'rb'), 'image/jpeg')
        
        if 'file' in kwargs:
            fields['file'] = ('file.yml', open(kwargs['file'], 'rb'), get_mime_type('file.yml'))
        
        multipart_encoder = MultipartEncoder(fields=fields)
        headers = {
            'accept': 'image/jpeg',
            'Content-Type': multipart_encoder.content_type,
            'API_KEY': self.api_key
        }
        
        response = requests.request(
            method="POST",
            url=url,
            headers=headers,
            data=multipart_encoder.to_string()
        )
        return response
