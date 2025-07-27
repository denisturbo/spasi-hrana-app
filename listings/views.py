from django.core.paginator import Paginator
from django.shortcuts import render
from spasihrana.requests import HttpRequest
from .forms import ListingCreation, ListingEdit
from listings.models import Listing
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
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
    def delete(self, request: HttpRequest, *args, **kwargs):
        self.object = self.get_object()

        if request.htmx:
            # Implementirame Paginatora ot MultipleObjectMixin zashtoto v DeleteView go nqma..
            current_page = request.GET.get('page', 1)
            self.object.delete()

            queryset = Listing.objects.filter(connection=self.request.user.businessuser)
            paginate_by = 10
            paginator = Paginator(queryset, paginate_by)
            page_obj = paginator.get_page(current_page)

            context = {
                'object_list': page_obj.object_list,
                'page_obj': page_obj,
                'is_paginated': page_obj.has_other_pages(),
                'paginator': paginator,
                }
            return render(request, 'htmx-partials/listing_table_partial.html', context)
        return super().delete(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args, **kwargs):
        #Post-a e prezapisan samo zaradi if-a da proverim dali zaqvkata se pravi ot HTMX (delete method)
        self.object = self.get_object()
        form = self.get_form()

        if request.htmx:
            return self.delete(request, *args, **kwargs)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

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
            return render(request, "htmx-partials/listing_table_partial.html", context)
        else:
            return render(request, self.template_name, context)