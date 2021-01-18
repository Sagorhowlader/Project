from django.http import HttpResponse


def eventview(request):
    return HttpResponse("hello")

