def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False

    if not s[0:2].isalpha():
        return False

    if not s.isalnum():
        return False

    for i in s:
        if i.isdigit():
            if i=='0':
                return False
            break

    for i in range(len(s)):
        if s[i].isdigit():
            if s[i:].isdigit():
                return  True
            else:
                return False


    return True


main()
