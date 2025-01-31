from django.contrib.auth.hashers import check_password, make_password
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from django.utils import timezone
# Create your views here.


@api_view(['GET'])
def check_session(request):
    session_key = request.COOKIES.get('sessionid')
    if session_key:
        return Response({'sessionid': session_key})
    return Response({'error': 'No sessionid found'}, status=400)

@api_view(['POST'])
def test_api(request):
    print(request)
    return Response({"message": "Test API works!"}, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
def sign_up(request):
    username = request.data.get('username')
    e_mail = request.data.get('e_mail')
    password = request.data.get('password')
    confirm_password = request.data.get('confirm_password')
    print("Received data: ", request.data)

    # Debugging
    if not confirm_password:
        return Response({"error": "Confirm password is required"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists!"}, status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(e_mail=e_mail).exists():
        return Response({"error": "Email already exists!"}, status=status.HTTP_400_BAD_REQUEST)
    if password != confirm_password:
        return Response({"error": "Password and confirm password do not match!"}, status=status.HTTP_400_BAD_REQUEST)

    # * Update request data
    user_data = request.data.copy()

    print("User data before serialization:", user_data)

    serializer = UserSerializer(data=user_data)
    if serializer.is_valid():
        print("Validated data:", serializer.validated_data)
        serializer.save()
        return Response({
            "message": "User created successfully",
            "redirect_url": "/login"
        }, status=status.HTTP_201_CREATED)
    print("Serializer errors:", serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def sign_in(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"error": "Both username and password are required"},
                        status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(username=username)
        
        if check_password(password, user.password):
            login(request, user)
            user.last_login = timezone.now()
            user.save()
            serializer = UserSerializer(user)
            session_key = request.COOKIES.get('sessionid')
            print("session_key: ", session_key)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)

    except User.DoesNotExist:
        return Response({"error": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)


