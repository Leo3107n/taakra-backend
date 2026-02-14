from rest_framework import serializers
from .models import User, Category, Competition, Registration

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
