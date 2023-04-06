# import requests

# # Define the API endpoint and any necessary parameters
# endpoint = 'https://raw.githubusercontent.com/kongvut/thai-province-data/master/api_province.json'


# # Send a GET request to the API endpoint with the specified parameters
# response = requests.get(endpoint)

# # Check if the request was successful
# if response.status_code == 200:
#     # Extract the response data as JSON
#     data = response.json()
#     a = []
#     # Do something with the data
#     for x in data:
#         print(x.keys())
#         # print(x['name_th'],x['name_en'])
#     #     a.append([x['province'],x['total_case']])
#     # z = sorted(a,key=lambda x:x[1],reverse=True)
#     # for y in z[1::
#     #     print(y[0],'-->',y[1])
# else:
#     # Print an error message if the request failed
#     print(f"Error: Could not retrieve data (status code: {response.status_code})")


true = 529837
print(true)