from wkregister.decorator import record, Records
import asyncio


@record()
def add(a: float, b: float):

    record = Records(
        org="commonsense",
        key="logs",
        userId="2",
        actionType="update",
        status="success",
        errorMessage=None,
        service="pay-service",
    )
    return {"result": a + b, "record": record}


asyncio.run(add(1, 2))
