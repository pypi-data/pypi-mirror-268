from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OlPowerCls:
	"""OlPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("olPower", core, parent)

	def set(self, enable: bool, init_preamble_pwr: float, olp_limit: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:LIMit:PCONtrol:OLPower \n
		Snippet: driver.configure.wcdmaMeas.prach.limit.pcontrol.olPower.set(enable = False, init_preamble_pwr = 1.0, olp_limit = 1.0) \n
		Enables or disables the check of the open loop power limits and specifies these limits. \n
			:param enable: Disables | enables the limit check.
			:param init_preamble_pwr: Initial preamble power
			:param olp_limit: Open loop power tolerance value.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('init_preamble_pwr', init_preamble_pwr, DataType.Float), ArgSingle('olp_limit', olp_limit, DataType.Float))
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:LIMit:PCONtrol:OLPower {param}'.rstrip())

	# noinspection PyTypeChecker
	class OlPowerStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: Disables | enables the limit check.
			- Init_Preamble_Pwr: float: Initial preamble power
			- Olp_Limit: float: Open loop power tolerance value."""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Init_Preamble_Pwr'),
			ArgStruct.scalar_float('Olp_Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Init_Preamble_Pwr: float = None
			self.Olp_Limit: float = None

	def get(self) -> OlPowerStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:LIMit:PCONtrol:OLPower \n
		Snippet: value: OlPowerStruct = driver.configure.wcdmaMeas.prach.limit.pcontrol.olPower.get() \n
		Enables or disables the check of the open loop power limits and specifies these limits. \n
			:return: structure: for return value, see the help for OlPowerStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:LIMit:PCONtrol:OLPower?', self.__class__.OlPowerStruct())
