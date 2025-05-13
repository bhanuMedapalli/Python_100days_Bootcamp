storage_number =0
for iterate_number in range(1, 101):
    if iterate_number %3 == 0 and iterate_number %5 ==0 :
        print("FizzBuzz")
    elif iterate_number %3 == 0:
        print("Fizz")
    elif iterate_number %5 == 0:
        print("Buzz")
    else:
        print(iterate_number)
