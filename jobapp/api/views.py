from account.models import CustomUser
from .serializers import JobAdvertSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from jobapp.models import JobAdvert


User = get_user_model()



@api_view(['POST'])
def jobadvert_create_view(request):
    if request.method == 'POST':
        current_user = request.user
        
        # request.user
        # user = User.objects.get(user=request.user)
        # post_by = JobAdvert(owner=current_user)

        request.data.owner = request.user
        serializer = JobAdvertSerializer(data=request.data)
        if serializer.is_valid():
            # data = {}
            jobadvert = serializer.save()
            # data['Title'] = 'Job Advert HHas '
            # data['Title'] = jobadvert.title
            return Response(data=serializer.data)
        print(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
