from ..config import settings
from ..database import MongoAPI
from ..enums.enums import EventsLogsEnum
from ..utility import get_datetime


class AuditoryLogs:
    @staticmethod
    def registry_log(origin: str, event: EventsLogsEnum, description: str, user: str):
        data = {
            'collection': settings.MONGO_COLLECTION_AUDITORY_LOGS,
            'Documents': {
                'origin': origin,
                'event': event,
                'description': description,
                'user_id': user,
                'created_at': get_datetime()
            }
        }

        mongodb = MongoAPI(data)
        mongodb.write(data)
