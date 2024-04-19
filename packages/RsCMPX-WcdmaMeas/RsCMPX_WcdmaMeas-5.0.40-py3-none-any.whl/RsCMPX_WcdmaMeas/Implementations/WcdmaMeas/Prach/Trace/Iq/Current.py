from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Iphase: List[float]: I amplitude of a constellation point
			- Qphase: List[float]: Q amplitude of a constellation point"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Iphase', DataType.FloatList, None, False, True, 1),
			ArgStruct('Qphase', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Iphase: List[float] = None
			self.Qphase: List[float] = None

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:PRACh:TRACe:IQ:CURRent \n
		Snippet: value: ResultData = driver.wcdmaMeas.prach.trace.iq.current.read() \n
		Returns the results in the I/Q constellation diagram. The constellation points are returned as pairs of I and Q values:
		<Reliability>, <Iphase>1, <Qphase>1, ..., <Iphase>3904, <Qphase>3904 \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:PRACh:TRACe:IQ:CURRent?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:PRACh:TRACe:IQ:CURRent \n
		Snippet: value: ResultData = driver.wcdmaMeas.prach.trace.iq.current.fetch() \n
		Returns the results in the I/Q constellation diagram. The constellation points are returned as pairs of I and Q values:
		<Reliability>, <Iphase>1, <Qphase>1, ..., <Iphase>3904, <Qphase>3904 \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:PRACh:TRACe:IQ:CURRent?', self.__class__.ResultData())
