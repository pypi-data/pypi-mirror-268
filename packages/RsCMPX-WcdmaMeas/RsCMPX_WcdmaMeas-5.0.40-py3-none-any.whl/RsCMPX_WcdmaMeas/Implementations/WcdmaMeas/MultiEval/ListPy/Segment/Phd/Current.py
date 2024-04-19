from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator' In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Return_Code: int: Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Phd: List[float]: Comma-separated list of phase discontinuity results, one value per slot. The list contains results for the indicated segment no. If another measurement has been enabled for a segment, but the phase discontinuity measurement is disabled, NCAPs are returned for that segment."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Return_Code'),
			ArgStruct('Phd', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Return_Code: int = None
			self.Phd: List[float] = None

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:PHD:CURRent \n
		Snippet: value: FetchStruct = driver.wcdmaMeas.multiEval.listPy.segment.phd.current.fetch(segment = repcap.Segment.Default) \n
		Returns the phase discontinuity vs. slot results for segment <no> in list mode. Each value indicates the phase
		discontinuity at the boundary between the slot and the previous slot. If the slot or the previous slot is not measured,
		NCAP is returned. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:PHD:CURRent?', self.__class__.FetchStruct())
