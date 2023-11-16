from rest_framework.parsers import MultiPartParser, DataAndFiles
import json
from django.http import QueryDict
class MultipartJsonParser(MultiPartParser):

    def parse(self, stream, media_type=None, parser_context=None):
        result = super().parse(
            stream,
            media_type=media_type,
            parser_context=parser_context
        )
        data = {}

        # for case1 with nested serializers
        # parse each field with json
        # for key, value in result.data.items():
        #     if type(value) != str:
        #         data[key] = value
        #         continue
        #     if '{' in value or "[" in value:
        #         try:
        #             data[key] = json.loads(value)
        #         except ValueError:
        #             data[key] = value
        #     else:
        #         data[key] = value

        # for case 2
        # find the data field and parse it
        data = json.loads(result.data["parent"][0])

        qdict = QueryDict('', mutable=True)
        qdict.update(data)
        return DataAndFiles(qdict, result.files)