from spotlight.api.rule.data_rule.model import DataRuleRequest


def _get_data_rule_request_info(id: str) -> dict:
    return {"endpoint": f"config/data_rule/{id}"}


def _get_data_rules_request_info() -> dict:
    return {"endpoint": f"config/data_rule"}


def _create_data_rule_request_info(request: DataRuleRequest) -> dict:
    return {"endpoint": f"config/data_rule", "json": request.request_dict()}


def _update_data_rule_request_info(id: str, request: DataRuleRequest) -> dict:
    return {"endpoint": f"config/data_rule/{id}", "json": request.request_dict()}


def _delete_data_rule_request_info(id: str) -> dict:
    return {"endpoint": f"config/data_rule/{id}"}
