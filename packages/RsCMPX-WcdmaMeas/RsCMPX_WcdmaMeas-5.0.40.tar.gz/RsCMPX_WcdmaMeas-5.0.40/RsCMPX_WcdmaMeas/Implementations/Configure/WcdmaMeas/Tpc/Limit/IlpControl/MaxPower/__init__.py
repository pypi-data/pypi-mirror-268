from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaxPowerCls:
	"""MaxPower commands group definition. 4 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maxPower", core, parent)

	@property
	def userDefined(self):
		"""userDefined commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_userDefined'):
			from .UserDefined import UserDefinedCls
			self._userDefined = UserDefinedCls(self._core, self._cmd_group)
		return self._userDefined

	def get_urp_class(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:MAXPower:URPClass \n
		Snippet: value: bool = driver.configure.wcdmaMeas.tpc.limit.ilpControl.maxPower.get_urp_class() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:MAXPower:URPClass?')
		return Conversions.str_to_bool(response)

	def set_urp_class(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:MAXPower:URPClass \n
		Snippet: driver.configure.wcdmaMeas.tpc.limit.ilpControl.maxPower.set_urp_class(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:MAXPower:URPClass {param}')

	def set(self, enable: bool, active_limit: enums.ActiveLimit) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:MAXPower \n
		Snippet: driver.configure.wcdmaMeas.tpc.limit.ilpControl.maxPower.set(enable = False, active_limit = enums.ActiveLimit.PC1) \n
		Enables or disables the check of the maximum UE output power limits for the Inner Loop Power Control mode and selects the
		set of limit settings to be used. \n
			:param enable: Disables | enables the limit check.
			:param active_limit: To use the limits defined by 3GPP, select the power class of the UE (PC1 to PC4 = power class 1, 2, 3, 3bis, 4) . For user-defined limit values, select USER and define the limits via method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.Tpc.Limit.IlpControl.MaxPower.UserDefined.set.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('active_limit', active_limit, DataType.Enum, enums.ActiveLimit))
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:MAXPower {param}'.rstrip())

	# noinspection PyTypeChecker
	class MaxPowerStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: Disables | enables the limit check.
			- Active_Limit: enums.ActiveLimit: To use the limits defined by 3GPP, select the power class of the UE (PC1 to PC4 = power class 1, 2, 3, 3bis, 4) . For user-defined limit values, select USER and define the limits via [CMDLINKRESOLVED Configure.WcdmaMeas.Tpc.Limit.IlpControl.MaxPower.UserDefined#set CMDLINKRESOLVED]."""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Active_Limit', enums.ActiveLimit)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Active_Limit: enums.ActiveLimit = None

	def get(self) -> MaxPowerStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:MAXPower \n
		Snippet: value: MaxPowerStruct = driver.configure.wcdmaMeas.tpc.limit.ilpControl.maxPower.get() \n
		Enables or disables the check of the maximum UE output power limits for the Inner Loop Power Control mode and selects the
		set of limit settings to be used. \n
			:return: structure: for return value, see the help for MaxPowerStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:MAXPower?', self.__class__.MaxPowerStruct())

	# noinspection PyTypeChecker
	class ActiveStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
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

	def get_active(self) -> ActiveStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:MAXPower:ACTive \n
		Snippet: value: ActiveStruct = driver.configure.wcdmaMeas.tpc.limit.ilpControl.maxPower.get_active() \n
		Queries the active limit values for the Inner Loop Power Control mode. These limit values result either from the
		configured UE power class or from the reported UE power class or have been defined manually. \n
			:return: structure: for return value, see the help for ActiveStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:MAXPower:ACTive?', self.__class__.ActiveStruct())

	def clone(self) -> 'MaxPowerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MaxPowerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
