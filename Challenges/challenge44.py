def main() -> None:
    n = int(input())
    set_english = set(map(int, input().split()))

    b = int(input())
    set_french = set(map(int, input().split()))

    print(len(set_english.difference(set_french)))


if __name__ == "__main__":
    main()
