from json import loads

from pynamodb.connection import Connection
from pynamodb.transactions import TransactWrite

from request import Request
from base.models.store import Store
from base.models.employee import Employee
from base.helpers.generate_uuid import generate_uuid


# input_data = {
#     "name": "La empanada magica",
#     "delay": 30,
#     "working_since": "2020-01-01 18:00:00",
#     "employees": ["Juan", "Pedro"],
# }


def handler(event, context):
    # Validation
    request = Request(**loads(event.get("body", {})))

    # Business logic, running safely under a transaction
    with TransactWrite(
        connection=Connection(), client_request_token=generate_uuid()
    ) as transaction:
        transaction.save(
            Store(
                name=request.name,
                delay=request.delay,
                working_since=request.working_since.strftime("%Y-%m-%d %H:%M:%S"),
            )
        )

        for employee_name in request.employees:
            transaction.save(Employee(name=employee_name))
