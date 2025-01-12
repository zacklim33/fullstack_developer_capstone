# Uncomment the required imports before adding the code

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from .models import CarMake, CarModel
from .populate import initiate


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Try to check if provide credential can be authenticated
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)


# Create a `logout_user` view to handle sign out request
def logout_user(request):
    data= {'userName':''}
    return JsonResponse(data)


# Create a `registration` view to handle sign up request
@csrf_exempt
def registration_user(request):
    #Load up user input data from request object
    data = json.loads(request.body)
    userName = data['userName']
    password = data['password']
    firstName = data['firstName']
    lastName = data['lastName']
    email = data['email']

    #booleans for userName or email exist
    bUsername = False
    bEmail = False

    #check if userName exist
    try:
        User.ojects.get(username=userName)
        bUsername=True
    except:
        logger.debug("{} is not a valid user".format(userName))

    #check if email exist
    try:
        User.objects.get(email=email)
        bEmail=True
    except:
        logger.debug("{} is already in database".format(email))

    if(not bUsername) and (not bEmail):
        user = User.objects.create_user(
            username=userName,
            first_name=firstName,
            last_name=lastName,
            password=password,
            email=email)

        #login user, and redirect to listing page
        login(request,user)

        data = {'userName':userName, 'status':'Authenticated'}        
        return JsonResponse(data)

    # if username already exists, redirect
    if(bUsername):
        data = {'userName': userName, 'error':"Already Registered"}
        return JsonResponse(data)

    #If email is used, redirect
    if(bEmail):
        data = {'email': email, 'error': "Email Taken"}
        return JsonResponse(data)


#Get cars 
def get_cars(request):
    #count = CarMake.objects.filter().count()
    #print(count)
    #if(count == 0):
    initiate()
    car_models = CarModel.objects.select_related('car_make')
    cars = []
    for car_model in car_models:
        print(car_model.name)
        cars.append({"CarModel": car_model.name, "CarMake": car_model.car_make.name})
    return JsonResponse({"CarModels":cars})


# # Update the `get_dealerships` view to render the index page with
# a list of dealerships
# def get_dealerships(request):
# ...

# Create a `get_dealer_reviews` view to render the reviews of a dealer
# def get_dealer_reviews(request,dealer_id):
# ...

# Create a `get_dealer_details` view to render the dealer details
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request):
# ...
