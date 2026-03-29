from dependency_injector import containers, providers
from dal.database import SessionLocal
from dal.repositories import PatientRepository, ExaminationRepository, ReportRepository
from bll.service import ExaminationService

class Container(containers.DeclarativeContainer):
    # Використовуємо Object, щоб передати сам клас SessionLocal як фабрику
    db_session = providers.Object(SessionLocal) 

    patient_repo = providers.Factory(PatientRepository, session_factory=db_session)
    exam_repo = providers.Factory(ExaminationRepository, session_factory=db_session)
    report_repo = providers.Factory(ReportRepository, session_factory=db_session)

    exam_service = providers.Factory(
        ExaminationService,
        patient_repo=patient_repo,
        exam_repo=exam_repo,
        report_repo=report_repo
    )