from src.models.settings.connection import db_connection_handler
from src.models.entities.attendees import Attendees
from src.models.entities.events import Events
from src.models.entities.check_ins import CheckIns
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from typing import Dict, List

class AttendeesRepository:
    def insert_attendees(self, attendeesInfo: Dict) -> Dict:
        with db_connection_handler as db:
            
            try:            
                attendees = Attendees(
                    id=attendeesInfo.get("uuid"),
                    name=attendeesInfo.get("name"),
                    email=attendeesInfo.get("email"),
                    event_id=attendeesInfo.get("event_id"),
                )
                db.session.add(attendees)
                db.session.commit()
                
                return attendeesInfo
            except IntegrityError:
               raise Exception("Participante ja cadastrado")
       
            except Exception as exception:
                db.session.rollback()
                raise exception
            
            
    def get_attendees_by_event_id(self, attendee_id: str) -> Attendees:
        with db_connection_handler as db:
            try:
                attendee = (
                    db.session
                    .query(Attendees)
                    .join(Events, Events.id == Attendees.event_id)
                    .filter(Attendees.id == attendee_id)
                    .with_entities(
                        Attendees.name,
                        Attendees.email,
                        Events.title
                    )
                    .one()
                )
                return attendee
            except NoResultFound:
                return None
            
    def get_attendees_by_id(self, event_id: str) -> List[Attendees]:
        with db_connection_handler as db:
            attendees = (
                db.session
                .query(Attendees)
                .outerjoin(CheckIns, CheckIns.attendeeId == Attendees.id)
                .filter(Attendees.event_id == event_id)
                .with_entities(
                    Attendees.id,
                    Attendees.name,
                    Attendees.email,
                    CheckIns.created_at.label("checkin_at"),
                    Attendees.created_at.label("created_at")
                )
                .all()
            )
            
            return attendees