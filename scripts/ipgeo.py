import socket
import IP2Location
import os

a = (input( "ip address: " ))
import urllib
import json

url = 'http://api.hostip.info/get_json.php'
info = json.loads( urllib.urlopen( url ).read() )
ip = info['ip']

urlFoLaction = "http://ipstack.com/json/{0}".format( ip )
locationInfo = json.loads( urllib.urlopen( urlFoLaction ).read() )
print( 'Country: ' + locationInfo['country_name'] )
print( 'City: ' + locationInfo['city'] )
print( '' )
print( 'Latitude: ' + str( locationInfo['latitude'] ) )
print( 'Longitude: ' + str( locationInfo['longitude'] ) )
print( 'IP: ' + str( locationInfo['ip'] ) )
