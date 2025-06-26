from django.shortcuts import render, redirect
from promocodes.forms import PromocodeCreation
from promocodes.models import Promocode
from customauth.models import BusinessUser
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

# Create your views here.

# def create(request):
#     if request.method == "POST":
#         form = PromocodeCreation(request.POST)
#         if form.is_valid():
#             new_promo = form.save(commit=False)
#             new_promo.connection = request.user.businessuser
#             new_promo.save()
#             return redirect('/')
#     else:
#         form = PromocodeCreation()
#
#
#     return render(request, "business/promocodes/create.html", {"form": form})


class CreatePromocode(CreateView):
    model = Promocode
    template_name = 'business/promocodes/create.html'
    form_class = PromocodeCreation
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        new_list = form.save(commit=False)
        new_list.connection = self.request.user.businessuser
        new_list.save()
        return super().form_valid(form)



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