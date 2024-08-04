# import requests
# import time
#
# # Define the URL and the authorization token
# url = "https://evoya.technocorp.uz/api/juvenile/dashboard_education_type_statistics/?date_from=2024-01-01&date_to=2024-08-01"
# headers = {
#     "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIyNTE3NzI3LCJqdGkiOiI2YTMwMGM3ZDUxOTg0MDk4YjI0NTQyMGZkMTZjODlkOCIsInVzZXJfaWQiOjZ9.zftbBtY5S9gd1gPtnaSRPBs3RKtCOul3X6WpUc8EnkY",
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
#
# }
#
# # Function to send a GET request
# def send_get_request():
#     response = requests.get(url, headers=headers)
#     print(response.content)
#     if response.status_code == 200:
#         print("Request succeeded.")
#     else:
#         print(f"Request failed with status code: {response.status_code}")
#
# # Number of requests to send
# num_requests = 1
#
#
# start_time = time.time()
#
# # Send requests in a for loop
# for i in range(num_requests):
#     send_get_request()
#
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"All requests sent. Total time taken: {elapsed_time:.2f} seconds.")
#
# print("All requests sent.")
#
#
#
#

