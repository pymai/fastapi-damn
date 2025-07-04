from datetime import datetime, time, timedelta
from uuid import UUID

from fastapi import Body, FastAPI

app = FastAPI()


@app.put("/items/{item_id}")
async def read_items(
        item_id: UUID,
        # Body: 用于指明参数来自于请求体（而不是 query 或 path）
        start_datetime: datetime = Body(),
        end_datetime: datetime = Body(),
        process_after: timedelta = Body(),
        repeat_at: time | None = Body(default=None),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_after,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }

# curl -X 'PUT' \
#   'http://127.0.0.1:8000/items/5e8f8f8e-8d3c-4c3b-9b26-57c4d9e861c5' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "start_datetime": "2025-07-04T10:00:00",
#   "end_datetime": "2025-07-04T15:30:00",
#   "process_after": "PT2H",
#   "repeat_at": "13:00:00"
# }
# '
