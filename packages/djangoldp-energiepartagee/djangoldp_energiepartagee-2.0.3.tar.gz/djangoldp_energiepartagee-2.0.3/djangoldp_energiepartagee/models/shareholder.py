from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model
from djangoldp.permissions import InheritPermissions


class Shareholder(Model):
    structure_name = models.TextField(
        blank=True, null=True, verbose_name="Nom de la Structure"
    )
    capital_amount = models.TextField(
        blank=True, null=True, verbose_name="Montant capital"
    )
    capital_percentage = models.TextField(
        blank=True, null=True, verbose_name="Pourcentage capital"
    )
    other_funds_amount = models.TextField(
        blank=True, null=True, verbose_name="Montant autres fonds"
    )
    other_funds_percentage = models.TextField(
        blank=True, null=True, verbose_name="Pourcentage autres fonds"
    )
    is_relay_investment = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Est un investissement relais?",
        default=False,
    )

    class Meta(Model.Meta):
        ordering = ["pk"]
        permission_classes = [InheritPermissions]
        rdf_type = "energiepartagee:shareholder"
        serializer_fields = [
            "structure_name",
            "capital_amount",
            "capital_percentage",
            "other_funds_amount",
            "other_funds_percentage",
            "is_relay_investment",
        ]
        verbose_name = _("Actionnaire")
        verbose_name_plural = _("Actionnaires")

        def __str__(self):
            return self.structure_name
