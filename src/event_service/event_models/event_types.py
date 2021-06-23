from enum import Enum

from event_models import auth_service_events as auth


class EventType(str, Enum):
    # Auth service events
    user_registered = "user_registered"
    user_password_updated = "user_password_updated"

    # Analytics service events
    ugc_service = "ugc_service"
    analytics_service = "analytics_service"

    # UGC service events
    like_added = "like_added"
    comment_added = "comment_added"


event_type_to_model_mapping = {
    EventType.user_registered.value: auth.UserRegistered,
    EventType.user_password_updated.value: auth.UserPasswordUpdated
}


