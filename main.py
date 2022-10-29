def pryamokutnyk(a,b):
    try:
        for i in range(0, a):
            for j in range(0,b):
                print("*", end = " ")
            print()
        print()
    except Exception as e:
        print(f"Error {e}")


def main():
    try:
        pryamokutnyk(int(input("Height -->")),int(input("Width -->")))
    except Exception as e:
        print(f"Error {e}")
main()