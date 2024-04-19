from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MinimumCls:
	"""Minimum commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Carrier_Ch_Power: float: Level of the uplink carrier, where the UE transmits at the maximal output power.
			- Inband_Emission: float: Relative level of the other uplink carrier transmitting at minimal output power."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Carrier_Ch_Power'),
			ArgStruct.scalar_float('Inband_Emission')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Carrier_Ch_Power: float = None
			self.Inband_Emission: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:TPC:DHIB:MINimum \n
		Snippet: value: ResultData = driver.wcdmaMeas.tpc.dhib.minimum.read() \n
		Return the dual carrier in-band emission results. The minimum, maximum and average results can be retrieved. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:TPC:DHIB:MINimum?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:TPC:DHIB:MINimum \n
		Snippet: value: ResultData = driver.wcdmaMeas.tpc.dhib.minimum.fetch() \n
		Return the dual carrier in-band emission results. The minimum, maximum and average results can be retrieved. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:TPC:DHIB:MINimum?', self.__class__.ResultData())
