from django.http import HttpResponse

from django.shortcuts import render # Import render function to render HTML templates

# Simple view function
def about(request):
    return HttpResponse("<h1>Welcome to Wscubetech!<h1>")

# Setup view function with parameters with String type
def userDetailsByName( request, name):
    return HttpResponse(f"<h1>Welcome {name}!<h1>")

# Setup view function with parameters with Integer type
def userDetailsById( request, id):
    return HttpResponse(f"<h1>Welcome User with ID: {id}!<h1>")

# Setup view function with parameters with Slug type
def userDetailsBySlug( request, slug):
    return HttpResponse(f"<h1>Welcome User with Slug: {slug}!<h1>")

#Setupt user with without a type
def userDetailsByData(request, data):
    return HttpResponse(f"<h1>Welcome User {data}!<h1>")


#rendor the index.html file from the templates directory
def home(request):
    return render(request, 'index.html')


# thsi function will render the index_dynamic.html file from the templates directory with dynamic data
def homeDynamic(request):
    
    data={
        "title": "Dynamic Title",
        "body": "Dynamic Body",
    }
    return render(request, 'index_dynamic.html', data)



