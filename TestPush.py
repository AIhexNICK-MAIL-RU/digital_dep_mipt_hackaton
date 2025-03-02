import re

temp = re.compile("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}")
with open("enron_3000.csv", "r") as mail_file:
    res = mail_file.read()

mails = re.findall(temp, res)

s = set(mails)
list_of_mail = list()

for m in s:
    count = mails.count(m)
    list_of_mail.append([m, count])

list_of_mail.sort(key = lambda x: x[1] , reverse=True)
del list_of_mail[20::]


for _ in list_of_mail:
    print (_[0], _[1])