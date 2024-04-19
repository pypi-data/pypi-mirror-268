from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RelativeCls:
	"""Relative commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("relative", core, parent)

	def set(self, channel_first: float or bool, channel_second: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:ACLR:RELative \n
		Snippet: driver.configure.wcdmaMeas.multiEval.limit.aclr.relative.set(channel_first = 1.0, channel_second = 1.0) \n
		Defines upper limits for the ACLR in channels one and two relative to the carrier power. Relative limits are only
		evaluated when the absolute limit is exceeded (method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Limit.Aclr.absolute)
		. \n
			:param channel_first: (float or boolean) For single uplink carrier: ±5 MHz from the center frequency For dual uplink carrier: ±7.5 MHz from the center frequency of both carriers
			:param channel_second: (float or boolean) For single uplink carrier: ±10 MHz from the center frequency For dual uplink carrier: ±12.5 MHz from the center frequency of both carriers
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('channel_first', channel_first, DataType.FloatExt), ArgSingle('channel_second', channel_second, DataType.FloatExt))
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:ACLR:RELative {param}'.rstrip())

	# noinspection PyTypeChecker
	class RelativeStruct(StructBase):
		"""Response structure. Fields: \n
			- Channel_First: float or bool: For single uplink carrier: ±5 MHz from the center frequency For dual uplink carrier: ±7.5 MHz from the center frequency of both carriers
			- Channel_Second: float or bool: For single uplink carrier: ±10 MHz from the center frequency For dual uplink carrier: ±12.5 MHz from the center frequency of both carriers"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Channel_First'),
			ArgStruct.scalar_float_ext('Channel_Second')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Channel_First: float or bool = None
			self.Channel_Second: float or bool = None

	def get(self) -> RelativeStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:ACLR:RELative \n
		Snippet: value: RelativeStruct = driver.configure.wcdmaMeas.multiEval.limit.aclr.relative.get() \n
		Defines upper limits for the ACLR in channels one and two relative to the carrier power. Relative limits are only
		evaluated when the absolute limit is exceeded (method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Limit.Aclr.absolute)
		. \n
			:return: structure: for return value, see the help for RelativeStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:ACLR:RELative?', self.__class__.RelativeStruct())
