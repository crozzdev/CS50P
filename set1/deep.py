def answers_the_great_questions(answer: str) -> str:
    if answer in ["42", "forty two", "forty-two"]:
        return "Yes"
    return "No"


def main():
    answer = (
        input(
            "What is the Answer to the Great Question of Life, the Universe, and Everything?\nR: "
        )
        .strip()
        .lower()
    )
    print(answers_the_great_questions(answer))


main()
