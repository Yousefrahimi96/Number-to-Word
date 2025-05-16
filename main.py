
from constans import UNDER_20, TENS, ABOVE_100

def num_to_word(num: int) -> str:
    if num < 20:
        return UNDER_20[num]
    
    elif num < 100:
        return TENS[num // 10 -2] + ' ' + (' ' if num // 10 ==0 else UNDER_20[num % 10])