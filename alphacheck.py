def check(target_str):
    al_count = 0
    dg_count = 0


    for i in target_str:
        if i.isalpha():
            al_count += 1
        
        if i.isdigit():
            dg_count += 1

    a = len(target_str) - al_count - dg_count

    return f'문자 : {al_count}개, 숫자 : {dg_count}개, 기호 : {a}개'

print(check('12345621@#$@#$aiden_show'))