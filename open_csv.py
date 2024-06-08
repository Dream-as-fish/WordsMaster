import pandas as pd


def switch_file():
    file_name = './resource/热词红宝书 第1版.xlsx'
    return file_name


file = switch_file()


def open_file(file_name):
    df = pd.read_excel(file_name)
    return df


if __name__ == '__main__':
    print(open_file(file))
