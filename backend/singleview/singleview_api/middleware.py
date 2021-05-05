class CustomHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-Singleview-Response-Id'] = request.META.get('HTTP_X_SINGLEVIEW_REQUEST_ID')
        return response