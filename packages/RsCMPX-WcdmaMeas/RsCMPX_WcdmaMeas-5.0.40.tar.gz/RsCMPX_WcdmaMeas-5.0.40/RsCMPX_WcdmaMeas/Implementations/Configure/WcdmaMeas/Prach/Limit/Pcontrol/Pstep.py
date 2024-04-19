from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PstepCls:
	"""Pstep commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pstep", core, parent)

	def set(self, enable: bool, preamble_pwr_step: float, pwr_step_limit: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:LIMit:PCONtrol:PSTep \n
		Snippet: driver.configure.wcdmaMeas.prach.limit.pcontrol.pstep.set(enable = False, preamble_pwr_step = 1.0, pwr_step_limit = 1.0) \n
		Enables or disables the check of the preamble power step limits and specifies these limits. \n
			:param enable: Disables | enables the limit check.
			:param preamble_pwr_step: Expected preamble power step size.
			:param pwr_step_limit: Preamble power step tolerance value.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('preamble_pwr_step', preamble_pwr_step, DataType.Float), ArgSingle('pwr_step_limit', pwr_step_limit, DataType.Float))
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:LIMit:PCONtrol:PSTep {param}'.rstrip())

	# noinspection PyTypeChecker
	class PstepStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: Disables | enables the limit check.
			- Preamble_Pwr_Step: float: Expected preamble power step size.
			- Pwr_Step_Limit: float: Preamble power step tolerance value."""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Preamble_Pwr_Step'),
			ArgStruct.scalar_float('Pwr_Step_Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Preamble_Pwr_Step: float = None
			self.Pwr_Step_Limit: float = None

	def get(self) -> PstepStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:LIMit:PCONtrol:PSTep \n
		Snippet: value: PstepStruct = driver.configure.wcdmaMeas.prach.limit.pcontrol.pstep.get() \n
		Enables or disables the check of the preamble power step limits and specifies these limits. \n
			:return: structure: for return value, see the help for PstepStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:LIMit:PCONtrol:PSTep?', self.__class__.PstepStruct())
