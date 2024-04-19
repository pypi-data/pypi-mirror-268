from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PstepCls:
	"""Pstep commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pstep", core, parent)

	def set(self, enable: bool, step_0_db: float, step_1_db: float, step_2_db: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:PSTep \n
		Snippet: driver.configure.wcdmaMeas.tpc.limit.ilpControl.pstep.set(enable = False, step_0_db = 1.0, step_1_db = 1.0, step_2_db = 1.0) \n
		Defines Inner Loop Power Control limits: upper limits for the absolute value of the power step error, depending on the
		expected step size. Also it enables or disables the limit check. \n
			:param enable: Disables | enables the limit check.
			:param step_0_db: Limit for steps with expected step size 0 dB.
			:param step_1_db: Limit for steps with expected step size ±1 dB.
			:param step_2_db: Limit for steps with expected step size ±2 dB.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('step_0_db', step_0_db, DataType.Float), ArgSingle('step_1_db', step_1_db, DataType.Float), ArgSingle('step_2_db', step_2_db, DataType.Float))
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:PSTep {param}'.rstrip())

	# noinspection PyTypeChecker
	class PstepStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: Disables | enables the limit check.
			- Step_0_Db: float: Limit for steps with expected step size 0 dB.
			- Step_1_Db: float: Limit for steps with expected step size ±1 dB.
			- Step_2_Db: float: Limit for steps with expected step size ±2 dB."""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Step_0_Db'),
			ArgStruct.scalar_float('Step_1_Db'),
			ArgStruct.scalar_float('Step_2_Db')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Step_0_Db: float = None
			self.Step_1_Db: float = None
			self.Step_2_Db: float = None

	def get(self) -> PstepStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:PSTep \n
		Snippet: value: PstepStruct = driver.configure.wcdmaMeas.tpc.limit.ilpControl.pstep.get() \n
		Defines Inner Loop Power Control limits: upper limits for the absolute value of the power step error, depending on the
		expected step size. Also it enables or disables the limit check. \n
			:return: structure: for return value, see the help for PstepStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:PSTep?', self.__class__.PstepStruct())
