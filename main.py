def num(a):
    try:
        if a < 0:
            return False
        elif a > 0:
            return True
    except Exception as e:
        print(f"Error {e}")


def main():
    try:
        r = num(int(input("Num -->")))
        print(r)
    except Exception as e:
        print(f"Error {e}")
main()