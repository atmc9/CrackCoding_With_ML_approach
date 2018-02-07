import LCSSeq

# Test1 - expected result - 'alll'
print(LCSSeq.longest_common_sub_sequence('lalall', 'alllal'))

# Test2 - expected result - 'apm'
print(LCSSeq.longest_common_sub_sequence('mappam', 'lalpm'))

# Test3 - expected result - 'uah'
print(LCSSeq.longest_common_sub_sequence('huah', 'uah'))

# Test4 - expected result - ''
print(LCSSeq.longest_common_sub_sequence('', 'trr'))

# Test5 - expected result - 'blah'
print(LCSSeq.longest_common_sub_sequence('blah', 'blahblah'))
