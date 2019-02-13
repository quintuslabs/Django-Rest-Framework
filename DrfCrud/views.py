from django.http import HttpResponse

def index(request):
    return HttpResponse('<!DOCTYPE html> <html> <body> <h1> <center>Rest Framework CRUD Operation</center> </h1> </body> </html>')
