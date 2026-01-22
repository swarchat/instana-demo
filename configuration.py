from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

#uri = "mongodb://localhost:27017/"
uri = "mongodb://ibm_cloud_8b41e1e2_cc4f_4f92_9043_3533a9a2cbcb:R6TMrO3pxLLmYb3oiQsqcxvsCFUaNCpW@8a517408-ec6a-462e-81eb-ca875ec17042-0.ciokg5nw0b2de5vi8ru0.databases.appdomain.cloud:30685,8a517408-ec6a-462e-81eb-ca875ec17042-1.ciokg5nw0b2de5vi8ru0.databases.appdomain.cloud:30685,8a517408-ec6a-462e-81eb-ca875ec17042-2.ciokg5nw0b2de5vi8ru0.databases.appdomain.cloud:30685/?tls=true&tlsCAFile=C%3A%5Cibm%5Cecm%5C2fc143c1-c95e-4e7b-93ac-d87975849575.pem"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.instana_db
collection = db["instana_collection"]

