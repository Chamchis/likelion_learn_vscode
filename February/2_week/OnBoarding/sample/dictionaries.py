# # # # # # 딕셔너리(Dictionaries)

# # # # # # student_1 = {
# # # # # #     "student_no": "2023_01234",
# # # # # #     "major" : "English",
# # # # # #     "grade" : 1
# # # # # # }

# # # # # # print(student_1["student_no"])

# # # # # # student_1["student_no"] = "2024_56789"

# # # # # # print(student_1)
# # # # # # print(student_1["student_no"])

# # # # # # # 추가
# # # # # # student_1["gpa"] = 4.5
# # # # # # print(student_1)

# # # # # # # 수정
# # # # # # student_1["gpa"] = 3.0
# # # # # # print(student_1)

# # # # # # # 삭제
# # # # # # del student_1["grade"]
# # # # # # print(student_1)

# # # # # student_1 = {
# # # # #     "student_no": "2023_01234",
# # # # #     "major" : "English",
# # # # #     "grade" : 1
# # # # # }

# # # # # # 데이터 접근
# # # # # # print(student_1.get("gpa", "해당 키-값 쌍이 없습니다."))

# # # # # # 딕셔너리의 키를 반환
# # # # # # print(list(student_1.keys()))

# # # # # # 딕셔너리의 값을 반환
# # # # # print(list(student_1.values()))

# # # # tech = {
# # # #     "HTML":"Advanced",
# # # #     "JavaScript":"Intermediate",
# # # #     "Python":"Expert",
# # # #     "Go":"Novice"
# # # # }
# # # # for key in tech.keys():
# # # #     print(key)

# # # # for value in tech.values():
# # # #     print(value)

# # # # 중첩(Nesting)

# # # student_1 = {
# # #     "student_no":1,
# # #     "gpa":3.0,
# # # }

# # # student_2 = {
# # #     "student_no":2,
# # #     "gpa":3.7,
# # # }

# # # students = [student_1, student_2]

# # # for student in students:
# # #     student['graduated'] = False
# # #     print(student)

# # student = {
# #     "subjects":["회계원리","프랑스어회화"]
# # }

# # print(student["subjects"])

# # subjects_list = student["subjects"]

# # for subject in subjects_list:
# #     print(subject)

# student = {
#     "scholarship":{
#         "name":"National",
#         "amount":"300M",
#     }
# }

# # print(student)

# # for key in student.keys():
# #     print(key)
# for value in student.values():
#     for value_2 in value:
#         print(value_2)