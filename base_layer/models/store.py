import os

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, ListAttribute

from base.helpers.generate_uuid import generate_uuid
from base.helpers.get_region import get_region
from base.helpers.get_current_ts import get_current_ts

class Store(Model):
    """ PynamoDB Store Model"""

    class Meta:
        table_name = "Stores"
        region = get_region()

    id = UnicodeAttribute(hash_key=True, default=generate_uuid)

    name = UnicodeAttribute()
    delay = NumberAttribute()
    working_since = UnicodeAttribute()

    created_at = UnicodeAttribute(default=get_current_ts)
