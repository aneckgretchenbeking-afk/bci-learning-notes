def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False

    if not s[:2].isalpha():
        return False

    if not s.isalnum():
        return False

    # 检查数字规则
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == "0":
                return False

            return s[i:].isdigit()

    return True


main()
