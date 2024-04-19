from datetime import timezone

from django.conf import settings

from graphene_django.types import DjangoObjectType
from graphene_django_cud.mutations import (
    DjangoBatchCreateMutation,
    DjangoBatchDeleteMutation,
    DjangoBatchPatchMutation,
)
from guardian.shortcuts import get_objects_for_user
from zoneinfo import ZoneInfo

from aleksis.core.schema.base import (
    DjangoFilterMixin,
    PermissionBatchPatchMixin,
    PermissionsTypeMixin,
)

from ..models import Absence, AbsenceReason


class AbsenceReasonType(PermissionsTypeMixin, DjangoFilterMixin, DjangoObjectType):
    class Meta:
        model = AbsenceReason
        fields = ("id", "short_name", "name")
        filter_fields = {
            "short_name": ["icontains", "exact"],
            "name": ["icontains", "exact"],
        }

    @classmethod
    def get_queryset(cls, queryset, info):
        return get_objects_for_user(info.context.user, "kolego.view_absencereason", queryset)


class AbsenceType(PermissionsTypeMixin, DjangoFilterMixin, DjangoObjectType):
    class Meta:
        model = Absence
        fields = ("id", "person", "reason", "comment", "datetime_start", "datetime_end")
        filter_fields = {
            "person__full_name": ["icontains", "exact"],
            "comment": ["icontains", "exact"],
        }

    @classmethod
    def get_queryset(cls, queryset, info):
        return get_objects_for_user(info.context.user, "kolego.view_absence", queryset)


class AbsenceBatchCreateMutation(DjangoBatchCreateMutation):
    class Meta:
        model = Absence
        fields = ("person", "reason", "comment", "datetime_start", "datetime_end")
        optional_fields = ("comment", "reason")
        permissions = ("kolego.add_absence",)  # FIXME

    @classmethod
    def handle_datetime_start(cls, value, name, info) -> int:
        value = value.replace(tzinfo=timezone.utc)
        return value

    @classmethod
    def handle_datetime_end(cls, value, name, info) -> int:
        value = value.replace(tzinfo=timezone.utc)
        return value

    @classmethod
    def before_save(cls, root, info, input, obj):  # noqa: A002
        for absence in obj:
            absence.timezone = ZoneInfo(settings.TIME_ZONE)  # FIXME Use TZ provided by client
        return obj


class AbsenceBatchDeleteMutation(DjangoBatchDeleteMutation):
    class Meta:
        model = Absence
        permission_required = "kolego.delete_absence"  # FIXME


class AbsenceBatchPatchMutation(PermissionBatchPatchMixin, DjangoBatchPatchMutation):
    class Meta:
        model = Absence
        fields = ("id", "person", "reason", "comment", "datetime_start", "datetime_end")
        permissions = ("kolego.change_absence",)  # FIXME

    @classmethod
    def handle_datetime_start(cls, value, name, info) -> int:
        value = value.replace(tzinfo=timezone.utc)
        return value

    @classmethod
    def handle_datetime_end(cls, value, name, info) -> int:
        value = value.replace(tzinfo=timezone.utc)
        return value

    @classmethod
    def before_save(cls, root, info, input, obj):  # noqa: A002
        for absence in obj:
            absence.timezone = ZoneInfo(settings.TIME_ZONE)  # FIXME Use TZ provided by client
        return obj


class AbsenceReasonBatchCreateMutation(DjangoBatchCreateMutation):
    class Meta:
        model = AbsenceReason
        fields = ("short_name", "name")
        optional_fields = ("name",)
        permissions = ("kolego.create_absencereason",)  # FIXME


class AbsenceReasonBatchDeleteMutation(DjangoBatchDeleteMutation):
    class Meta:
        model = AbsenceReason
        permission_required = "kolego.delete_absencereason"  # FIXME


class AbsenceReasonBatchPatchMutation(PermissionBatchPatchMixin, DjangoBatchPatchMutation):
    class Meta:
        model = AbsenceReason
        fields = ("id", "short_name", "name")
        permissions = ("kolego.change_absencereason",)  # FIXME
