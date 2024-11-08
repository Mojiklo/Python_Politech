# TODO Напишите функцию find_common_participants
def find_common_participants(list_1, list_2, separator=","):

    list_1 = list_1.split(separator)

    list_2 = list_2.split(separator)

    both_list = set(list_1).intersection(list_2)
    sort_list = sorted(both_list)
    return sort_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(
    participants_first_group, participants_second_group, "|"))

# TODO Провеьте работу функции с разделителем отличным от запятой
