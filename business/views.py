from django.shortcuts import render, redirect
from .forms import ListingCreation
from django.contrib.auth.decorators import permission_required

# Create your views here.




@permission_required('customauth.can_create_listing', raise_exception=True) 
def create(request):
    if request.method == "POST":
        
        form = ListingCreation(request.POST, request.FILES)
        if form.is_valid(): 
            new_list = form.save(commit=False)
            new_list.connection = request.user.businessuser # connection e vruzkata mejdu Listinga i modela za user
            new_list.save()
            return redirect('/')
    else:
        form = ListingCreation()

    return render(request, "business/create.html", {"form": form})