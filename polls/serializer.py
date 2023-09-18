from rest_framework import serializers
from .models import jadval, phone
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User 


class jadvalSerializer(serializers.ModelSerializer):
    class Meta:
        model=jadval
        fields = ('name', 'nechtaligi', 'user')

    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User, username=self.context['request'].user)
        return super(jadvalSerializer, self).create(validated_data)


class phoneSerializer(serializers.ModelSerializer):
    class Meta:
        model=phone
        fields=('name', 'number', 'user')

    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User, username=self.context['request'].user)
        return super(phoneSerializer, self).create(validated_data)