# region				----- External Imports -----
from django import forms
# endregion

# region				----- Internal Imports -----
from .models import Company, Shareholder
# endregion

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'registration_code',
                  'establishment_date', 'capital']
        widgets = {
            'establishment_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'placeholder': 'YYYY-MM-DD',
                    'class': 'date-input'
                }
            ),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3 or len(name) > 100:
            raise forms.ValidationError(
                "Nimi peab olema 3 kuni 100 tähemärki."
            )
        return name

    def clean_registration_code(self):
        registration_code = self.cleaned_data['registration_code']
        if not registration_code.isdigit() or len(registration_code) != 7:
            raise forms.ValidationError(
                "Registrikood peab olema 7 numbrit."
            )
        return registration_code

    def clean_establishment_date(self):
        establishment_date = self.cleaned_data.get(
            'establishment_date'
        )

        if isinstance(establishment_date, str):
            establishment_date = parse_date(establishment_date)

        if not establishment_date:
            raise ValidationError(
                "Sisesta õige formaadis nt 2024-12-12."
            )

        return establishment_date

    def clean_capital(self):
        capital = self.cleaned_data['capital']
        if capital < 2500:
            raise forms.ValidationError(
                "Kapital peab olema vähemalt 2500 eurot."
            )
        return capital


class ShareholderForm(forms.ModelForm):
    class Meta:
        model = Shareholder
        fields = ['shareholder_type', 'name',
                  'personal_code', 'registration_code',
                  'share_amount', 'is_founder']

    def clean_share_amount(self):
        amount = self.cleaned_data['share_amount']
        if amount < 1:
            raise forms.ValidationError(
                "Osa suurus peab olema vähemalt 1 euro."
            )
        return amount
