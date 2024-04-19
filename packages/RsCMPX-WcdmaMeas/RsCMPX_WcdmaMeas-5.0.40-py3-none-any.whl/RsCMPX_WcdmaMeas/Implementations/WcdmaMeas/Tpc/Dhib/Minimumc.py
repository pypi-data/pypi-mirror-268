from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MinimumcCls:
	"""Minimumc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimumc", core, parent)

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Carrier_Ch_Power: float or bool: Level of the uplink carrier, where the UE transmits at the maximal output power.
			- Inband_Emission: float or bool: Relative level of the other uplink carrier transmitting at minimal output power."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Carrier_Ch_Power'),
			ArgStruct.scalar_float_ext('Inband_Emission')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Carrier_Ch_Power: float or bool = None
			self.Inband_Emission: float or bool = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WCDMa:MEASurement<instance>:TPC:DHIB:MINimumc \n
		Snippet: value: CalculateStruct = driver.wcdmaMeas.tpc.dhib.minimumc.calculate() \n
		Return the dual carrier in-band emission results. The minimum, maximum and average results can be retrieved. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WCDMa:MEASurement<Instance>:TPC:DHIB:MINimumc?', self.__class__.CalculateStruct())
