from rest_framework import serializers


class Req_Serializers(serializers.Serializer):
    keyword = serializers.CharField(max_length=1000)