import random, strutils, httpclient, libnotify


proc connect(url: string, timeout: int): tuple[msg: string, ok: bool] =
  try:
    let me  = newNotifyClient("RandIP")
    let res = httpclient.request(url,
                                 httpMethod = httpclient.HttpHEAD,
                                 timeout = timeout * 1000)
    if "200 OK" == res.status:
      let fixIp = url & " 200 OK"
      let cstr: string = fixIp
      send_new_notification(me, "RandIP", cstr, "", timeout=0, urgency=NotificationUrgency.Normal)
      echo res.status
      return (res.status, true)
    elif "401 Unauthorized" == res.status:
      let fixIp = url & " 401 Unauthorized"
      let cstr: string = fixIp
      send_new_notification(me, "RandIP", cstr, "", timeout=0, urgency=NotificationUrgency.Normal)
      echo res.status
    else:
      echo res.status
      return (res.status, false)
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
   let res = connect(url, timeout)
