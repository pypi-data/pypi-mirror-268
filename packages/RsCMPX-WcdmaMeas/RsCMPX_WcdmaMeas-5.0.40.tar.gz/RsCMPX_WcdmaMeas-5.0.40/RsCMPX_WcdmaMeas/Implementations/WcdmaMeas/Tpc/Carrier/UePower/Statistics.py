from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StatisticsCls:
	"""Statistics commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("statistics", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Max_Output_Power: int: Number of trace values for maximum output power
			- Min_Outpu_Power: int: Number of trace values for minimum output power"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Max_Output_Power'),
			ArgStruct.scalar_int('Min_Outpu_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Max_Output_Power: int = None
			self.Min_Outpu_Power: int = None

	def fetch(self, carrier=repcap.Carrier.Default) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:TPC:CARRier<carrier>:UEPower:STATistics \n
		Snippet: value: ResultData = driver.wcdmaMeas.tpc.carrier.uePower.statistics.fetch(carrier = repcap.Carrier.Default) \n
		Return the Statistics values, indicating how many trace values have been considered to derive the results. The results
		are the maximum, minimum and average values of the maximum output power and the minimum output power per carrier.
		The command returns all parameters listed below, independent of the selected TPC setup. Depending on the TPC setup,
		either a result value or an indicator is returned (e.g. NAV) . \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:TPC:CARRier{carrier_cmd_val}:UEPower:STATistics?', self.__class__.ResultData())

	def read(self, carrier=repcap.Carrier.Default) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:TPC:CARRier<carrier>:UEPower:STATistics \n
		Snippet: value: ResultData = driver.wcdmaMeas.tpc.carrier.uePower.statistics.read(carrier = repcap.Carrier.Default) \n
		Return the Statistics values, indicating how many trace values have been considered to derive the results. The results
		are the maximum, minimum and average values of the maximum output power and the minimum output power per carrier.
		The command returns all parameters listed below, independent of the selected TPC setup. Depending on the TPC setup,
		either a result value or an indicator is returned (e.g. NAV) . \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:TPC:CARRier{carrier_cmd_val}:UEPower:STATistics?', self.__class__.ResultData())
