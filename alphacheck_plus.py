# 문자열이 주어지면 숫자, 문자, 기호가 몇개인지 출력하는 함수를 만들어라

def check(input_str):
    char_count = 0
    digit_count = 0
    symbol_count = 0

    for char in input_str:
        if char.isalpha():
            char_count += 1

        elif char.isdigit():
            digit_count += 1

        else:
            symbol_count += 1

    return char_count, digit_count, symbol_count

input_str = '12345621@#$@#$aiden_show'
char_count, digit_count, symbol_count = check(input_str)
print(f'문자 : {char_count}개, 숫자 : {digit_count}개, 기호 : {symbol_count}개')