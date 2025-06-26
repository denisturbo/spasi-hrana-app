from django.shortcuts import render, redirect
from .forms import ListingCreation
from django.contrib.auth.decorators import permission_required
from listings.models import Listing
from customauth.models import BusinessUser
from django.views.generic import ListView, CreateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

# Create your views here.




# @permission_required('customauth.can_create_listing', raise_exception=True)
# def create(request):
#     if request.method == "POST":
#
#         form = ListingCreation(request.POST, request.FILES)
#         if form.is_valid():
#             new_list = form.save(commit=False)
#             new_list.connection = request.user.businessuser # connection e vruzkata mejdu Listinga i modela za user
#             new_list.save()
#             return redirect('/')
#     else:
#         form = ListingCreation()
#
#     return render(request, "business/offers/create.html", {"form": form})

class CreateListing(PermissionRequiredMixin, CreateView):
    permission_required = ('customauth.can_create_listing')
    model = Listing
    template_name = 'business/offers/create.html'
    form_class = ListingCreation
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        new_list = form.save(commit=False)
        new_list.connection = self.request.user.businessuser
        new_list.save()
        return super().form_valid(form)

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
    template_name = 'business/offers/data-table.html'

    def get_queryset(self):
        business = get_object_or_404(BusinessUser, user=self.request.user)
        return Listing.objects.filter(connection=business)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        business = get_object_or_404(BusinessUser, user=self.request.user)
        context['business'] = business
        return context