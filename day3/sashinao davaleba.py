#piroba
#იუზერს input-ით შემოაქვს წინადადება.
# შექმენი ცარიელი სტრინგი " " 
# for ციკლით გადაუარე ინფუთით შემოტანილ წინადადებას და შექმნილ 
# ცარიელ სტრინგს მიუმატე ( + ) ყველა სიმბოლო რომელიც  არ უდრის "i"-ს 




# users_sentence = "i you like reading"
# temporary_string = " "
# for x in users_sentence:
#     if x != "i":
#         temporary_string += x

# count = 0
# for x in users_sentence:
#     if x == "i":
#         count += 1
# print(count)


#shevqmnat sia (cifrebisgan) davprintot elementebis jami
#2) shevqmnat sia cifrebisgan da gadavuarot ciklit, luwebi calke davprintot kentebi calke.

user = "this month is january"
temporary_string = " "
count = 0
for x in user:
    if x != "i":
        temporary_string += x
        count += 1
print(count)
print(temporary_string)


# x = [1, 2, 3, 4, 5]
# print(len(x))
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for a in x:
#     if a%2 == 1:
#         print(a)
# new_number_list = []
# for a in x:
#     if a%2 != 1:
#         new_number_list.append(a)
# print(new_number_list)