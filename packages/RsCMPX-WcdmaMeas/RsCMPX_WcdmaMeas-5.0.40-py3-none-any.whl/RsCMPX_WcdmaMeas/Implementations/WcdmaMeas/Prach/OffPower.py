from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OffPowerCls:
	"""OffPower commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offPower", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:PRACh:OFFPower \n
		Snippet: value: List[float] = driver.wcdmaMeas.prach.offPower.fetch() \n
		Return the OFF power results. \n
		Suppressed linked return values: reliability \n
			:return: off_power: OFF power before preamble, OFF power after preamble"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:PRACh:OFFPower?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:WCDMa:MEASurement<instance>:PRACh:OFFPower \n
		Snippet: value: List[float] = driver.wcdmaMeas.prach.offPower.read() \n
		Return the OFF power results. \n
		Suppressed linked return values: reliability \n
			:return: off_power: OFF power before preamble, OFF power after preamble"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WCDMa:MEASurement<Instance>:PRACh:OFFPower?', suppressed)
		return response

	def calculate(self) -> List[float or bool]:
		"""SCPI: CALCulate:WCDMa:MEASurement<instance>:PRACh:OFFPower \n
		Snippet: value: List[float or bool] = driver.wcdmaMeas.prach.offPower.calculate() \n
		Return the OFF power results. \n
		Suppressed linked return values: reliability \n
			:return: off_power: (float or boolean items) OFF power before preamble, OFF power after preamble"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:WCDMa:MEASurement<Instance>:PRACh:OFFPower?', suppressed)
		return Conversions.str_to_float_or_bool_list(response)
