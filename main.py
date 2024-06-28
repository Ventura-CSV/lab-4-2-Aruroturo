def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    total = 0
    for _ in range(5):
        number = int(input("enter a number: "))
        total += number
    print(total)

    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
