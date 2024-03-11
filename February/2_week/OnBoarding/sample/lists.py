# # 리스트(lists)

# # mbti = ['INFP', 'ENFP', "ISTJ", "ESTP"]

# # print(mbti)
# # print(mbti[0])

# # mbti[0] = 'INFJ'

# # print(mbti)
# # print(mbti[0])

# # my_list = [123,'apple']
# # print(my_list)


# # colors = ['red', 'blue', 'green']

# # 수정
# # colors[2] = 'black'

# # print(colors)

# # 추가 1
# # colors.append('purple')
# # print(colors)

# # 추가 2
# # colors.insert(1, 'yellow')
# # print(colors)

# # colors.insert(0, 'yellow')
# # print(colors)

# # colors.insert(4, 'yellow')
# # print(colors)

# # 제거 1
# # del colors[0]
# # print(colors)

# # 제거 2
# # color = colors.pop(0)
# # print(colors)
# # print(color)

# # 제거 3
# # colors.remove('blue')
# # print(colors)

# # 리스트 정렬
# # colors = ['blue', 'red', 'gray', 'black', 'yellow', 'orange']

# # 정렬 1
# # colors.sort()
# # print(colors)

# # colors.sort(reverse=True)
# # print(colors)

# # 정렬 2
# # print(sorted(colors))

# # 길이 - 요소의 갯수
# # print(len(colors))

# # # print(colors[7])
# # print(colors[-1])

# # 리스트 슬라이싱
# # colors = ['blue', 'red', 'gray', 'black', 'yellow', 'orange']

# # colors_2 = colors[:]

# # colors_2.pop()

# # print(colors)
# # print(colors_2)

# # print(colors[1:5])
# # print(colors[:4])
# # print(colors[2:])

# # print(colors[-5:])

# # scores = [88,100,96,43,65,78]
# # scores.sort(reverse=True)
# # # print(scores)

# # for score in scores:
# #     if score >= 80:
# #         print(score)
# #     else:
# #         print("Fail")

# scores = [88,100,96,43,65,78]

# max_val = max(scores)
# min_val = min(scores)
# sum_val = sum(scores)
# avg_val = sum(scores) / len(scores)
# print(avg_val)

# # sum_values = 0
# # for score in scores:
# #     sum_values += score
# # print(sum_values)