from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:WCDMa:MEASurement<instance>:PRACh:TRACe:UEPower:CURRent \n
		Snippet: value: List[float] = driver.wcdmaMeas.prach.trace.uePower.current.read() \n
		Return the result values of the UE power bargraph. \n
		Suppressed linked return values: reliability \n
			:return: ue_power: Comma-separated list of values, one result per measured preamble (see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.Prach.mpreamble)"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WCDMa:MEASurement<Instance>:PRACh:TRACe:UEPower:CURRent?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:PRACh:TRACe:UEPower:CURRent \n
		Snippet: value: List[float] = driver.wcdmaMeas.prach.trace.uePower.current.fetch() \n
		Return the result values of the UE power bargraph. \n
		Suppressed linked return values: reliability \n
			:return: ue_power: Comma-separated list of values, one result per measured preamble (see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.Prach.mpreamble)"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:PRACh:TRACe:UEPower:CURRent?', suppressed)
		return response
