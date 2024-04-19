from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MinPowerCls:
	"""MinPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minPower", core, parent)

	def set(self, enable: bool, upper_limit: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:MINPower \n
		Snippet: driver.configure.wcdmaMeas.tpc.limit.ilpControl.minPower.set(enable = False, upper_limit = 1.0) \n
		Defines an Inner Loop Power Control limit: upper limit for the minimum UE output power. Also it enables or disables the
		limit check. \n
			:param enable: Disables | enables the limit check.
			:param upper_limit: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('upper_limit', upper_limit, DataType.Float))
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:MINPower {param}'.rstrip())

	# noinspection PyTypeChecker
	class MinPowerStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: Disables | enables the limit check.
			- Upper_Limit: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Upper_Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Upper_Limit: float = None

	def get(self) -> MinPowerStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:MINPower \n
		Snippet: value: MinPowerStruct = driver.configure.wcdmaMeas.tpc.limit.ilpControl.minPower.get() \n
		Defines an Inner Loop Power Control limit: upper limit for the minimum UE output power. Also it enables or disables the
		limit check. \n
			:return: structure: for return value, see the help for MinPowerStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:MINPower?', self.__class__.MinPowerStruct())
