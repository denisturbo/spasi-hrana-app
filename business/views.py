from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from business.models import Listing
from .forms import ListingCreation
# Create your views here.





def create(request):
    if request.method == "POST":
        form = ListingCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ListingCreation()

    return render(request, "business/create.html", {"form": form})