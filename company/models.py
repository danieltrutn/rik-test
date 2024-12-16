# region				----- External Imports -----
from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
# endregion

# region				----- Internal Imports -----
from .choices import SHAREHOLDER_TYPES 
# endregion

class Company(models.Model):
    # region              ----- Information -----
    name = models.CharField(
        verbose_name=_("Nimi"),
        validators=[
            RegexValidator(regex=r'^[a-zA-Z0-9 ]+$', message=_("Nimi võib sisaldada ainult tähti, numbreid ja tühikuid.")),
        ],
        max_length=100
    )

    registration_code = models.CharField(
        verbose_name=_("Registrikood"),
        max_length=7,
        unique=True,
        validators=[
            RegexValidator(regex=r'^\d{7}$', message=_("Registrikood peab olema täpselt 7 numbrit.")),
        ]
    )

    capital = models.PositiveIntegerField(
        verbose_name=_("Kapital (EUR)"),
        validators=[MinValueValidator(2500, _("Kapital peab olema vähemalt 2500 eurot."))]
    )
    # endregion

    # region              ----- Dates -----
    establishment_date = models.DateTimeField(
        verbose_name=_("Asutamiskuupäev"),
        default=now
    )
    # endregion



class Shareholder(models.Model):
    # region              ----- Information -----
    shareholder_type = models.CharField(
        verbose_name=_("Osaniku tüüp"),
        max_length=20,
        choices=SHAREHOLDER_TYPES 
    )

    name = models.CharField(
        verbose_name=_("Nimi"),
        max_length=100
    )

    personal_code = models.CharField(
        verbose_name=_("Isikukood"),
        max_length=20,
        blank=True,
        null=True
    )

    registration_code = models.CharField(
        verbose_name=_("Registrikood"),
        max_length=7,
        blank=True,
        null=True
    )

    share_amount = models.PositiveIntegerField(
        verbose_name=_("Osa suurus (EUR)"),
        validators=[MinValueValidator(1, _("Osa suurus peab olema vähemalt 1 euro."))]
    )

    is_founder = models.BooleanField(
        verbose_name=_("Asutaja"),
        default=False,
    )
    # endregion

    # region           ----- Relation -----
    company = models.ForeignKey(
        Company, 
        related_name='shareholders', 
        on_delete=models.CASCADE
    )
    # endregion