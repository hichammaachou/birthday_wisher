import pandas
import datetime
import smtplib
import random

##################### Extra Hard Starting Project ######################
rand_int = random.randint(1,3)
my_email = "maachouhicham093@gmail.com"
password = "hwoqjdrowjrnxclz"
now = datetime.datetime.now()
# 1. Update the birthdays.csv
birthdays = pandas.read_csv('birthdays.csv').to_dict(orient='records')
for i in birthdays:
    receiver = i['email']
    date = datetime.date(year=i['year'],month=i['month'],day=i['day'])
    if now.month == date.month and now.day == date.day:
        with open(f'letter_templates\\letter_{rand_int}.txt') as file:
            data = file.readlines()
            data[0] = data[0].replace('[NAME]',f'{i["name"]}')
        with open('letter_templates\\sent_letter.txt','w')  as file: 
            for i in data:

                file.write(i)
        with open('letter_templates\sent_letter.txt') as file:
            letter = file.read()     
        connection = smtplib.SMTP('smtp.gmail.com',587)
        connection.starttls()    
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,to_addrs=receiver,msg=f'Subject: Happy birthday\n\n{letter}')
        connection.close()
# 2. Check if today matches a birthday in the birthdays.csv



        
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.






