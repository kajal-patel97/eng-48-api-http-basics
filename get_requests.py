import requests

# # build URL
path_url = 'http://api.postcodes.io/postcodes/'
# argument = 'CR03SW'
# post_codes = requests.get(path_url + argument)
#
# print(post_codes)

# #turn this into a dictionary
# dict_response = post_codes.json()
#
# #getting out data
# print(dict_response.keys())
#
# #getting the response
# print(dict_response['status'])
# print(dict_response['result'].keys())
# print(dict_response['result']['admin_district'])
# for key in dict_response['result']:
#     print(key, '-->', dict_response['result'][key])


#Task

## 1- Play around with API and getting data
    # This prints out the keys in the get request
        #print(dict_response.keys())

    #This prints out the status of the website (which inlcudes the URL and argument passed through)
        #print(dict_response['status'])

    # This prints out the results as a dictionary
        #print(dict_response['result'])

# 2 - from a postcode retrieve: lonitude, latitude, nuts, admin ward
    #This prints out the longitude, latitude, nuts and admin_ward
# print(dict_response['result']['longitude'])
# print(dict_response['result']['latitude'])
# print(dict_response['result']['nuts'])
# print(dict_response['result']['admin_ward'])


# 3 - build a function that returns a lat of a postcode
def postcode_lat():
    ask_postcode = input('What is the postcode you want to find the latitude of')
    result = requests.get(path_url + ask_postcode.strip())
    post_code_dictionary = result.json()
    return post_code_dictionary['result']['latitude']

# 4 - build another function that returns the log of a post code
def postcode



# 5 - Allows me to search a postcode, and get the following data exported to a TXT file:
#         - postcode
#          -lonitude, latitude, nuts, admin ward