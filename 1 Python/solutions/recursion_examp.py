def countUp(n):
    if n>=1:
        countUp(n - 1)
        print(n)

countUp(5)


from time import sleep
def count_down(num):
    sleep(1)
    print(num)
    if num == 0:
        return True
    return count_down(num - 1)
    
print('blast off in t minus:')
message = 'blast off 🚀' if count_down(5) else ''
print(message)



new_num = 1
num = 7
for i in range(1,num):
    new_num = new_num * i
print(f'from loop: {new_num}')


def fact(num):
    if num <= 1:
        return 1
    else:
        return num * fact(num -1)

print(f'from recursion:  {fact(6)}')