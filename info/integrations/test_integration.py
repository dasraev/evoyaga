import requests
import json
from rest_framework.views import APIView
import datetime
import uuid
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
def check_status_code(response):
    if response.status_code == 200:
        return response.json()['result']['data']
    else:
        return None

class AccessTokenView(APIView):
    permission_classes = [AllowAny,]
    def get(self,request):
        url = "http://10.1.27.97:8787/api/v1/auth/token/get"
        headers = {
            "X-Timestamp": f"{int(datetime.datetime.now().timestamp())}",
            "X-Request-Id": str(uuid.uuid4()),
        }

        data = {
            "data": {
                "username": "eVoyagaYetmagan",
                "password": "mq9xTfaFSzxILH12BX08"
            },
            "ident": {
                "user-id": "e-voyagaYetmagan"
            }
        }

        response = requests.post(
            url = url,
            data = json.dumps(data,indent=4),
            headers = headers
        )
        print(response.json())

        return Response(response.json())


class RefreshTokenView(APIView):
    permission_classes = [AllowAny,]
    def get(self,request):
        url = "http://10.1.27.97:8787/api/v1/auth/token/refresh"
        headers = {
            "X-Timestamp": f"{int(datetime.datetime.now().timestamp())}",
            "X-Request-Id": str(uuid.uuid4()),
        }
        token = get_access_token()['result']['data']
        data = {
    "data": {
        "refreshToken": token['refreshToken'],
        "accessToken": token['token']
    },
    "ident": {
        "user-id": "e-voyagaYetmagan"
    }
}

        response = requests.post(
            url = url,
            data = json.dumps(data,indent=4),
            headers = headers
        )
        print(response.json())

        return Response(response.json())

def get_access_token():
    url = "http://10.1.27.97:8787/api/v1/auth/token/get"
    headers = {
        "X-Timestamp": f"{int(datetime.datetime.now().timestamp())}",
        "X-Request-Id": str(uuid.uuid4()),
    }

    data = {
        "data": {
            "username": "eVoyagaYetmagan",
            "password": "mq9xTfaFSzxILH12BX08"
        },
        "ident": {
            "user-id": "e-voyagaYetmagan"
        }
    }

    response = requests.post(
        url = url,
        data = json.dumps(data,indent=4),
        headers = headers
    )

    return response.json()

class TestIntegration:
    def sudlangan_by_pinfl(self, data, headers):


        url = "http://10.1.27.97:8787/api/v1/registration/sud.by.pinfl"

        response = requests.post(
            url=url,
            data=json.dumps(data, indent=4),
            headers=headers,
        )
        # Responseda nima qaytishiga qarab
        return response

    def emi_shtraf_by_pinfl(self,data,headers):

        url = "http://10.1.27.97:8787/api/v1/offender/administrative.by.pinfl"
        response = requests.post(
            url = url,
            data = json.dumps(data,indent=4),
            headers = headers
        )
        return response


    def prof_uchot_by_pinfl(self,data,headers):
        url = "http://10.1.27.97:8787/api/v1/ic/get.by.pinfl"
        response = requests.post(
            url = url,
            data = json.dumps(data,indent=4),
            headers = headers
        )
        return response


class SudView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        pinfl = self.request.query_params.get('pinfl')
        headers = {
            "X-Timestamp": f"{int(datetime.datetime.now().timestamp())}",
            "X-Request-Id": str(uuid.uuid4()),
        }

        data_request = {
            "data": {
                "pinfl": pinfl
            },
            "ident": {
                # "X-token":  "T9KvyzItpdrtUhK6Hx3kcnlFtnl",
                "X-token": get_access_token()['result']['data']['token'],
                "user-id": "e-voyagaYetmagan"
            }
        }
        obj = TestIntegration()
        sudlangan = obj.sudlangan_by_pinfl(data_request, headers)
        data = {}
        data['sudlangan'] = sudlangan.json()
        return Response(data)


class ProfView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        pinfl = self.request.query_params.get('pinfl')
        headers = {
            "X-Timestamp": f"{int(datetime.datetime.now().timestamp())}",
            "X-Request-Id": str(uuid.uuid4()),
        }

        data_request = {
            "data": {
                "pinfl": pinfl,
                "type":"PROFUCHPROB"
            },
            "ident": {
                # "X-token":  "T9KvyzItpdrtUhK6Hx3kcnlFtnl",
                "X-token": get_access_token()['result']['data']['token'],
                "user-id": "e-voyagaYetmagan"
            }
        }

        obj = TestIntegration()
        sudlangan = obj.prof_uchot_by_pinfl(data_request, headers)
        data = {}
        data['sudlangan'] = sudlangan.json()
        return Response(data)


class EmiView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        pinfl = self.request.query_params.get('pinfl')
        headers = {
            "X-Timestamp": f"{int(datetime.datetime.now().timestamp())}",
            "X-Request-Id": str(uuid.uuid4()),
        }

        data_request = {
            "data": {
                "pinfl": pinfl
            },
            "ident": {
                # "X-token":  "T9KvyzItpdrtUhK6Hx3kcnlFtnl",
                "X-token": get_access_token()['result']['data']['token'],
                "user-id": "e-voyagaYetmagan"
            }
        }
        obj = TestIntegration()
        sudlangan = obj.emi_shtraf_by_pinfl(data_request, headers)
        data = {}
        data['sudlangan'] = sudlangan.json()
        return Response(data)


class IntegrationView(APIView):
    permission_classes = [AllowAny,]
    def get(self,request):
        pinfl = self.request.query_params.get('pinfl')
        headers = {
            "X-Timestamp": f"{int(datetime.datetime.now().timestamp())}",
            "X-Request-Id": str(uuid.uuid4()),
        }

        data_request = {
            "data": {
                "pinfl": pinfl
            },
            "ident": {
                "X-token":  get_access_token(),
                # "X-token":  get_access_token()['result']['data']['token'],T9KvyzItpdrtUhK6Hx3kcnlFtnl
                "user-id": "e-voyagaYetmagan"
            }
        }
        obj = TestIntegration()
        sudlangan = obj.sudlangan_by_pinfl(data_request,headers)

        # emi_shtraf = obj.emi_shtraf_by_pinfl(data_request,headers)

        # data_request['data']["type"] = "PROFUCHPROB"

        # prof_uchot = obj.prof_uchot_by_pinfl(data_request,headers)
        data = {}
        data['sudlangan'] = sudlangan.json()
        # data['emi_shtraf'] = emi_shtraf.json()
        # data['prof_uchot'] = prof_uchot.json()

        print('ZZZZZZZ',data)

        return Response(data)