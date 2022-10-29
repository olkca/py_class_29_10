def faktorial(a):
    try:
        n = 1
        for i in range(2, a+1):
            n=n*i
        print(n)
    except Exception as e:
        print(f"Error {e}")


def main():
    try:
        faktorial(int(input("Num -->")))
    except Exception as e:
        print(f"Error {e}")
main()