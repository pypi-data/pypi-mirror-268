from datetime import datetime
from typing import Optional, Union

from spotlight.api.data.model import WhereClause
from spotlight.core.common.base import Base
from spotlight.core.common.enum import RuleSeverity, RuleType, EventType


class DataRuleRequest(Base):
    display_name: str
    severity: RuleSeverity
    type: RuleType
    predicate: Optional[Union[str, WhereClause]]


class DataRuleResponse(Base):
    id: str
    display_name: str
    severity: RuleSeverity
    type: RuleType
    predicate: Optional[Union[str, WhereClause]]
    created_by: str
    created_at: datetime
    updated_by: Optional[str]
    updated_at: Optional[int]


class DataRuleEvent(Base):
    rule: DataRuleResponse
    event_type: EventType
