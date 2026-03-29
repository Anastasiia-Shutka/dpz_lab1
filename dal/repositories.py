import csv
from dal.interfaces import IPatientRepository, IExaminationRepository, IReportRepository
from models.models import Patient, Examination, Report

class PatientRepository(IPatientRepository):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def read_csv(self, path):
        with open(path, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader) 
            return [row for row in reader if row]

    def save(self, patient):
        with self.session_factory() as session:
            session.add(patient)
            session.commit()
            session.refresh(patient)
            return patient

class ExaminationRepository(IExaminationRepository):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def save(self, exam):
        with self.session_factory() as session:
            session.add(exam)
            session.commit()
            session.refresh(exam)
            return exam

class ReportRepository(IReportRepository):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def save(self, report):
        with self.session_factory() as session:
            session.add(report)
            session.commit()
            session.refresh(report)
            return report