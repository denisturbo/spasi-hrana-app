from django.shortcuts import render, redirect
from .forms import ListingCreation
from django.contrib.auth.decorators import permission_required

# Create your views here.




@permission_required('business.can_create_listing', raise_exception=True) 
def create(request):
    if request.method == "POST":
        form = ListingCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ListingCreation()

    return render(request, "business/create.html", {"form": form})