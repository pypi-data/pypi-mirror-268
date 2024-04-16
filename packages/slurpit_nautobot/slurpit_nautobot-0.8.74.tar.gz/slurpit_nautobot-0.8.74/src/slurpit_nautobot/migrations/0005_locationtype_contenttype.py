from nautobot.dcim.models import Device
from nautobot.dcim.models import LocationType
from django.contrib.contenttypes.models import ContentType
from django.db import migrations, models
from .. import get_config


def migrate_content_type(apps, schema_editor):
    location_type, _ = LocationType.objects.get_or_create(**get_config('LocationType'))
    if location_type.content_types.count() == 0:
        location_type.content_types.add(ContentType.objects.get_for_model(Device))

class Migration(migrations.Migration):

    dependencies = [
        ('slurpit_nautobot', '0004_auto_20240408_1105'),
    ]

    operations = [
        migrations.RunPython(migrate_content_type),
    ]
