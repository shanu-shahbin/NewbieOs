from django.shortcuts import render

# Create your views here.

def Companies(request):
    return render(request,'company/companies.html')