from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator' In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Return_Code: int: Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Dpcch: float: RMS CDE values for the indicated channels
			- Dpdch: float: RMS CDE values for the indicated channels
			- Hsdpcch: float: RMS CDE values for the indicated channels
			- Edpcch: float: RMS CDE values for the indicated channels
			- Edpdch_1: float: RMS CDE values for the indicated channels
			- Edpdch_2: float: RMS CDE values for the indicated channels
			- Edpdch_3: float: RMS CDE values for the indicated channels
			- Edpdch_4: float: RMS CDE values for the indicated channels"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Return_Code'),
			ArgStruct.scalar_float('Dpcch'),
			ArgStruct.scalar_float('Dpdch'),
			ArgStruct.scalar_float('Hsdpcch'),
			ArgStruct.scalar_float('Edpcch'),
			ArgStruct.scalar_float('Edpdch_1'),
			ArgStruct.scalar_float('Edpdch_2'),
			ArgStruct.scalar_float('Edpdch_3'),
			ArgStruct.scalar_float('Edpdch_4')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Return_Code: int = None
			self.Dpcch: float = None
			self.Dpdch: float = None
			self.Hsdpcch: float = None
			self.Edpcch: float = None
			self.Edpdch_1: float = None
			self.Edpdch_2: float = None
			self.Edpdch_3: float = None
			self.Edpdch_4: float = None

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:CDERror:AVERage \n
		Snippet: value: FetchStruct = driver.wcdmaMeas.multiEval.listPy.segment.cdError.average.fetch(segment = repcap.Segment.Default) \n
		Returns the RMS CDE vs. slot results for segment <no> in list mode. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:CDERror:AVERage?', self.__class__.FetchStruct())
