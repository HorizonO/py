def leap_year_or_not(year):
    # 世纪闰年:能被400整除的为世纪闰年。
    # 普通闰年:能被4整除但不能被100整除的年份为普通闰年。
    # 闰年共有366天,其他年只有365天。

    if int(year) % 400 == 0:
        return True
    elif int(year) % 100 != 0 and int(year) % 4 == 0:
        return True
    else:
        return False


def calculate_days_of_year(year):
    leap = leap_year_or_not(year)
    if leap:
        days = 366
        run = "是"
    else:
        days = 365
        run = "不是"
    print("{}年{}闰年，有{}天。".format(year, run, days))


if __name__ == "__main__":
    print("输入年份:")
    n = input()
    calculate_days_of_year(n)