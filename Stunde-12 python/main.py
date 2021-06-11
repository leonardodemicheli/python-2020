from calculator import Calculator
print('hello welcome to my Calculator')
print('Press Enter to type your Calculation')
answer_a = int(input('type your first number here and press Enter ->'))
operator = input('type your operator here and press Enter ->')
while operator != '+' and operator != '-' and operator != '*' and operator != '/' and operator != '%':
        print('operator was not found')
        operator = input('type your operator here and press Enter ->')

answer_b = int(input('type your second number here and press Enter ->'))

calculate = Calculator(answer_a, answer_b)

if operator == '+':
    print(answer_a, operator, answer_b, '=', calculate.add())

elif operator == '-':
    print(answer_a, operator, answer_b, '=', calculate.sub())

elif operator == '*':
    print(answer_a, operator, answer_b, '=', calculate.mul())

elif operator == '/':
    print(answer_a, operator, answer_b, '=', calculate.div())

elif operator == '%':
    print(answer_a, operator, answer_b, '=', calculate.mod())

else:
    print('operator incorrect')