from rest_framework.response import Response
from rest_framework.status import *


class APIResponse400(Response):
    def __init__(self, data=None, template_name=None, headers=None, exception=False, content_type=None):
        message = {
            'success': False,
            'response_code' : 400,
            'message' : data
        }
        super().__init__(message, HTTP_400_BAD_REQUEST, template_name, headers, exception, content_type)


class APIResponse201(Response):
    
    def __init__(self, data=None, template_name=None, headers=None, exception=False, content_type=None):
        message = {
            'success': True,
            'response_code' : 200,
            'message' : data
        }
        super().__init__(message, HTTP_201_CREATED, template_name, headers, exception, content_type)

