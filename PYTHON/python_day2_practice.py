s = "hello world"
vowels = "aeiouAEIOU"
count = 0

for ch in s:
    if ch in vowels:
        count += 1

print("Vowel count:", count)


for i in range(1, 51):
    if i % 3 == 0:
        continue
    print(i)



i = 1
while i <= 10:
    print(i)
    i += 1


for i in range(1, 20):
    if i == 8:
        break
    print(i)


squares = [x*x for x in range(1, 11)]
print(squares)
