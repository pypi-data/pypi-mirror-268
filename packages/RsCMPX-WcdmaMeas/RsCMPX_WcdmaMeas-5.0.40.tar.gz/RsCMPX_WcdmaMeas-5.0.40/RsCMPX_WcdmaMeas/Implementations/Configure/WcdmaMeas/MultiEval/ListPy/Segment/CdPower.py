from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CdPowerCls:
	"""CdPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cdPower", core, parent)

	def set(self, mod_statistics: int, enable_cdp: bool, enable_cde: bool, enable_pcde: bool = None, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:CDPower \n
		Snippet: driver.configure.wcdmaMeas.multiEval.listPy.segment.cdPower.set(mod_statistics = 1, enable_cdp = False, enable_cde = False, enable_pcde = False, segment = repcap.Segment.Default) \n
		Defines the statistical length for the AVERage, MINimum, MAXimum and SDEViation calculation and enables the calculation
		of the different code domain results in segment no. <no>; see 'Multi-evaluation list mode'. The statistical length for
		CDP, CDE, PCDE and modulation results is identical (see also method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.ListPy.
		Segment.Modulation.set) . \n
			:param mod_statistics: The statistical length is limited by the length of the segment (see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.ListPy.Segment.Setup.set) .
			:param enable_cdp: OFF: Disable measurement ON: Enable measurement of code domain power.
			:param enable_cde: Disable or enable measurement of code domain error.
			:param enable_pcde: Disable or enable measurement of peak code domain error.
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('mod_statistics', mod_statistics, DataType.Integer), ArgSingle('enable_cdp', enable_cdp, DataType.Boolean), ArgSingle('enable_cde', enable_cde, DataType.Boolean), ArgSingle('enable_pcde', enable_pcde, DataType.Boolean, None, is_optional=True))
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:CDPower {param}'.rstrip())

	# noinspection PyTypeChecker
	class CdPowerStruct(StructBase):
		"""Response structure. Fields: \n
			- Mod_Statistics: int: The statistical length is limited by the length of the segment (see [CMDLINKRESOLVED Configure.WcdmaMeas.MultiEval.ListPy.Segment.Setup#set CMDLINKRESOLVED]) .
			- Enable_Cdp: bool: OFF: Disable measurement ON: Enable measurement of code domain power.
			- Enable_Cde: bool: Disable or enable measurement of code domain error.
			- Enable_Pcde: bool: Disable or enable measurement of peak code domain error."""
		__meta_args_list = [
			ArgStruct.scalar_int('Mod_Statistics'),
			ArgStruct.scalar_bool('Enable_Cdp'),
			ArgStruct.scalar_bool('Enable_Cde'),
			ArgStruct.scalar_bool('Enable_Pcde')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mod_Statistics: int = None
			self.Enable_Cdp: bool = None
			self.Enable_Cde: bool = None
			self.Enable_Pcde: bool = None

	def get(self, segment=repcap.Segment.Default) -> CdPowerStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:CDPower \n
		Snippet: value: CdPowerStruct = driver.configure.wcdmaMeas.multiEval.listPy.segment.cdPower.get(segment = repcap.Segment.Default) \n
		Defines the statistical length for the AVERage, MINimum, MAXimum and SDEViation calculation and enables the calculation
		of the different code domain results in segment no. <no>; see 'Multi-evaluation list mode'. The statistical length for
		CDP, CDE, PCDE and modulation results is identical (see also method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.ListPy.
		Segment.Modulation.set) . \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for CdPowerStruct structure arguments."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:CDPower?', self.__class__.CdPowerStruct())
