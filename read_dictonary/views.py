from rest_framework.decorators import api_view
from .serializers import Req_Serializers
from rest_framework.response import Response
from rest_framework import status


def process_list(dictionary_data: list):
    response = {}
    for data in dictionary_data:
        data_split = data.split("=", 1)
        response[data_split[0].lower()] = data_split[1]
    return response


@api_view(['POST'])
def snippet_list(request):
    with open("static/dictionary.txt", 'r') as f:
        data = f.readlines()
    definitions_data = process_list(data)

    serializer = Req_Serializers(data=request.data)

    if serializer.is_valid():
        key = serializer.data['keyword'].strip().lower()
        if key in definitions_data:
            return Response({"word": key, "definition": definitions_data[key]}, status=status.HTTP_200_OK)
        else:
            return Response({"word": key, "error": "Word Not present"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


