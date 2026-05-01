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
            merged_patient = session.merge(patient)
            session.commit()
            session.refresh(merged_patient)
            session.expunge(merged_patient)
            return merged_patient

    def get_all(self):
        with self.session_factory() as session:
            patients = session.query(Patient).all()
            for p in patients:
                session.expunge(p)
            return patients

    def get_by_id(self, patient_id):
        with self.session_factory() as session:
            patient = session.query(Patient).filter(Patient.id == patient_id).first()
            if patient:
                session.expunge(patient)
            return patient

    def delete(self, patient_id):
        with self.session_factory() as session:
            patient = session.query(Patient).filter(Patient.id == patient_id).first()
            if patient:
                session.delete(patient)
                session.commit()

    def delete_all(self):
        with self.session_factory() as session:
            session.query(Patient).delete()
            session.commit()

class ExaminationRepository(IExaminationRepository):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def save(self, exam):
        with self.session_factory() as session:
            merged_exam = session.merge(exam)
            session.commit()
            session.refresh(merged_exam)
            session.expunge(merged_exam)
            return merged_exam

class ReportRepository(IReportRepository):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def save(self, report):
        with self.session_factory() as session:
            merged_report = session.merge(report)
            session.commit()
            session.refresh(merged_report)
            session.expunge(merged_report)
            return merged_report