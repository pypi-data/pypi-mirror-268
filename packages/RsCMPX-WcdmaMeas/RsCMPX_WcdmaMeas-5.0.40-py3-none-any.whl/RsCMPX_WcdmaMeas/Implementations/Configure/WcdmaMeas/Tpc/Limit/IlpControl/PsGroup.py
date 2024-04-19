from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PsGroupCls:
	"""PsGroup commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("psGroup", core, parent)

	def set(self, enable: bool, group_10_x_0_db: float, group_10_x_1_dba_lg_2: float, group_10_x_1_db: float, group_10_x_2_db: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:PSGRoup \n
		Snippet: driver.configure.wcdmaMeas.tpc.limit.ilpControl.psGroup.set(enable = False, group_10_x_0_db = 1.0, group_10_x_1_dba_lg_2 = 1.0, group_10_x_1_db = 1.0, group_10_x_2_db = 1.0) \n
		Defines Inner Loop Power Control limits: upper limits for the absolute value of the power step group error, depending on
		the expected step size. Also it enables or disables the limit check. \n
			:param enable: Disables | enables the limit check.
			:param group_10_x_0_db: Limit for groups with expected step size 10 x 0 dB (algorithm 2) .
			:param group_10_x_1_dba_lg_2: Limit for groups with expected step size 10 x ±1 dB + 40 x 0 dB (algorithm 2) .
			:param group_10_x_1_db: Limit for groups with expected step size 10 x ±1 dB (algorithm 1) .
			:param group_10_x_2_db: Limit for groups with expected step size 10 x ±2 dB (algorithm 1) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('group_10_x_0_db', group_10_x_0_db, DataType.Float), ArgSingle('group_10_x_1_dba_lg_2', group_10_x_1_dba_lg_2, DataType.Float), ArgSingle('group_10_x_1_db', group_10_x_1_db, DataType.Float), ArgSingle('group_10_x_2_db', group_10_x_2_db, DataType.Float))
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:PSGRoup {param}'.rstrip())

	# noinspection PyTypeChecker
	class PsGroupStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: Disables | enables the limit check.
			- Group_10_X_0_Db: float: Limit for groups with expected step size 10 x 0 dB (algorithm 2) .
			- Group_10_X_1_Dba_Lg_2: float: Limit for groups with expected step size 10 x ±1 dB + 40 x 0 dB (algorithm 2) .
			- Group_10_X_1_Db: float: Limit for groups with expected step size 10 x ±1 dB (algorithm 1) .
			- Group_10_X_2_Db: float: Limit for groups with expected step size 10 x ±2 dB (algorithm 1) ."""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Group_10_X_0_Db'),
			ArgStruct.scalar_float('Group_10_X_1_Dba_Lg_2'),
			ArgStruct.scalar_float('Group_10_X_1_Db'),
			ArgStruct.scalar_float('Group_10_X_2_Db')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Group_10_X_0_Db: float = None
			self.Group_10_X_1_Dba_Lg_2: float = None
			self.Group_10_X_1_Db: float = None
			self.Group_10_X_2_Db: float = None

	def get(self) -> PsGroupStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:PSGRoup \n
		Snippet: value: PsGroupStruct = driver.configure.wcdmaMeas.tpc.limit.ilpControl.psGroup.get() \n
		Defines Inner Loop Power Control limits: upper limits for the absolute value of the power step group error, depending on
		the expected step size. Also it enables or disables the limit check. \n
			:return: structure: for return value, see the help for PsGroupStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:PSGRoup?', self.__class__.PsGroupStruct())
