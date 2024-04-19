from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EmaskCls:
	"""Emask commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("emask", core, parent)

	@property
	def dcarrier(self):
		"""dcarrier commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dcarrier'):
			from .Dcarrier import DcarrierCls
			self._dcarrier = DcarrierCls(self._core, self._cmd_group)
		return self._dcarrier

	@property
	def absolute(self):
		"""absolute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_absolute'):
			from .Absolute import AbsoluteCls
			self._absolute = AbsoluteCls(self._core, self._cmd_group)
		return self._absolute

	# noinspection PyTypeChecker
	class RelativeStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Point_A: float or bool: No parameter help available
			- Point_B: float or bool: No parameter help available
			- Point_C: float or bool: No parameter help available
			- Point_D: float or bool: No parameter help available
			- Point_E: float or bool: No parameter help available
			- Point_F: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Point_A'),
			ArgStruct.scalar_float_ext('Point_B'),
			ArgStruct.scalar_float_ext('Point_C'),
			ArgStruct.scalar_float_ext('Point_D'),
			ArgStruct.scalar_float_ext('Point_E'),
			ArgStruct.scalar_float_ext('Point_F')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Point_A: float or bool = None
			self.Point_B: float or bool = None
			self.Point_C: float or bool = None
			self.Point_D: float or bool = None
			self.Point_E: float or bool = None
			self.Point_F: float or bool = None

	def get_relative(self) -> RelativeStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:EMASk:RELative \n
		Snippet: value: RelativeStruct = driver.configure.wcdmaMeas.multiEval.limit.emask.get_relative() \n
		Defines relative limits for the spectrum emission curves. \n
			:return: structure: for return value, see the help for RelativeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:EMASk:RELative?', self.__class__.RelativeStruct())

	def set_relative(self, value: RelativeStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:EMASk:RELative \n
		Snippet with structure: \n
		structure = driver.configure.wcdmaMeas.multiEval.limit.emask.RelativeStruct() \n
		structure.Point_A: float or bool = 1.0 \n
		structure.Point_B: float or bool = 1.0 \n
		structure.Point_C: float or bool = 1.0 \n
		structure.Point_D: float or bool = 1.0 \n
		structure.Point_E: float or bool = 1.0 \n
		structure.Point_F: float or bool = 1.0 \n
		driver.configure.wcdmaMeas.multiEval.limit.emask.set_relative(value = structure) \n
		Defines relative limits for the spectrum emission curves. \n
			:param value: see the help for RelativeStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:EMASk:RELative', value)

	def clone(self) -> 'EmaskCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EmaskCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
