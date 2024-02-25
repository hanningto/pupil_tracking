from django.shortcuts import render
from arc_app.models import RfidTags
from .forms import TagForm

# Create your views

# view to show the form
def index(request):

    if request.method =="POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
    form = TagForm
    return render(request, 'index.html', {'form':form}) 


# view to show a list of registered pupils     
def info(request):
    tag_list = RfidTags.objects.all()
    tag_dict = {'rfid_tags': tag_list}
    return render(request, 'info.html', context=tag_dict) 

