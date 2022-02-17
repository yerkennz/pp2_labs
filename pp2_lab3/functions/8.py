def spy_game(nums):
    v = '!'
    for x in nums:
        if x == '0' or x == '7':
            v += x
    if '007' in v[1:]:
        return True
    else:
        return False

l = input()
print(spy_game(l))