word = input()

n = len(word)
if n % 2 != 0:
    print(word[n // 2])
else:
    print(word[(n // 2) - 1 : (n // 2) + 1])