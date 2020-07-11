#i have created this file made by rishabh\
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext=request.POST.get("text","default")
    remove=request.POST.get("remove","off")
    fullcaps=request.POST.get("fullcaps","off")
    newlineremover=request.POST.get("newlineremover","off")
    count=request.POST.get("count","off")
    

    print(remove)
    print(djtext)
    if remove=="on":

        punchuations='''!()-{};:.,<>@#$%^&*+*~'"'''
        analyzed=""
        for char in djtext:
            if char not in punchuations:
                analyzed=analyzed+char
        
        params={"purpose":"removed punctuations","analyzed_text":analyzed}
        djtext=analyzed
        # return render(request,"analyze.html",params)
    if(fullcaps=="on"):
        analyzed=""
        for c in djtext:
            analyzed=analyzed+ c.upper()
        
        params={"purpose":"upper caps","analyzed_text":analyzed}
        djtext=analyzed
        # return render(request,"analyze.html",params)
    if(newlineremover=="on"):
        analyzed=""
        for c in djtext:
            if c !="\n" and c!="\r":
                analyzed=analyzed+ c.upper()
        djtext=analyzed   
        params={"purpose":"Removed new lines","analyzed_text":analyzed}
     
       # return render(request,"analyze.html",params)
    djtext=analyzed
    if(count=="on"):
        analyzed=""
        i=0
        for c in djtext:
            i=i+1
             
        analyzed=f"no of characters in your string is {i}"
        params={"purpose":"character count","analyzed_text":analyzed}
    return render(request,"analyze.html",params)
    if (remove !="on" and newlineremover !="on" and count !="on" and fullcaps !="on"):
        return HttpResponse("please select any operation") 
    
def about(request):
    return render(request,'about.html')
