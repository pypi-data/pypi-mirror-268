from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UserDefinedCls:
	"""UserDefined commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("userDefined", core, parent)

	def set(self, nominal_max_power: float, upper_limit: float, lower_limit: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:LIMit:PCONtrol:MAXPower:UDEFined \n
		Snippet: driver.configure.wcdmaMeas.prach.limit.pcontrol.maxPower.userDefined.set(nominal_max_power = 1.0, upper_limit = 1.0, lower_limit = 1.0) \n
		Sets the user-defined maximum output power limits. To activate the usage of this limit set, see method RsCMPX_WcdmaMeas.
		Configure.WcdmaMeas.Prach.Limit.Pcontrol.MaxPower.set. \n
			:param nominal_max_power: Nominal maximum output power of the UE
			:param upper_limit: Tolerance value for too high maximum UE power
			:param lower_limit: Tolerance value for too low maximum UE power
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('nominal_max_power', nominal_max_power, DataType.Float), ArgSingle('upper_limit', upper_limit, DataType.Float), ArgSingle('lower_limit', lower_limit, DataType.Float))
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:LIMit:PCONtrol:MAXPower:UDEFined {param}'.rstrip())

	# noinspection PyTypeChecker
	class UserDefinedStruct(StructBase):
		"""Response structure. Fields: \n
			- Nominal_Max_Power: float: Nominal maximum output power of the UE
			- Upper_Limit: float: Tolerance value for too high maximum UE power
			- Lower_Limit: float: Tolerance value for too low maximum UE power"""
		__meta_args_list = [
			ArgStruct.scalar_float('Nominal_Max_Power'),
			ArgStruct.scalar_float('Upper_Limit'),
			ArgStruct.scalar_float('Lower_Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Nominal_Max_Power: float = None
			self.Upper_Limit: float = None
			self.Lower_Limit: float = None

	def get(self) -> UserDefinedStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:LIMit:PCONtrol:MAXPower:UDEFined \n
		Snippet: value: UserDefinedStruct = driver.configure.wcdmaMeas.prach.limit.pcontrol.maxPower.userDefined.get() \n
		Sets the user-defined maximum output power limits. To activate the usage of this limit set, see method RsCMPX_WcdmaMeas.
		Configure.WcdmaMeas.Prach.Limit.Pcontrol.MaxPower.set. \n
			:return: structure: for return value, see the help for UserDefinedStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:LIMit:PCONtrol:MAXPower:UDEFined?', self.__class__.UserDefinedStruct())
