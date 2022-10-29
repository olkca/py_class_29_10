def pryamokutnyk(a,b):
    for i in range(0, a):
        for j in range(0,b):
            print("*", end = " ")
        print()
    print()


def main():
    pryamokutnyk(int(input("Height -->")),int(input("Width -->")))

main()