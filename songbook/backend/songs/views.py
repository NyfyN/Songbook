from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Tab
from .serializers import TabSerializer


def check_session(request):
    session_key = request.COOKIES.get('sessionid')
    if session_key:
        return Response({'sessionid': session_key})
    return Response({'error': 'No sessionid found'}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def is_authenticated(request):
    if request.user.is_authenticated:
        print("WORK")
        return Response({"authenticated": True})
    else:
        print("NOT WORK")
        return Response({"authenticated": False})

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def add_tab(request):
    check_session(request)
    # folder_name = request.data.get('folderName')
    # if not folder_name:
    #     return Response({"error": "Folder name is required"}, status=status.HTTP_400_BAD_REQUEST)

    # # Przykład zapisu do bazy danych (upewnij się, że masz model Tab)
    # tab = Tab(name=folder_name, user=request.user)
    # tab.save()

    # return Response({"message": "Folder added successfully"}, status=status.HTTP_201_CREATED)

