from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.events import Events
from src.models.entities.attendees import Attendees
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from src.errors.error_types.http_conflict import HttpConflictError
class EventsRepository:
    def insert_event(self, eventsInfo: Dict) -> Dict:
       with db_connection_handler as db: 
           try:
                event = Events(
                    id=eventsInfo.get("uuid"),
                    title=eventsInfo.get("title"),
                    details=eventsInfo.get("details"),
                    slug=eventsInfo.get("slug"),
                    maximum_attendees=eventsInfo.get("maximum_attendees")
                )
                db.session.add(event)
                db.session.commit()
                
                return eventsInfo
           except IntegrityError:
               raise HttpConflictError("Evento já cadastrado")
           
           except Exception as exception:
               db.session.rollback()
               raise exception
       
       
    def get_event_by_id(self, event_id: str) -> Events:
        with db_connection_handler as db:
            try:
                
                event = db.session.query(Events).filter(Events.id == event_id).one()
                return event
            
            except NoResultFound:
                return None
            
    def count_attendees_by_event_id(self, event_id: str) -> Dict:
        with db_connection_handler as db:
            try:
                event_count = (db.session
                                .query(Events)
                                .join(Attendees, Events.id == Attendees.event_id)
                                .filter(Events.id == event_id)
                                .with_entities(
                                    Events.maximum_attendees,
                                    Attendees.id
                                )
                                .all()
                               )
                if not len(event_count):
                    return {
                        "maximum_attendees": 0,
                        "attendees_count": 0
                    }
                return {
                    "maximum_attendees": event_count[0].maximum_attendees,
                    "attendees_count": len(event_count)
                }
            except NoResultFound:
                return None