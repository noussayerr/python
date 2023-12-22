from django.shortcuts import render,redirect

def index(request):
    if 'count' in request.session:
        request.session['count']+=1
    else:
        request.session['count']=0
    return render(request,"index.html")
def dele(request):
    del request.session['count']	
    return redirect ('/')