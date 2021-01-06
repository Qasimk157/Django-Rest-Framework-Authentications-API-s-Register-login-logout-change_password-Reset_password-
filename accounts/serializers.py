

from rest_framework import serializers
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','username', 'email', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

##to add entaties we have to add these things as
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'],email=validated_data['email'],
                                        password=validated_data['password'])

        return user


from rest_framework import serializers
from django.contrib.auth.models import User

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)