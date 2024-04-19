from django.db import models
from django.utils.translation import gettext_lazy as _

from djangoldp.models import Model
from djangoldp.permissions import AuthenticatedOnly, ReadOnly

from djangoldp_energiepartagee.models.production_site import ProductionSite


class PartnerLink(Model):
    name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Nom du lien de partenariat"
    )
    production_sites = models.ManyToManyField(
        ProductionSite,
        blank=True,
        verbose_name="Sites de production",
        related_name="partner_links",
    )

    class Meta(Model.Meta):
        ordering = ["name"]
        permission_classes = [AuthenticatedOnly, ReadOnly]
        rdf_type = "energiepartagee:partner_link"
        serializer_fields = ["@id", "name"]
        verbose_name = _("Lien de partenariat")
        verbose_name_plural = _("Liens de partenariat")

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.urlid
