from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
@api_view(['POST'])
def create_user(request):
    if request.method == "POST":
        username = request.data.get('username')
        e_mail = request.data.get('e_mail')

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exist!"}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(e_mail=e_mail).exists():
            return Response({"error": "Email already exist!"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
