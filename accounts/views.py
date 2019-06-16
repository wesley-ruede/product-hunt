from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
#functions as referenced from urls.py -- accounts

def signup(request): #reference to urls.py
	if request.method == "POST": #user is attempting to store info on server
		#user wants an account
		if request.POST['password1'] == request.POST['password2']: #double password authentication
			try: #try to create a user
				user = User.objects.get(username=request.POST['username']) #check username 
				return render(request, 'accounts/signup.html', {'error': 'Username not available, try a new name'}) #if username is no good return an error
			except User.DoesNotExist: #if the user does not exist
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1']) #user object to store credentials and username
				auth.login(request, user) #user created and authenticated
				return redirect('home') #send user home
		else:
			return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})
	else:
		#user wants to enter info
		return render(request, 'accounts/signup.html') #reference to html in template

def login(request): #reference to urls.py
	return render(request, 'accounts/login.html') #reference to html in template

def logout(request): #reference to urls.py
	# TODO Need to route to homepage
	# and don't forget to log out
	return render(request, 'accounts/signup.html') #reference to html in template