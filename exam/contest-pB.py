#contest-pB

day_list_24 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_list_25 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def count_to_date(count):
    i = 0

    if count > 366:
        count -= 366
        while count > day_list_25[i]:
            count -= day_list_25[i]
            i += 1
        count = max(1, count)

        return (2025, i + 1, count)
    else:
        while count > day_list_24[i]:
            count -= day_list_24[i]
            i += 1
        count = max(1, count)
        return (2024, i + 1, count)

def date_to_count(date):
    month = int(date[:2])
    day = int(date[2:])
    count = 0

    # 計算date是該年第幾天
    for i in range(month - 1):
        count += day_list_24[i]
    count += day

    return count




def check():
    date = input()
    day = int(date[-2:])
    month = int(date[-4:-2])
    year = int(date[:4])

    # Case 0: 不合理的日期
    if month > 12 or day > 31 or day == 0 or month == 0:
        return False

    # Case 1: 2月:閏年&2/29
    if month == 2:
        if day == 29:
            if leap_year(year):
                return True
            else:
                return False
        if day > 28:
            return False

    # Case 2: 8月
    if month == 8:
        return day <= 31

    # Case 3:偶數月(2&8月已排除)
    if month % 2 == 0:
        return day <= 30

    # Case 4: 奇數月
    return day <= 31

def when(): 
    insert = input().split()
    date1 = insert[0]
    num = int(insert[1])
    count = date_to_count(date1) + num

    date_output = count_to_date(count)

    return date_output

def time():
    date = input().split()
    return abs(date_to_count(date[1]) - date_to_count(date[0]))

cmd = input()

if cmd == "check":
    if check():
        print("Yes")
    else:
        print("No")
elif cmd == "when":
    date = when()
    output = ""
    for item in date:
        if item < 10:
            output += "0" + str(item)
        else:
            output += str(item)
    print(output)

else:
    print(time())





