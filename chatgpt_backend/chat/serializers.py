#!/usr/bin/env python

from rest_framework import serializers

class ChatSerializer(serializers.Serializer):
    message = serializers.CharField()
