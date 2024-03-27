from dataclasses import dataclass
import datetime

@dataclass
class User:
    username: str
    created_at: datetime.datetime
    birthday: datetime.datetime | None = None

# also check
# basics_02_decorators/basics_02_dataclassDecorator
