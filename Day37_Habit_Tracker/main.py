import requests
import datetime as dt

PIXELA_API = "souiebasoukonomunenoana"
PIXELA_USERNAME = "johntarou69420"

pixela = "https://pixe.la/v1/users"
pixela_graph = f"{pixela}/{PIXELA_USERNAME}/graphs"
headers = {"X-USER-TOKEN": PIXELA_API}
today = dt.datetime.now().strftime("%Y%m%d")

graph_id = "codingtracker"
graph_name = "Coding Tracker"
#
# pixela_post_params = {
#     "token": PIXELA_API,
#     "username": PIXELA_USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
# response = requests.post(pixela, json=pixela_post_params)
# # print(response.text)
#
#
# graph_settings = {
#     "id": graph_id,
#     "name": graph_name,
#     "unit": "minutes",
#     "type": "int",
#     "color": "ajisai",
# }

# response = requests.post(pixela_graph, json=graph_settings, headers=headers)
# print(response.text)
# today = str(dt.datetime.now().date()).split("-")
# today = "".join(today)

# tracking_params = {"date": "20220502", "quantity": input("How many minutes did you code today? ")}
#
# response = requests.post(f"{pixela_graph}/{graph_id}", json=tracking_params, headers=headers)
#
# response = requests.put(f"{pixela_graph}/{graph_id}/{today}", json={"quantity": input("How many minutes did you code today? ")},
#                         headers=headers)
response = requests.delete(f"{pixela_graph}/{graph_id}/{today}", headers=headers)
print(response.text)
