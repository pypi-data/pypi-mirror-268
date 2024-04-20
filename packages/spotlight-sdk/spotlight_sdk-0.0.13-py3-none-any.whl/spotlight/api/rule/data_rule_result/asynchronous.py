from typing import Dict, Any, List, Optional

from spotlight.api.rule.data_rule_result.__util import (
    _get_data_rule_result_request_info,
    _get_data_rule_results_request_info,
)
from spotlight.core.common.decorators import async_data_request
from spotlight.core.common.requests import (
    __async_get_request,
)


@async_data_request()
async def async_get_data_rule_result(id: str) -> Dict[str, Any]:
    """
    Asynchronously get data rule result by ID.

    Args:
        id (str): Data rule result ID

    Returns:
        Dict[str, Any]: Data rule result response
    """
    request_info = _get_data_rule_result_request_info(id)
    return await __async_get_request(**request_info)


@async_data_request()
def async_get_data_rule_results(
    data_rule_id: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """
    Asynchronously get all data rule results or results for a specific data rule if data_rule_id is provided.

    Args:
        data_rule_id (Optional[str]): The ID of the specific data rule to get results for. Default is None.

    Returns:
        List[Dict[str, Any]]: List of data rule result responses
    """
    request_info = _get_data_rule_results_request_info(data_rule_id)
    return __async_get_request(**request_info)
