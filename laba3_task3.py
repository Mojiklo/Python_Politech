# TODO  Напишите функцию count_letters

def count_letters(text):
    lower_text = text.lower()
    letter_counts = {}
    for letter in lower_text:
        if letter.isalpha():
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    return letter_counts

# TODO Напишите функцию calculate_frequency


def calculate_frequency(letter):
    letter_frequencies = {}
    total = sum(letter.values())

    for letter, count in letter.items():
        letter_frequencies[letter] = count / total

    return letter_frequencies


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

lower_main_str = main_str.lower()


# TODO Распечатайте в столбик букву и её частоту в тексте

letter_counts = count_letters(main_str)
frequency = calculate_frequency(letter_counts)


for letter, count in frequency.items():
    print(f"{letter}: {count:.2f}")
