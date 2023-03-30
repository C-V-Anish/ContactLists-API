from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(min_length=8,write_only=True)
    email=serializers.EmailField(min_length=15)
    first_name=serializers.CharField(min_length=6,max_length=20)
    last_name=serializers.CharField(min_length=6,max_length=10)
    # username=serializers.CharField(min_length=12,max_length=32)
    
    

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']
    
    def validate(self, attrs):
        email=attrs.get('email','')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'msg':'Email already in use'})
        return super().validate(attrs)
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    


