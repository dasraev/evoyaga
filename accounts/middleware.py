
from django.conf import settings
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
import logging
from datetime import datetime


logger = logging.getLogger(__name__)
handler = logging.FileHandler('custom_request.log')
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

class CustomRequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        response = self.get_response(request)
        user = request.user
        request_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        request_path = request.path
        if user.is_authenticated:
            log_message = f'METHOD:{request.method}, USER_ID: {user.id},  USER_LOGIN: {user.login},USER_FIRST_NAME: {user.first_name},USER_LAST_NAME: {user.last_name}, Time: {request_time}, Path: {request_path}'
        else:
            log_message = f'METHOD:{request.method} ,USER:ANONYMOUS,  Time: {request_time}, Path: {request_path}'

        logger.info(log_message)

        return response


