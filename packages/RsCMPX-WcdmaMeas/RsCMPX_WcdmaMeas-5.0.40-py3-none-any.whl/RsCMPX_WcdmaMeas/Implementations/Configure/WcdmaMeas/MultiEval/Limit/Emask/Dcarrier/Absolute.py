from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AbsoluteCls:
	"""Absolute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("absolute", core, parent)

	def set(self, point_ij: float or bool, point_jk: float or bool, point_kl: float or bool, point_mn: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:EMASk:DCARrier:ABSolute \n
		Snippet: driver.configure.wcdmaMeas.multiEval.limit.emask.dcarrier.absolute.set(point_ij = 1.0, point_jk = 1.0, point_kl = 1.0, point_mn = 1.0) \n
		Defines absolute limits for the spectrum emission curves of DC HSPA connections. \n
			:param point_ij: (float or boolean) Absolute limit line I-J referenced to a 1 MHz filter.
			:param point_jk: (float or boolean) Absolute limit line J-K referenced to a 1 MHz filter.
			:param point_kl: (float or boolean) Absolute limit line K-L referenced to a 1 MHz filter.
			:param point_mn: (float or boolean) Absolute limit line M-N referenced to a 30 kHz filter.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('point_ij', point_ij, DataType.FloatExt), ArgSingle('point_jk', point_jk, DataType.FloatExt), ArgSingle('point_kl', point_kl, DataType.FloatExt), ArgSingle('point_mn', point_mn, DataType.FloatExt))
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:EMASk:DCARrier:ABSolute {param}'.rstrip())

	# noinspection PyTypeChecker
	class AbsoluteStruct(StructBase):
		"""Response structure. Fields: \n
			- Point_Ij: float or bool: Absolute limit line I-J referenced to a 1 MHz filter.
			- Point_Jk: float or bool: Absolute limit line J-K referenced to a 1 MHz filter.
			- Point_Kl: float or bool: Absolute limit line K-L referenced to a 1 MHz filter.
			- Point_Mn: float or bool: Absolute limit line M-N referenced to a 30 kHz filter."""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Point_Ij'),
			ArgStruct.scalar_float_ext('Point_Jk'),
			ArgStruct.scalar_float_ext('Point_Kl'),
			ArgStruct.scalar_float_ext('Point_Mn')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Point_Ij: float or bool = None
			self.Point_Jk: float or bool = None
			self.Point_Kl: float or bool = None
			self.Point_Mn: float or bool = None

	def get(self) -> AbsoluteStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:EMASk:DCARrier:ABSolute \n
		Snippet: value: AbsoluteStruct = driver.configure.wcdmaMeas.multiEval.limit.emask.dcarrier.absolute.get() \n
		Defines absolute limits for the spectrum emission curves of DC HSPA connections. \n
			:return: structure: for return value, see the help for AbsoluteStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:EMASk:DCARrier:ABSolute?', self.__class__.AbsoluteStruct())
