# coding: utf8
from datetime import datetime
from uuid import uuid1, uuid4
# from faker import Faker
    # f1 = Faker()
    # f1.seed(now.second)
    # str(f1.uuid4())[:8]

# This function generates duplicate IDs when using from Django Admin.
# Also when doing migrations the function is called and the  default value changes
def create_id(identifier):
    identifier = ('route_')
    now = datetime.utcnow()

    id_base = "{}{}{}{}{}{}{}{}"
    id_base = id_base.format(
        identifier,
        now.year,
        now.month,
        now.day,
        now.hour,
        now.minute,
        now.second,
        str(uuid4())[:8]
    )
    return id_base
