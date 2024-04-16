import json
from .._request import RequestAPI, HttpMethod

IMAGES_CONFIG = {
    "dall-e-3": {
        "quality": ["standard"],
        "resolution": ["1024x1024"],
    }
}


class ImageObject:
    def __init__(self, data):
        self.url = data.get("url")

class ImageResponse:
    def __init__(self, response, data_dict=False):
        self.data = []
        self.message = response.get("message", "")
        self.error = response.get("error", "")
        if data_dict:
            self.data = response.get("data", [])
        else:
            for item in response.get("data"):
                self.data.append(ImageObject(item))

class Images:

    URL = 'https://trainings.boltiot.com/api/aitools/v1/images/generations'

    request_api = RequestAPI()
    def __init__(self, api_key=None):
        self.api_key = api_key

    def _valid_settings(self, model, size, quality):
        image_config = IMAGES_CONFIG.get(model)
        if not image_config:
            print("model not found")
            return False
        if quality not in image_config.get("quality"):
            print("model quality not supported")
            return False

        if size not in image_config.get("resolution"):
            print("model size/resolution not supported")
            return False
        return True

    def generate(self, model, prompt, n=1, size="256x256", response_format="url", quality="standard"):
        model = model.lower()
        if not self._valid_settings(model, size, quality):
            return
        data = {
            "model":model,
            "prompt":prompt,
            "n":n,
            "size":size,
            "response_format": response_format
        }
        response = self.request_api._make_request(self.URL, HttpMethod.POST, data)
        return ImageResponse(response)
        
    
    def create(self, model, prompt, n=1, size="256x256", response_format="url", quality="standard"):
        model = model.lower()
        if not self._valid_settings(model, size, quality):
            return
        
        data = {
            "model":model,
            "prompt":prompt,
            "n":n,
            "size":size,
            "response_format": response_format
        }
        response = self.request_api._make_request(self.URL, HttpMethod.POST, data)
        return response
        
    
