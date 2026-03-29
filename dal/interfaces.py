from abc import ABC, abstractmethod

class IPatientRepository(ABC):
    @abstractmethod
    def save(self, patient):
        pass

    @abstractmethod
    def read_csv(self, path):
        pass


class IExaminationRepository(ABC):
    @abstractmethod
    def save(self, exam):
        pass


class IReportRepository(ABC):
    @abstractmethod
    def save(self, report):
        pass