from django.shortcuts import render

def index(request):
    index_select={
    "languages":['Python','C++','Java'],
    "locations":['beja','jendouba','kef']
    }
    return render(request,'index.html',index_select)
def submit(request):
    
    data={
        "name" : request.POST['user_name'],
        "Location" : request.POST['Location'],
        "Language" : request.POST['Language'],
        "comment" : request.POST['comment']
    }
    return render(request,'submit.html',data)
