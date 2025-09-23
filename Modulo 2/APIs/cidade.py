import requests
'''import requests

response = requests.get('https://play.google.com/store/apps/details?id=com.drivezone.car.race.game')
'''
usuario = {"name": "miguel",}
#response = requests.post('https://68d00787ec1a5ff338263f44.mockapi.io/cidade/Cidadaos',json=usuario)
response = requests.delete('https://68d00787ec1a5ff338263f44.mockapi.io/cidade/Cidadaos/3)
print(response.status_code)
print(response.text)