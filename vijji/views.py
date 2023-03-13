from django.shortcuts import render

# Create your views here.
def jinja_print1(request):
    return render(request,"jinja_print1.html",context={"name":"jagadeesh",'age':21})