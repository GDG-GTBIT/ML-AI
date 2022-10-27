import requests
import smtplib
from datetime import datetime


my_email = #ENTER YOUR EMAIL
password = #ENTER YOUR PASSWORD


API_KEY = #GET THE API KEY
URL="https://api.nasa.gov/planetary/apod"

today_date = datetime.now().strftime("%Y-%m-%d")


params={
    "date":today_date,
    "api_key": API_KEY
}




response = requests.get(URL, params=params)

data = response.json()

title = data["title"]

print(data)
print(title)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,to_addrs= #TO ADDRESS ,msg=f"Subject:{title}t\n\n "
                            f"HDurl:{data['hdurl']}.\n\n"
                            f"Explanation:{data['explanation']}.\n\n"
                            f"Service_version:{data['service_version']}.\n\n  "
                            f"Date:{today_date}."
                        )