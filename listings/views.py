from django.shortcuts import render, redirect
from .forms import ListingCreation
from django.contrib.auth.decorators import permission_required
from listings.models import Listing
from customauth.models import BusinessUser
from django.views.generic import ListView, CreateView, DeleteView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

# Create your views here.


class CreateListing(PermissionRequiredMixin, CreateView):
    permission_required = ('customauth.can_create_listing')
    model = Listing
    template_name = 'business/offers/create.html'
    form_class = ListingCreation
    success_url = reverse_lazy('listings:infotable')

    def form_valid(self, form):
        new_list = form.save(commit=False)
        new_list.connection = self.request.user.businessuser
        new_list.save()
        return super().form_valid(form)

class DeleteListing(PermissionRequiredMixin, DeleteView):
    permission_required = ('customauth.can_create_listing')
    model = Listing
    success_url = reverse_lazy('listings:infotable')


def delete_list(request, pk):
    listing = get_object_or_404(Listing, pk=pk, connection=request.user.businessuser)
    listing.delete()
    listing_list = Listing.objects.filter(connection=request.user.businessuser)

    return render(request, 'htmx-partials/listing_table_partial.html', {"object_list": listing_list})

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