#1 zadanie
def invert(lst):
    result = []
    for num in lst:
        result.append(-num)
    return result 

#2 zadanie
def past(h, m, s):
    return  (h * 3600000 + m * 60000 + s * 1000)

#3 zadanie
def count_sheeps(Sheeps):
    return len([sheep for sheep in Sheeps if sheep])

#4 zadanie 
def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    else:
        return n * m

#5 zadanie
def maps(a):
    result = []
    for num in a:
        result.append(num * 2)
    return result

#6 zadanie
def descending_order(num):
    counter = 0
    arr = list(str(num))
    for i in arr:
        arr[counter]= int(i)
        counter += 1
    arr.sort()
    arr = list(reversed(arr))
    ans = ""
    for i in arr:
        ans += str(i)
    return int(ans)

#7 zadanie 
def greet():
    return "hello world!"

#8 zadanie
def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 !=0:
        return True
    elif flower1 % 2 != 0 and flower2 % 2 == 0:
        return True
    else:
        return False

#9 zadanie 
def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result

#10 zadanie 
