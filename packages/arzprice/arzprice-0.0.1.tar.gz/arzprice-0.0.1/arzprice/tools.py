def p_to_e_int(number_in_persian):
    english_number = ''
    for char in number_in_persian:
        if char.isdigit():
            english_number += char
    return int(english_number)
def p_to_e_str(number_in_persian):
    persian_to_english = {
    '۰': '0', '۱': '1', '۲': '2', '۳': '3', '۴': '4',
    '۵': '5', '۶': '6', '۷': '7', '۸': '8', '۹': '9'}
    english_number = ''
    for digit in number_in_persian:
        if digit in persian_to_english:
            english_number += persian_to_english[digit]
        else:
            english_number += digit
    return english_number