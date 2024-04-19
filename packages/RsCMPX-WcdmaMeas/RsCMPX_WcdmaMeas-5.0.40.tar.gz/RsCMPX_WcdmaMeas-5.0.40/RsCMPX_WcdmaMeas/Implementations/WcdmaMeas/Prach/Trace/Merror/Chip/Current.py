from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:PRACh:TRACe:MERRor:CHIP:CURRent \n
		Snippet: value: List[float] = driver.wcdmaMeas.prach.trace.merror.chip.current.fetch() \n
		Return the values of the magnitude error vs chip diagram. \n
		Suppressed linked return values: reliability \n
			:return: mag_error_chip: Comma-separated list of 4096 values, one per chip of the preselected preamble"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:PRACh:TRACe:MERRor:CHIP:CURRent?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:WCDMa:MEASurement<instance>:PRACh:TRACe:MERRor:CHIP:CURRent \n
		Snippet: value: List[float] = driver.wcdmaMeas.prach.trace.merror.chip.current.read() \n
		Return the values of the magnitude error vs chip diagram. \n
		Suppressed linked return values: reliability \n
			:return: mag_error_chip: Comma-separated list of 4096 values, one per chip of the preselected preamble"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WCDMa:MEASurement<Instance>:PRACh:TRACe:MERRor:CHIP:CURRent?', suppressed)
		return response
