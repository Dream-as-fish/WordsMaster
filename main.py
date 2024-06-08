from open_csv import open_file


def main():
    df = open_file('words.csv')
    print(df)


if __name__ == '__main__':
    main()
