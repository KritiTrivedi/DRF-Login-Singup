# views.py
# from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import  User

from user.serializer import  UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

# Create your views here.

@api_view(['POST']) 
def register(request):
    try:

            existing_user = User.objects.filter(email=request.data.get('email'))
            if existing_user:
                return Response("User Already Exists")
            password = request.data['password']
            hashed_password = make_password(password)
            request.data['password'] = hashed_password
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
               serializer.save()
               return Response({
                    'status':True,
                    'message':'Resigration Successfully',
                    'data':serializer.data
                })
            return Response({
                         'status': False,
                         'message':'Invalid Data',
                         'data':serializer.errors
                   })
    except Exception as e:
            return Response({
                  'status':False,
                  'message':'Something went wrong'
             })

@api_view(['POST'])
@permission_classes([AllowAny])
def Login(request):
    try:
        user = User.objects.filter(email=request.data['email']).first()
        if check_password(request.data['password'], user.password):
             refresh = RefreshToken.for_user(user)
             return Response({
                    'status': True,
                    'message': 'Login Successful',
                    'data': {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }
                })
        return Response({
             'status':False,
             'Message':'Invalid Credentials'
        })
    except Exception as e:
        print("Error:", e)
        return Response({
            'status': False,
            'message': 'Something went wrong'
        })
