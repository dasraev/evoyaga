import datetime
from django.utils import timezone
import uuid
import requests
import json
from info.models import AccessRefreshToken

class IntegrationSudEmiProf:
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


def login():
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

    return {"access": response.json()["result"]["data"]["token"],
            "refresh": response.json()["result"]["data"]["refreshToken"]}


def get_refresh_token(refresh,access):

    url = "http://10.1.27.97:8787/api/v1/auth/token/refresh"
    headers = {
        "X-Timestamp": f"{int(datetime.datetime.now().timestamp())}",
        "X-Request-Id": str(uuid.uuid4()),
    }
    data = {
        "data": {
            "refreshToken": refresh,
            "accessToken": access
        },
        "ident": {
            "user-id": "e-voyagaYetmagan"
        }
    }

    response = requests.post(
        url=url,
        data=json.dumps(data, indent=4),
        headers=headers
    )
    return {"access": response.json()["result"]["data"]["token"],
            "refresh": response.json()["result"]["data"]["refreshToken"]}

def get_access_token():
    obj = AccessRefreshToken.objects.last()

    if obj:
        print(11,obj.date_time_access)
        print(22,obj.date_time_refresh)
        if obj.date_time_access > timezone.now():
            return obj.access
        elif obj.date_time_refresh > timezone.now():
            refresh_token = get_refresh_token(obj.refresh,obj.access)
            obj.access = refresh_token['access']
            obj.refresh = refresh_token['refresh']
            obj.date_time_access = timezone.now() + datetime.timedelta(hours=23)
            obj.save()
            return refresh_token['access']
        else:
            token = login()
            obj = AccessRefreshToken.objects.last()
            obj.access = token['access']
            obj.refresh = token['refresh']
            obj.date_time_access = timezone.now() + datetime.timedelta(hours=23)
            obj.date_time_refresh = timezone.now() + datetime.timedelta(days=350)
            obj.save()
            return token['access']
    else:
        token = login()
        obj = AccessRefreshToken()
        obj.access = token['access']
        obj.refresh = token['refresh']
        obj.date_time_access = timezone.now() + datetime.timedelta(hours = 23)
        obj.date_time_refresh = timezone.now() + datetime.timedelta(days = 350)
        obj.save()
        return token['access']



###
###