from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StatisticsCls:
	"""Statistics commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("statistics", core, parent)

	def read(self) -> float:
		"""SCPI: READ:WCDMa:MEASurement<instance>:TPC:DHIB:STATistics \n
		Snippet: value: float = driver.wcdmaMeas.tpc.dhib.statistics.read() \n
		Return the Statistics values, indicating how many trace values have been considered to derive the maximum, minimum and
		average dual carrier in-band emission results. \n
		Suppressed linked return values: reliability \n
			:return: statistics: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:WCDMa:MEASurement<Instance>:TPC:DHIB:STATistics?', suppressed)
		return Conversions.str_to_float(response)

	def fetch(self) -> float:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:TPC:DHIB:STATistics \n
		Snippet: value: float = driver.wcdmaMeas.tpc.dhib.statistics.fetch() \n
		Return the Statistics values, indicating how many trace values have been considered to derive the maximum, minimum and
		average dual carrier in-band emission results. \n
		Suppressed linked return values: reliability \n
			:return: statistics: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:TPC:DHIB:STATistics?', suppressed)
		return Conversions.str_to_float(response)
