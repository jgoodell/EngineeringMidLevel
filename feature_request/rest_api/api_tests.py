import requests, json

# setup the basic URI and credentials.
api_url = "http://localhost:8080"
user = "admin"
password = "Password"

# client GET tests.
response = requests.get(api_url + "/clients/",
                        auth=(user,
                              password)
                        )
print(response)
print(response.json())

# client POST tests.
data = json.dumps({"name":"ClientC"})
response = requests.post(api_url + "/clients/",
                         data,
                         auth=(user,
                               password))
import pdb; pdb.set_trace()
assert response.status_code == 200

