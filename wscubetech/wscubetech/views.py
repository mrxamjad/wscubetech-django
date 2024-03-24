from django.http import HttpResponse

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



