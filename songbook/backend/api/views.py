# from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from log_reg.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def api_home(request, *args, **kwargs):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
    return JsonResponse(received_json_data)
