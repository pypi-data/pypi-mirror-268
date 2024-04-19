from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MinimumCls:
	"""Minimum commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Pwr_Steps_0_Db: float: No parameter help available
			- Pwr_Steps_B_1_Db: float: No parameter help available
			- Pwr_Steps_Cm_1_Db: float: No parameter help available
			- Pwr_Steps_Group_A: float: No parameter help available
			- Pwr_Steps_Group_B: float: No parameter help available
			- Pwr_Steps_Group_C: float: No parameter help available
			- Start_Slot_Group_A: int: No parameter help available
			- Pwr_Steps_Eg: float: No parameter help available
			- Pwr_Steps_Fh: float: No parameter help available
			- Pwr_Steps_Group_Eg: float: No parameter help available
			- Pwr_Steps_Group_Fh: float: No parameter help available
			- Start_Slot_Group_Eg: int: No parameter help available
			- Start_Slot_Group_Fh: int: No parameter help available
			- Pwr_Steps_Up: float: No parameter help available
			- Pwr_Steps_Down: float: No parameter help available
			- Init_Pwr_Step: float: No parameter help available
			- Rpwr_Steps: float: No parameter help available
			- Rpwr_Steps_Group: float: No parameter help available
			- Pwr_Step_Ncm_Cm: float: No parameter help available
			- Pwr_Step_Cm_Ncm: float: No parameter help available
			- Epwr_Steps_B_1_D_B: float: No parameter help available
			- Epwr_Steps_Cm_1_D_B: float: No parameter help available
			- Epwr_Steps_Eg: float: No parameter help available
			- Epwr_Steps_Fh: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Pwr_Steps_0_Db'),
			ArgStruct.scalar_float('Pwr_Steps_B_1_Db'),
			ArgStruct.scalar_float('Pwr_Steps_Cm_1_Db'),
			ArgStruct.scalar_float('Pwr_Steps_Group_A'),
			ArgStruct.scalar_float('Pwr_Steps_Group_B'),
			ArgStruct.scalar_float('Pwr_Steps_Group_C'),
			ArgStruct.scalar_int('Start_Slot_Group_A'),
			ArgStruct.scalar_float('Pwr_Steps_Eg'),
			ArgStruct.scalar_float('Pwr_Steps_Fh'),
			ArgStruct.scalar_float('Pwr_Steps_Group_Eg'),
			ArgStruct.scalar_float('Pwr_Steps_Group_Fh'),
			ArgStruct.scalar_int('Start_Slot_Group_Eg'),
			ArgStruct.scalar_int('Start_Slot_Group_Fh'),
			ArgStruct.scalar_float('Pwr_Steps_Up'),
			ArgStruct.scalar_float('Pwr_Steps_Down'),
			ArgStruct.scalar_float('Init_Pwr_Step'),
			ArgStruct.scalar_float('Rpwr_Steps'),
			ArgStruct.scalar_float('Rpwr_Steps_Group'),
			ArgStruct.scalar_float('Pwr_Step_Ncm_Cm'),
			ArgStruct.scalar_float('Pwr_Step_Cm_Ncm'),
			ArgStruct.scalar_float('Epwr_Steps_B_1_D_B'),
			ArgStruct.scalar_float('Epwr_Steps_Cm_1_D_B'),
			ArgStruct.scalar_float('Epwr_Steps_Eg'),
			ArgStruct.scalar_float('Epwr_Steps_Fh')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Pwr_Steps_0_Db: float = None
			self.Pwr_Steps_B_1_Db: float = None
			self.Pwr_Steps_Cm_1_Db: float = None
			self.Pwr_Steps_Group_A: float = None
			self.Pwr_Steps_Group_B: float = None
			self.Pwr_Steps_Group_C: float = None
			self.Start_Slot_Group_A: int = None
			self.Pwr_Steps_Eg: float = None
			self.Pwr_Steps_Fh: float = None
			self.Pwr_Steps_Group_Eg: float = None
			self.Pwr_Steps_Group_Fh: float = None
			self.Start_Slot_Group_Eg: int = None
			self.Start_Slot_Group_Fh: int = None
			self.Pwr_Steps_Up: float = None
			self.Pwr_Steps_Down: float = None
			self.Init_Pwr_Step: float = None
			self.Rpwr_Steps: float = None
			self.Rpwr_Steps_Group: float = None
			self.Pwr_Step_Ncm_Cm: float = None
			self.Pwr_Step_Cm_Ncm: float = None
			self.Epwr_Steps_B_1_D_B: float = None
			self.Epwr_Steps_Cm_1_D_B: float = None
			self.Epwr_Steps_Eg: float = None
			self.Epwr_Steps_Fh: float = None

	def read(self, carrier=repcap.Carrier.Default) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:TPC:CARRier<carrier>:PSTeps:MINimum \n
		Snippet: value: ResultData = driver.wcdmaMeas.tpc.carrier.psteps.minimum.read(carrier = repcap.Carrier.Default) \n
		Return the power step and power step group single value results per carrier. The minimum, maximum and average results can
		be retrieved. The command returns all parameters listed below, independent of the selected TPC setup. However, only for
		some of the parameters measured values are available. For the other parameters, only an indicator is returned (e.g. NAV) .
		'Step A' to 'step H' refer to the test steps of the Inner Loop Power Control mode (results <2_Step0dB_ABC> to
		<14_StartFH> and <22_EPStepsB1dB> to <25_EPStepsFH>) . The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:TPC:CARRier{carrier_cmd_val}:PSTeps:MINimum?', self.__class__.ResultData())

	def fetch(self, carrier=repcap.Carrier.Default) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:TPC:CARRier<carrier>:PSTeps:MINimum \n
		Snippet: value: ResultData = driver.wcdmaMeas.tpc.carrier.psteps.minimum.fetch(carrier = repcap.Carrier.Default) \n
		Return the power step and power step group single value results per carrier. The minimum, maximum and average results can
		be retrieved. The command returns all parameters listed below, independent of the selected TPC setup. However, only for
		some of the parameters measured values are available. For the other parameters, only an indicator is returned (e.g. NAV) .
		'Step A' to 'step H' refer to the test steps of the Inner Loop Power Control mode (results <2_Step0dB_ABC> to
		<14_StartFH> and <22_EPStepsB1dB> to <25_EPStepsFH>) . The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:TPC:CARRier{carrier_cmd_val}:PSTeps:MINimum?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Pwr_Steps_0_Db: float or bool: No parameter help available
			- Pwr_Steps_B_1_Db: float or bool: No parameter help available
			- Pwr_Steps_Cm_1_Db: float or bool: No parameter help available
			- Pwr_Steps_Group_A: float or bool: No parameter help available
			- Pwr_Steps_Group_B: float or bool: No parameter help available
			- Pwr_Steps_Group_C: float or bool: No parameter help available
			- Start_Slot_Group_A: float or bool: No parameter help available
			- Pwr_Steps_Eg: float or bool: No parameter help available
			- Pwr_Steps_Fh: float or bool: No parameter help available
			- Pwr_Steps_Group_Eg: float or bool: No parameter help available
			- Pwr_Steps_Group_Fh: float or bool: No parameter help available
			- Start_Slot_Group_Eg: float or bool: No parameter help available
			- Start_Slot_Group_Fh: float or bool: No parameter help available
			- Pwr_Steps_Up: float or bool: No parameter help available
			- Pwr_Steps_Down: float or bool: No parameter help available
			- Epwr_Steps_B_1_D_B: enums.ResultStatus2: No parameter help available
			- Epwr_Steps_Cm_1_D_B: enums.ResultStatus2: No parameter help available
			- Epwr_Steps_Eg: enums.ResultStatus2: No parameter help available
			- Epwr_Steps_Fh: enums.ResultStatus2: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Pwr_Steps_0_Db'),
			ArgStruct.scalar_float_ext('Pwr_Steps_B_1_Db'),
			ArgStruct.scalar_float_ext('Pwr_Steps_Cm_1_Db'),
			ArgStruct.scalar_float_ext('Pwr_Steps_Group_A'),
			ArgStruct.scalar_float_ext('Pwr_Steps_Group_B'),
			ArgStruct.scalar_float_ext('Pwr_Steps_Group_C'),
			ArgStruct.scalar_float_ext('Start_Slot_Group_A'),
			ArgStruct.scalar_float_ext('Pwr_Steps_Eg'),
			ArgStruct.scalar_float_ext('Pwr_Steps_Fh'),
			ArgStruct.scalar_float_ext('Pwr_Steps_Group_Eg'),
			ArgStruct.scalar_float_ext('Pwr_Steps_Group_Fh'),
			ArgStruct.scalar_float_ext('Start_Slot_Group_Eg'),
			ArgStruct.scalar_float_ext('Start_Slot_Group_Fh'),
			ArgStruct.scalar_float_ext('Pwr_Steps_Up'),
			ArgStruct.scalar_float_ext('Pwr_Steps_Down'),
			ArgStruct.scalar_enum('Epwr_Steps_B_1_D_B', enums.ResultStatus2),
			ArgStruct.scalar_enum('Epwr_Steps_Cm_1_D_B', enums.ResultStatus2),
			ArgStruct.scalar_enum('Epwr_Steps_Eg', enums.ResultStatus2),
			ArgStruct.scalar_enum('Epwr_Steps_Fh', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Pwr_Steps_0_Db: float or bool = None
			self.Pwr_Steps_B_1_Db: float or bool = None
			self.Pwr_Steps_Cm_1_Db: float or bool = None
			self.Pwr_Steps_Group_A: float or bool = None
			self.Pwr_Steps_Group_B: float or bool = None
			self.Pwr_Steps_Group_C: float or bool = None
			self.Start_Slot_Group_A: float or bool = None
			self.Pwr_Steps_Eg: float or bool = None
			self.Pwr_Steps_Fh: float or bool = None
			self.Pwr_Steps_Group_Eg: float or bool = None
			self.Pwr_Steps_Group_Fh: float or bool = None
			self.Start_Slot_Group_Eg: float or bool = None
			self.Start_Slot_Group_Fh: float or bool = None
			self.Pwr_Steps_Up: float or bool = None
			self.Pwr_Steps_Down: float or bool = None
			self.Epwr_Steps_B_1_D_B: enums.ResultStatus2 = None
			self.Epwr_Steps_Cm_1_D_B: enums.ResultStatus2 = None
			self.Epwr_Steps_Eg: enums.ResultStatus2 = None
			self.Epwr_Steps_Fh: enums.ResultStatus2 = None

	def calculate(self, carrier=repcap.Carrier.Default) -> CalculateStruct:
		"""SCPI: CALCulate:WCDMa:MEASurement<instance>:TPC:CARRier<carrier>:PSTeps:MINimum \n
		Snippet: value: CalculateStruct = driver.wcdmaMeas.tpc.carrier.psteps.minimum.calculate(carrier = repcap.Carrier.Default) \n
		Return the power step and power step group single value results per carrier. The minimum, maximum and average results can
		be retrieved. The command returns all parameters listed below, independent of the selected TPC setup. However, only for
		some of the parameters measured values are available. For the other parameters, only an indicator is returned (e.g. NAV) .
		'Step A' to 'step H' refer to the test steps of the Inner Loop Power Control mode (results <2_Step0dB_ABC> to
		<14_StartFH> and <22_EPStepsB1dB> to <25_EPStepsFH>) . The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'CALCulate:WCDMa:MEASurement<Instance>:TPC:CARRier{carrier_cmd_val}:PSTeps:MINimum?', self.__class__.CalculateStruct())
