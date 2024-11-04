# TODO Напишите функцию find_common_participants
def find_common_participants(list_1, list_2, separator = ","):
    new_list_1 = ""
    new_list_2 = ""

    for i in range(len(list_1)):
        if list_1[i] != separator:
            new_list_1 += list_1[i]
        else: new_list_1 += " "
    list_1 = new_list_1.split()
    for i in range(len(list_2)):
        if list_2[i] != separator:
            new_list_2 += list_2[i]
        else: new_list_2 += " "
    list_2 = new_list_2.split()

    both_list = set(list_1).intersection(list_2)
    sort_list = list(sorted(both_list))
    return sort_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

a = "|"
print(find_common_participants(participants_first_group, participants_second_group, a))
# TODO Провеьте работу функции с разделителем отличным от запятой
