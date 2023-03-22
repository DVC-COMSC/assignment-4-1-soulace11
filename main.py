def main():
    ##################################################
    # Comlete your code here
    ##################################################
    number = int(input('Enter the number: '))


if __name__ == '__main__':
    main()

num = int(input("Enter a number greater than 1: "))
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
if is_prime and num > 1:
    print("True")
else:
    print("False")