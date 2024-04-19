from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UephdCls:
	"""Uephd commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uephd", core, parent)

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Overall_Max_Ph_D: float or bool: Overall maximum phase discontinuity
			- Overall_Min_Dist: float or bool: The overall minimum slot distance between the two results exceeding the dynamic limit
			- Count_Upper_Limit: float or bool: Number of results exceeding the upper limit
			- Count_Dyn_Limit: float or bool: The number of results exceeding the dynamic limit"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Overall_Max_Ph_D'),
			ArgStruct.scalar_float_ext('Overall_Min_Dist'),
			ArgStruct.scalar_float_ext('Count_Upper_Limit'),
			ArgStruct.scalar_float_ext('Count_Dyn_Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Overall_Max_Ph_D: float or bool = None
			self.Overall_Min_Dist: float or bool = None
			self.Count_Upper_Limit: float or bool = None
			self.Count_Dyn_Limit: float or bool = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WCDMa:MEASurement<instance>:MEValuation:MODulation:UEPHd \n
		Snippet: value: CalculateStruct = driver.wcdmaMeas.multiEval.modulation.uephd.calculate() \n
		Returns the UE phase discontinuity single value results for signals without HSPA channels. The results depend on the
		upper limit and the dynamic limit, see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Limit.Phd.set. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WCDMa:MEASurement<Instance>:MEValuation:MODulation:UEPHd?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Overall_Max_Ph_D: float: Overall maximum phase discontinuity
			- Overall_Min_Dist: int: The overall minimum slot distance between the two results exceeding the dynamic limit
			- Count_Upper_Limit: int: Number of results exceeding the upper limit
			- Count_Dyn_Limit: int: The number of results exceeding the dynamic limit"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Overall_Max_Ph_D'),
			ArgStruct.scalar_int('Overall_Min_Dist'),
			ArgStruct.scalar_int('Count_Upper_Limit'),
			ArgStruct.scalar_int('Count_Dyn_Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Overall_Max_Ph_D: float = None
			self.Overall_Min_Dist: int = None
			self.Count_Upper_Limit: int = None
			self.Count_Dyn_Limit: int = None

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:MEValuation:MODulation:UEPHd \n
		Snippet: value: ResultData = driver.wcdmaMeas.multiEval.modulation.uephd.read() \n
		Returns the UE phase discontinuity single value results for signals without HSPA channels. The results depend on the
		upper limit and the dynamic limit, see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Limit.Phd.set. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:MEValuation:MODulation:UEPHd?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:MODulation:UEPHd \n
		Snippet: value: ResultData = driver.wcdmaMeas.multiEval.modulation.uephd.fetch() \n
		Returns the UE phase discontinuity single value results for signals without HSPA channels. The results depend on the
		upper limit and the dynamic limit, see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Limit.Phd.set. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:MODulation:UEPHd?', self.__class__.ResultData())
