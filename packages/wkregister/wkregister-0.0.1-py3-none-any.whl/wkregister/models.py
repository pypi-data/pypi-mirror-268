from dataclasses import dataclass, asdict
from datetime import datetime
import uuid


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
