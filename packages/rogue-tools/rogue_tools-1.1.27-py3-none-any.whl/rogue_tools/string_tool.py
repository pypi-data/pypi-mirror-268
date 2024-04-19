import difflib
import random
# 相似度比较

def diff(str1,str2):
    seq   = difflib.SequenceMatcher(None,str1,str2)
    ratio = seq.ratio()
    return ratio

def rnd_str(length,include_lower=True,include_upper=True,include_number=True,include_symbol=False):
    add_str = ''
    if include_lower:
        add_str+='qwertyuiopasdfghjklzxcvbnm'
    if include_upper:
        add_str+='QWERTYUIOPASDFGHJKLZXCVBNM'
    if include_number:
        add_str+='1234567890'
    if include_symbol:
        add_str+='~!@#$%^&*()_+[]\;,./|:"<>?'
    return ''.join(random.sample(add_str, length))