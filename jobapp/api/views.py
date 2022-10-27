from django.shortcuts import redirect
from account.models import CustomUser
from .serializers import JobAdvertSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from jobapp.models import JobAdvert
from django.contrib import messages
# from rest_framework.reverse import reverse


User = get_user_model()



@api_view(['POST'])
def jobadvert_create_view(request):
    if request.method == 'POST':
        current_user = request.user
        try:
            post_by = JobAdvert(owner=current_user)
        except:
            post_by = None
        
        if post_by is not None:
            serializer = JobAdvertSerializer(post_by, data=request.data)
        else:
            # messages.info(request, 'You need to be logged in to access this')
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        if serializer.is_valid():
            data = {}
            jobadvert = serializer.save()
            data['Success'] = 'Job advert has been created'
            data['Title'] = jobadvert.title
            data['Posted By'] = jobadvert.owner.username
            messages.success(request, 'Job advert has been created')
            return Response(data=data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def jobapplication_create_view(request):
    if request.method == 'POST':
        current_user = request.user


