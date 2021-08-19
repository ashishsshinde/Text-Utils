
from django.http import HttpResponse
from django.shortcuts import render

def index(request):   
    return  render(request,'index.html')
 

def analyze(request):
    djtext=request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc', 'off')
    uppercase=request.POST.get('uppercase', 'off')
    lowercase=request.POST.get('lowercase', 'off')
    print(removepunc)
    print(djtext)
    
    if removepunc == "on":
        #analyzed = djtext
        punctuation = '''[]!@#$%^&*(){}?<>:";'.,/'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char

        params={'purpose':'remove punctuation', 'Analyzed_text': analyzed}        
        return render(request, 'analyze.html', params)



    elif( uppercase == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params={'purpose':'UPPERCASE', 'Analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    
    elif( lowercase == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()

        params={'purpose':'lowercase', 'Analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    else:
        return HttpResponse("Error")




