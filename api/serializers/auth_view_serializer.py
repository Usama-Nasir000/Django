from rest_framework import serializers
from api.models.user_model import CustomUser

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'country', 'date_of_birth', 'gender', 'phone', 'password', 'password2','user_image']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        """Ensure both password fields match"""
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        """Create user with hashed password"""
        validated_data.pop("password2")  # Remove password2 before saving
        password = validated_data.pop("password")  # Extract password

        user = CustomUser(**validated_data)  # Create user instance
        user.set_password(password)  # Hash password
        user.save()
        return user
    
class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model = CustomUser
        fields=['email', 'password']
        
