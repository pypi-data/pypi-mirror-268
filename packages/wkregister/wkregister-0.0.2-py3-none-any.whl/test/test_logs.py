import unittest
from wkregister.decorator import record  # Import your decorator
from wkregister.models import Records
import asyncio


@record()
def add(a: float, b: float):

    record = Records(
        org="nmi",
        key="commonsense",
        userId="2",
        actionType="update",
        status="success",
        errorMessage=None,
        service="pay-service",
    )
    return {"result": a + b, "record": record}


class TestLogs(unittest.TestCase):

    def test_log(self):
        # Await the asynchronous method
        asyncio.run(add(12, 12))

        # Assert your test condition
        self.assertTrue(True)
