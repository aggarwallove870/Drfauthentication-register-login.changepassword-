from email import message
from urllib import response
import requests
import random
from django.conf import settings


def send_otp(mobile_no,otp):
    API_key= '62b99f2a-1df2-11ed-9c12-0200cd936042'
    url=f'https://2factor.in/API/V1/{API_key}/SMS/{mobile_no}/{otp}'
    response=requests.get(url)
    return True

# def send_email():
#     print("email sent")
# send_email("subject","messages","loveaggarwal179@gmail.com","loveaggarwal@snakescript.com")
