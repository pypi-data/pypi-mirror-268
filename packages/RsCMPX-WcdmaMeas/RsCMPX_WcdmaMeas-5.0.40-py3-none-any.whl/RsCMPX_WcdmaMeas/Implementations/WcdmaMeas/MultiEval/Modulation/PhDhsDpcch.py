from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PhDhsDpcchCls:
	"""PhDhsDpcch commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phDhsDpcch", core, parent)

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Overall_Max_Ph_D: float or bool: No parameter help available
			- Measure_Points: float or bool: No parameter help available
			- Count_Dyn_Limit: float or bool: Number of results exceeding the limit
			- Ratio_Dyn_Limit: float or bool: Percentage of results exceeding the limit
			- Meas_Point_Acurr: float or bool: No parameter help available
			- Meas_Point_Amax: float or bool: No parameter help available
			- Meas_Point_Bcurr: float or bool: No parameter help available
			- Meas_Point_Bmax: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Overall_Max_Ph_D'),
			ArgStruct.scalar_float_ext('Measure_Points'),
			ArgStruct.scalar_float_ext('Count_Dyn_Limit'),
			ArgStruct.scalar_float_ext('Ratio_Dyn_Limit'),
			ArgStruct.scalar_float_ext('Meas_Point_Acurr'),
			ArgStruct.scalar_float_ext('Meas_Point_Amax'),
			ArgStruct.scalar_float_ext('Meas_Point_Bcurr'),
			ArgStruct.scalar_float_ext('Meas_Point_Bmax')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Overall_Max_Ph_D: float or bool = None
			self.Measure_Points: float or bool = None
			self.Count_Dyn_Limit: float or bool = None
			self.Ratio_Dyn_Limit: float or bool = None
			self.Meas_Point_Acurr: float or bool = None
			self.Meas_Point_Amax: float or bool = None
			self.Meas_Point_Bcurr: float or bool = None
			self.Meas_Point_Bmax: float or bool = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WCDMa:MEASurement<instance>:MEValuation:MODulation:PHDHsdpcch \n
		Snippet: value: CalculateStruct = driver.wcdmaMeas.multiEval.modulation.phDhsDpcch.calculate() \n
		Returns the phase discontinuity HS-DPCCH single value results for signals with HS-DPCCH. The results depend on the
		dynamic limit and points A and B (see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Limit.PhsDpcch.set) .
		The values described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead,
		one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WCDMa:MEASurement<Instance>:MEValuation:MODulation:PHDHsdpcch?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Overall_Max_Ph_D: float: No parameter help available
			- Measure_Points: int: No parameter help available
			- Count_Dyn_Limit: int: Number of results exceeding the limit
			- Ratio_Dyn_Limit: float: Percentage of results exceeding the limit
			- Meas_Point_Acurr: float: No parameter help available
			- Meas_Point_Amax: float: No parameter help available
			- Meas_Point_Bcurr: float: No parameter help available
			- Meas_Point_Bmax: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Overall_Max_Ph_D'),
			ArgStruct.scalar_int('Measure_Points'),
			ArgStruct.scalar_int('Count_Dyn_Limit'),
			ArgStruct.scalar_float('Ratio_Dyn_Limit'),
			ArgStruct.scalar_float('Meas_Point_Acurr'),
			ArgStruct.scalar_float('Meas_Point_Amax'),
			ArgStruct.scalar_float('Meas_Point_Bcurr'),
			ArgStruct.scalar_float('Meas_Point_Bmax')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Overall_Max_Ph_D: float = None
			self.Measure_Points: int = None
			self.Count_Dyn_Limit: int = None
			self.Ratio_Dyn_Limit: float = None
			self.Meas_Point_Acurr: float = None
			self.Meas_Point_Amax: float = None
			self.Meas_Point_Bcurr: float = None
			self.Meas_Point_Bmax: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:MEValuation:MODulation:PHDHsdpcch \n
		Snippet: value: ResultData = driver.wcdmaMeas.multiEval.modulation.phDhsDpcch.read() \n
		Returns the phase discontinuity HS-DPCCH single value results for signals with HS-DPCCH. The results depend on the
		dynamic limit and points A and B (see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Limit.PhsDpcch.set) .
		The values described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead,
		one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:MEValuation:MODulation:PHDHsdpcch?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:MODulation:PHDHsdpcch \n
		Snippet: value: ResultData = driver.wcdmaMeas.multiEval.modulation.phDhsDpcch.fetch() \n
		Returns the phase discontinuity HS-DPCCH single value results for signals with HS-DPCCH. The results depend on the
		dynamic limit and points A and B (see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Limit.PhsDpcch.set) .
		The values described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead,
		one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:MODulation:PHDHsdpcch?', self.__class__.ResultData())
