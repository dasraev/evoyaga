from rest_framework.views import APIView
from juvenile import models as juvenile_models
from rest_framework.response import Response
import base64, requests, json, xmltodict
import xml.etree.ElementTree as ET
from django.http import Http404
from info.models import Region, District
from rest_framework.permissions import AllowAny
import datetime
import uuid
from .utils import login,get_refresh_token,get_access_token,IntegrationSudEmiProf

def get_gender(gender):
    if gender == '1':
        return 'M'
    else:
        return 'F'


def get_convicted_auth_token():
    url = "https://stat.mvd.uz/api/uis/v1/oauth/token"
    header = {
        "Content-Type": "application/json",
        "Authorization": "Basic d2ViY2xpZW50OkVGRTU4NkY3NUQzMzZFNDRCRDI0QjhDRDQ1RUE4"
    }
    params = {
        'grant_type': 'password',
        'grant_method': 'password',
    }
    data = {
        "username": "eGov.integratoin",
        "password": "integratoin1050"
    }
    json_object = json.dumps(data, indent=4)
    response = requests.post(
        url,
        data=json_object,
        headers=header,
        params=params,
    )
    data = response.json()
    return data['access_token']


def get_authorization_token():
    url = "https://iskm.egov.uz:9444/oauth2/token"
    Consumer_key = 'rewFnDWmKyhDdv7fL77Ov1laTgIa'
    Consumer_secret = '9Px65YpLAc5qxLvyhWoAkPqf4poa'
    header = {
        "Content-Type": "application/json",
    }
    params = {
        'grant_type': 'password',
        'username': 'mvd-eve',
        'password': 'aCee2VzTMa1cJJw6D1Z4',
    }
    response = requests.post(
        url,
        headers=header,
        params=params,
        auth=(Consumer_key, Consumer_secret)
    )
    data = response.json()
    print('1111111111111111', data)
    return data['access_token']


def get_inspector_authorization_token():
    url = "http://172.250.1.65:7101/Agency/token"
    header = {
        "Content-Type": "application/json",
    }
    params = {
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache',
    }
    data = {
        "Login": "Nazorat",
        "Password": "11V_NazoR@T",
        "CurrentSystem": "1"
    }
    json_object = json.dumps(data, indent=4)
    response = requests.post(
        url,
        data=json_object,
        headers=header,
        params=params,
    )
    data = response.json()
    return data['access_token']


def get_birth_passport_data(request):
    doc_seria = request.GET.get('doc_seria', None)
    doc_number = request.GET.get('doc_number', None)
    url = "https://apimgw.egov.uz:8243/justice/service/birth/v1/"
    token = get_authorization_token()
    header = {
        'Content-Type': 'Application/json',
        "Authorization": f"Bearer {token}",
    }
    data = {
        "id": "123",
        "cert_series": doc_seria,
        "cert_number": doc_number
    }
    json_object = json.dumps(data, indent=4)
    response = requests.post(
        url,
        headers=header,
        data=json_object
    )
    return response.json()


def get_inspector_doc_data(request):
    pinfl = request.GET.get('pinfl', None)
    url = "http://172.250.1.67:7116/api/Staff/GetPersonDocuments/"
    token = get_inspector_authorization_token()
    header = {
        'Content-Type': 'Application/json',
        "Authorization": f"Bearer {token}",
    }
    data = {
        "PINPP": pinfl,
    }
    json_object = json.dumps(data, indent=4)
    response = requests.post(
        url,
        headers=header,
        data=json_object
    )
    return response.json()


def get_address(request):
    pinfl = request.GET.get('pinfl', None)
    url = "https://apimgw.egov.uz:8243/mvd/services/address/info/pin/v1"
    token = get_authorization_token()
    header = {
        'Content-Type': 'Application/json',
        "Authorization": f"Bearer {token}",
    }
    data = {
        "pinpp": pinfl,
    }
    json_object = json.dumps(data, indent=4)
    response = requests.post(
        url,
        headers=header,
        data=json_object
    )
    response_json = response.json()
    if response.status_code == 200:
        if 'Data' in response_json:
            gcp_region_id = response_json['Data']['PermanentRegistration']['Region']['Id']

            our_region = Region.objects.get(extra_id=gcp_region_id)

            response_json['Data']['PermanentRegistration']['Region']['our_region_id'] = our_region.id
    return response_json


def get_is_registered_psychiatrist_dispensary_by_pinfl(request):
    pinfl = request.GET.get('pinfl', None)
    url = "https://apimgw.egov.uz:8243/minzdrav/disp/psycho/v1/by-pinpp"
    token = get_authorization_token()
    header = {
        'Content-Type': 'Application/json',
        "Authorization": f"Bearer {token}",
    }
    data = {
        "pinpp": pinfl,
    }
    json_object = json.dumps(data, indent=4)
    response = requests.post(
        url,
        headers=header,
        data=json_object
    )
    return response.json()


def get_is_registered_psychiatrist_dispensary_by_birth_doc(request):
    serial = request.GET.get('serial', None)
    number = request.GET.get('number', None)
    birthDate = request.GET.get('birthDate', None)
    url = "https://apimgw.egov.uz:8243/minzdrav/disp/psycho/v1/by-cert"
    token = get_authorization_token()
    header = {
        'Content-Type': 'Application/json',
        "Authorization": f"Bearer {token}",
    }
    data = {
        "serial": serial,
        "number": number,
        "birthDate": birthDate,
    }
    json_object = json.dumps(data, indent=4)
    response = requests.post(
        url,
        headers=header,
        data=json_object
    )
    return response.json()


def get_is_registered_narko_dispensary_by_pinfl(request):
    pinfl = request.GET.get('pinfl', None)
    url = "https://apimgw.egov.uz:8243/minzdrav/disp/narko/v1/by-pinpp"
    token = get_authorization_token()
    header = {
        'Content-Type': 'Application/json',
        "Authorization": f"Bearer {token}",
    }
    data = {
        "pinpp": pinfl,
    }
    json_object = json.dumps(data, indent=4)
    response = requests.post(
        url,
        headers=header,
        data=json_object
    )
    return response.json()


def get_is_registered_narko_dispensary_by_birth_doc(request):
    serial = request.GET.get('serial', None)
    number = request.GET.get('number', None)
    birthDate = request.GET.get('birthDate', None)
    url = "https://apimgw.egov.uz:8243/minzdrav/disp/narko/v1/by-cert"
    token = get_authorization_token()
    header = {
        'Content-Type': 'Application/json',
        "Authorization": f"Bearer {token}",
    }
    data = {
        "serial": serial,
        "number": number,
        "birthDate": birthDate,
    }
    json_object = json.dumps(data, indent=4)
    response = requests.post(
        url,
        headers=header,
        data=json_object
    )
    return response.json()


def get_passport_data(request):
    pinfl = request.GET.get('pinfl', None)
    passport_data = request.GET.get('passport_data', None)
    # url = "https://apimgw.egov.uz:8243/gcp/pinser/v1"
    url = "https://apimgw.egov.uz:8243/gcp/docrest/v1"
    token = get_authorization_token()
    header = {
        'Content-Type': 'application/json',
        "Authorization": f"Bearer {token}",
    }
    data = {
        "transaction_id": 1,
        "is_consent": "Y",
        "pinpp": pinfl,
        "document": passport_data,
        "langId": 1,
        "is_photo": 'Y',
        "Sender": "M",
        "sender_pinfl": pinfl

    }
    json_data = json.dumps(data, indent=4)
    response = requests.post(url, headers=header, data=json_data)
    return response.json()


def get_passport_data2(request):
    pinfl = request.GET.get('pinfl', None)
    passport_data = request.GET.get('passport_data', None)
    url = "https://apimgw.egov.uz:8243/gcp/pinser/v1"
    token = get_authorization_token()
    header = {
        'Content-Type': 'text/xml',
        "Authorization": f"Bearer {token}",
    }
    data = f"""
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:eas="http://fido.com/EasuEGServices">
            <soapenv:Header/>
            <soapenv:Body>
                <eas:CEPRequest>
                    <eas:Data><![CDATA[<?xml version="1.0"?>
            <DataCEPRequest xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" >
                <pinpp>{pinfl}</pinpp>
                <document>{passport_data}</document>
                <langId>1</langId>
            </DataCEPRequest>]]></eas:Data>
                    <eas:Signature>?</eas:Signature>
                    <eas:PublicCert>?</eas:PublicCert>
                    <eas:SignDate>?</eas:SignDate>
                </eas:CEPRequest>
            </soapenv:Body>
            </soapenv:Envelope>
        """
    response = requests.post(
        url,
        headers=header,
        data=data
    )
    xml_text = None
    root = ET.fromstring(response.content)
    for child in root.iter('*'):
        if child.text != None and child.text != '1':
            xml_text = child.text

    try:
        response_data = ET.fromstring(xml_text)
        wrong_date = response_data[0][19].text
        day = wrong_date[8:10]
        month = wrong_date[5:7]
        year = wrong_date[0:4]
        pasport_given_date = f'{year}-{month}-{day}'
        data = {
            'first_name': response_data[0][2].text,
            'last_name': response_data[0][1].text,
            'father_name': response_data[0][3].text,
            'birth_date': response_data[0][6].text,
            'gender': get_gender(response_data[0][16].text),
            'passport_given_date': pasport_given_date
        }
        return data
    except:
        raise Http404


def get_passport_data_with_foto(request, passport_data):
    pinfl = request.GET.get('pinfl', None)
    url = "https://apimgw.egov.uz:8243/gcp/photoservice/v1"
    token = get_authorization_token()
    header = {
        'Content-Type': 'text/xml',
        "Authorization": f"Bearer {token}",
    }
    data = f"""
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:idm="http://fido.com/IdmsEGMICServices">
            <soapenv:Header/>
            <soapenv:Body>
                <idm:GetDataByPinppRequest>
                    <idm:Data><![CDATA[<?xml version="1.0"?>
                    <DataByPinppRequest xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="file:///d:/STS/workspaceEASU/IdmsEGMICServices/src/main/resources/xsdData/GetDatabyDoc.xsd">
                    <pinpp>{pinfl}</pinpp>
                    <doc_give_date>{passport_data['passport_given_date']}</doc_give_date>
                    <langId>1</langId>
                    <is_consent_pers_data>Y</is_consent_pers_data>
                    </DataByPinppRequest>]]></idm:Data>
                    <idm:Signature></idm:Signature>
                    <idm:PublicCert></idm:PublicCert>
                    <idm:SignDate></idm:SignDate>
                </idm:GetDataByPinppRequest>
            </soapenv:Body>
            </soapenv:Envelope>
                        """
    response = requests.post(
        url,
        headers=header,
        data=data
    )
    xml_text = None
    root = ET.fromstring(response.content)
    for child in root.iter('*'):
        if child.text != None and child.text != '1':
            xml_text = child.text

    if xml_text == '2':
        return passport_data
    response_data = ET.fromstring(xml_text)

    passport_data['photo'] = response_data[0][0].text
    return passport_data


def get_is_convicted(request):
    # passport_data2 = get_inspector_doc_data(request=request)

    pinfl = request.GET.get('pinfl', None)
    passportSerial = request.GET.get('passportSerial', None)
    passportNumber = request.GET.get('passportNumber', None)
    birthDate = request.GET.get('birthDate', None)
    firstName = request.GET.get('firstName', None)
    lastName = request.GET.get('lastName', None)

    url = "https://stat.mvd.uz/api/uis/v1/api/e-xukumat/request"
    token = get_convicted_auth_token()
    header = {
        'Content-Type': 'Application/json',
        "Authorization": f"Bearer {token}",
    }

    data = {
        "pinfl": pinfl,
        "passportSerial": passportSerial,
        "passportNumber": passportNumber,
        "birthDate": birthDate,
        "firstName": firstName,
        "lastName": lastName
    }

    json_object = json.dumps(data, indent=4)

    response = requests.post(
        url,
        headers=header,
        data=json_object
    )
    return response.json()


# Biometrik passport, ID Karta, Tug'ilganlik haqida guvohnoma, Kinder passport,
class GetPassportData(APIView):
    queryset = juvenile_models.Juvenile.objects.all()

    def get(self, request, format=None):
        passport_data = get_passport_data(request=request)
        return Response(passport_data)


class GetAddress(APIView):
    queryset = juvenile_models.Juvenile.objects.all()

    def get(self, request, format=None):
        address = get_address(request=request)
        return Response(address)


class GetBirthPasportData(APIView):
    queryset = juvenile_models.Juvenile.objects.all()

    def get(self, request, format=None):
        birth_passport_data = get_birth_passport_data(request=request)
        return Response(birth_passport_data)


class GetIsRegisteredPsychiatristDispensaryByPinfl(APIView):
    queryset = juvenile_models.Juvenile.objects.all()

    def get(self, request, format=None):
        is_registered_psychiatrist_dispensary = get_is_registered_psychiatrist_dispensary_by_pinfl(request=request)
        return Response(is_registered_psychiatrist_dispensary)


class GetIsRegisteredPsychiatristDispensaryByBirthDoc(APIView):
    queryset = juvenile_models.Juvenile.objects.all()

    def get(self, request, format=None):
        is_registered_psychiatrist_dispensary = get_is_registered_psychiatrist_dispensary_by_birth_doc(request=request)
        return Response(is_registered_psychiatrist_dispensary)


class GetIsRegisteredNarkoDispensaryByPinfl(APIView):
    queryset = juvenile_models.Juvenile.objects.all()

    def get(self, request, format=None):
        is_registered_narko_dispensary = get_is_registered_narko_dispensary_by_pinfl(request=request)
        return Response(is_registered_narko_dispensary)


class GetIsRegisteredNarkoDispensaryByBirthDoc(APIView):
    queryset = juvenile_models.Juvenile.objects.all()

    def get(self, request, format=None):
        is_registered_narko_dispensary = get_is_registered_narko_dispensary_by_birth_doc(request=request)
        return Response(is_registered_narko_dispensary)


class GetProphylacticApiView(APIView):
    queryset = juvenile_models.Juvenile.objects.all()

    def get(self, request, format=None):
        inspector_doc_data = get_inspector_doc_data(request=request)
        return Response(inspector_doc_data)


class GetIsConvictedApiView(APIView):
    queryset = juvenile_models.Juvenile.objects.all()

    def get(self, request, format=None):
        # inspector_doc_data = get_is_convicted(request=request)
        return Response('inspector_doc_data')



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
                "X-token": get_access_token(),
                "user-id": "e-voyagaYetmagan"
            }
        }
        obj = IntegrationSudEmiProf()
        sudlangan = obj.sudlangan_by_pinfl(data_request, headers)
        response = sudlangan.json()['result']
        data = {}

        if response['code'] == 200 and response['message'].lower() == 'success':
            data['sudlangan'] = bool(response['data'])
            return Response(data)
        else:
            data['sudlangan'] = None
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
                "X-token": get_access_token(),
                "user-id": "e-voyagaYetmagan"
            }
        }
        obj = IntegrationSudEmiProf()
        emi = obj.emi_shtraf_by_pinfl(data_request, headers)
        data = {}
        response = emi.json()['result']
        if response['code'] == 200 and response['message'].lower() == 'success':
            filtered_data = [item for item in response['data'] if item.get("violation_article").replace(" ", "")[:2] == "47"]
            data['47-modda'] = bool(filtered_data)
            return Response(data)
        else:
            data['47-modda'] = None
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
                "X-token": get_access_token(),
                "user-id": "e-voyagaYetmagan"
            }
        }

        obj = IntegrationSudEmiProf()
        prof = obj.prof_uchot_by_pinfl(data_request, headers)
        data = {}
        response = prof.json()['result']
        if response['code'] == 200 and response['message'].lower() == 'success':
            filtered_data = [item for item in response['data'] if
                             item.get("R56") != "11" and item.get("R56") != "12" and item.get("R56") != "14" and item.get("R56") != "16" and item.get("R56") != "18" and
                              item.get("R56") != "19" and item.get("R56") != "21" and item.get("R56") != "77" ]
            data['prof_uchot'] = bool(filtered_data)
            return Response(data)
        else:
            data['prof_uchot'] = None
            return Response(data)





