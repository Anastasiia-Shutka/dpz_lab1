from models.models import Patient, Examination, Report

class ExaminationService:
    def __init__(self, patient_repo, exam_repo, report_repo):
        self.patient_repo = patient_repo
        self.exam_repo = exam_repo
        self.report_repo = report_repo

    def process_csv(self, path: str):
        rows = self.patient_repo.read_csv(path)
        with self.patient_repo.session_factory() as session:
            session.query(Report).delete()
            session.query(Examination).delete()
            session.query(Patient).delete()
            session.commit()

        for row in rows:
            name, dob, gender, history = [item.strip() for item in row]

            patient = Patient(
                full_name=name,
                dob=dob,
                gender=gender,
                medical_history=history
            )
            saved_patient = self.patient_repo.save(patient)

            exam = Examination(
                patient_id=saved_patient.id,
                body_part="Dermatoscopy"
            )
            saved_exam = self.exam_repo.save(exam)

            report = Report(
                exam_id=saved_exam.id,
                conclusion="AI Analysis OK"
            )
            self.report_repo.save(report)

        return True