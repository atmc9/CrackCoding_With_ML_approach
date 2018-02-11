import wildcardmatch

# Test 1 expected outcome false
print(wildcardmatch.wildcard_match('aab', 'c*a*b'))

# Test 2 expected outcome false
print(wildcardmatch.wildcard_match('aaa', 'aa'))

# Test 3 expected outcome true
print(wildcardmatch.wildcard_match('aab', 'aa**?'))


# edge cases
# Test 1 expected outcome true
print(wildcardmatch.wildcard_match('', ''))

# Test 2 expected outcome false
print(wildcardmatch.wildcard_match('', '?'))

# Test 3 expected outcome true
print(wildcardmatch.wildcard_match('', '*'))
