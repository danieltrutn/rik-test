# region ----- External Imports -----
from django.db.models.signals import post_migrate
from django.utils.timezone import make_aware
from django.dispatch import receiver
from datetime import datetime
# endregion

# region ----- Internal Imports -----
from company import models as company_models
from company.choices import SHAREHOLDER_TYPES 
# endregion

@receiver(post_migrate)
def create_dummy_data(sender, **kwargs):
    if sender.name == 'company':
        if not company_models.Company.objects.exists():
            try:
                company1 = company_models.Company.objects.create(
                    name="Swedbank",
                    registration_code="1234567",
                    capital=25000,
                    establishment_date=make_aware(datetime(2023, 2, 1))
                )
                company2 = company_models.Company.objects.create(
                    name="SEB",
                    registration_code="2345678",
                    capital=30000,
                    establishment_date=make_aware(datetime(2023, 1, 1))
                )

                INDIVIDUAL = SHAREHOLDER_TYPES [0][0]
                LEGAL_ENTITY = SHAREHOLDER_TYPES [1][0]

                company_models.Shareholder.objects.create(
                    shareholder_type=INDIVIDUAL,
                    name="John Doe",
                    personal_code="50001019999",
                    share_amount=15000,
                    is_founder=True,
                    company=company1
                )
                company_models.Shareholder.objects.create(
                    shareholder_type=LEGAL_ENTITY,
                    name="InvestCorp",
                    registration_code="7654321",
                    share_amount=10000,
                    is_founder=True,
                    company=company1
                )
                company_models.Shareholder.objects.create(
                    shareholder_type=INDIVIDUAL,
                    name="Jane Smith",
                    personal_code="60002029988",
                    share_amount=20000,
                    is_founder=True,
                    company=company2
                )

                print("Andmed lisatud!")
            except Exception as e:
                print(f"Tekkis viga: {e}")