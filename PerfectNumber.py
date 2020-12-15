def perfectNumber(num):
    summ = 0
    num = int(num)
  
    for divisor in range(1,num):
        if num % divisor == 0:
            summ += divisor

    if num == summ:
        return "Perfect Number"
    else: 
        return "It is not a Perfect Number"


if '__main__' == __name__:
    print("Input a number: ")
    num = input()
    print(perfectNumber(num))