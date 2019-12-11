import requests

# build URL
path_url = 'http://api.postcodes.io/postcodes/'
argument = 'e146gt'




post_codes = requests.get(path_url + argument)

print(post_codes)

#turn this into a dictionary
dict_response = post_codes.json()

#getting out data
print(dict_response.keys())

#getting the response
print(dict_response['status'])
print(dict_response['result'].keys())
print(dict_response['result']['admin_district'])

for key in dict_response['result']:
    print(key, '-->', dict_response['result'][key])