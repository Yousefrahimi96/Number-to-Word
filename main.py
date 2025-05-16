from constans import UNDER_20, TENS, ABOVE_100


def num_to_word(num: int) -> str:
    if num < 20:
        return UNDER_20[num]
    
    if num < 100:
        return TENS[num // 10 -2] + ' ' + (' ' if num // 10 ==0 else UNDER_20[num % 10])  
    pivot = max([key for key in ABOVE_100 if key <= num])
    
    p1 = num_to_word(num // pivot)
    p2 = ABOVE_100[pivot]
    if num % pivot == 0:
        return f'{p1} {p2}'
    
    return f'{p1} {p2} {num_to_word(num % pivot)}'

if __name__ == '__main__':
    num = int(input('Please Enter a number: '))
    if num >= 0 and num <= 999999999999:
        print(num_to_word(num))
    else:
        print('Number is out of range')
    