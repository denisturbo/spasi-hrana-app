from django.shortcuts import render, redirect
from django.template.response import TemplateResponse

from promocodes.forms import PromocodeCreation
from promocodes.models import Promocode
from customauth.models import BusinessUser
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

# Create your views here.


class CreatePromocode(CreateView):
    model = Promocode
    template_name = 'business/promocodes/create.html'
    form_class = PromocodeCreation
    success_url = reverse_lazy('promocodes:create')

    def form_valid(self, form):
        new_list = form.save(commit=False)
        new_list.connection = self.request.user.businessuser
        new_list.save()
        return super().form_valid(form)

class DeletePromocode(PermissionRequiredMixin, DeleteView):
    permission_required = ('customauth.can_create_listing')
    model = Promocode
    success_url = reverse_lazy('index')



class InfoTableList(PermissionRequiredMixin, ListView):
    permission_required = ('customauth.can_create_listing')
    paginate_by = 1
    model = Promocode
    template_name = 'business/promocodes/data-table.html'

    def get_queryset(self):
        business = get_object_or_404(BusinessUser, user=self.request.user)
        return Promocode.objects.filter(connection=business)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        business_user = get_object_or_404(BusinessUser, user=self.request.user)
        context['promocode'] = business_user
        return context

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()

        if request.headers.get('HX-Request'):
            print('vliza')
            return TemplateResponse(request, "htmx-partials/promocode_table_partial.html", context)
        else:
            return TemplateResponse(request, self.template_name, context)