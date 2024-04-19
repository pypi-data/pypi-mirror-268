from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoldp.models import Model
from djangoldp.permissions import InheritPermissions

from djangoldp_energiepartagee.models.actor import Actor
from djangoldp_energiepartagee.models.region import Region
from djangoldp_energiepartagee.permissions import EPRegionalAdminPermission

CITIZEN_PROJECT_STATUS_CHOICES = [
    ("draft", "Brouillon"),
    ("validation", "En cours de validation"),
    ("published", "Publié"),
    ("retired", "Dépublié"),
]


class CitizenProject(Model):
    founder = models.ForeignKey(
        Actor,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Fondateur",
        related_name="founded_projects",
    )
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Name")
    short_description = models.TextField(
        blank=True, null=True, verbose_name="Courte description"
    )
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="Ville")
    postcode = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Code Postal"
    )
    address = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Adresse"
    )
    # region = models.CharField(max_length=50, blank=True, null=True, verbose_name="Région")
    region = models.ForeignKey(
        Region,
        max_length=50,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Région",
        related_name="projects",
    )
    department = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Département"
    )
    action_territory = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Territoire d'action du projet",
    )
    picture = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Photo"
    )
    video = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Vidéo"
    )
    website = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Site"
    )
    facebook_link = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Facebook"
    )
    linkedin_link = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="LinkedIn"
    )
    twitter_link = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Twitter"
    )
    instagram_link = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Instragram"
    )
    contact_picture = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Contact: Photo"
    )
    contact_name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Contact: Nom"
    )
    contact_first_name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Contact: Prénom"
    )
    contact_email = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Contact: Email"
    )
    contact_phone = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Contact: Téléphone"
    )
    contact_visibility = models.BooleanField(
        blank=True, null=True, verbose_name="Visibilité du contact", default=False
    )
    status = models.CharField(
        choices=CITIZEN_PROJECT_STATUS_CHOICES,
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Etat d'avancement du projet",
    )
    lat = models.DecimalField(
        max_digits=30,
        decimal_places=25,
        blank=True,
        null=True,
        verbose_name="Latitude",
    )
    lng = models.DecimalField(
        max_digits=30,
        decimal_places=25,
        blank=True,
        null=True,
        verbose_name="Longitude",
    )
    production_tracking_url = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="URL monitoring du site de production",
    )
    fundraising_url = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="URL Page Collecte locale",
    )
    wp_project_url = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Lien du projet sur le site principal",
    )

    class Meta(Model.Meta):
        ordering = ["pk"]
        permission_classes = [InheritPermissions | EPRegionalAdminPermission]
        inherit_permissions = ["founder"]
        rdf_type = "energiepartagee:citizen_project"
        nested_fields = [
            "communication_profile",
            "partnered_by",
            "earned_distinctions",
            "testimonies",
            "production_sites",
        ]
        verbose_name = _("Projet Citoyen")
        verbose_name_plural = _("Projets Citoyens")
        depth = 2

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.urlid
