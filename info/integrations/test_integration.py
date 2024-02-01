from rest_framework.views import APIView
import datetime
import uuid
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .utils import get_access_token,IntegrationSudEmiProf



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
        return Response(sudlangan.json())




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
        return Response(emi.json())

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
        return Response(prof.json())
        ####





