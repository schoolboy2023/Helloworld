from django.http  import HttpResponse

# Create your views here.

def homepageView(request):

    return HttpResponse("Hello, World")

