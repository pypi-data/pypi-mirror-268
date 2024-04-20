from typing import Optional


def _get_data_rule_result_request_info(id: str) -> dict:
    return {"endpoint": f"config/data_rule_result/{id}"}


def _get_data_rule_results_request_info(data_rule_id: Optional[str] = None) -> dict:
    endpoint = "config/data_rule_result"
    if data_rule_id:
        endpoint += f"?data_rule_id={data_rule_id}"
    return {"endpoint": endpoint}
