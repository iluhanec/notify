from enum import Enum


class EventSource(str, Enum):
    auth_service = "auth_service"
    admin_service = "admin_service"
    ugc_service = "ugc_service"
    analytics_service = "analytics_service"


event_source_to_queue_mapping = {
    EventSource.admin_service: "admin_service_queue",
    EventSource.analytics_service: "analytics_service_queue",
    EventSource.auth_service: "auth_service_queue",
}
