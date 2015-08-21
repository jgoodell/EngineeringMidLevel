import requests, json

# setup the basic URI and credentials.
api_url = "http://localhost:8080"
user = "admin"
password = "password"

# Test POST

# client POST tests.
response = requests.post(api_url + "/clients/",
                         json.dumps({'name':'ClientA'}),
                         auth=(user,
                               password))
import pdb; pdb.set_trace()
assert response.status_code == 200

response = requests.get(api_url + "/clients/",
                        auth=(user,
                              password)
                        )
print(response.json())
