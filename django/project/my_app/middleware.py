import json
from django.core import serializers
class DemoMiddleware(object):
    def process_request(self, request):
        print("middleware called")
        # print(dir(request))
        # print(request.META)
        # obj = serializers.deserialize('json', request.body)
        print(request.body)
        request.META["HTTP_AUTHORIZATION"] = "Bearer 1234567890987654321234567890"
        print(request.META["HTTP_AUTHORIZATION"])
        # print(request.user.email)

    def process_template_response(self, request, response):
        return response

    def process_response(self, request, response):
        return response

