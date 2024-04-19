from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SetupCls:
	"""Setup commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("setup", core, parent)

	def set(self, segment_length: int, level: float, frequency: float, retrigger: enums.Retrigger = None, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:SETup \n
		Snippet: driver.configure.wcdmaMeas.multiEval.listPy.segment.setup.set(segment_length = 1, level = 1.0, frequency = 1.0, retrigger = enums.Retrigger.IFPower, segment = repcap.Segment.Default) \n
		Defines the length and analyzer settings of a selected segment. In general, this command must be sent for all segments
		measured. \n
			:param segment_length: Number of measured timeslots in the segment. The sum of the length of all active segments must not exceed 6000. Ignoring this limit results in NCAPs for the remaining slots. The statistical length for result calculation covers at most the first 1000 slots of a segment. The sum of the length of all segments (active plus inactive) must not exceed 12000. 'Inactive' means that no measurement at all is enabled for the segment.
			:param level: Expected nominal power in the segment. The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the specifications document.
			:param frequency: No help available
			:param retrigger: Specifies whether a trigger event is required for the segment or not. The setting is ignored for the first segment of a measurement and for trigger mode ONCE (see method RsCMPX_WcdmaMeas.Trigger.WcdmaMeas.MultiEval.ListPy.mode) . OFF: measure the segment without retrigger ON: trigger event required, trigger source configured via method RsCMPX_WcdmaMeas.Trigger.WcdmaMeas.MultiEval.source IFPower: trigger event required, IF Power trigger IFPSync: trigger event required, IF Power (Sync) trigger
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('segment_length', segment_length, DataType.Integer), ArgSingle('level', level, DataType.Float), ArgSingle('frequency', frequency, DataType.Float), ArgSingle('retrigger', retrigger, DataType.Enum, enums.Retrigger, is_optional=True))
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup {param}'.rstrip())

	# noinspection PyTypeChecker
	class SetupStruct(StructBase):
		"""Response structure. Fields: \n
			- Segment_Length: int: Number of measured timeslots in the segment. The sum of the length of all active segments must not exceed 6000. Ignoring this limit results in NCAPs for the remaining slots. The statistical length for result calculation covers at most the first 1000 slots of a segment. The sum of the length of all segments (active plus inactive) must not exceed 12000. 'Inactive' means that no measurement at all is enabled for the segment.
			- Level: float: Expected nominal power in the segment. The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the specifications document.
			- Frequency: float: No parameter help available
			- Retrigger: enums.Retrigger: Specifies whether a trigger event is required for the segment or not. The setting is ignored for the first segment of a measurement and for trigger mode ONCE (see [CMDLINKRESOLVED Trigger.WcdmaMeas.MultiEval.ListPy#Mode CMDLINKRESOLVED]) . OFF: measure the segment without retrigger ON: trigger event required, trigger source configured via [CMDLINKRESOLVED Trigger.WcdmaMeas.MultiEval#Source CMDLINKRESOLVED] IFPower: trigger event required, IF Power trigger IFPSync: trigger event required, IF Power (Sync) trigger"""
		__meta_args_list = [
			ArgStruct.scalar_int('Segment_Length'),
			ArgStruct.scalar_float('Level'),
			ArgStruct.scalar_float('Frequency'),
			ArgStruct.scalar_enum('Retrigger', enums.Retrigger)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Segment_Length: int = None
			self.Level: float = None
			self.Frequency: float = None
			self.Retrigger: enums.Retrigger = None

	def get(self, segment=repcap.Segment.Default) -> SetupStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:SETup \n
		Snippet: value: SetupStruct = driver.configure.wcdmaMeas.multiEval.listPy.segment.setup.get(segment = repcap.Segment.Default) \n
		Defines the length and analyzer settings of a selected segment. In general, this command must be sent for all segments
		measured. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for SetupStruct structure arguments."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup?', self.__class__.SetupStruct())
