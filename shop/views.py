from rest_framework import generics
from .serializer import RegisterSerializer,LoginSerializer,UserSerializer,ProductSerilizer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser,Products
from django.contrib.auth import login, authenticate

# Register API
class RegisterAPI(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

  

    
# Login API
class LoginView(APIView):
    
    def post(self, request, format=None):
        username = request.data.get('email')
        password = request.data.get('password')
        user = None
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
                return Response({"umessage":"user doesn exist"},status=status.HTTP_401_UNAUTHORIZED)
        if not user:
            user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
class ProductView(generics.ListCreateAPIView):
     serializer_class=ProductSerilizer
     queryset=Products.objects.all()

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
     serializer_class=ProductSerilizer
     queryset=Products.objects.all()
 