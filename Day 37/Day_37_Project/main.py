import requests
import confidential

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {"token": confidential.PIXELA_TOKEN,
               "username": confidential.PIXELA_USERNAME,
               "agreeTermsOfService": "yes",
               "notMinor": "yes"}

"""response = requests.post(url=pixela_endpoint, json=user_params)    #Pixela takes parameters in json format
print(response.text)
"""
# This is just to create an account on pixela using API POST calls. Just needs to be run once.
# ----------------------------------------------------------------------------

graph_endpoint = f"{pixela_endpoint}/{confidential.PIXELA_USERNAME}/graphs"
graph_id = "graph1"

graph_config = {"id": graph_id,
                "name": "Cycling Graph",
                "unit": "Km",
                "type": "float",
                "color": "momiji"}

headers = {"X-USER-TOKEN": confidential.PIXELA_TOKEN}

"""
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
"""
# This is just to create a graph on Pixela. Just has to be run once
# ----------------------------------------------------------------------------

pixel_posting_endpoint = f"{graph_endpoint}/{graph_id}"

pixel_params = {"date": "20230107",
                "quantity": "20.9"}

response = requests.post(url=pixel_posting_endpoint, json=pixel_params, headers=headers)
# print(response.text)
# We created a pixel on Pixela now we will update and/delete it.
# ----------------------------------------------------------------------------

# We will have to use the put method here as we are updating already existing data

pixel_update_endpoint = f"{pixel_posting_endpoint}/20230107"

update_params = {"quantity": "4"}

response = requests.put(url=pixel_update_endpoint, json=update_params, headers=headers)
# print(response.text)

# To delete we will use the same method but we use the delete method

pixel_delete_endpoint = pixel_update_endpoint   # Both are the same according to the docs

response=requests.delete(url=pixel_delete_endpoint, headers=headers)    #Doesen't take any parameters according to docs
print(response.text)
