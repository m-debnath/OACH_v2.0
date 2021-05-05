class CustomHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-Servicedelivery-Response-Id'] = request.META.get('HTTP_X_SERVICEDELIVERY_REQUEST_ID')
        return response