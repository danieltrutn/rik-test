# region				----- External Imports -----
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.core.paginator import Paginator
from django.forms import formset_factory
from django.db.models import Q
# endregion

# region				----- Internal Imports -----
from .models import Company, Shareholder
from .forms import CompanyForm, ShareholderForm
from .choices import SHAREHOLDER_TYPES
# endregion

class HomeView(ListView):
    model = Company
    template_name = 'company/home.html'
    context_object_name = 'companies'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        if query:
            return Company.objects.filter(
                Q(name__icontains=query) |
                Q(registration_code__icontains=query) |
                Q(shareholders__name__icontains=query)
            ).distinct()
        return Company.objects.none()

    def get_context_data(self, **kwargs):
        context = super()\
            .get_context_data(**kwargs)
        context['query'] = self.request.GET.get('query', '')
        return context

class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company/company_detail.html'
    context_object_name = 'company'

    def get_context_data(self, **kwargs):
        context = super()\
            .get_context_data(**kwargs)
        context['shareholders'] = \
            self.object.shareholders.all()
        
        return context

class CreateCompanyView(FormView):
    template_name = "company/create_company.html"
    form_class = CompanyForm
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super()\
            .get_context_data(**kwargs)
        ShareholderFormSet = formset_factory(
            ShareholderForm, extra=1
        )

        if self.request.POST:
            context["shareholder_formset"] = \
                ShareholderFormSet(self.request.POST)
        else:
            context["shareholder_formset"] = \
                ShareholderFormSet()

        return context

    def form_valid(self, form):
        ShareholderFormSet = formset_factory(
            ShareholderForm, extra=1
        )
        shareholder_formset = \
            ShareholderFormSet(self.request.POST)

        if shareholder_formset.is_valid():
            company = form.save()

            total_share_amount = sum(
                form.cleaned_data.get('share_amount', 0)
                for form in shareholder_formset if form.cleaned_data
            )

            if total_share_amount != company.capital:
                form.add_error(
                    'capital',
                    "Osanike osade summa peab olema võrdne kogukapitaliga."
                )
                return self.form_invalid(form)

            for form in shareholder_formset:
                if form.cleaned_data:
                    shareholder = form.save(commit=False)
                    shareholder.is_founder = True
                    shareholder.company = company
                    shareholder.save()

            return redirect("company_detail", pk=company.pk)
        else:
            return self.render_to_response(
                self.get_context_data(
                    form=form,
                    shareholder_formset=shareholder_formset
                )
            )

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form)
        )