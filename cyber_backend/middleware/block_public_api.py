import os
from django.http import HttpResponseNotFound
from django.conf import settings

class BlockPublicAPI:
    def __init__(self, get_response):
        self.get_response = get_response
        self.expected_token = os.getenv("FRONTEND_SECRET")

    def __call__(self, request):
        # admin page ან static/media ფაილები არ უნდა დაიბლოკოს
        if request.path.startswith("/admin/") or request.path.startswith(settings.MEDIA_URL) or request.path.startswith(settings.STATIC_URL):
            return self.get_response(request)

        frontend_token = request.headers.get("x-frontend-secret")

        if frontend_token != self.expected_token:
            return HttpResponseNotFound()

        return self.get_response(request)
