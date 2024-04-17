# WK Register

The WK Register is a library for logging data to a Kafka topic.

## Getting started

Configure your Kafka environment variables first:

- BOOTSTRAP_SERVER (in server:port format)
- SECURITY_PROTOCOL
- SASL_MECHANISM
- SASL_USERNAME
- SAS_PASSWORD

## Usage Example

To use the library, add the @record decorator to any function whose output you wish to send to Kafka, and include a record key in the function's return value as demonstrated below:

```python
from wkregister.decorator import record

@record()
def add(a: float, b: float):

    return {"result": a + b, "record": Record}
```

The library processes the record key to ensure that a Record object is sent. The structure of the Record is defined as follows:

```python
from dataclasses import dataclass, asdict
from uuid import uuid4
from datetime import datetime

@dataclass
class Records:
    org: str = ""
    key: str = ""
    userId: str = ""
    actionType: str = ""
    status: str = ""
    errorMessage: str = ""
    service: str = ""
    id: str = str(uuid.uuid4())
    timestamp: str = str(datetime.today())

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}

```

Import and use Record like this:

```python
from wkregister.decorator import record, Records
# or
from wkregister.models import Records

record = Records(
        org="testOrg",
        key="logs",
        userId="1",
        actionType="insert",
        status="success",
        errorMessage=None,
        service="pay-service",
    )
```

## Complete Example

Here’s a comprehensive example:

```python
from wkregister.decorator import record, Records
import asyncio

@record()
def add(a: float, b: float):

    record = Records(
        org="testorg",
        key="logs",
        userId="1",
        actionType="insert",
        status="success",
        errorMessage=None,
        service="pay-service",
    )
    return {"result": a + b, "record": record}


    result = asyncio.run(add(12, 12))

```

## Fast API integration

### Define Environment Variables

Start by defining the environment variables using Pydantic. This setup allows your FastAPI application to read configuration variables from environment files or the environment itself, ensuring sensitive credentials are not hard-coded into the application.

```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    BOOTSTRAP_SERVER: str
    SECURITY_PROTOCOL: str
    SASL_MECHANISM: str
    SASL_USERNAME: str
    SAS_PASSWORD: str

    class Config:
        env_file = ".env"  # Assumes you have a .env file in your project root

# Load settings from the environment
settings = Settings()

```

### Add a Decorator for Logging

Import library and add decorator

```python
from fastapi import FastAPI
from wkregister.decorator import record, Records

app = FastAPI()

@app.get("/")
@record()
def root():
    # Create a record object with relevant logging details
    record = Records(
        org="testorg",
        key="logs",
        userId="1",
        actionType="insert",
        status="success",
        errorMessage=None,
        service="pay-service",
    )
    # The record is returned for demonstration purposes
    return {"result": "ok", "record": record}
```
