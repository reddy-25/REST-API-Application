from django.contrib.auth.models import User
from .models import advisor, booking
from rest_framework import serializers



class advisor_serializer(serializers.ModelSerializer):
    class Meta:
        model = advisor
        fields = ['id','advisor_name', 'photo_url']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password')
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],     password = validated_data['password'])
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class booking_serializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = ['booking_time']

class full_details_booking(serializers.ModelSerializer):
    class Meta:
       model = booking
       fields = ['id','advisor_name', 'photo_url', 'advisor_id', 'booking_time']

