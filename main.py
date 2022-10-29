def num(a):
    try:
        return a*a*a
    except Exception as e:
        print(f"Error {e}")


def main():
    try:
        r = num(int(input("Num -->")))
        print(r)
    except Exception as e:
        print(f"Error {e}")
main()