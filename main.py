from math import sqrt
def num(a):
    try:
        prime = True

        i = 2
        while i <= sqrt(a):
            if a % i == 0:
                prime = False
                break
            i += 1

        if prime:
            print("Просте")
        else:
            print("Складне")
    except Exception as e:
        print(f"Error {e}")


def main():
    try:
        num(int(input("Num -->")))
    except Exception as e:
        print(f"Error {e}")
main()