from django.shortcuts import render,HttpResponse

# Create your views here.



def first (request):
    return HttpResponse("This is MY FIRST FUNC")


def second(request):
    return render(request,'first.html')
    