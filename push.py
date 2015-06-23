import httplib, urllib
conn = httplib.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": "a3EMhuqmqmV7CGHGtXECprEJbARHp2",
    "user": "FGqYMSRmzXF1e85yFO10gozXL314YO",
    "message": "hello world",
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()
