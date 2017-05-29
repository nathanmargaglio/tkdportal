from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Income


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ('school', 'date', 'check', 'cash',
                  'credit_card', 'vending', 'ez_payment')
