import requests, json
import os
from datetime import datetime as dt
from dotenv import load_dotenv

load_dotenv()

USERNAME = 'kondamanish'
TOKEN = os.getenv('TOKEN')
pixela_endpoint = os.getenv("PIXEL_ENDPOINT")

print(pixela_endpoint)
GRAPH_ID = 'graph-1'
# ------------------Create User-----------------
# params = {
#     'token':TOKEN,
#     'username':USERNAME,
#     "agreeTermsOfService":"yes",
#     "notMinor":'yes'
# }
# res = requests.post(url=pixela_endpoint, json=params)
# data = res.text


# -----------Create Graph--------------
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# headers = {
#     "X-USER-TOKEN":TOKEN
# }
# graph_params = {
#     'id':GRAPH_ID,
#     'name':"Cycling Graph",
#     'unit':"Km",
#     'type':"float",
#     'color':'momiji'
# }
# res_graph = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(res_graph.text)


# ---------------- ADD Send data (pixel) to the Graph ----------------
# today_date = dt.now()
# graph_data_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

# optional_data = {
#     'name':'konda',
#     'age':23,
#     'city':'pune'
# }
# graph_data_params={
#   'date': "20260809",   #today_date.strftime('%Y%m%d'),
#   'quantity':"3.80",
#   'optionalData':json.dumps(optional_data),
# }
# # print(graph_data_params)
# res = requests.post(url=graph_data_endpoint, json=graph_data_params , headers=headers)
# print(res.text)


# -------------- Update Pixel --------------------------------------
# updat_graph_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{today_date.strftime("%Y%m%d")}"
# # print(updat_graph_pixel_endpoint)
# upate_pixel_params = {
#     'quantity':"6.6"
# }
# res = requests.put(url=updat_graph_pixel_endpoint, headers=headers, json=upate_pixel_params)
# print(res.text)


# ------------------Delete a Pixle from  graph-----------------------
# DELETE /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
# delete_graph_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{today_date.strftime("%Y%m%d")}"
# res = requests.delete(url=delete_graph_pixel_endpoint, headers=headers)
# print(res.text)






