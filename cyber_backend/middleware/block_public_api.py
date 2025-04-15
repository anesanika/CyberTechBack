import os
from django.http import HttpResponseNotFound

class BlockPublicAPI:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        api_paths = ['/api/', '/api/token/', '/api/token/refresh/', "/store/", "/store/products/", "/store/category/"]
        if any(request.path.startswith(p) for p in api_paths):
            frontend_token = request.headers.get("x-frontend-secret")
            expected_token = os.getenv("FRONTEND_SECRET")

            if frontend_token != expected_token:
                return HttpResponseNotFound()

        return self.get_response(request)
