start = int(input("Enter the beginning of range: "))
end = int(input("Enter the end of range: "))
for i in range(start, end + 1):
    print(i, end=" ")
print()
for i in range(end, start -1, -1):
    print(i, end=" ")
print()
for i in range(start, end + 1):
    if i % 7 == 0:
        print(i, end=" ")
print()
count = 0
for i in range(start, end + 1):
    if i % 5 ==0:
        count += 1
        print(count, end=" ")