from typing import Callable, Dict, FrozenSet, NewType

from django.apps import apps
from django.db import models
from django.utils.translation import gettext_lazy as _

from .encoding import DECODER, ENCODER


class FieldLog(models.Model):
    app_label = models.CharField(max_length=100, editable=False)
    model = models.CharField(_("model class name"), max_length=100, editable=False)
    instance_id = models.CharField(max_length=255, editable=False)
    field = models.CharField(_("field name"), max_length=100, editable=False)
    timestamp = models.DateTimeField(auto_now=True, editable=False)
    old_value = models.JSONField(
        encoder=ENCODER, decoder=DECODER, blank=True, null=True, editable=False
    )
    new_value = models.JSONField(
        encoder=ENCODER, decoder=DECODER, blank=True, null=True, editable=False
    )
    extra_data = models.JSONField(encoder=ENCODER, decoder=DECODER, default=dict)
    created = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return f"({self.field}) {self.old_value} -> {self.new_value}"

    @staticmethod
    def from_db_field(field_class, value):
        if field_class.__class__ is models.BinaryField:
            value = bytes(value, "utf-8")
        elif field_class.__class__ is models.DecimalField:
            value = round(value, field_class.decimal_places)
        elif field_class.__class__ is models.ForeignKey:
            return field_class.related_model.objects.get(pk=value)

        return field_class.to_python(value)

    @classmethod
    def from_db(cls, db, field_names, values):
        field_class = apps.get_model(values[1], values[2])._meta.get_field(values[4])
        instance = super().from_db(db, field_names, values)
        iid = instance.instance_id
        instance.instance_id = int(iid) if iid.isdigit() else iid
        instance.old_value = (
            cls.from_db_field(field_class, instance.old_value)
            if not instance.created
            else None
        )
        instance.new_value = cls.from_db_field(field_class, instance.new_value)

        return instance

    @property
    def model_class(self):
        return apps.get_model(self.app_label, self.model)

    @property
    def instance(self):
        return self.model_class.objects.get(pk=self.instance_id)

    @property
    def previous_log(self):
        return (
            self.__class__.objects.filter(
                app_label=self.app_label,
                model=self.model,
                instance_id=self.instance_id,
                field=self.field,
            )
            .exclude(pk=self.pk)
            .order_by("pk")
            .last()
        )


LoggableModel = NewType("LoggableModel", models.Model)
Callback = Callable[[LoggableModel, FrozenSet[str], Dict[str, FieldLog]], None]
