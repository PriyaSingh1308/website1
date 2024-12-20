from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
  #  return HttpResponse("home page")
    return render (request,'index.html')
   
   
def plateform(request):
      return render (request,'plateform.html')
  
def resources(request):
      return render (request,'resources.html')  
def prizing(request):
      return render (request,'prizing.html')
def solution(request):
      return render (request,'solution.html')
def company(request):
      return render (request,'company.html')      