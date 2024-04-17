from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model
from djangoldp.permissions import InheritPermissions

from djangoldp_energiepartagee.models.actor import Actor
from djangoldp_energiepartagee.models.shareholder import Shareholder


class CapitalDistribution(Model):
    actor = models.ForeignKey(
        Actor,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Acteur",
        related_name="capital_distributions",
    )
    shareholder = models.ForeignKey(
        Shareholder,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Shareholder",
        related_name="capital_distribution",
    )
    individuals_count = models.DecimalField(
        max_digits=30, decimal_places=2, blank=True, null=True
    )
    individuals_capital = models.DecimalField(
        max_digits=30, decimal_places=2, blank=True, null=True
    )
    other_funds_capital = models.DecimalField(
        max_digits=30, decimal_places=2, blank=True, null=True
    )
    other_funds_residents = models.DecimalField(
        max_digits=30, decimal_places=2, blank=True, null=True
    )
    other_funds_excluding_residents = models.DecimalField(
        max_digits=30, decimal_places=2, blank=True, null=True
    )
    other_ess_orgs_capital = models.DecimalField(
        max_digits=30, decimal_places=2, blank=True, null=True
    )
    other_ess_orgs_other_funds = models.DecimalField(
        max_digits=30, decimal_places=2, blank=True, null=True
    )
    communities_capital = models.DecimalField(
        max_digits=30, decimal_places=2, blank=True, null=True
    )
    neighboring_communities_capital = models.DecimalField(
        max_digits=30, decimal_places=2, blank=True, null=True
    )
    other_private_orgs_capital = models.DecimalField(
        max_digits=30, decimal_places=2, blank=True, null=True
    )
    other_private_orgs_other_funds = models.DecimalField(
        max_digits=30, decimal_places=2, blank=True, null=True
    )

    class Meta(Model.Meta):
        ordering = ["pk"]
        permission_classes = [InheritPermissions]
        inherit_permissions = ["actor"]
        rdf_type = "energiepartagee:capital_distribution"
        serializer_fields = [
            "shareholder",
            "individuals_count",
            "individuals_capital",
            "other_funds_capital",
            "other_funds_residents",
            "other_funds_excluding_residents",
            "other_ess_orgs_capital",
            "other_ess_orgs_other_funds",
            "communities_capital",
            "neighboring_communities_capital",
            "other_private_orgs_capital",
            "other_private_orgs_other_funds",
        ]
        nested_fields = ["shareholder"]
        verbose_name = _("Distribution du capital")
        verbose_name_plural = _("Distribution des capitaux")

    def __str__(self):
        return self.urlid
