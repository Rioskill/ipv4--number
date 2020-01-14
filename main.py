def tobin(a):
  res = bin(int(a))[2:]
  return '0' * (8 - len(res)) + res

def convert(l):
  res = [tobin(quadrant) for quadrant in l]
  return res[0] + res[1] + res[2] + res[3]

def check_ip(ip):
  if len(ip) != 4:
    return False
  for i in ip:
    if int(i) > 255 or int(i) < 0:
      return False
  return True    

def check_mask(mask):
  if len(mask) != 4:
    return False
  p = int(mask[0])
  for i in mask[1:]:
    if int(i) > 255 or int(i) < 0 or int(i) > p:
      return False
    p = int(i)
  return True

ip = input('ip: ').split('.')
mask = input('mask: ').split('.')

if check_ip(ip):
  if check_mask(mask):
    print(int(convert(ip)[convert(mask).find('0'):], 2))
  else:
    print('mask is not valid')
else:
  print('ip is not valid')
