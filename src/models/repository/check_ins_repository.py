from src.models.entities.check_ins import CheckIns
from src.models.settings.connection import db_connection_handler
from sqlalchemy.exc import IntegrityError



class CheckInsRepository:
    def insert_check_ins(self, attendee_id: str) -> str:
        with db_connection_handler as db:
            try:
                check_ins = CheckIns(
                    
                    attendeeId=attendee_id,
                )
                db.session.add(check_ins)
                db.session.commit()

                return attendee_id
            except IntegrityError:
                raise Exception("Check-in ja registrado")
            except Exception as exception:
                db.session.rollback()
                raise exception