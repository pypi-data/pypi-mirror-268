from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EpStepCls:
	"""EpStep commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("epStep", core, parent)

	def set(self, enable: bool, max_count: int, step_1_db: float, step_2_db: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:EPSTep \n
		Snippet: driver.configure.wcdmaMeas.tpc.limit.ilpControl.epStep.set(enable = False, max_count = 1, step_1_db = 1.0, step_2_db = 1.0) \n
		Defines Inner Loop Power Control limits for exceptions and enables or disables the limit check. \n
			:param enable: No help available
			:param max_count: Maximum allowed exceptions for sections BC, EF and GH
			:param step_1_db: Exceptional limit for step size 1 dB
			:param step_2_db: Exceptional limit for step size 2 dB
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('max_count', max_count, DataType.Integer), ArgSingle('step_1_db', step_1_db, DataType.Float), ArgSingle('step_2_db', step_2_db, DataType.Float))
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:EPSTep {param}'.rstrip())

	# noinspection PyTypeChecker
	class EpStepStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: No parameter help available
			- Max_Count: int: Maximum allowed exceptions for sections BC, EF and GH
			- Step_1_Db: float: Exceptional limit for step size 1 dB
			- Step_2_Db: float: Exceptional limit for step size 2 dB"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_int('Max_Count'),
			ArgStruct.scalar_float('Step_1_Db'),
			ArgStruct.scalar_float('Step_2_Db')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Max_Count: int = None
			self.Step_1_Db: float = None
			self.Step_2_Db: float = None

	def get(self) -> EpStepStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:EPSTep \n
		Snippet: value: EpStepStruct = driver.configure.wcdmaMeas.tpc.limit.ilpControl.epStep.get() \n
		Defines Inner Loop Power Control limits for exceptions and enables or disables the limit check. \n
			:return: structure: for return value, see the help for EpStepStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:EPSTep?', self.__class__.EpStepStruct())
