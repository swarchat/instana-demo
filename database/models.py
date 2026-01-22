from pydantic import BaseModel
from datetime import datetime

class ECMSirion(BaseModel):
    login_time:float
    is_login_fail:bool = False
    contract_list_time:float
    is_contract_list_fail:bool = False
    contract_details_time:float
    is_contract_details_fail:bool = False
    contract_return_time:float
    is_contract_return_fail:bool = False
    sow_search_time:float
    is_sow_search_fail:bool = False
    message:str
    creation: int = int(datetime.timestamp(datetime.now()))