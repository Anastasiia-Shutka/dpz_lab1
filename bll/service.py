from models.models import Patient, Examination, Report

class ExaminationService:
    def __init__(self, patient_repo, exam_repo, report_repo):
        self.patient_repo = patient_repo
        self.exam_repo = exam_repo
        self.report_repo = report_repo

    def process_csv(self, path: str):
        try:
            self.patient_repo.delete_all()
            
            rows = self.patient_repo.read_csv(path)
            count_added = 0

            for row in rows:
                if not row or len(row) < 4:
                    continue
                
                name_raw, dob, gender, history = [item.strip() for item in row]

                patient = self.create_patient(name_raw, dob, gender, history)

                exam = self.exam_repo.save(Examination(patient_id=patient.id, body_part="General"))
                self.report_repo.save(Report(exam_id=exam.id, conclusion="Imported"))
                
                count_added += 1

                if count_added >= 100:
                    break
            
            print(f"DONE: Added {count_added} rows")
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        
    def get_all_patients(self):
        return self.patient_repo.get_all()

    def get_patient_by_id(self, p_id):
        return self.patient_repo.get_by_id(p_id)

    def create_patient(self, name, dob, gender, history):
        patient = Patient(full_name=name, dob=dob, gender=gender, medical_history=history)
        return self.patient_repo.save(patient)

    def update_patient(self, p_id, name, dob, gender, history):
        patient = self.get_patient_by_id(p_id)
        if patient:
            patient.full_name = name
            patient.dob = dob
            patient.gender = gender
            patient.medical_history = history
            return self.patient_repo.save(patient)

    def delete_patient(self, p_id):
        return self.patient_repo.delete(p_id)