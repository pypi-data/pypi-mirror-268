from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PbCls:
	"""Pb commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pb", core, parent)

	def set(self, initial_pwr_step: float or bool, power_step: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ULCM:PB \n
		Snippet: driver.configure.wcdmaMeas.tpc.limit.ulcm.pb.set(initial_pwr_step = 1.0, power_step = 1.0) \n
		Configures a power step limit for the measurement mode UL Compressed Mode, CM pattern B. \n
			:param initial_pwr_step: (float or boolean) Symmetrical tolerance value for the UE TX power in the first slot after the gap
			:param power_step: (float or boolean) Symmetrical tolerance value for the UE TX power in the nonCM - CM and CM - nonCM power step
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('initial_pwr_step', initial_pwr_step, DataType.FloatExt), ArgSingle('power_step', power_step, DataType.FloatExt))
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ULCM:PB {param}'.rstrip())

	# noinspection PyTypeChecker
	class PbStruct(StructBase):
		"""Response structure. Fields: \n
			- Initial_Pwr_Step: float or bool: Symmetrical tolerance value for the UE TX power in the first slot after the gap
			- Power_Step: float or bool: Symmetrical tolerance value for the UE TX power in the nonCM - CM and CM - nonCM power step"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Initial_Pwr_Step'),
			ArgStruct.scalar_float_ext('Power_Step')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Initial_Pwr_Step: float or bool = None
			self.Power_Step: float or bool = None

	def get(self) -> PbStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ULCM:PB \n
		Snippet: value: PbStruct = driver.configure.wcdmaMeas.tpc.limit.ulcm.pb.get() \n
		Configures a power step limit for the measurement mode UL Compressed Mode, CM pattern B. \n
			:return: structure: for return value, see the help for PbStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ULCM:PB?', self.__class__.PbStruct())
