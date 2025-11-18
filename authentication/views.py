from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
import json

@csrf_exempt
def login_user(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(
        username = username,
        password = password
    )

    # check if user exist
    if user is not None:
        if user.is_active:
            login(request, user)

            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login successful!"
            }, status = 201)

        else:
            return JsonResponse({
                "status": False,
                "message": "Login failed, account is disabled."
            }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Login failed, please check your username or password"
        }, status=401) 




@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password_1 = data['password_1']
        password_2 = data['password_2']

        if password_1 != password_2:
            return JsonResponse({
                "status": False,
                "message": "Passwords do not match. Please check them again!"
            }, status=401)
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({
                "status": False,
                "message": "Username already exists."
            }, status=401)
        
        # create new user
        user = User.objects.create_user(username=username, password=password_1)
        user.save()
        
        return JsonResponse({
            "status": 'success',
            "username": user.username,
            "message": "User created successfully!"
        }, status=201)
    
    else:
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=401)
