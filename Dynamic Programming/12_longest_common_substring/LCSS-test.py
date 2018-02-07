import LCSS

# Test1 - expected result - 'esh'
print(LCSS.Long_Common_Sub_String('anvesh', 'mahesh'))

# Test2 - expected result - 'abcd'
print(LCSS.Long_Common_Sub_String('abcdxyz', 'xyzabcd'))

# Test3 - expected result - 'abcdez'
print(LCSS.Long_Common_Sub_String('zxabcdezy', 'yzabcdezx'))


# Test4 - Edge case 1
print(LCSS.Long_Common_Sub_String('', ''))

# Test5 - Edge case 2
print(LCSS.Long_Common_Sub_String('', str()))
