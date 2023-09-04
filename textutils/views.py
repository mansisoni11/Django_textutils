from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyze(request):
    # get text
    
    djtext=request.POST.get('text','default')
   
    # checkbox b=value
    
    removepunc =request.POST.get('removepunc','off')
    fullCAPS =request.POST.get('fullCAPS','off')
    newlineremover =request.POST.get('newlineremover','off')
    extrspaceremover=request.POST.get('extrspaceremover','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed

    
    if(fullCAPS=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
            params={'purpose':'changed to uppercase','analyzed_text':analyzed}
            djtext = analyzed
        # return render(request,'analyze.html',params)
    
    if(extrspaceremover=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
         if  not djtext[index] ==" " and djtext[index+1]==" ":
            analyzed=analyzed+char
                  
         params={'purpose':'removed newline','analyzed_text':analyzed}
         djtext=analyzed
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

  
    if(removepunc!="on" and newlineremover !="on" and extrspaceremover!="on" and fullCAPS!="on") :
        return HttpResponse("please select any operation and try again")
