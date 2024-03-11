# 의사 선생님 - 담당하는 환자리스트를 가지고 있다.
# 우리는 의사의 이름, 환자 정보, 전체 담당 환자의 정보를 받고자 한다.
class Doctor:
  def __init__(self, name, patient_num):
    self.name = name +"_doctor"
    self.patients = ["환자{}".format(i) for i in range(patient_num)]
  def __str__(self):
    return self.name
  def __repr__(self):
    return self.name
  def __getitem__(self, index):
    return self.patients[index]
  def __len__(self):
    return len(self.patients)
  def __lt__(self, other):
    return len(self.patients) < len(other.patients)
doctor1 = Doctor("지훈", 30)
doctor2 = Doctor("여진", 28)
print(doctor1, ' , ' ,doctor2)
print(doctor1.patients[27])
print(len(doctor1))

print(doctor1 > doctor2)