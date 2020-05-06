from django.shortcuts import render
from django.http import HttpResponse
from app.models import Topic,Webpage,AccessRecord
from . import forms
from app.forms import NewUserForm
# Create your views here.

"""
def index(request):
    my_dict={'insert_me':"Hello I am from Views.py"}
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request,'index.html',context=date_dict)
"""
def form_name_view(request):
    form = forms.FormName()

    if request.method =='POST':
        form= forms.FormName(request.POST)

        if form.is_valid():
            # do something code
            print("validation Success")
            print("Name:"+ form.cleaned_data['name'])
            print("Email:"+ form.cleaned_data['email'])
            print("text:"+ form.cleaned_data['text'])

    return render(request,'form.html',{'form':form})


def index(request):
    return render(request,'index.html')

# for the user submit form
def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'index.html',{'form':form})
