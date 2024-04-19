from wkregister.decorator import record, Records
import asyncio


@record()
def add(a: float, b: float):

    record = Records(
        org="nmi",
        key="testOrg4",
        userId="2",
        actionType="update",
        status="success",
        errorMessage=None,
        service="pay-service",
        payload={"hola": "mundo"},
    )
    return {"result": a + b, "record": record}


asyncio.run(add(1, 2))
