from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2 style='color:limegreen'>Welcome to GiftBuddy...Here you can store your best gift ideas, assign them to recipients, track gifted/ungifted/regifted status, and check them off on your budget!<h2>")

