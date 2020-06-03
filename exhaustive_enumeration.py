target = int(input('Enter an integer: '))
answer = 0

while answer**2 < target:
    answer += 1

if answer**2 == target:
    print(f'Root square of {target} is {answer}')
else:
    print(f'{target} does not have root square')
