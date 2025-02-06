def main():
    n1, n2 = 0, 1
    count = 15
   
    print(n1, n2)  # printing 0 and 5

    for i in range(2, count):  # loop starts from 2 because 0 and 5 are already printed
        n3 = n1 + n2
        print(n3, end=' ')
        n1 = n2
        n2 = n3

if __name__ == "__main__":
    main()

