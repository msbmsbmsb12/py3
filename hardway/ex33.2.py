def my_while(loops, step):
    i = 0
    numbers = []
    while i < loops:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += step
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    
    print("The numbers: ")
    for num in numbers:
        print(num)

my_while(6,1)