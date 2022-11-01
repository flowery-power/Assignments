def recursive(x):
    dict = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
    }

    num_list = [d for d in x]

    if len(num_list) == 1:
        print(dict[num_list[0]], end="")
        return

    else:
        print(dict[num_list[0]], end=", ")
        num = ''.join([i for i in num_list[1:]])
        return recursive(num)


recursive(input())
