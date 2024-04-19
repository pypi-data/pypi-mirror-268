from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


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
			- Dpcch: List[float]: RMS CDP values for the indicated channels
			- Dpdch: List[float]: RMS CDP values for the indicated channels
			- Hsdpcch: List[float]: RMS CDP values for the indicated channels
			- Edpcch: List[float]: RMS CDP values for the indicated channels
			- Edpdch_1: List[float]: RMS CDP values for the indicated channels
			- Edpdch_2: List[float]: RMS CDP values for the indicated channels
			- Edpdch_3: List[float]: RMS CDP values for the indicated channels
			- Edpdch_4: List[float]: RMS CDP values for the indicated channels"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Return_Code', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Dpcch', DataType.FloatList, None, False, True, 1),
			ArgStruct('Dpdch', DataType.FloatList, None, False, True, 1),
			ArgStruct('Hsdpcch', DataType.FloatList, None, False, True, 1),
			ArgStruct('Edpcch', DataType.FloatList, None, False, True, 1),
			ArgStruct('Edpdch_1', DataType.FloatList, None, False, True, 1),
			ArgStruct('Edpdch_2', DataType.FloatList, None, False, True, 1),
			ArgStruct('Edpdch_3', DataType.FloatList, None, False, True, 1),
			ArgStruct('Edpdch_4', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Return_Code: List[int] = None
			self.Dpcch: List[float] = None
			self.Dpdch: List[float] = None
			self.Hsdpcch: List[float] = None
			self.Edpcch: List[float] = None
			self.Edpdch_1: List[float] = None
			self.Edpdch_2: List[float] = None
			self.Edpdch_3: List[float] = None
			self.Edpdch_4: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:LIST:CDPower:CURRent \n
		Snippet: value: FetchStruct = driver.wcdmaMeas.multiEval.listPy.cdPower.current.fetch() \n
		Return the RMS CDP vs. slot results in list mode. The values listed below in curly brackets {} are returned for the
		segments {...}seg 1, {...}seg 2, ..., {...}seg n, with n determined by method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.
		MultiEval.ListPy.count. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:LIST:CDPower:CURRent?', self.__class__.FetchStruct())
