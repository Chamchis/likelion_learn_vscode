# 원격 진료 시스템
# 사람 > 의사,환자
class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
class Doctor(Person):
    total_appointments = 0
    def __init__(self,name,age,hospital):
        super().__init__(name,age)
        self.hospital = hospital
        self._appointments = 0
    @classmethod
    def update_total_appointments(cls):
        cls.total_appointments += 1
    def appointments(self):
        self.appointments += 1    

class Patient(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
class Appointments:
    def __init__(self,doctor,patient) -> None:
        self.doctor = doctor
        self.patient = patient
    def done(self):
        self.doctor._appointments += 1
        self.doctor.update_total_appointments()

patient = Patient('JANE','70')
doctor = Doctor('Hudson',44,'Berlin Hospital')
appointments = Appointments(doctor,patient)
appointments.done()
print(doctor._appointments)
patient = Patient('Denia','70')
doctor = Doctor('Ural',44,'London Hospital')
appointments1 = Appointments(doctor,patient)
appointments1.done()
print(doctor._appointments)

