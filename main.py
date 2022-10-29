def num(a):
    try:

    except Exception as e:
        print(f"Error {e}")


def main():
    try:
        num(5)
    except Exception as e:
        print(f"Error {e}")
main()