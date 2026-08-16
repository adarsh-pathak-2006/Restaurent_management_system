from rest_framework.views import APIView
from django.conf import settings
from .serializers import RegisterSerializer
from django.db.models import Q
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User=get_user_model()

class RegisterAPI(APIView):
    def post(self, request):
        serial=RegisterSerializer(data=request.data)
        if serial.is_valid():
            username=serial.validated_data['username']
            email=serial.validated_data['email']
            role=serial.validated_data['role']
            password=serial.validated_data['password']

            if User.objects.filter(Q(username=username) | Q(email=email)).exists():
                return Response({'message':'username or email already exists'}, status=400)
            User.objects.create_user(username=username, email=email, role=role, password=password)
            return Response({'message':'user registration successfull'}, status=201)
        return Response(serial.errors, status=400)
