start = int(input("Enter the beginning of range: "))
end = int(input("Enter the end of range: "))
for i in range(start, end + 1):
    if i % 7 == 0:
        print(i)