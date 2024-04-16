from datetime import datetime, timezone
from lazy_schema import Schema

log_schema = Schema.new(
    message="",
    type="info",
    keyword=None,
    date_created=lambda: datetime.now(timezone.utc),
)
