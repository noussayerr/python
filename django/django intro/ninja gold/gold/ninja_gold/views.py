from django.shortcuts import render,redirect
import random
from time import gmtime, strftime

def index(request):
    return render(request,"index.html")

def money(request):
    #if request.POST['which_form'] == '1':
     #   return HttpResponse('hey')
    
    if 'gold' and 'msg' in request.session:
        msg=""
        match request.POST['which_form']:
            case '1':
                x=random.randint(5,10)
                request.session['gold'] +=x
                msg=(f"earned {x} golds from farm ! {strftime("%b %d , %Y %H:%M %p", gmtime())}")
            case '2':
                x=random.randint(5,10)
                request.session['gold'] +=x
                msg=(f"earned {x} golds from cave ! {strftime("%b %d , %Y %H:%M %p", gmtime())}")
                
            case '3':
                x=random.randint(2,5)
                request.session['gold'] +=x
                msg=(f"earned {x} golds from house ! ({strftime("%b %d , %Y %H:%M %p", gmtime())})")
                
            case '4':
                x=random.randint(1,2)
                if x==1:
                    win=random.randint(0,50)
                    request.session['gold'] +=win
                    msg=(f"earned {win} golds from casino ! {strftime("%b %d , %Y %H:%M %p", gmtime())}")
                else:
                    lost=random.randint(0,50)
                    request.session['gold'] -=lost
                    msg=(f"lost {lost} golds from casino ! {strftime("%b %d , %Y %H:%M %p", gmtime())}")
        request.session['msg'].append(msg)
        request.session.save()
    else:
         request.session['gold']=0
         request.session['msg'] = []
    return redirect('/')