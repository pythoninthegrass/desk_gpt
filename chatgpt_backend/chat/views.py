#!/usr/bin/env python

from .serializers import ChatSerializer
from decouple import config
from openai import OpenAI
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

API_KEY = config("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)


def generate_response(message):
    response = client.chat.completions.create(model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": message
        }
    ])
    return response.choices[0].message.content


class ChatAPIView(APIView):
    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.validated_data.get('message')
            response_message = generate_response(message)
            return Response({"response": response_message}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

