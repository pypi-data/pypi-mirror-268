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
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:LIST:PHD:CURRent \n
		Snippet: value: List[float] = driver.wcdmaMeas.multiEval.listPy.phd.current.fetch() \n
		Returns the phase discontinuity vs. slot results in list mode. Each value indicates the phase discontinuity at the
		boundary between the slot and the previous slot. If the slot or the previous slot is not measured, NCAP is returned. \n
		Suppressed linked return values: reliability \n
			:return: phd: Comma-separated list of phase discontinuity results, one value per slot. The list contains results for all active segments (segments for which any measurement has been enabled) . If another measurement has been enabled for a segment, but the phase discontinuity measurement is disabled, NCAPs are returned for that segment. Example: segment 1 with 10 slots active, segment 2 with 50 slots inactive, segment 3 with 12 slots active. 22 phase discontinuity results are returned."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:LIST:PHD:CURRent?', suppressed)
		return response
