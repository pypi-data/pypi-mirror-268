from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PhdCls:
	"""Phd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phd", core, parent)

	def set(self, enable: bool, upper: float, dynamic: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:PHD \n
		Snippet: driver.configure.wcdmaMeas.multiEval.limit.phd.set(enable = False, upper = 1.0, dynamic = 1.0) \n
		Defines upper and dynamic limits for the phase discontinuity determined by full-slot measurements (signals without HSPA
		channels) . \n
			:param enable: Disables | enables the limit check.
			:param upper: No help available
			:param dynamic: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('upper', upper, DataType.Float), ArgSingle('dynamic', dynamic, DataType.Float))
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:PHD {param}'.rstrip())

	# noinspection PyTypeChecker
	class PhdStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: Disables | enables the limit check.
			- Upper: float: No parameter help available
			- Dynamic: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Upper'),
			ArgStruct.scalar_float('Dynamic')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Upper: float = None
			self.Dynamic: float = None

	def get(self) -> PhdStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:PHD \n
		Snippet: value: PhdStruct = driver.configure.wcdmaMeas.multiEval.limit.phd.get() \n
		Defines upper and dynamic limits for the phase discontinuity determined by full-slot measurements (signals without HSPA
		channels) . \n
			:return: structure: for return value, see the help for PhdStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:PHD?', self.__class__.PhdStruct())
