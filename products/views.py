from django.shortcuts import render

# home page views will be referenced here

def home(request): # home function with request so forwared http requests can be served
	return render(request, 'products/home.html') #render the requested html page located in products/templates/products
