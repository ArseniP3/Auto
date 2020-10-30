import random
#20. Найти количество четных чисел в массиве.

def arr20():
    arr = list()
    for i in range (100):
        arr.append(random.randint(0,1000))
    print(arr)
    count = 0
    for i in arr:
        if i % 2 == 0:
            count = count + 1
    print('Количество четных чисел в массиве равно :', count)
arr20()

#21. Найти количество чисел в массиве, которые делятся на 3, но не делятся на 7.

def arr21():
    arr = list()
    for i in range(100):
        arr.append(random.randint(0, 1000))
    print(arr)
    count = 0
    for i in arr:
        if i % 3 == 0 and i % 7 != 0:
            count = count + 1
    print('Количество чисел в массиве которые делятся на 3 и не делятся на 7 :', count)
arr21()

#22. Определите, каких чисел в массиве больше: которые делятся на первый элемент массива или которые делятся на последний элемент массива.

def arr22():
    arr = list()
    for i in range(50):
        arr.append(random.randint(1, 15))
    print(arr)
    countOfFirstElement = 0
    x = arr[0]
    y = arr[-1]
    for i in arr:
        if i % x == 0:
            countOfFirstElement = countOfFirstElement + 1
    countOfLastElement = 0
    for i in arr:
        if i % y ==0:
            countOfLastElement = countOfLastElement + 1
    if countOfFirstElement>countOfLastElement:
        result = countOfFirstElement - countOfLastElement
        print('Элементов, которые делятся на первый элемент массива больше на',result)
    elif countOfFirstElement == countOfLastElement:
        print('Элементов, которые делятся на последний аргумент столько же, сколько и элементов которые делятся на первый аргумент ')
    else:
        result = countOfLastElement-countOfFirstElement
        print('Элементов, которые делятся на последний элемент больше на', result)
arr22()

#23. Найдите сумму и произведение элементов массива.

def arr23():
    arr = list()
    for i in range(11):
        arr.append(random.randint(1, 15))
    print(arr)

    composition = 1
    sum = 0
    for i in arr:
        sum = sum + i
        composition = composition*i
    print('Сумма всех элементов массива: ', sum, 'Произведение всех элементов массива равно', composition)
arr23()

#24. Найдите сумму четных чисел массива.
def arr24():
    arr = []
    for i in range(100):
        arr.append(random.randint(1,100))
    count = 0
    for i in arr:
        if i % 2 == 0:
            count = count + 1
    print('Количество чётных элементов в массиве равно: ', count)
arr24()

#25. Найдите сумму нечетных чисел массива, которые не превосходят 11.
def arr25():
    arr = []
    for i in range (100):
        arr.append(random.randint(0,100))

    sum = 0
    for i in arr:
        if i % 2 !=0 and i < 11:
            sum = sum + i
    print ('Сумма нечетных чисел, которые не превосходят 11 равна:', sum)
arr25()

#26. Найдите сумму чисел массива, которые расположены до первого четного числа массива. Если четных чисел в массиве нет, то найти сумму всех чисел за исключением крайних.
def arr26():
    arr = []
    for i in range (100):
        arr.append(random.randint(51,101))
    print(arr)
    count = 0
    sum= 0
    for i in arr:
        if i % 2 == 0:
            count = count + 1

    if count >= 1:
        for i in arr:
            if i % 2 == 0:
                break
            else:
                sum = sum+i
        print('Сумма элементов, которые расположены до первого четного элемента равна:',sum)
    else:
        arr.pop([0])
        arr.append([-1])
        for i in arr:
            sum=sum+i
        print('В массиве нет четных элементов. Сумма всех элементов массива кроме первого и последнего равна', sum)
arr26()

#27. Найдите сумму чисел массива, которые стоят на четных местах.
def arr27():
    arr = []
    for i in range(100):
        arr.append(random.randint(0,100))
    sum = 0
    for i in arr:
        if i !=0 or arr[i] % 2 == 0:
           sum = sum+i
    print('Сумма чисел массива, которые стоят на четных местах массива равна',sum)
arr27()

#28. Найдите сумму чисел массива, которые стоят на нечетных местах и при этом превосходят сумму крайних элементов массива.