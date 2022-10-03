from time import sleep

from kit_oem import KitOEM

sensor =  KitOEM()

while True:

  read = sensor.read()
  print("{:.2f}".format(read))
  sleep(1)
