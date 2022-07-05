from optparse import TitledHelpFormatter
from wsgiref import headers
from bs4 import BeautifulSoup
from matplotlib.pyplot import title
import requests
import time
import datetime
import smtplib
import html5lib

URL = 'https://www.amazon.com/Total-Wireless-Apple-iPhone-Generation/dp/B09VY71F9M/?_encoding=UTF8&pd_rd_w=6KYGq&content-id=amzn1.sym.7f957896-9457-4ac3-8c2b-58f2b6be2857&pf_rd_p=7f957896-9457-4ac3-8c2b-58f2b6be2857&pf_rd_r=0S5AZPY420JTK71WK3PX&pd_rd_wg=s7HI0&pd_rd_r=8f80be5f-8d0d-48ee-bcb4-48a3c5f96223&ref_=pd_gw_exports_top_sellers_unrec'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36", "X-Amzn-Trace-Id": "Root=1-62ba6baa-420274ac51dc2bf4238c3fec"}
page = requests.get(URL, headers=headers)
soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
title = soup2.find(id='productTitle').get_text()
print(title)