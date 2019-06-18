from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

# home page views will be referenced here

def home(request): # home function with request so forwared http requests can be served
    products = Product.objects
    return render(request, 'products/home.html',{'products':products}) #render the requested html page located in products/templates/products

@login_required(login_url="/accounts/signup") #decorator to impose login and send user to signup page if they are not logged in
def create(request):
    if request.method == 'POST': #must POST GET is unsafe
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']: #all fields required
            product = Product() #store values as object
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'): #check that urls starts with http or https
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url'] # if the url is missing http then append to url
            product.icon = request.FILES['icon'] #store icon
            product.image = request.FILES['image'] #store image
            product.pub_date = timezone.datetime.now() #save date and time as current date and time
            product.hunter = request.user #store user
            product.save() #save the product 
            return redirect('/products/' + str(product.id)) #forward user to products urls based on int product id
        else:
            return render(request, 'products/create.html',{'error':'All fields are required.'}) #if all required field are not present reload page and display error 
    else:
        return render(request, 'products/create.html') #if all else fails send user back to create.html


def detail(request, product_id): #int product id
	product = get_object_or_404(Product, pk=product_id) # get the Product object based on int product_id or deliver 404
	return render(request, 'products/detail.html',{'product':product}) #forward user to details.html


@login_required(login_url="/accounts/signup") #decorator to impose login and send user to signup page if they are not logged in
def upvote(request, product_id): #int product id
    if request.method == 'POST': #must POST GET is unsafe
        product = get_object_or_404(Product, pk=product_id) # get the Product object based on int product_id or deliver 404
        product.vote_totals += 1 #increment vote_totals
        product.save() #update product
        return redirect('/products/' + str(product.id)) #forward user to products urls based on int product id
