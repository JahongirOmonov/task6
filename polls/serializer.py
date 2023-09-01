from rest_framework import serializers
from .models import jadval, phone


class jadvalSerializer(serializers.ModelSerializer):
    class Meta:
        model=jadval
        fields = ('name', 'nechtaligi')


class phoneSerializer(serializers.ModelSerializer):
    class Meta:
        model=phone
        fields=('name', 'number')