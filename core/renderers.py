from rest_framework.renderers import JSONRenderer
import json


class UserRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code  # Get the HTTP status code
        response_data = {}

        if 'ErrorDetail' in str(data):
            response_data['errors'] = data
        else:
            response_data['data'] = data

        response_data['status'] = status_code  # Include the HTTP status code in the response

        response = json.dumps(response_data)
        return response
