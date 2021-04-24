import os

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

from base.helpers.generate_uuid import generate_uuid
from base.helpers.get_region import get_region
from base.helpers.get_current_ts import get_current_ts

class Employee(Model):
    """ PynamoDB Employee Model"""

    class Meta:
        table_name = "Employees"
        region = get_region()

    id = UnicodeAttribute(hash_key=True, default=generate_uuid)

    name = UnicodeAttribute()

    created_at = UnicodeAttribute(default=get_current_ts)
