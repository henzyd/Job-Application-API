from django.shortcuts import redirect
from account.models import CustomUser
from .serializers import JobAdvertSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from jobapp.models import JobAdvert, JobApplication
from django.contrib import messages
# from rest_framework.reverse import reverse
from django.contrib.auth.decorators import login_required


User = get_user_model()



@login_required
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
            if serializer.is_valid():
                data = {}
                jobadvert = serializer.save()
                data['Success'] = 'Job advert has been CREATED'
                data['Title'] = jobadvert.title
                data['Posted By'] = jobadvert.owner.username
                messages.success(request, 'Job advert has been created')
                return Response(data=data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            # messages.info(request, 'You need to be logged in to access this')
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    return Response(status=status.HTTP_400_BAD_REQUEST)

# jobadvert.

@login_required
@api_view(['GET', 'PUT', 'DELETE'])
def jobadvert_detail_view(request, slug_company, slug_title):
    print('uche')
    current_user = request.user
    try:
        job_advert = JobAdvert.objects.all().filter(company_name=slug_company, title=slug_title).first()
    except JobAdvert.DoesNotExist:
        print('kihfjbrihfbj')
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = JobAdvertSerializer(job_advert)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        try:
            post_by = JobAdvert(owner=current_user)
        except:
            post_by = None
        
        job_advert = JobAdvert(owner=pos)
        
        if post_by is not None:
            serializer = JobAdvertSerializer(job_advert, data=request.data)
            if serializer.is_valid():
                data = {}
                jobadvert = serializer.save()
                data['Success'] = 'Job advert has been UPDATED'
                data['Title'] = jobadvert.title
                data['Posted By'] = jobadvert.owner.username
                messages.success(request, 'Job advert has been created')
                return Response(data=data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            # messages.info(request, 'You need to be logged in to access this')
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    elif request.method == 'DELETE':
        operation = job_advert.delete()
        data = {}
        if operation:
            data['Success'] = 'Post deleted sucessfully'
        else:
            data['Failure'] = 'Post deletion failed'
        return Response(data=data)

    return Response(status=status.HTTP_400_BAD_REQUEST)

    




## app.blog.__all__

@api_view(['POST'])
def jobapplication_create_view(request, slug):
    if request.method == 'POST':
        current_user = request.user

        job_advert = JobAdvert.objects.get(applicants=slug)






