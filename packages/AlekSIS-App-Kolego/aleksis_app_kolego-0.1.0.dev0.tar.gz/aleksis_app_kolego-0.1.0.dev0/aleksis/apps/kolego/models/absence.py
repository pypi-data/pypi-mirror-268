from django.db import models
from django.utils.translation import gettext_lazy as _

from colorfield.fields import ColorField

from aleksis.core.managers import PolymorphicBaseManager
from aleksis.core.mixins import ExtensibleModel
from aleksis.core.models import FreeBusy

from ..managers import AbsenceQuerySet


class AbsenceReason(ExtensibleModel):
    short_name = models.CharField(verbose_name=_("Short name"), max_length=255, unique=True)
    name = models.CharField(verbose_name=_("Name"), max_length=255)

    colour = ColorField(verbose_name=_("Colour"), blank=True)

    count_as_absent = models.BooleanField(
        default=True,
        verbose_name=_("Count as absent"),
        help_text=_(
            "If checked, this excuse type will be counted as absent. If not checked,"
            "it won't show up in absence reports."
        ),
    )

    default = models.BooleanField(verbose_name=_("Default Reason"), default=False)

    def __str__(self):
        if self.name:
            return f"{self.short_name} ({self.name})"
        else:
            return self.short_name

    def save(self, *args, **kwargs):
        # Ensure that there is only one default absence reason
        if self.default:
            reasons = AbsenceReason.objects.filter(default=True)
            if self.pk:
                reasons.exclude(pk=self.pk)
            reasons.update(default=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_default(cls) -> "AbsenceReason":
        try:
            return cls.objects.get(default=True)
        except cls.ObjectDoesNotExist:
            return cls.objects.create(default=True, short_name="u", name=_("Unexcused"))

    class Meta:
        verbose_name = _("Absence reason")
        verbose_name_plural = _("Absence reasons")
        constraints = [
            models.UniqueConstraint(
                fields=["default"],
                condition=models.Q(default=True),
                name="only_one_default_absence_reason",
            )
        ]


class Absence(FreeBusy):
    objects = PolymorphicBaseManager.from_queryset(AbsenceQuerySet)()

    reason = models.ForeignKey(
        "AbsenceReason",
        on_delete=models.PROTECT,
        related_name="absences",
        verbose_name=_("Absence reason"),
    )

    person = models.ForeignKey(
        "core.Person",
        on_delete=models.CASCADE,
        related_name="kolego_absences",
        verbose_name=_("Person"),
    )

    comment = models.TextField(verbose_name=_("Comment"), blank=True)

    def __str__(self):
        return f"{self.person} ({self.datetime_start} - {self.datetime_end})"

    class Meta:
        verbose_name = _("Absence")
        verbose_name_plural = _("Absences")
