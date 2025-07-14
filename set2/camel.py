def convert_camelCase_to_snake_case(name: str) -> str:
    converted_name_list = []
    for char in name:
        if char.isupper():
            converted_name_list.append("_")
            converted_name_list.append(char.lower())
        else:
            converted_name_list.append(char)

    # print(f"the converted name list is: {converted_name_list}")

    return "".join(converted_name_list)


def main():
    camel_case = input("camelCase: ")
    snake_case = convert_camelCase_to_snake_case(camel_case)

    print(f"snake_case: {snake_case}")


main()
