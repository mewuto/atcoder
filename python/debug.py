import random
import os
import filecmp


def generate():
    with open("input.txt", mode="w") as f:
        a = random.randint(1, 100)
        f.write(f"{a}\n")
        # 改行した時のランダム生成
        b = random.randint(1, 100)
        c = random.randint(1, 100)
        f.write(f"{b} {c}\n")

        # 英字のランダム生成
        s = []
        length = random.randint(1, 100)
        for i in range(length):
            s.append(chr(random.randint(ord("a"), ord("z"))))
        s = "".join(s)
        f.write(f"{s}\n")
    return


def is_same():
    os.system("python3 main.py < input.txt > out1.txt")
    os.system("python3 sample.py  < input.txt > out2.txt")
    if filecmp.cmp("out1.txt", "out2.txt"):
        return True
    else:
        return False


def main():
    while True:
        generate()
        if not is_same():
            break


main()
