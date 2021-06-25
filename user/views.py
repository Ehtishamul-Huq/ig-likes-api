from rest_framework import status, generics
from rest_framework.generics import CreateAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from user.serializers import UserRegistrationSerializer, UserLoginSerializer,UserSerializer
from .models import User

class UserRegistrationView(CreateAPIView):

    serializer_class = UserRegistrationSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)

            
class UserLoginView(RetrieveAPIView):

    serializer_class = UserLoginSerializer    

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        obj = User.objects.get(email=request.data['email'])
        user_serializer = UserSerializer(obj.profile)
        return Response({
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            "data": user_serializer.data,
             'token' : serializer.data['token'],
            }, 
            status=status.HTTP_200_OK)