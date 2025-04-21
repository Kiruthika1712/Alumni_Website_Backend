from rest_framework import serializers
from .models import mailVerification

# serializer of mailVerification model
class mailverSerializer(serializers.ModelSerializer):
    class Meta:
        model = mailVerification
        fields =['email', 'otp']