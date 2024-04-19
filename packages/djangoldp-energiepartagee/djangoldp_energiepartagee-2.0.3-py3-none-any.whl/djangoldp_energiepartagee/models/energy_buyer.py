from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model
from djangoldp.permissions import InheritPermissions

from djangoldp_energiepartagee.models.energy_buyer_type import ContractType


class EnergyBuyer(Model):
    name = models.CharField(max_length=250, blank=True, null=True, verbose_name="Nom")
    contract_type = models.ForeignKey(
        ContractType,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Type de contrat",
        related_name="contract",
    )

    class Meta(Model.Meta):
        ordering = ["pk"]
        permission_classes = [InheritPermissions]
        inherit_permissions = ["energy_bought"]
        rdf_type = "energiepartagee:energy_buyer"
        verbose_name = _("Acheteur d'énergie")
        verbose_name_plural = _("Acheteurs d'énergies")

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.urlid
