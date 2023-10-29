from datetime import date
from dateutil import parser

def to_date(payload: str) -> date:
    if payload is None:
        return None
    return parser.parse(payload).date()