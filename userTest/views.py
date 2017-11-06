from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def strTest(request,year,num):
    return HttpResponse("%s.%s"%(year,num))
# def getName(request):
#     # id = request.GET.get('id')
#     # name = request.GET.get('name')
#     # age = request.GET.get('age')
#
#     age = request.GET.getlist('name')
#     id = request.GET['id']
#
#
#     return HttpResponse((id,age))
def getNameTest(request , date):
    id = request.GET['id']
    name = request.GET['name']
    age = request.GET['age']
    return render(request,'index.html',{'date':date,'id':id,'name':name,'age':age})