import random
left=1
right=1000
number = random.randint(left,right)
print ("Загадано число от 1 до 1000")
predict = random.randint(left,right)
count = 1
while number != predict:   
    a = (left + right) // 2
    count+=1
    predict = random.randint(left,right)
    if a > number:
        right = a
    elif a < number:
        left = a
print('Загаданное число',number)
print('Угадано с',count,'попыток')