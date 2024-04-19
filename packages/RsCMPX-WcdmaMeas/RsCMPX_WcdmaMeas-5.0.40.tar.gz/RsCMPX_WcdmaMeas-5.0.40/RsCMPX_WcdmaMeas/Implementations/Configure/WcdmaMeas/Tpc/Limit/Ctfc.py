from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CtfcCls:
	"""Ctfc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ctfc", core, parent)

	def set(self, power_step_limit: float, calc_beta_factors: bool, power_step_size: float = None) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:CTFC \n
		Snippet: driver.configure.wcdmaMeas.tpc.limit.ctfc.set(power_step_limit = 1.0, calc_beta_factors = False, power_step_size = 1.0) \n
		Configures a power step limit for the measurement mode Change of TFC. \n
			:param power_step_limit: Symmetrical tolerance value for the power step size.
			:param calc_beta_factors: Enables or disables the automatic calculation of the expected power step size from the configured beta factors.
			:param power_step_size: The expected power step size applicable if the automatic calculation from beta factors is disabled.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('power_step_limit', power_step_limit, DataType.Float), ArgSingle('calc_beta_factors', calc_beta_factors, DataType.Boolean), ArgSingle('power_step_size', power_step_size, DataType.Float, None, is_optional=True))
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:CTFC {param}'.rstrip())

	# noinspection PyTypeChecker
	class CtfcStruct(StructBase):
		"""Response structure. Fields: \n
			- Power_Step_Limit: float: Symmetrical tolerance value for the power step size.
			- Calc_Beta_Factors: bool: Enables or disables the automatic calculation of the expected power step size from the configured beta factors.
			- Power_Step_Size: float: The expected power step size applicable if the automatic calculation from beta factors is disabled."""
		__meta_args_list = [
			ArgStruct.scalar_float('Power_Step_Limit'),
			ArgStruct.scalar_bool('Calc_Beta_Factors'),
			ArgStruct.scalar_float('Power_Step_Size')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Power_Step_Limit: float = None
			self.Calc_Beta_Factors: bool = None
			self.Power_Step_Size: float = None

	def get(self) -> CtfcStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:CTFC \n
		Snippet: value: CtfcStruct = driver.configure.wcdmaMeas.tpc.limit.ctfc.get() \n
		Configures a power step limit for the measurement mode Change of TFC. \n
			:return: structure: for return value, see the help for CtfcStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:CTFC?', self.__class__.CtfcStruct())
