from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Ue_Power: float: UE power
			- Max_Output_Power: float: Maximum output power
			- Min_Outpu_Power: float: Minimum output power"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Ue_Power'),
			ArgStruct.scalar_float('Max_Output_Power'),
			ArgStruct.scalar_float('Min_Outpu_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ue_Power: float = None
			self.Max_Output_Power: float = None
			self.Min_Outpu_Power: float = None

	def fetch(self, carrier=repcap.Carrier.Default) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:TPC:CARRier<carrier>:UEPower:AVERage \n
		Snippet: value: ResultData = driver.wcdmaMeas.tpc.carrier.uePower.average.fetch(carrier = repcap.Carrier.Default) \n
		Return the UE power and minimum/maximum output power single value results per carrier. The minimum, maximum and average
		values of these results can be retrieved. The command returns all parameters listed below, independent of the selected
		TPC setup. However, only for some of the parameters measured values are available. For the other parameters, only an
		indicator is returned (e.g. NAV) . The values described below are returned by FETCh and READ commands. CALCulate commands
		return limit check results instead, one value for each result listed below. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:TPC:CARRier{carrier_cmd_val}:UEPower:AVERage?', self.__class__.ResultData())

	def read(self, carrier=repcap.Carrier.Default) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:TPC:CARRier<carrier>:UEPower:AVERage \n
		Snippet: value: ResultData = driver.wcdmaMeas.tpc.carrier.uePower.average.read(carrier = repcap.Carrier.Default) \n
		Return the UE power and minimum/maximum output power single value results per carrier. The minimum, maximum and average
		values of these results can be retrieved. The command returns all parameters listed below, independent of the selected
		TPC setup. However, only for some of the parameters measured values are available. For the other parameters, only an
		indicator is returned (e.g. NAV) . The values described below are returned by FETCh and READ commands. CALCulate commands
		return limit check results instead, one value for each result listed below. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:TPC:CARRier{carrier_cmd_val}:UEPower:AVERage?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Ue_Power: float or bool: UE power
			- Max_Output_Power: float or bool: Maximum output power
			- Min_Outpu_Power: float or bool: Minimum output power"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Ue_Power'),
			ArgStruct.scalar_float_ext('Max_Output_Power'),
			ArgStruct.scalar_float_ext('Min_Outpu_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ue_Power: float or bool = None
			self.Max_Output_Power: float or bool = None
			self.Min_Outpu_Power: float or bool = None

	def calculate(self, carrier=repcap.Carrier.Default) -> CalculateStruct:
		"""SCPI: CALCulate:WCDMa:MEASurement<instance>:TPC:CARRier<carrier>:UEPower:AVERage \n
		Snippet: value: CalculateStruct = driver.wcdmaMeas.tpc.carrier.uePower.average.calculate(carrier = repcap.Carrier.Default) \n
		Return the UE power and minimum/maximum output power single value results per carrier. The minimum, maximum and average
		values of these results can be retrieved. The command returns all parameters listed below, independent of the selected
		TPC setup. However, only for some of the parameters measured values are available. For the other parameters, only an
		indicator is returned (e.g. NAV) . The values described below are returned by FETCh and READ commands. CALCulate commands
		return limit check results instead, one value for each result listed below. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'CALCulate:WCDMa:MEASurement<Instance>:TPC:CARRier{carrier_cmd_val}:UEPower:AVERage?', self.__class__.CalculateStruct())
