from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StandardDevCls:
	"""StandardDev commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("standardDev", core, parent)

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Dpcch: float or bool: RCDE values for the indicated channels
			- Dpdch: float or bool: RCDE values for the indicated channels
			- Hsdpcch: float or bool: RCDE values for the indicated channels
			- Edpcch: float or bool: RCDE values for the indicated channels
			- Edpdch_1: float or bool: RCDE values for the indicated channels
			- Edpdch_2: float or bool: RCDE values for the indicated channels
			- Edpdch_3: float or bool: RCDE values for the indicated channels
			- Edpdch_4: float or bool: RCDE values for the indicated channels"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Dpcch'),
			ArgStruct.scalar_float_ext('Dpdch'),
			ArgStruct.scalar_float_ext('Hsdpcch'),
			ArgStruct.scalar_float_ext('Edpcch'),
			ArgStruct.scalar_float_ext('Edpdch_1'),
			ArgStruct.scalar_float_ext('Edpdch_2'),
			ArgStruct.scalar_float_ext('Edpdch_3'),
			ArgStruct.scalar_float_ext('Edpdch_4')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Dpcch: float or bool = None
			self.Dpdch: float or bool = None
			self.Hsdpcch: float or bool = None
			self.Edpcch: float or bool = None
			self.Edpdch_1: float or bool = None
			self.Edpdch_2: float or bool = None
			self.Edpdch_3: float or bool = None
			self.Edpdch_4: float or bool = None

	def calculate(self, carrier=repcap.Carrier.Default) -> CalculateStruct:
		"""SCPI: CALCulate:WCDMa:MEASurement<instance>:MEValuation:CARRier<carrier>:RCDerror:SDEViation \n
		Snippet: value: CalculateStruct = driver.wcdmaMeas.multiEval.carrier.rcdError.standardDev.calculate(carrier = repcap.Carrier.Default) \n
		Returns the RCDE vs slot values measured in a selected slot. In addition to the current values, average, maximum and
		standard deviation values can be retrieved. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'CALCulate:WCDMa:MEASurement<Instance>:MEValuation:CARRier{carrier_cmd_val}:RCDerror:SDEViation?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Dpcch: float: RCDE values for the indicated channels
			- Dpdch: float: RCDE values for the indicated channels
			- Hsdpcch: float: RCDE values for the indicated channels
			- Edpcch: float: RCDE values for the indicated channels
			- Edpdch_1: float: RCDE values for the indicated channels
			- Edpdch_2: float: RCDE values for the indicated channels
			- Edpdch_3: float: RCDE values for the indicated channels
			- Edpdch_4: float: RCDE values for the indicated channels"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Dpcch'),
			ArgStruct.scalar_float('Dpdch'),
			ArgStruct.scalar_float('Hsdpcch'),
			ArgStruct.scalar_float('Edpcch'),
			ArgStruct.scalar_float('Edpdch_1'),
			ArgStruct.scalar_float('Edpdch_2'),
			ArgStruct.scalar_float('Edpdch_3'),
			ArgStruct.scalar_float('Edpdch_4')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Dpcch: float = None
			self.Dpdch: float = None
			self.Hsdpcch: float = None
			self.Edpcch: float = None
			self.Edpdch_1: float = None
			self.Edpdch_2: float = None
			self.Edpdch_3: float = None
			self.Edpdch_4: float = None

	def fetch(self, carrier=repcap.Carrier.Default) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:CARRier<carrier>:RCDerror:SDEViation \n
		Snippet: value: ResultData = driver.wcdmaMeas.multiEval.carrier.rcdError.standardDev.fetch(carrier = repcap.Carrier.Default) \n
		Returns the RCDE vs slot values measured in a selected slot. In addition to the current values, average, maximum and
		standard deviation values can be retrieved. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:CARRier{carrier_cmd_val}:RCDerror:SDEViation?', self.__class__.ResultData())

	def read(self, carrier=repcap.Carrier.Default) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:MEValuation:CARRier<carrier>:RCDerror:SDEViation \n
		Snippet: value: ResultData = driver.wcdmaMeas.multiEval.carrier.rcdError.standardDev.read(carrier = repcap.Carrier.Default) \n
		Returns the RCDE vs slot values measured in a selected slot. In addition to the current values, average, maximum and
		standard deviation values can be retrieved. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:MEValuation:CARRier{carrier_cmd_val}:RCDerror:SDEViation?', self.__class__.ResultData())
