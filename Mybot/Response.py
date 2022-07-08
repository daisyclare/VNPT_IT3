from datetime import datetime

def sample_response(input):
  user_mess = str(input).lower()

  if user_mess in ("Xin chào", "hello", "ok","Chào bot"):
    return "Hello :v"
  if user_mess in ("time", "time?"):
    now = "Hôm nay: " + datetime.now().strftime("%d-%m-%y, %H:%M:%S")
    return str(now)
  
  return "Welcome"