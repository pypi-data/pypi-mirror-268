from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AbsoluteCls:
	"""Absolute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("absolute", core, parent)

	def set(self, limit_g_3_m_84: float or bool, limit_h_1_mhz: float or bool, limit_h_30_khz: float or bool, limit_hmode: enums.LimitHmode) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:EMASk:ABSolute \n
		Snippet: driver.configure.wcdmaMeas.multiEval.limit.emask.absolute.set(limit_g_3_m_84 = 1.0, limit_h_1_mhz = 1.0, limit_h_30_khz = 1.0, limit_hmode = enums.LimitHmode.A) \n
		Defines absolute limits for the spectrum emission curves. \n
			:param limit_g_3_m_84: (float or boolean) Absolute limit line G referenced to a 3.84 MHz filter.
			:param limit_h_1_mhz: (float or boolean) Absolute limit line H is referenced to a 1 MHz or 100 kHz filter, depending on the line H mode.
			:param limit_h_30_khz: (float or boolean) Absolute limit line H referenced to a 30 kHz filter.
			:param limit_hmode: Line H mode
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('limit_g_3_m_84', limit_g_3_m_84, DataType.FloatExt), ArgSingle('limit_h_1_mhz', limit_h_1_mhz, DataType.FloatExt), ArgSingle('limit_h_30_khz', limit_h_30_khz, DataType.FloatExt), ArgSingle('limit_hmode', limit_hmode, DataType.Enum, enums.LimitHmode))
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:EMASk:ABSolute {param}'.rstrip())

	# noinspection PyTypeChecker
	class AbsoluteStruct(StructBase):
		"""Response structure. Fields: \n
			- Limit_G_3_M_84: float or bool: Absolute limit line G referenced to a 3.84 MHz filter.
			- Limit_H_1_Mhz: float or bool: Absolute limit line H is referenced to a 1 MHz or 100 kHz filter, depending on the line H mode.
			- Limit_H_30_Khz: float or bool: Absolute limit line H referenced to a 30 kHz filter.
			- Limit_Hmode: enums.LimitHmode: Line H mode"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Limit_G_3_M_84'),
			ArgStruct.scalar_float_ext('Limit_H_1_Mhz'),
			ArgStruct.scalar_float_ext('Limit_H_30_Khz'),
			ArgStruct.scalar_enum('Limit_Hmode', enums.LimitHmode)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Limit_G_3_M_84: float or bool = None
			self.Limit_H_1_Mhz: float or bool = None
			self.Limit_H_30_Khz: float or bool = None
			self.Limit_Hmode: enums.LimitHmode = None

	def get(self) -> AbsoluteStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:EMASk:ABSolute \n
		Snippet: value: AbsoluteStruct = driver.configure.wcdmaMeas.multiEval.limit.emask.absolute.get() \n
		Defines absolute limits for the spectrum emission curves. \n
			:return: structure: for return value, see the help for AbsoluteStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:EMASk:ABSolute?', self.__class__.AbsoluteStruct())
