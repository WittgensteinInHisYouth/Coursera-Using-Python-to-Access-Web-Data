import re


def FindSumRegex(text):
    hand = open(text)
    result = 0
    for line in hand:
        if re.search("[0-9]+", line):
            #print(re.findall("[0-9]+", line))
            for num in re.findall("[0-9]+", line):
                result += int(num)
    return result


if __name__ =="__main__":
    print(FindSumRegex("regex_sum_946756.txt"))