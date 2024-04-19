from django.db import models
from django.utils.translation import gettext_lazy as _

from djangoldp.models import Model
from djangoldp.permissions import AuthenticatedOnly, ReadOnly

from djangoldp_energiepartagee.models.citizen_project import CitizenProject
from djangoldp_energiepartagee.models.production_site import ProductionSite


class EarnedDistinction(Model):
    name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Distinction"
    )
    citizen_projects = models.ManyToManyField(
        CitizenProject,
        blank=True,
        verbose_name="Projets Distingués",
        related_name="earned_distinctions",
    )
    production_sites = models.ManyToManyField(
        ProductionSite,
        blank=True,
        verbose_name="Sites de Production Distingués",
        related_name="earned_distinctions",
    )

    class Meta(Model.Meta):
        ordering = ["name"]
        permission_classes = [AuthenticatedOnly, ReadOnly]
        rdf_type = "energiepartagee:distinction"
        serializer_fields = ["@id", "name"]
        verbose_name = _("Distinction")
        verbose_name_plural = _("Distinctions")

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.urlid
