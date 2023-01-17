from django.http import HttpResponse

# FBVs
def index(data):
    return HttpResponse("Hey index view for app1 from project my_site")   