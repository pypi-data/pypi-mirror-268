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

	def set(self, expected_0_db: float, expected_1_db: float, expected_2_db: float, expected_3_db: float, expected_4_to_7_db: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:PCONtrol:EPSTep \n
		Snippet: driver.configure.wcdmaMeas.multiEval.limit.pcontrol.epStep.set(expected_0_db = 1.0, expected_1_db = 1.0, expected_2_db = 1.0, expected_3_db = 1.0, expected_4_to_7_db = 1.0) \n
		Defines tolerance values (Expected Power Step Limits) depending on the nominal power step size. \n
			:param expected_0_db: Tolerance value for power step size 0 dB
			:param expected_1_db: Tolerance value for power step size 1 dB
			:param expected_2_db: Tolerance value for power step size 2 dB
			:param expected_3_db: Tolerance value for power step size 3 dB
			:param expected_4_to_7_db: Tolerance value for power step size 4 dB to 7 dB
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('expected_0_db', expected_0_db, DataType.Float), ArgSingle('expected_1_db', expected_1_db, DataType.Float), ArgSingle('expected_2_db', expected_2_db, DataType.Float), ArgSingle('expected_3_db', expected_3_db, DataType.Float), ArgSingle('expected_4_to_7_db', expected_4_to_7_db, DataType.Float))
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:PCONtrol:EPSTep {param}'.rstrip())

	# noinspection PyTypeChecker
	class EpStepStruct(StructBase):
		"""Response structure. Fields: \n
			- Expected_0_Db: float: Tolerance value for power step size 0 dB
			- Expected_1_Db: float: Tolerance value for power step size 1 dB
			- Expected_2_Db: float: Tolerance value for power step size 2 dB
			- Expected_3_Db: float: Tolerance value for power step size 3 dB
			- Expected_4_To_7_Db: float: Tolerance value for power step size 4 dB to 7 dB"""
		__meta_args_list = [
			ArgStruct.scalar_float('Expected_0_Db'),
			ArgStruct.scalar_float('Expected_1_Db'),
			ArgStruct.scalar_float('Expected_2_Db'),
			ArgStruct.scalar_float('Expected_3_Db'),
			ArgStruct.scalar_float('Expected_4_To_7_Db')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Expected_0_Db: float = None
			self.Expected_1_Db: float = None
			self.Expected_2_Db: float = None
			self.Expected_3_Db: float = None
			self.Expected_4_To_7_Db: float = None

	def get(self) -> EpStepStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:PCONtrol:EPSTep \n
		Snippet: value: EpStepStruct = driver.configure.wcdmaMeas.multiEval.limit.pcontrol.epStep.get() \n
		Defines tolerance values (Expected Power Step Limits) depending on the nominal power step size. \n
			:return: structure: for return value, see the help for EpStepStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:PCONtrol:EPSTep?', self.__class__.EpStepStruct())
