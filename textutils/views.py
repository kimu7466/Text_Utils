from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render (request, "index.html")

def analyze(request):
    djtext = request.POST.get("text","default")
    removepunc = request.POST.get("removepunc","off")
    uppercase = request.POST.get("uppercase","off")
    newlineremove = request.POST.get("newlineremove","off")
    spaceremove = request.POST.get("spaceremove","off")
    charcount = request.POST.get("charcount","off")
    purpose = "None"
    result = djtext
    count = 0
        
    if removepunc =="on":
        purpose = "Remove Punctuations. "
        puncs = """`~!@#$%^&*_+\\|:;"',<.>/?=+-"""
        result = ""
        for ch in djtext:
            if not ch in puncs:
                result += ch
        djtext = result

    if uppercase =="on":
        purpose += "Upper Case. "
        result = ""
        for ch in djtext:
                result += ch.upper()
        djtext = result
        
    if newlineremove =="on":
        purpose += "New Line Remove. "
        result = ""
        for ch in djtext:
            if not (ch == "\n" or ch == "\r"):
                result += ch
        djtext = result
        
    if spaceremove =="on":
        purpose += "Extra Space Remove. "
        result = ""
        for index, ch in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " ") :
                result += ch
        djtext = result
        
    if charcount =="on":
        purpose += "character Counter. "
        res = ""
        for ch in djtext:
            if not (ch == "\n" or ch == "\r"): 
                res += ch
        djtext = result

        count = len(res)
        
    context = {
        "result":result,
        "purpose":purpose,
        "count":count
    }
    return render (request, "results.html", context)

    