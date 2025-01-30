def count(num1, num2):
    count = 0
    while num1 >= 0 or num2 >= 0:
        if num1 == 0 or num2 == 0:
            break

        if num1 < num2:
            num2 = num2-num1
            count += 1
        else:
            num1 -= num2
            count += 1
    return count

count(0,0)

