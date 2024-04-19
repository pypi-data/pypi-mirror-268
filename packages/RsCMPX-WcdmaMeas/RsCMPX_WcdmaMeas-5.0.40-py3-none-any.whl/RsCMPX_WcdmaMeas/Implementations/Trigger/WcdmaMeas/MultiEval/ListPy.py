from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPyCls:
	"""ListPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.Mode:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:MEValuation:LIST:MODE \n
		Snippet: value: enums.Mode = driver.trigger.wcdmaMeas.multiEval.listPy.get_mode() \n
		Specifies the trigger mode for list mode measurements. For configuration of retrigger flags, see method RsCMPX_WcdmaMeas.
		Configure.WcdmaMeas.MultiEval.ListPy.Segment.Setup.set. \n
			:return: mode: ONCE: A trigger event is only required to start the measurement. As a result, the entire range of segments to be measured is captured without additional trigger event. The retrigger flags of the segments are ignored. SEGMent: The retrigger flag of each segment is evaluated. It defines whether the measurement waits for a trigger event before capturing the segment, or not.
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:MEValuation:LIST:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.Mode)

	def set_mode(self, mode: enums.Mode) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:MEValuation:LIST:MODE \n
		Snippet: driver.trigger.wcdmaMeas.multiEval.listPy.set_mode(mode = enums.Mode.ONCE) \n
		Specifies the trigger mode for list mode measurements. For configuration of retrigger flags, see method RsCMPX_WcdmaMeas.
		Configure.WcdmaMeas.MultiEval.ListPy.Segment.Setup.set. \n
			:param mode: ONCE: A trigger event is only required to start the measurement. As a result, the entire range of segments to be measured is captured without additional trigger event. The retrigger flags of the segments are ignored. SEGMent: The retrigger flag of each segment is evaluated. It defines whether the measurement waits for a trigger event before capturing the segment, or not.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.Mode)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:MEValuation:LIST:MODE {param}')
