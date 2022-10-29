def num(a , b):
    try:
        if a < b:
            print(b)
        elif a > b:
            print(a)
        elif a == b:
            print("Числа рівні")
    except Exception as e:
        print(f"Error {e}")


def main():
    try:
        num(int(input("Num_1 -->")) , int(input("Num_2 -->")))

    except Exception as e:
        print(f"Error {e}")
main()