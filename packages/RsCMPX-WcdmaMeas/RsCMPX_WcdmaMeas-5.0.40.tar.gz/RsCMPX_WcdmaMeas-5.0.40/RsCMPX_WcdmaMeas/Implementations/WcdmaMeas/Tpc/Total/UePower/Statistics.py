from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StatisticsCls:
	"""Statistics commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("statistics", core, parent)

	def fetch(self) -> int:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:TPC:TOTal:UEPower:STATistics \n
		Snippet: value: int = driver.wcdmaMeas.tpc.total.uePower.statistics.fetch() \n
		Return the Statistics values, indicating how many trace values have been considered to derive the maximum, minimum and
		average values of the maximum output power over all carriers. \n
		Suppressed linked return values: reliability \n
			:return: max_output_power: Number of trace values for maximum output power over all carriers"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:TPC:TOTal:UEPower:STATistics?', suppressed)
		return Conversions.str_to_int(response)

	def read(self) -> int:
		"""SCPI: READ:WCDMa:MEASurement<instance>:TPC:TOTal:UEPower:STATistics \n
		Snippet: value: int = driver.wcdmaMeas.tpc.total.uePower.statistics.read() \n
		Return the Statistics values, indicating how many trace values have been considered to derive the maximum, minimum and
		average values of the maximum output power over all carriers. \n
		Suppressed linked return values: reliability \n
			:return: max_output_power: Number of trace values for maximum output power over all carriers"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:WCDMa:MEASurement<Instance>:TPC:TOTal:UEPower:STATistics?', suppressed)
		return Conversions.str_to_int(response)
