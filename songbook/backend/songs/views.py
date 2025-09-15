from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Tab
from .serializers import TabSerializer
from django.views.decorators.csrf import csrf_exempt


def check_session(request):
    session_key = request.COOKIES.get('sessionid')
    if session_key:
        return Response({'sessionid': session_key})
    return Response({'error': 'No sessionid found'}, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def is_authenticated(request):
    print(Response({"authenticated": request.user.is_authenticated}))
    return Response({"authenticated": request.user.is_authenticated})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_tab(request):
    
    folder_name = request.data.get('folderName')
    if not folder_name:
        return Response({"error": "Folder name is required"}, status=400)

    try:
        tab = Tab(name=folder_name, user=request.user, color="#FFFFFF")
        tab.save()
        return Response({"message": "Folder added successfully"}, status=201)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_tabs(request):
    tabs = Tab.objects.filter(user=request.user).order_by('-created_at')

    tabs_data = [
        {
            "id": tab.id,
            "name": tab.name,
            "color": tab.color,
            "created_at": tab.created_at
        }
        for tab in tabs
    ]

    return Response(tabs_data)
