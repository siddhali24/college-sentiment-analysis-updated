from django.http import HttpResponse

def review_view(request):
    return HttpResponse("Django is working")