from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages



def index(request):
    # messages.error(request,'welcome')
    # return HttpResponse('Hello World')
    return render(request,'tts/index.html')


def convert(request):
    text=request.POST.get('text','none')
    email=request.POST.get('email','none')
    b=request.POST.get('b','none')


    par={
        'text1':text,
        'email1':email,
        'name':f"{email}.wav"

    }
    
    
    try:

        from gtts import gTTS

        
        language="en"
        myobj=gTTS(text=text,lang=language,slow=False)
        
        myobj.save(f"text_to_sppech/static/{email}.wav")
        
    except:
        return render(request,'tts/problem.html',par)
    messages.success(request,"File Converted SucessFully")    
    return render(request,'tts/success.html',par)
def success(request):
    
    pass
def problem(request):
    
    pass
    
    

# Create your views here.
