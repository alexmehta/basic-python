import requests, time, threading, _thread

from bs4 import BeautifulSoup

x = 1


def main():
    page = requests.get(
        "https://weather.com/en-IN/weather/tenday/l/193ae648ec30e1c1f5cdb2e4e7db1b02450d40f5318c227367737eb47c09ea06")
    content = page.content
    soup = BeautifulSoup(content, "html.parser")
    l = []
    table = soup.find_all("table", {"class": "twc-table"})
    for items in table:
        for i in range(len(items.find_all("tr")) - 1):
            d = {}
            try:
                d["day"] = items.find_all("span", {"class": "date-time"})[i].text
                d["date"] = items.find_all("span", {"class": "day-detail"})[i].text
                d["desc"] = items.find_all("td", {"class": "description"})[i].text
                d["temp"] = items.find_all("td", {"class": "temp"})[i].text
                d["precip"] = items.find_all("td", {"class": "precip"})[i].text
                d["wind"] = items.find_all("td", {"class": "wind"})[i].text
                d["humidity"] = items.find_all("td", {"class": "humidity"})[i].text
            except:
                d["day"] = "None"
                d["date"] = "None"
                d["desc"] = "None"
                d["temp"] = "None"
                d["precip"] = "None"
                d["wind"] = "None"
                d["humidity"] = "None"
            # print("")
            l.append(d)

    import pandas

    df = pandas.DataFrame(l)
    print(df)
    df.to_csv("output.csv")


def email():
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders

    email_user = 'orangespock@gmail.com'
    email_password = '*password taken out*'
    email_send = 'orangespock@gmail.com'

    subject = 'Weather for Today'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = 'This is your weather today'
    msg.attach(MIMEText(body, 'plain'))

    filename = 'output.csv'
    attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)

    server.sendmail(email_user, email_send, text)
    server.quit()
    time.sleep(86400)


while x is 1:
    main()
    email()
