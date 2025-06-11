from django.shortcuts import render, redirect
from .forms import ListingCreation
from django.contrib.auth.decorators import permission_required
from listings.models import Listing
from django.views.generic import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin


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


# @permission_required('customauth.can_create_listing', raise_exception=True) 
# def infotable(request):
#     business = BusinessUser.objects.get(user=request.user) # business related stuff
#     listings = Listing.objects.filter(connection=business) # shows all listings of logged business
#     return render(request, 'htmx-partials/data-table.html', {
#                                                     'business': business,
#                                                     "listings": listings,
#                                                     })


class InfoTableList(PermissionRequiredMixin, ListView):
    permission_required = ('customauth.can_create_listing')
    paginate_by = 1
    model = Listing
    template_name = 'htmx-partials/data-table.html'
