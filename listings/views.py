from django.shortcuts import render
from django.template.response import TemplateResponse

from spasihrana.requests import HttpRequest
from .forms import ListingCreation, ListingEdit
from listings.models import Listing
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
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


class EditListing(PermissionRequiredMixin, UpdateView):
    permission_required = ('customauth.can_create_listing')
    model = Listing
    form_class = ListingEdit
    template_name = 'business/offers/edit.html'
    success_url = reverse_lazy('listings:infotable')

    def get_queryset(self):
        return Listing.objects.filter(connection=self.request.user.businessuser)

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
    paginate_by = 10
    model = Listing
    template_name = 'business/offers/data-table.html'

    def get_queryset(self):
        return Listing.objects.filter(connection=self.request.user.businessuser)

    def get(self, request: HttpRequest, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()

        if request.htmx:
            print('vliza')
            return TemplateResponse(request, "htmx-partials/listing_table_partial.html", context)
        else:
            return TemplateResponse(request, self.template_name, context)