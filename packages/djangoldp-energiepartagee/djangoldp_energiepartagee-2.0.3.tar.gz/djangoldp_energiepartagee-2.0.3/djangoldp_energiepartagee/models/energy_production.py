from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model
from djangoldp.permissions import InheritPermissions

from djangoldp_energiepartagee.models.energy_buyer import EnergyBuyer
from djangoldp_energiepartagee.models.energy_type import EnergyType
from djangoldp_energiepartagee.models.production_site import ProductionSite


class EnergyProduction(Model):
    production_site = models.ForeignKey(
        ProductionSite,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Site de production",
        related_name="energy_productions",
    )
    energy_buyer = models.ForeignKey(
        EnergyBuyer,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Acheteur d'énergie",
        related_name="energy_bought",
    )
    energy_type = models.ForeignKey(
        EnergyType,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Type d'énergie",
        related_name="energy_production",
    )
    energy_contract = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Contrat associé"
    )
    reference_unit = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Unité de référence"
    )
    estimated_capacity = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Puissance estimée"
    )
    installed_capacity = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Puissance installée"
    )
    consumption_equivalence = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Equivalence en nombre de foyers",
    )
    yearly_production = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Production annuelle"
    )
    estimated_yearly_production = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Production annuelle estimée"
    )
    technology_used = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Technologie utilisée"
    )
    estimated_injection_capacity = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Capacité d'injection estimée",
    )

    class Meta(Model.Meta):
        ordering = ["pk"]
        permission_classes = [InheritPermissions]
        inherit_permissions = ["production_site"]
        rdf_type = "energiepartagee:energy_production"
        verbose_name = _("Énergie produite")
        verbose_name_plural = _("Énergies produites")

    def __str__(self):
        if self.production_site.name:
            return self.production_site.name
        else:
            return self.urlid
