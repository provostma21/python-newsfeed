from datetime import datetime

# Sets the date format
def format_date(date):
  return date.strftime('%m/%d/%y')

def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

# Adds plural filter to make a word plural if there are multiple of them
def format_plural(amount, word):
  if amount != 1:
    return word + 's'

  return word
