from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpectrumCls:
	"""Spectrum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spectrum", core, parent)

	def set(self, spec_statistics: int, enable_aclr: bool, enable_emask: bool, enable_obw: bool, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:SPECtrum \n
		Snippet: driver.configure.wcdmaMeas.multiEval.listPy.segment.spectrum.set(spec_statistics = 1, enable_aclr = False, enable_emask = False, enable_obw = False, segment = repcap.Segment.Default) \n
		Defines the statistical length for the AVERage and MAXimum calculation and enables the calculation of the different
		spectrum results in segment no. <no>; see 'Multi-evaluation list mode'. \n
			:param spec_statistics: The statistical length is limited by the length of the segment (see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.ListPy.Segment.Setup.set) .
			:param enable_aclr: OFF: Disable measurement. ON: Enable measurement of ACLR.
			:param enable_emask: Disable or enable measurement of spectrum emission mask.
			:param enable_obw: Disable or enable measurement of occupied bandwidth.
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('spec_statistics', spec_statistics, DataType.Integer), ArgSingle('enable_aclr', enable_aclr, DataType.Boolean), ArgSingle('enable_emask', enable_emask, DataType.Boolean), ArgSingle('enable_obw', enable_obw, DataType.Boolean))
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SPECtrum {param}'.rstrip())

	# noinspection PyTypeChecker
	class SpectrumStruct(StructBase):
		"""Response structure. Fields: \n
			- Spec_Statistics: int: The statistical length is limited by the length of the segment (see [CMDLINKRESOLVED Configure.WcdmaMeas.MultiEval.ListPy.Segment.Setup#set CMDLINKRESOLVED]) .
			- Enable_Aclr: bool: OFF: Disable measurement. ON: Enable measurement of ACLR.
			- Enable_Emask: bool: Disable or enable measurement of spectrum emission mask.
			- Enable_Obw: bool: Disable or enable measurement of occupied bandwidth."""
		__meta_args_list = [
			ArgStruct.scalar_int('Spec_Statistics'),
			ArgStruct.scalar_bool('Enable_Aclr'),
			ArgStruct.scalar_bool('Enable_Emask'),
			ArgStruct.scalar_bool('Enable_Obw')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Spec_Statistics: int = None
			self.Enable_Aclr: bool = None
			self.Enable_Emask: bool = None
			self.Enable_Obw: bool = None

	def get(self, segment=repcap.Segment.Default) -> SpectrumStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:SPECtrum \n
		Snippet: value: SpectrumStruct = driver.configure.wcdmaMeas.multiEval.listPy.segment.spectrum.get(segment = repcap.Segment.Default) \n
		Defines the statistical length for the AVERage and MAXimum calculation and enables the calculation of the different
		spectrum results in segment no. <no>; see 'Multi-evaluation list mode'. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for SpectrumStruct structure arguments."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SPECtrum?', self.__class__.SpectrumStruct())
