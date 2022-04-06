import requests

# route 1 -- ping
def call_ping_route():
  r = requests.get('127.0.0.1:5000/ping')# make the request
  return r

# route 2 -- random word
def call_random_word_route():
  r = requests.get('127.0.0.1:5000/word') # make the request
  return r

# route 3 -- string count
def call_string_count():
  r = requests.post('127.0.0.1:5000/string_count', json = 'example_string') # make the request
  return r

route_callers = [
  call_ping_route
  call_random_word_route
  call_string_count
  ]

for call_route in route_callers:
  r = call_route()
  r.raise_for_status() # first, check r for errors
  data = r.json()
  print(data) # print the response
