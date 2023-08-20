from rest_framework import serializers
from .models import User
import django.contrib.auth.password_validation as validators


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  'role'
                  ]

    @staticmethod
    def validate_password(data):
        validators.validate_password(password=data, user=User)
        return data

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],
                                   email=validated_data['email'],
                                   first_name=validated_data['first_name'],
                                   last_name=validated_data['last_name'],
                                   role=validated_data['role']
                                  )
        user.set_password(validated_data['password'])
        user.save()
        return user
