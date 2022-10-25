from .serializers import UserRegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect




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


@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['paswword']
        user = authenticate(username, password)
        
        if user is None:
            messages.error(request, 'Invalid input nitgtg')
            return redirect('login')
        # else:
        #     messages(request, 'innmo')
        #     return redirect('home')

