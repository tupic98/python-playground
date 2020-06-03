target = int(input('Enter an integer: '))
epsilon = 0.01
step = epsilon**2
answer = 0.0

while abs(answer**2 - target) >= epsilon and answer <= target:
    answer += step

if abs(answer**2 - target) >= epsilon:
    print(f'No root square found for {target}')
else:
    print(f'Root square of {target} is {answer}')
