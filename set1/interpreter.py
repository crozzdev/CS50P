def math_intepreter(expression: str) -> str:

    result = 0.0
    first_operand, operation, second_operand = expression.split(" ")

    match operation:
        case "+":
            result = float(first_operand) + float(second_operand)
        case "-":
            result = float(first_operand) - float(second_operand)
        case "*":
            result = float(first_operand) * float(second_operand)
        case "/":
            result = float(first_operand) / float(second_operand)
        case _:
            return "Please enter a valid operator"

    return f"{result:.1f}"


def main():
    expression = input("Expression: ")
    print(math_intepreter(expression))


main()
