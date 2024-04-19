from dataclasses import dataclass, field, asdict
from typing import Dict
import uuid
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
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: str = field(default_factory=lambda: str(datetime.today()))
    payload: Dict = field(default_factory=dict)

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}
