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

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.role = validated_data.get('role', instance.role)
        
        password = validated_data.get('password', None)
        if password is not None:
            instance.set_password(password)  # Set the password if provided
        
        instance.save()
        return instance
