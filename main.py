from fastapi import FastAPI, APIRouter, HTTPException
from configuration import collection, client
from database.schemas import ecm_sirion_record_list
from database.models import ECMSirion


app = FastAPI()
router = APIRouter()

@app.get("/home")
async def homePage():
   try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
   except Exception as e:
    print(e)
   return {"message": "Hello Instana"}

@app.get("/home")
async def get_home():
   return {"data":"Hello"}

@router.get("/")
async def get_all_records():
   data = collection.find()
   return ecm_sirion_record_list(data)

@router.post("/")
async def create_record(ecm_sirion:ECMSirion):
   try:
      resp = collection.insert_one(ecm_sirion.model_dump(by_alias=True))
      return {"status_code":201, "id":str(resp.inserted_id)}
   except Exception as e:
      return HTTPException(status_code=501, detail= f"Exception occured --  {e}")


app.include_router(router)