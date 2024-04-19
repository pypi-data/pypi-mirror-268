from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ........Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:LIST:SPECtrum:EMASk:DC:AVERage \n
		Snippet: value: List[float] = driver.wcdmaMeas.multiEval.listPy.spectrum.emask.dc.average.fetch() \n
		Return the limit line margin values in the 4 emission mask areas above the carrier frequency for all measured list mode
		segments. A positive result indicates that the trace is located above the limit line, i.e. the limit is exceeded. \n
		Suppressed linked return values: reliability \n
			:return: emask_margin: Comma-separated list of values, one per measured segment"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:LIST:SPECtrum:EMASk:DC:AVERage?', suppressed)
		return response
