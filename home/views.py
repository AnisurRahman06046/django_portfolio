from django.shortcuts import render
from .models import HomeModel
# Create your views here.
def home(request):
    data = HomeModel.objects.all()
    return render(request,'home.html',{'datas':data})