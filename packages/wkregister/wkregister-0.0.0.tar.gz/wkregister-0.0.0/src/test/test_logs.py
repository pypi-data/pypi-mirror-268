import unittest
from wkregister.decorator import record  # Import your decorator
from wkregister.models import Records
import asyncio


@record()
def add(a: float, b: float):

    record = Records(
        org="commonsense",
        key="logs",
        userId="1",
        actionType="insert",
        status="success",
        errorMessage=None,
        service="pay-service",
    )
    return {"result": a + b, "record": record}


class TestLogs(unittest.TestCase):

    def test_log(self):
        # Await the asynchronous method
        result = asyncio.run(add(12, 12))

        # Assert your test condition
        self.assertTrue(True)
