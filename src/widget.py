from .masks import get_mask_account, get_mask_card_number

# card_number = str(input())


def mask_account_card(card_number: str) -> str:
    """Функция обработки информации о картах и счетах"""
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # num = ""
    num_new = ""

    cn = card_number.split(" ")
    if "счет" in cn[0].lower():
        num = "".join(cn[1:])
        for el in num:
            if el == "" or el == " " or el is None or el not in numbers:
                print("Введите корректный номер счета")
            else:
                num_new += el
        b_number = get_mask_account(num_new)
        if b_number is None:
            new_card = "Введите корректный номер счета"
        else:
            new_card = cn[0] + " " + b_number
    elif "visa" in cn[0].lower() or "visa" in cn[1].lower():
        num = "".join(cn[2:])
        for el in num:
            if el == "" or el == " " or el is None or el not in numbers:
                print("Введите корректный номер карты")
            else:
                num_new += el

        b_number = get_mask_card_number(num_new)

        if b_number is None:
            new_card = "Введите корректный номер карты"
        else:
            cn = " ".join(cn[:2])
            new_card = cn + " " + b_number
    elif "maestro" in cn[0].lower() or "mastercard" in cn[0].lower():
        num = "".join(cn[1:])
        for el in num:
            if el == "" or el == " " or el is None or el not in numbers:
                print("Введите корректный номер карты")
            else:
                num_new += el
        b_number = get_mask_card_number(num_new)

        if b_number is None:
            new_card = "Введите корректный номер карты"
        else:
            new_card = cn[0] + " " + b_number
        return new_card


def get_date(d: str) -> str:
    """Функция сортировки по дате"""
    date_time = d.split("T")[0]
    if date_time is None or date_time == "" or date_time == " ":
        date_time = "Введите корректные данные"
    else:
        date_time = f"{date_time[-2:]}.{date_time[5:7]}.{date_time[:4]}"
    return date_time
