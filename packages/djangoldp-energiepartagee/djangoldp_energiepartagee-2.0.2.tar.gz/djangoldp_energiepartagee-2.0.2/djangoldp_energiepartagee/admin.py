from django.conf import settings
from django.contrib import admin
from djangoldp.admin import DjangoLDPAdmin

from djangoldp_energiepartagee.models import *


@admin.register(
    CommunicationProfile,
    Testimony,
)
class EmptyAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


@admin.register(
    College,
    Collegeepa,
    Integrationstep,
    Interventionzone,
    Legalstructure,
    Paymentmethod,
    Profile,
    Regionalnetwork,
    CapitalDistribution,
    EarnedDistinction,
    EnergyBuyer,
    EnergyType,
    EnergyProduction,
    ContractType,
    Partner,
    PartnerLink,
    PartnerType,
    ProductionSite,
    Shareholder,
)
class EPModelAdmin(DjangoLDPAdmin):
    readonly_fields = ("urlid",)
    exclude = ("is_backlink", "allow_create_backlink")
    extra = 0


@admin.register(Region)
class EPRegionAdmin(EPModelAdmin):
    filter_horizontal = ('admins',)


class TestimonyInline(admin.TabularInline):
    model = Testimony
    fk_name = "citizen_project"
    exclude = ("urlid", "is_backlink", "allow_create_backlink")
    extra = 0


class CommunicationProfileInline(admin.StackedInline):
    model = CommunicationProfile
    fk_name = "citizen_project"
    exclude = ("urlid", "is_backlink", "allow_create_backlink")
    extra = 0


@admin.register(CitizenProject)
class CitizenProjectAdmin(DjangoLDPAdmin):
    # list_display = ('urlid', 'name', 'allow_self_registration')
    exclude = ("urlid", "is_backlink", "allow_create_backlink")
    inlines = [CommunicationProfileInline, TestimonyInline]
    search_fields = ["urlid", "name", "partners__actor__members__user__urlid"]
    ordering = ["urlid"]


@admin.register(Actor)
class ActorAdmin(EPModelAdmin):
    list_display = ("longname", "shortname", "updatedate", "createdate")
    search_fields = ["longname", "shortname"]


@admin.register(Relatedactor)
class RelatedactorAdmin(EPModelAdmin):
    list_display = ("__str__", "role")
    search_fields = [
        "actor__longname",
        "actor__shortname",
        "user__first_name",
        "user__last_name",
        "user__email",
    ]


if not getattr(settings, "IS_AMORCE", False):

    @admin.register(Contribution)
    class ContributionAdmin(EPModelAdmin):
        list_display = ("actor", "year", "updatedate", "createdate")
        search_fields = ["actor__longname", "actor__shortname"]

        def get_readonly_fields(self, request, obj=None):
            if obj and obj.contributionstatus in (
                "a_ventiler",
                "valide",
            ):
                return self.readonly_fields + ("amount",)
            return self.readonly_fields

else:

    admin.site.register(Contribution, EmptyAdmin)
