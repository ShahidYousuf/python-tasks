from rest_framework import serializers
from .models import Quote
from django.contrib.auth.models import User

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('__all__')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model =  User
        fields = ('username', 'password')
