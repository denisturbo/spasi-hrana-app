from django.template.response import TemplateResponse
from promocodes.forms import PromocodeCreation, EditPromocode
from promocodes.models import Promocode
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from spasihrana.requests import HttpRequest


# Create your views here.

class CreatePromocode(CreateView):
    model = Promocode
    template_name = 'business/promocodes/create.html'
    form_class = PromocodeCreation
    success_url = reverse_lazy('promocodes:infotable')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        promocode = form.save(commit=False)
        promocode.connection = self.request.user.businessuser
        promocode.save()
        form.save_m2m()
        return super().form_valid(form)




class PromocodeEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('customauth.can_create_listing')
    model = Promocode
    form_class = EditPromocode
    template_name = 'business/promocodes/edit.html'
    success_url = reverse_lazy('promocodes:infotable')


    def get_queryset(self):
        return Promocode.objects.filter(connection=self.request.user.businessuser)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        promocode = form.save(commit=False)
        promocode.connection = self.request.user.businessuser
        promocode.save()
        form.save_m2m()
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
        return Promocode.objects.filter(connection=self.request.user.businessuser)

    def get(self,request:HttpRequest,  *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()

        if request.htmx:
            print('vliza')
            return TemplateResponse(request, "htmx-partials/promocode_table_partial.html", context)
        else:
            return TemplateResponse(request, self.template_name, context)