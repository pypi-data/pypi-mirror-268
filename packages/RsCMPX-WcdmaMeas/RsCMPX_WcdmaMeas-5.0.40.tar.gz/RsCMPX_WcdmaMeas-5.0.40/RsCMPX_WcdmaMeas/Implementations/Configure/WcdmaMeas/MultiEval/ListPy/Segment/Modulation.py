from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModulationCls:
	"""Modulation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	# noinspection PyTypeChecker
	class ModulationStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Mod_Statistics: int: The statistical length is limited by the length of the segment (see [CMDLINKRESOLVED Configure.WcdmaMeas.MultiEval.ListPy.Segment.Setup#set CMDLINKRESOLVED]) .
			- Enable_Ue_Power: bool: OFF: Disable measurement. ON: Enable measurement of UE power.
			- Enable_Evm: bool: Disable or enable measurement of EVM.
			- Enable_Mag_Error: bool: Disable or enable measurement of magnitude error.
			- Enable_Phase_Err: bool: Disable or enable measurement of phase error.
			- Enable_Freq_Error: bool: Disable or enable measurement of frequency error.
			- Enable_Iq: bool: Disable or enable measurement of I/Q origin offset and imbalance."""
		__meta_args_list = [
			ArgStruct.scalar_int('Mod_Statistics'),
			ArgStruct.scalar_bool('Enable_Ue_Power'),
			ArgStruct.scalar_bool('Enable_Evm'),
			ArgStruct.scalar_bool('Enable_Mag_Error'),
			ArgStruct.scalar_bool('Enable_Phase_Err'),
			ArgStruct.scalar_bool('Enable_Freq_Error'),
			ArgStruct.scalar_bool('Enable_Iq')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mod_Statistics: int = None
			self.Enable_Ue_Power: bool = None
			self.Enable_Evm: bool = None
			self.Enable_Mag_Error: bool = None
			self.Enable_Phase_Err: bool = None
			self.Enable_Freq_Error: bool = None
			self.Enable_Iq: bool = None

	def set(self, structure: ModulationStruct, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:MODulation \n
		Snippet with structure: \n
		structure = driver.configure.wcdmaMeas.multiEval.listPy.segment.modulation.ModulationStruct() \n
		structure.Mod_Statistics: int = 1 \n
		structure.Enable_Ue_Power: bool = False \n
		structure.Enable_Evm: bool = False \n
		structure.Enable_Mag_Error: bool = False \n
		structure.Enable_Phase_Err: bool = False \n
		structure.Enable_Freq_Error: bool = False \n
		structure.Enable_Iq: bool = False \n
		driver.configure.wcdmaMeas.multiEval.listPy.segment.modulation.set(structure, segment = repcap.Segment.Default) \n
		Defines the statistical length for the AVERage, MAXimum, and SDEViation calculation and enables the calculation of the
		different modulation results in segment no. <no>; see 'Multi-evaluation list mode'. The statistical length for CDP, CDE
		and modulation results is identical (see also method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.ListPy.Segment.
		CdPower.set) . \n
			:param structure: for set value, see the help for ModulationStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
		"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write_struct(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:MODulation', structure)

	def get(self, segment=repcap.Segment.Default) -> ModulationStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:MODulation \n
		Snippet: value: ModulationStruct = driver.configure.wcdmaMeas.multiEval.listPy.segment.modulation.get(segment = repcap.Segment.Default) \n
		Defines the statistical length for the AVERage, MAXimum, and SDEViation calculation and enables the calculation of the
		different modulation results in segment no. <no>; see 'Multi-evaluation list mode'. The statistical length for CDP, CDE
		and modulation results is identical (see also method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.ListPy.Segment.
		CdPower.set) . \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for ModulationStruct structure arguments."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:MODulation?', self.__class__.ModulationStruct())
