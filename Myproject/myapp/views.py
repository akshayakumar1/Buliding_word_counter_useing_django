from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #dynamic contex
    # context={
    #     'name':'rahul',
    #     'age':22,
    #     'nationality':'hindu',


    # }
    
    # return render(request,'index.html',context)
    return render(request,'form.html')

def counter(request):

    words= request.POST["words"]
    amounts_of_words=len(words.split())
    
    return render(request,'counter.html',{'amounts':amounts_of_words})
