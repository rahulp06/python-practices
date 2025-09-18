""" if salary < 500000 -- 0 TDS
TDS Will be applicable if salary is more than 5lpa
then
0-3 -- TDS --0
3-6 -- TDS is 5% -- 300000 : 15000
6-9 -- TDS is 10% -- 300000 : 30000
9-15 -- TDS is 15%      600000: 90000
                        300000: 90000
more than 15lpa tds is 30%"""

salary = int(input())
if salary <= 500000:
    tds = 0
    print(f"TDS = {tds}% You need not to pay tax.")
elif  salary <= 600000:
    tds = 5
    print(f"TDS = {tds}%. You need to pay tax of {(salary * tds) / 100}")
elif  salary <= 900000:
    tds = 10
    print(f"TDS = {tds}%. You need to pay tax of {(salary * tds) / 100}")
elif salary <= 1500000:
    tds = 15
    print(f"TDS = {tds}%. You need to pay tax of {(salary * tds) / 100}")
else:
    tds = 30
    print(f"TDS = {tds}%. You need to pay tax of {(salary * tds) / 100}")