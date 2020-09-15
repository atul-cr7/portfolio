from django.shortcuts import render
from .forms import  Contact
from django.core.mail import send_mail


# view for home page
def show(request):
    if request.method=="POST":
        fm=Contact(request.POST)
        if(fm.is_valid()):
            NAME=fm.cleaned_data['Name']
            EMAIL=fm.cleaned_data['Email']
            MESSAGE=fm.cleaned_data['Message']
            send_mail(NAME,MESSAGE,EMAIL,['atulcr79872@gmail.com'],fail_silently=False,)
            fm=Contact()
        return render(request,'home/home.html',{'name':NAME,'form':fm})

    else:
        fm=Contact()
    return render(request,'home/home.html',{'form':fm,})
