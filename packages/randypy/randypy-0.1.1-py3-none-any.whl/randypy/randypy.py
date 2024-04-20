import random
import string
import uuid
import datetime

def percentage():
  return random.random()

def randyint(min_value, max_value):
  return random.randint(min_value, max_value)

def randyfloat(min_value, max_value):
  return random.uniform(min_value, max_value)

def choice(seq):
  return random.choice(seq)

def shuffle(seq):
  random.shuffle(seq)
  return seq

def string(length):
  characters = string.ascii_letters + string.digits
  string = ''.join(random.choice(characters) for _ in range(length))
  return string

def name():
  first_names = ["John", "Jane", "Michael", "Emily", "David", "Sarah", "Daniel", "Olivia", "Christopher", "Sophia",
    "William", "Elizabeth", "Matthew", "Samantha", "Andrew", "Jessica", "Joseph", "Ashley", "Joshua", "Amanda"]
  last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
    "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson"]
  first_name = random.choice(first_names)
  last_name = random.choice(last_names)
  return f"{first_name} {last_name}"

def email(domain="example.com"):
  username = string(8)
  email = f"{username}@{domain}"
  return email

def password(length=12, include_digits=True, include_special_chars=True):
    password_chars = list(string.ascii_letters)

    if include_digits:
      digits = string.digits
      password_chars.extend(random.choice(digits))
    if include_special_chars:
      special_chars = string.punctuation
      password_chars.extend(random.choice(special_chars))

    random.shuffle(password_chars)
    password = ''.join(password_chars[:length])
    return password

def uuid():
  return str(uuid.uuid4())

def date(start_date, end_date):
  start_date = datetime.strptime(start_date, '%Y-%m-%d')
  end_date = datetime.strptime(end_date, '%Y-%m-%d')
  random_days = random.randint(0, (end_date - start_date).days)
  random_date = start_date + datetime.timedelta(days=random_days)
  return random_date.strftime('%Y-%m-%d')

def color():
  return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))