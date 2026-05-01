from dependency_injector import containers, providers
from dal.database import SessionLocal
from dal.repositories import PatientRepository, ExaminationRepository, ReportRepository
from bll.service import ExaminationService
from utils.output_strategies import OutputFactory 

class Container(containers.DeclarativeContainer):
    db_session = providers.Object(SessionLocal) 

    output_strategy = providers.Singleton(OutputFactory.get_strategy)

    patient_repo = providers.Factory(PatientRepository, session_factory=db_session)
    exam_repo = providers.Factory(ExaminationRepository, session_factory=db_session)
    report_repo = providers.Factory(ReportRepository, session_factory=db_session)

    exam_service = providers.Factory(
        ExaminationService,
        patient_repo=patient_repo,
        exam_repo=exam_repo,
        report_repo=report_repo,
        output_strategy=output_strategy
    )
