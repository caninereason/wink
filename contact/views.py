from django.http import HttpResponse


def contact_view(request):
    return HttpResponse("Contact app works!")
