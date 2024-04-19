from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PaCls:
	"""Pa commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pa", core, parent)

	def set(self, initial_pwr_step: float or bool, power_step: float or bool, power_step_group: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ULCM:PA \n
		Snippet: driver.configure.wcdmaMeas.tpc.limit.ulcm.pa.set(initial_pwr_step = 1.0, power_step = 1.0, power_step_group = 1.0) \n
		Configures a power step limit for the measurement mode UL Compressed Mode, CM pattern A. \n
			:param initial_pwr_step: (float or boolean) Symmetrical tolerance value for UE TX power in the first slot after the gap
			:param power_step: (float or boolean) Symmetrical tolerance value for UE TX power in a recovery period
			:param power_step_group: (float or boolean) Symmetrical tolerance value for the aggregate UE TX power in the recovery period comprising the 7 rising or falling power steps after each gap
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('initial_pwr_step', initial_pwr_step, DataType.FloatExt), ArgSingle('power_step', power_step, DataType.FloatExt), ArgSingle('power_step_group', power_step_group, DataType.FloatExt))
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ULCM:PA {param}'.rstrip())

	# noinspection PyTypeChecker
	class PaStruct(StructBase):
		"""Response structure. Fields: \n
			- Initial_Pwr_Step: float or bool: Symmetrical tolerance value for UE TX power in the first slot after the gap
			- Power_Step: float or bool: Symmetrical tolerance value for UE TX power in a recovery period
			- Power_Step_Group: float or bool: Symmetrical tolerance value for the aggregate UE TX power in the recovery period comprising the 7 rising or falling power steps after each gap"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Initial_Pwr_Step'),
			ArgStruct.scalar_float_ext('Power_Step'),
			ArgStruct.scalar_float_ext('Power_Step_Group')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Initial_Pwr_Step: float or bool = None
			self.Power_Step: float or bool = None
			self.Power_Step_Group: float or bool = None

	def get(self) -> PaStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ULCM:PA \n
		Snippet: value: PaStruct = driver.configure.wcdmaMeas.tpc.limit.ulcm.pa.get() \n
		Configures a power step limit for the measurement mode UL Compressed Mode, CM pattern A. \n
			:return: structure: for return value, see the help for PaStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ULCM:PA?', self.__class__.PaStruct())
