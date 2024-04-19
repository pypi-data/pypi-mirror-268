from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator' In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Return_Code: int: Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Pcd_Error: float: Peak code domain error
			- Pcd_Error_Phase: enums.PcdErrorPhase: No parameter help available
			- Pcd_Error_Code_Nr: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Return_Code'),
			ArgStruct.scalar_float('Pcd_Error'),
			ArgStruct.scalar_enum('Pcd_Error_Phase', enums.PcdErrorPhase),
			ArgStruct.scalar_int('Pcd_Error_Code_Nr')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Return_Code: int = None
			self.Pcd_Error: float = None
			self.Pcd_Error_Phase: enums.PcdErrorPhase = None
			self.Pcd_Error_Code_Nr: int = None

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:PCDE:MAXimum \n
		Snippet: value: FetchStruct = driver.wcdmaMeas.multiEval.listPy.segment.pcde.maximum.fetch(segment = repcap.Segment.Default) \n
		Returns the peak code domain error (PCDE) results for segment <no> in list mode. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:PCDE:MAXimum?', self.__class__.FetchStruct())
