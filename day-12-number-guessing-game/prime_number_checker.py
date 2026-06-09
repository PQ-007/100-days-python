def is_prime(num):
    f = 0
    for i in range(1, num + 1):
        if num % i == 0:
            f += 1
    if f == 2:     return True
    else:    return False
    
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")