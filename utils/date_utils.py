from datetime import date
from dateutil import parser

def to_date(payload: str) -> date:
    if not payload:
        return None
    return parser.parse(payload).date()