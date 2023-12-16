#stepik_4.2_leap_year
a = int(input())
if (a%4==0 and a%100!=0) or a%400==0:
    print("YES")
else:
    print("NO")