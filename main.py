import random

from open_csv import open_file


def rand_number(len_of_file):
    rand_num = random.randint(0, len_of_file - 1)
    return rand_num


def main():
    df = open_file('./resource/考研英语大纲词汇5500.xlsx')

    while True:
        word_number = rand_number(len(df))
        choose_word = df.loc[word_number]
        print(choose_word)

        whether = input("输入Enter打印下一个单词（输入q退出）：").strip().lower()
        if whether.strip().lower() == 'q':
            break


if __name__ == '__main__':
    main()
