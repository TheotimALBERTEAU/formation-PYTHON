def Luhn(num : str) -> bool:
    final_somme = 0
    reversed_num = num[::-1].replace(" ", "")
    for i, number in enumerate(reversed_num):
        number = int(number)
        if i % 2 != 0:
            number *= 2
            if number >= 10:
                number -= 9
        final_somme += number
    return final_somme % 10 == 0