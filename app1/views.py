from django.shortcuts import render,HttpResponse

# Create your views here.

# from .models import Student
# def welcome(request):
    # print(request.method)                     #GET METHOD
    # print(request.user)                     # ananymous user
    # print(request.__dict__)
    # print(request.GET)                       # for runserver                        # query parameter
    # studs = list(Student.objects.values("name"))
    # final_studs = list(map(lambda x : x["name"], studs ))
    # return HttpResponse(f"welcome to Django Application...., {final_studs}")

# ----------------------------------------------------------------------------------------------------
# HTTP:

# def welcome(request):
#     return render(request, "sample2.html")



def welcome(request):
    return render(request, "home.html")

