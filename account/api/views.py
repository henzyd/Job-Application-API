from .serializers import UserRegistrationSerializer, LoginSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.signals import user_logged_in



@api_view(['POST'])
def user_registration(request):
    '''
    This is the register url port
    '''
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            data = {}
            user = serializer.save()
            data['Success'] = 'User has been created'
            data['username'] = user.username
            data['email'] = user.email
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ## FIXME
# @api_view(['POST'])
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['paswword']
#         user = authenticate(username, password)
        
#         if user is None:
#             messages.error(request, 'Invalid input nitgtg')
#             return redirect('login')
#         # else:
#         #     messages(request, 'innmo')
#         #     return redirect('home')


@api_view(['POST'])
def user_login(request):
    if request.method == "POST":
        
        serializer = LoginSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        user = authenticate(request, username = serializer.validated_data['username'], password = serializer.validated_data['password'])
        if user:
            if user.is_active:
                try:
                    refresh = RefreshToken.for_user(user)
                    
                    user_details = {}
                    user_details['id']   = user.id
                    user_details['username'] = user.username
                    user_details['email'] = user.email
                    user_details['refresh_token'] = str(refresh)
                    user_details['access_token'] = str(refresh.access_token)
                    user_logged_in.send(sender=user.__class__,
                                        request=request, user=user)

                    data = {
                    'message' : "success",
                    'data' : user_details,
                    }
                    return Response(data, status=status.HTTP_200_OK)


                except Exception as e:
                    raise e
            
            else:
                data = {
                    'message'  : "failed",
                    'errors': 'This account is not active'
                    }
                return Response(data, status=status.HTTP_403_FORBIDDEN)


        else:
            data = {
                'message'  : "failed",
                'errors': 'Please provide a valid username and password'
                }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    


