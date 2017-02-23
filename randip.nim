import random, strutils, httpclient

proc connect(url: string, timeout: int): tuple[msg: string, ok: bool] =
  try:
    let res = httpclient.request(url,
                                 httpMethod = httpclient.HttpHEAD,
                                 timeout = timeout * 1000)
    if "200 OK" == res.status:
      echo res.status
      return (res.status, true)
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
