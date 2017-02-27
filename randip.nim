import random, strutils, httpclient, libnotify


proc connect(url: string, timeout: int): tuple[msg: string, ok: bool] =
  try:
    let me  = newNotifyClient("RandIP")
    var client = newHttpClient(timeout = timeout * 1000)
    var resp = client.request(url)
    if "200 OK" == resp.status:
      let fixIp = url & " 200 OK"
      let cstr: string = fixIp
      send_new_notification(me, "RandIP", cstr, "", timeout=3, urgency=NotificationUrgency.Normal)
      echo resp.status
      return (resp.status, true)
    elif "401 Unauthorized" == resp.status:
      let fixIp = url & " 401 Unauthorized"
      let cstr: string = fixIp
      send_new_notification(me, "RandIP", cstr, "", timeout=3, urgency=NotificationUrgency.Normal)
      echo resp.status
      return (resp.status, false)
    elif "500 Internal Server Error" == resp.status:
      let fixIp = url & " 500 Internal Server Error"
      let cstr: string = fixIp
      send_new_notification(me, "RandIP", cstr, "", timeout=3, urgency=NotificationUrgency.Normal)
      echo resp.status
      return (resp.status, false)
    else:
      let cstr: string = resp.status
      echo resp.status
      send_new_notification(me, "RandIP", cstr, "", timeout=3, urgency=NotificationUrgency.Normal)
      client.close()
      return (resp.status, false)
  except:
    echo getCurrentExceptionMsg()
    return ("Unknown error", false)

while true:
   randomize()
   var
      ip0 = random(255) + 1
      ip1 = random(255) + 1
      ip2 = random(255) + 1
      ip3 = random(255) + 1
      ipAddr = (join([$ip0, $ip1, $ip2, $ip3], "."))
      url = "http://" & ipAddr
      timeout = 3
   echo "Connecting to " & ipAddr
   discard connect(url, timeout)
   
