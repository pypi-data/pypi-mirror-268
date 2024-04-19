from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MpedchCls:
	"""Mpedch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mpedch", core, parent)

	def set(self, enable: bool, nom_max_power: float, upper_limit: float, lower_limit: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:MPEDch \n
		Snippet: driver.configure.wcdmaMeas.tpc.limit.mpedch.set(enable = False, nom_max_power = 1.0, upper_limit = 1.0, lower_limit = 1.0) \n
		Configures UE power limits for the measurement mode Max. Power E-DCH. \n
			:param enable: Disables | enables the limit check.
			:param nom_max_power: Nominal maximum UE power.
			:param upper_limit: Upper limit = nominal power + this value.
			:param lower_limit: Lower limit = nominal power + this value.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('nom_max_power', nom_max_power, DataType.Float), ArgSingle('upper_limit', upper_limit, DataType.Float), ArgSingle('lower_limit', lower_limit, DataType.Float))
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:MPEDch {param}'.rstrip())

	# noinspection PyTypeChecker
	class MpedchStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: Disables | enables the limit check.
			- Nom_Max_Power: float: Nominal maximum UE power.
			- Upper_Limit: float: Upper limit = nominal power + this value.
			- Lower_Limit: float: Lower limit = nominal power + this value."""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Nom_Max_Power'),
			ArgStruct.scalar_float('Upper_Limit'),
			ArgStruct.scalar_float('Lower_Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Nom_Max_Power: float = None
			self.Upper_Limit: float = None
			self.Lower_Limit: float = None

	def get(self) -> MpedchStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:MPEDch \n
		Snippet: value: MpedchStruct = driver.configure.wcdmaMeas.tpc.limit.mpedch.get() \n
		Configures UE power limits for the measurement mode Max. Power E-DCH. \n
			:return: structure: for return value, see the help for MpedchStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:MPEDch?', self.__class__.MpedchStruct())
