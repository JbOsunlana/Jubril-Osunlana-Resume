from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def Contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home?submitted= True')
        else:
            form = ContactForm
            if 'submitted' in request.GET:
                submitted = True
    
    
    return render(request, 'home.html', {'form':form, 'submitted':submitted})