from datetime import datetime


def format_date(date):
  return date.strftime('%m/%d/%y')

print(format_date(datetime.now()))

def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

print(format_url('http://google.com/test/'))
print(format_url('https://www.google.com?q=test'))