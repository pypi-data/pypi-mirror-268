from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Carrier_Power: float or bool: Power at the nominal carrier UL frequency
			- Aclr_Minus_2: float or bool: Power of the adjacent channels (±1st adjacent channels at ±5 MHz from the UL frequency, ±2nd adjacent channels at ±10 MHz from the UL frequency)
			- Aclr_Minus_1: float or bool: Power of the adjacent channels (±1st adjacent channels at ±5 MHz from the UL frequency, ±2nd adjacent channels at ±10 MHz from the UL frequency)
			- Aclr_Plus_1: float or bool: Power of the adjacent channels (±1st adjacent channels at ±5 MHz from the UL frequency, ±2nd adjacent channels at ±10 MHz from the UL frequency)
			- Aclr_Plus_2: float or bool: Power of the adjacent channels (±1st adjacent channels at ±5 MHz from the UL frequency, ±2nd adjacent channels at ±10 MHz from the UL frequency)
			- Obw: float or bool: Occupied bandwidth
			- Sem_Margin_Abij: float or bool: No parameter help available
			- Sem_Margin_Bcjk: float or bool: No parameter help available
			- Sem_Margin_Cdkl: float or bool: No parameter help available
			- Sem_Margin_Efmn: float or bool: No parameter help available
			- Sem_Margin_Fenm: float or bool: No parameter help available
			- Sem_Margin_Dclk: float or bool: No parameter help available
			- Sem_Margin_Cbkj: float or bool: No parameter help available
			- Sem_Margin_Baji: float or bool: No parameter help available
			- Ue_Power: enums.ResultStatus2: User equipment power
			- Emask_Margin_Ad: float or bool: No parameter help available
			- Emask_Margin_Da: float or bool: No parameter help available
			- Carrier_Power_L: enums.ResultStatus2: Power at the nominal carrier frequency; left/right carrier of the dual carrier HSPA connection
			- Carrier_Power_R: enums.ResultStatus2: Power at the nominal carrier frequency; left/right carrier of the dual carrier HSPA connection"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Carrier_Power'),
			ArgStruct.scalar_float_ext('Aclr_Minus_2'),
			ArgStruct.scalar_float_ext('Aclr_Minus_1'),
			ArgStruct.scalar_float_ext('Aclr_Plus_1'),
			ArgStruct.scalar_float_ext('Aclr_Plus_2'),
			ArgStruct.scalar_float_ext('Obw'),
			ArgStruct.scalar_float_ext('Sem_Margin_Abij'),
			ArgStruct.scalar_float_ext('Sem_Margin_Bcjk'),
			ArgStruct.scalar_float_ext('Sem_Margin_Cdkl'),
			ArgStruct.scalar_float_ext('Sem_Margin_Efmn'),
			ArgStruct.scalar_float_ext('Sem_Margin_Fenm'),
			ArgStruct.scalar_float_ext('Sem_Margin_Dclk'),
			ArgStruct.scalar_float_ext('Sem_Margin_Cbkj'),
			ArgStruct.scalar_float_ext('Sem_Margin_Baji'),
			ArgStruct.scalar_enum('Ue_Power', enums.ResultStatus2),
			ArgStruct.scalar_float_ext('Emask_Margin_Ad'),
			ArgStruct.scalar_float_ext('Emask_Margin_Da'),
			ArgStruct.scalar_enum('Carrier_Power_L', enums.ResultStatus2),
			ArgStruct.scalar_enum('Carrier_Power_R', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Carrier_Power: float or bool = None
			self.Aclr_Minus_2: float or bool = None
			self.Aclr_Minus_1: float or bool = None
			self.Aclr_Plus_1: float or bool = None
			self.Aclr_Plus_2: float or bool = None
			self.Obw: float or bool = None
			self.Sem_Margin_Abij: float or bool = None
			self.Sem_Margin_Bcjk: float or bool = None
			self.Sem_Margin_Cdkl: float or bool = None
			self.Sem_Margin_Efmn: float or bool = None
			self.Sem_Margin_Fenm: float or bool = None
			self.Sem_Margin_Dclk: float or bool = None
			self.Sem_Margin_Cbkj: float or bool = None
			self.Sem_Margin_Baji: float or bool = None
			self.Ue_Power: enums.ResultStatus2 = None
			self.Emask_Margin_Ad: float or bool = None
			self.Emask_Margin_Da: float or bool = None
			self.Carrier_Power_L: enums.ResultStatus2 = None
			self.Carrier_Power_R: enums.ResultStatus2 = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WCDMa:MEASurement<instance>:MEValuation:SPECtrum:CURRent \n
		Snippet: value: CalculateStruct = driver.wcdmaMeas.multiEval.spectrum.current.calculate() \n
		Returns the ACLR power and spectrum emission single value results of the multi-evaluation measurement. The current,
		average and maximum values can be retrieved. The return values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each of the results 1 to 18, 29 and 30 listed below.
		The frequency positions are only returned by FETCh and READ commands. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WCDMa:MEASurement<Instance>:MEValuation:SPECtrum:CURRent?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Carrier_Power: float: Power at the nominal carrier UL frequency
			- Aclr_Minus_2: float: Power of the adjacent channels (±1st adjacent channels at ±5 MHz from the UL frequency, ±2nd adjacent channels at ±10 MHz from the UL frequency)
			- Aclr_Minus_1: float: Power of the adjacent channels (±1st adjacent channels at ±5 MHz from the UL frequency, ±2nd adjacent channels at ±10 MHz from the UL frequency)
			- Aclr_Plus_1: float: Power of the adjacent channels (±1st adjacent channels at ±5 MHz from the UL frequency, ±2nd adjacent channels at ±10 MHz from the UL frequency)
			- Aclr_Plus_2: float: Power of the adjacent channels (±1st adjacent channels at ±5 MHz from the UL frequency, ±2nd adjacent channels at ±10 MHz from the UL frequency)
			- Obw: float: Occupied bandwidth
			- Sem_Margin_Abij: float: No parameter help available
			- Sem_Margin_Bcjk: float: No parameter help available
			- Sem_Margin_Cdkl: float: No parameter help available
			- Sem_Margin_Efmn: float: No parameter help available
			- Sem_Margin_Fenm: float: No parameter help available
			- Sem_Margin_Dclk: float: No parameter help available
			- Sem_Margin_Cbkj: float: No parameter help available
			- Sem_Margin_Baji: float: No parameter help available
			- Ue_Power: float: User equipment power
			- Sem_Margin_Ad: float: No parameter help available
			- Sem_Margin_Da: float: No parameter help available
			- Sem_Abij_At_Freq: float: No parameter help available
			- Sem_Bcjk_At_Freq: float: No parameter help available
			- Sem_Cdkl_At_Freq: float: No parameter help available
			- Sem_Efmn_At_Freq: float: No parameter help available
			- Sem_Fenm_At_Freq: float: No parameter help available
			- Sem_Dclk_At_Freq: float: No parameter help available
			- Sem_Cbkj_At_Freq: float: No parameter help available
			- Sem_Baji_At_Freq: float: No parameter help available
			- Sem_Adat_Freq: float: No parameter help available
			- Sem_Da_At_Freq: float: No parameter help available
			- Carrier_Power_L: float: Power at the nominal carrier frequency; left/right carrier of the dual carrier HSPA connection
			- Carrier_Power_R: float: Power at the nominal carrier frequency; left/right carrier of the dual carrier HSPA connection"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Carrier_Power'),
			ArgStruct.scalar_float('Aclr_Minus_2'),
			ArgStruct.scalar_float('Aclr_Minus_1'),
			ArgStruct.scalar_float('Aclr_Plus_1'),
			ArgStruct.scalar_float('Aclr_Plus_2'),
			ArgStruct.scalar_float('Obw'),
			ArgStruct.scalar_float('Sem_Margin_Abij'),
			ArgStruct.scalar_float('Sem_Margin_Bcjk'),
			ArgStruct.scalar_float('Sem_Margin_Cdkl'),
			ArgStruct.scalar_float('Sem_Margin_Efmn'),
			ArgStruct.scalar_float('Sem_Margin_Fenm'),
			ArgStruct.scalar_float('Sem_Margin_Dclk'),
			ArgStruct.scalar_float('Sem_Margin_Cbkj'),
			ArgStruct.scalar_float('Sem_Margin_Baji'),
			ArgStruct.scalar_float('Ue_Power'),
			ArgStruct.scalar_float('Sem_Margin_Ad'),
			ArgStruct.scalar_float('Sem_Margin_Da'),
			ArgStruct.scalar_float('Sem_Abij_At_Freq'),
			ArgStruct.scalar_float('Sem_Bcjk_At_Freq'),
			ArgStruct.scalar_float('Sem_Cdkl_At_Freq'),
			ArgStruct.scalar_float('Sem_Efmn_At_Freq'),
			ArgStruct.scalar_float('Sem_Fenm_At_Freq'),
			ArgStruct.scalar_float('Sem_Dclk_At_Freq'),
			ArgStruct.scalar_float('Sem_Cbkj_At_Freq'),
			ArgStruct.scalar_float('Sem_Baji_At_Freq'),
			ArgStruct.scalar_float('Sem_Adat_Freq'),
			ArgStruct.scalar_float('Sem_Da_At_Freq'),
			ArgStruct.scalar_float('Carrier_Power_L'),
			ArgStruct.scalar_float('Carrier_Power_R')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Carrier_Power: float = None
			self.Aclr_Minus_2: float = None
			self.Aclr_Minus_1: float = None
			self.Aclr_Plus_1: float = None
			self.Aclr_Plus_2: float = None
			self.Obw: float = None
			self.Sem_Margin_Abij: float = None
			self.Sem_Margin_Bcjk: float = None
			self.Sem_Margin_Cdkl: float = None
			self.Sem_Margin_Efmn: float = None
			self.Sem_Margin_Fenm: float = None
			self.Sem_Margin_Dclk: float = None
			self.Sem_Margin_Cbkj: float = None
			self.Sem_Margin_Baji: float = None
			self.Ue_Power: float = None
			self.Sem_Margin_Ad: float = None
			self.Sem_Margin_Da: float = None
			self.Sem_Abij_At_Freq: float = None
			self.Sem_Bcjk_At_Freq: float = None
			self.Sem_Cdkl_At_Freq: float = None
			self.Sem_Efmn_At_Freq: float = None
			self.Sem_Fenm_At_Freq: float = None
			self.Sem_Dclk_At_Freq: float = None
			self.Sem_Cbkj_At_Freq: float = None
			self.Sem_Baji_At_Freq: float = None
			self.Sem_Adat_Freq: float = None
			self.Sem_Da_At_Freq: float = None
			self.Carrier_Power_L: float = None
			self.Carrier_Power_R: float = None

	def fetch(self, aclr_mode: enums.AclrMode = None) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:SPECtrum:CURRent \n
		Snippet: value: ResultData = driver.wcdmaMeas.multiEval.spectrum.current.fetch(aclr_mode = enums.AclrMode.ABSolute) \n
		Returns the ACLR power and spectrum emission single value results of the multi-evaluation measurement. The current,
		average and maximum values can be retrieved. The return values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each of the results 1 to 18, 29 and 30 listed below.
		The frequency positions are only returned by FETCh and READ commands. \n
			:param aclr_mode: ABSolute: ACLR power is displayed in dBm as an absolute value. RELative: ACLR power is displayed in dB relative to carrier power.
			:return: structure: for return value, see the help for ResultData structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('aclr_mode', aclr_mode, DataType.Enum, enums.AclrMode, is_optional=True))
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:SPECtrum:CURRent? {param}'.rstrip(), self.__class__.ResultData())

	def read(self, aclr_mode: enums.AclrMode = None) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:MEValuation:SPECtrum:CURRent \n
		Snippet: value: ResultData = driver.wcdmaMeas.multiEval.spectrum.current.read(aclr_mode = enums.AclrMode.ABSolute) \n
		Returns the ACLR power and spectrum emission single value results of the multi-evaluation measurement. The current,
		average and maximum values can be retrieved. The return values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each of the results 1 to 18, 29 and 30 listed below.
		The frequency positions are only returned by FETCh and READ commands. \n
			:param aclr_mode: ABSolute: ACLR power is displayed in dBm as an absolute value. RELative: ACLR power is displayed in dB relative to carrier power.
			:return: structure: for return value, see the help for ResultData structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('aclr_mode', aclr_mode, DataType.Enum, enums.AclrMode, is_optional=True))
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:MEValuation:SPECtrum:CURRent? {param}'.rstrip(), self.__class__.ResultData())
