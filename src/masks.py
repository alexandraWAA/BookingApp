def get_mask_card_number(card_number: str) -> str:
    """Функцию маскировки номера банковской карты"""
    new_card_number = ""
    number_part1 = ""
    number_part2 = ""
    number_part3 = ""
    card_number_new = card_number.replace(" ", "")

    if 20 >= len(card_number_new) >= 16 and card_number_new.isdigit:
        for el in card_number_new[:4]:
            number_part1 += el
        new_card_number += number_part1 + " "
        for el in card_number_new[4:-10]:
            number_part2 += el
        new_card_number += number_part2 + "**" + " " + "****" + " "
        for el in card_number_new[-4:]:
            number_part3 += el
        new_card_number += number_part3
        return new_card_number
    else:
        return "Введите корректный номер карты"


def get_mask_account(card_number: str) -> str:
    """Функцию маскировки номера банковского счета"""
    # new_card_number = ""
    number_part = ""
    if 17 <= len(card_number) <= 25:
        for el in card_number[-4:]:
            number_part += el
        new_card_number = "**" + number_part
        return new_card_number
    else:
        print("Введите номер счета корректной длины")
