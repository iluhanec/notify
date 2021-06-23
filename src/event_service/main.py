from fastapi import FastAPI, HTTPException
from pydantic import ValidationError

from event_models.event_sources import EventSource, event_source_to_queue_mapping
from event_models.event_types import EventType, event_type_to_model_mapping


app = FastAPI()


@app.post("/items/{event_source}/{event_type}")
def put_event_to_queue(event_source: EventSource, event_type: EventType, event: dict):

    queue = event_source_to_queue_mapping.get(event_source, None)
    if not queue:
        raise HTTPException(status_code=400, detail="Invalid queue")

    try:
        parsed_event = event_type_to_model_mapping[event_type](**event)
        return parsed_event
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())


