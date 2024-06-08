import pandas as pd


def switch_file():
    file_name = './words.csv'
    return file_name


file = switch_file()


def open_file(file_name):
    df = pd.read_csv(file_name)
    return df


if __name__ == '__main__':
    print(open_file(file))
