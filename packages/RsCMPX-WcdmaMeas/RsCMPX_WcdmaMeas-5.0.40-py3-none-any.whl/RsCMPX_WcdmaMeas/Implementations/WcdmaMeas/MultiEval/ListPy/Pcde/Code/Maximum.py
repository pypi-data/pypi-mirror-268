from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def fetch(self) -> List[int]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:LIST:PCDE:CODE:MAXimum \n
		Snippet: value: List[int] = driver.wcdmaMeas.multiEval.listPy.pcde.code.maximum.fetch() \n
		Return the code number for which the peak code domain error was measured, for all measured list mode segments. \n
		Suppressed linked return values: reliability \n
			:return: pcd_error_code_nr: Comma-separated list of values, one per measured segment"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:LIST:PCDE:CODE:MAXimum?', suppressed)
		return response
