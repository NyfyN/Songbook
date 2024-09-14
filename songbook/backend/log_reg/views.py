from django.contrib.auth.hashers import check_password, make_password
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
@api_view(['POST'])
def sign_up(request):
  # Zobacz, co jest przesyłane

    username = request.data.get('username')
    e_mail = request.data.get('e_mail')
    password = request.data.get('password')
    confirm_password = request.data.get('confirm_password')
    print("Received data: ", request.data)

    # Debugowanie
    if not confirm_password:
        return Response({"error": "Confirm password is required"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists!"}, status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(e_mail=e_mail).exists():
        return Response({"error": "Email already exists!"}, status=status.HTTP_400_BAD_REQUEST)
    if password != confirm_password:
        return Response({"error": "Password and confirm password do not match!"}, status=status.HTTP_400_BAD_REQUEST)

    # Hashowanie hasła
    # hashed_passwd = make_password(password)

    # Zaktualizuj dane żądania
    user_data = request.data.copy()
    # user_data['password'] = hashed_passwd

    print("User data before serialization:", user_data)

    serializer = UserSerializer(data=user_data)
    if serializer.is_valid():
        print("Validated data:", serializer.validated_data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print("Serializer errors:", serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def sign_in(request):
    if request.method == "POST":
        username = request.data.get('username')
        password = request.data.get('password')
        print("USERNAME: ", username)

        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid password1"}, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response({"error": "User does not exist!"}, status=status.HTTP_400_BAD_REQUEST)
