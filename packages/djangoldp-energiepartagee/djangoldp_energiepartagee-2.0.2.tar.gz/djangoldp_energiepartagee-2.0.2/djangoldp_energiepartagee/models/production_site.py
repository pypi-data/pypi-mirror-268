from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model
from djangoldp.permissions import InheritPermissions

from djangoldp_energiepartagee.models.citizen_project import CitizenProject
from djangoldp_energiepartagee.models.region import Region
from djangoldp_energiepartagee.permissions import EPRegionalAdminPermission


class ProductionSite(Model):
    citizen_project = models.ForeignKey(
        CitizenProject,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Projet citoyen",
        related_name="production_sites",
    )
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    # FIXME: Should be a property of produced energies
    reference_unit = models.TextField(
        blank=True, null=True, verbose_name="Unité de référence"
    )
    # FIXME: Should be a choice I think
    progress_status = models.CharField(
        max_length=248, blank=True, null=True, verbose_name="Progress status"
    )
    total_development_budget = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Budget total de développement",
    )
    total_investment_budget = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Budget total d'investissement",
    )
    yearly_turnover = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Chiffre d'affaire annuel"
    )
    address = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Adresse"
    )
    postcode = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Code Postal"
    )
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="Ville")
    department = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Département"
    )
    region = models.ForeignKey(
        Region,
        max_length=50,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Région",
        related_name="production_sites",
    )
    lat = models.DecimalField(
        max_digits=30,
        decimal_places=25,
        blank=True,
        null=True,
        verbose_name="Lattitude",
    )
    lng = models.DecimalField(
        max_digits=30,
        decimal_places=25,
        blank=True,
        null=True,
        verbose_name="Longitude",
    )
    expected_commissionning_year = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Année de mise en service prévue",
    )
    effective_commissionning_year = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Année de mise en service effective",
    )
    picture = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Photo"
    )
    investment_capacity_ratio = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Ratio investissement par puissance €/kW",
    )
    grants_earned_amount = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Montant des subventions reçues pour le Site de production (en €)",
    )
    production_tracking_url = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="URL monitoring du site de production",
    )

    class Meta(Model.Meta):
        ordering = ["pk"]
        permission_classes = [InheritPermissions | EPRegionalAdminPermission]
        inherit_permissions = ["citizen_project"]
        rdf_type = "energiepartagee:production_site"
        nested_fields = [
            "partner_links",
            "energy_productions",
        ]
        serializer_fields = [
            "name",
            "description",
            "reference_unit",
            "progress_status",
            "total_development_budget",
            "total_investment_budget",
            "yearly_turnover",
            "address",
            "city",
            "department",
            "region",
            "lat",
            "lng",
            "expected_commissionning_year",
            "effective_commissionning_year",
            "picture",
            "investment_capacity_ratio",
            "grants_earned_amount",
            "production_tracking_url",
            "partner_links",
            "energy_productions",
        ]
        verbose_name = _("Site de production")
        verbose_name_plural = _("Sites de productions")
        depth = 2

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.urlid
