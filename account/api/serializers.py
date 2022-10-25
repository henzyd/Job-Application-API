from django.contrib.auth import get_user_model
# from django.contrib.auth.urls
from rest_framework import serializers


User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password_2 = serializers.CharField(max_length=128)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password_2']

    def save(self):
        user = User(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
        )
        password = self.validated_data['password']
        password_2 = self.validated_data['password_2']

        if password != password_2:
            return serializers.ValidationError({'Response': 'Both passwords don\'t match'})
        
        user.set_password(password)
        user.save()
        return user


