from rest_framework import viewsets, permissions,generics
from registration.models import User
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer





class OTPView(APIView):
    permission_classes = (IsAuthenticated,)            

    def get(self, request):
        user= request.user
        otp = request.GET['otp']
        if user.otp == int(otp):
            user.is_verified = True
            message = "User verified Successfully"
        else:
            message = "OTP verification failed"
        content = {'message':message}
        return Response(content)



    
