from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


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
			- Return_Code: List[int]: Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Carrier_Power: List[float]: Power at the nominal carrier frequency in uplink
			- Aclr_Minus_2: List[float]: Power of the adjacent channels (±1st adjacent channels at ±5 MHz from the UL frequency, ±2nd adjacent channels at ±10 MHz from the UL frequency)
			- Aclr_Minus_1: List[float]: Power of the adjacent channels (±1st adjacent channels at ±5 MHz from the UL frequency, ±2nd adjacent channels at ±10 MHz from the UL frequency)
			- Aclr_Plus_1: List[float]: Power of the adjacent channels (±1st adjacent channels at ±5 MHz from the UL frequency, ±2nd adjacent channels at ±10 MHz from the UL frequency)
			- Aclr_Plus_2: List[float]: Power of the adjacent channels (±1st adjacent channels at ±5 MHz from the UL frequency, ±2nd adjacent channels at ±10 MHz from the UL frequency)
			- Obw: List[float]: Occupied bandwidth
			- Emask_Margin_Ab: List[float]: No parameter help available
			- Emask_Margin_Bc: List[float]: No parameter help available
			- Emask_Margin_Cd: List[float]: No parameter help available
			- Emask_Margin_Ef: List[float]: No parameter help available
			- Emask_Margin_Fe: List[float]: No parameter help available
			- Emask_Margin_Dc: List[float]: No parameter help available
			- Emask_Margin_Cb: List[float]: No parameter help available
			- Emask_Margin_Ba: List[float]: No parameter help available
			- Ue_Power: List[float]: User equipment power
			- Emask_Margin_Had: List[float]: No parameter help available
			- Emask_Margin_Hda: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Return_Code', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Carrier_Power', DataType.FloatList, None, False, True, 1),
			ArgStruct('Aclr_Minus_2', DataType.FloatList, None, False, True, 1),
			ArgStruct('Aclr_Minus_1', DataType.FloatList, None, False, True, 1),
			ArgStruct('Aclr_Plus_1', DataType.FloatList, None, False, True, 1),
			ArgStruct('Aclr_Plus_2', DataType.FloatList, None, False, True, 1),
			ArgStruct('Obw', DataType.FloatList, None, False, True, 1),
			ArgStruct('Emask_Margin_Ab', DataType.FloatList, None, False, True, 1),
			ArgStruct('Emask_Margin_Bc', DataType.FloatList, None, False, True, 1),
			ArgStruct('Emask_Margin_Cd', DataType.FloatList, None, False, True, 1),
			ArgStruct('Emask_Margin_Ef', DataType.FloatList, None, False, True, 1),
			ArgStruct('Emask_Margin_Fe', DataType.FloatList, None, False, True, 1),
			ArgStruct('Emask_Margin_Dc', DataType.FloatList, None, False, True, 1),
			ArgStruct('Emask_Margin_Cb', DataType.FloatList, None, False, True, 1),
			ArgStruct('Emask_Margin_Ba', DataType.FloatList, None, False, True, 1),
			ArgStruct('Ue_Power', DataType.FloatList, None, False, True, 1),
			ArgStruct('Emask_Margin_Had', DataType.FloatList, None, False, True, 1),
			ArgStruct('Emask_Margin_Hda', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Return_Code: List[int] = None
			self.Carrier_Power: List[float] = None
			self.Aclr_Minus_2: List[float] = None
			self.Aclr_Minus_1: List[float] = None
			self.Aclr_Plus_1: List[float] = None
			self.Aclr_Plus_2: List[float] = None
			self.Obw: List[float] = None
			self.Emask_Margin_Ab: List[float] = None
			self.Emask_Margin_Bc: List[float] = None
			self.Emask_Margin_Cd: List[float] = None
			self.Emask_Margin_Ef: List[float] = None
			self.Emask_Margin_Fe: List[float] = None
			self.Emask_Margin_Dc: List[float] = None
			self.Emask_Margin_Cb: List[float] = None
			self.Emask_Margin_Ba: List[float] = None
			self.Ue_Power: List[float] = None
			self.Emask_Margin_Had: List[float] = None
			self.Emask_Margin_Hda: List[float] = None

	def fetch(self, aclr_mode: enums.AclrMode = None) -> FetchStruct:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:LIST:SPECtrum:CURRent \n
		Snippet: value: FetchStruct = driver.wcdmaMeas.multiEval.listPy.spectrum.current.fetch(aclr_mode = enums.AclrMode.ABSolute) \n
		Returns the ACLR power and spectrum emission single value results in list mode. The values listed below in curly brackets
		{} are returned for the segments {...}seg 1, {...}seg 2, ..., {...}seg n, with n determined by method RsCMPX_WcdmaMeas.
		Configure.WcdmaMeas.MultiEval.ListPy.count. \n
			:param aclr_mode: ABSolute: ACLR power is displayed in dBm as an absolute value. RELative: ACLR power is displayed in dB relative to carrier power.
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('aclr_mode', aclr_mode, DataType.Enum, enums.AclrMode, is_optional=True))
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:LIST:SPECtrum:CURRent? {param}'.rstrip(), self.__class__.FetchStruct())
