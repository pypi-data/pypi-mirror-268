"""ScenarioList model.

```
from allphins.models import ScenarioList
```
"""
from typing import Optional

from allphins.const import ALLPHINS_API_URL
from allphins.models.base import BaseModel
from allphins.utils import validate_uuid4


class ScenarioList(BaseModel):
    """ScenarioList model."""

    path = f'{ALLPHINS_API_URL}/scenario_lists/'

    def __init__(self, scenario_list_id: Optional[str]):
        """Instantiate a Scenario list from a scenario list UUID.

        Args:
            scenario_list_id (str): UUID of the scenario list.

        Raises:
            ValueError: If the scenario list_id is not a valid UUID.
        """
        if not validate_uuid4(scenario_list_id):
            raise ValueError(f'{scenario_list_id} is not a valid UUID.')

        super().__init__(scenario_list_id)
