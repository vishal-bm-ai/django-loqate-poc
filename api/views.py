from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rest_framework import status
from django_loqate_poc.loqate_key import KEY

class AddressFindAPIView(APIView):

    def post(self,request,*args,**kwargs):
        text = request.data['text']
        url = "https://api.addressy.com/Capture/Interactive/Find/v1.1/json3.ws"
        params ={
            'Key': KEY,
            'Text': text,
            'Limit':10
        }
        try:
            response = requests.post(url=url,params=params)
        except Exception as e:
            print(e)
        return Response(response.json())

class AddressRetrieveAPIView(APIView):

    def post(self,request,*args,**kwargs):
        id = request.data['id']
        url = "https://api.addressy.com/Capture/Interactive/Retrieve/v1/json3.ws"
        params={
            'Key':KEY,
            'id':id,
        }
        try:
            response = requests.post(url=url,params=params)
        except Exception as e:
            print(e)
        return Response(response.json())    
