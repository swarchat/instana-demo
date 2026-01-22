def ecm_sirion_record(ecm_sirion):
    return {
        "id": str(ecm_sirion["_id"]),
        "login_time":ecm_sirion["login_time"],
        "is_login_fail":ecm_sirion["is_login_fail"],
        "contract_list_time":ecm_sirion["contract_list_time"],
        "is_contract_list_fail":ecm_sirion["is_contract_list_fail"],
        "contract_details_time":ecm_sirion["contract_details_time"],
        "is_contract_details_fail":ecm_sirion["is_contract_details_fail"],
        "contract_return_time":ecm_sirion["contract_return_time"],
        "is_contract_return_fail":ecm_sirion["is_contract_return_fail"],
        "sow_search_time":ecm_sirion["sow_search_time"],
        "is_sow_search_fail":ecm_sirion["is_sow_search_fail"],
        "creation":ecm_sirion["creation"],
        "message":ecm_sirion["message"]
    }

def ecm_sirion_record_list(ecm_sirion_list):
    return [ecm_sirion_record(ecm_sirion) for ecm_sirion in ecm_sirion_list]