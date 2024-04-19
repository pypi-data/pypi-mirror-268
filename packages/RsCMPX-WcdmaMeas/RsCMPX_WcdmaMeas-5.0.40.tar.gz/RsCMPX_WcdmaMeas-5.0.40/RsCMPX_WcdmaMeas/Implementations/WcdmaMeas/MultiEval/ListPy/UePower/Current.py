from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:LIST:UEPower:CURRent \n
		Snippet: value: List[float] = driver.wcdmaMeas.multiEval.listPy.uePower.current.fetch() \n
		Returns the UE power vs. slot results in list mode. \n
		Suppressed linked return values: reliability \n
			:return: ue_power: User equipment power, one value per slot. The list contains results for all active segments (segments for which any measurement has been enabled) . If another measurement has been enabled for a segment, but the UE power vs. slot measurement is disabled, NCAPs are returned for that segment. Example: segment 1 with 10 slots active, segment 2 with 50 slots inactive, segment 3 with 12 slots active. 22 power results are returned."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:LIST:UEPower:CURRent?', suppressed)
		return response
