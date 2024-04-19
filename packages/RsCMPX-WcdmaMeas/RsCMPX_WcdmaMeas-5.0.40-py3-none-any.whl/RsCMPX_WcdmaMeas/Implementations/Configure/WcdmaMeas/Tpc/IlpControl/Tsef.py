from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TsefCls:
	"""Tsef commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsef", core, parent)

	def set(self, length: int, statistics: int) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:ILPControl:TSEF \n
		Snippet: driver.configure.wcdmaMeas.tpc.ilpControl.tsef.set(length = 1, statistics = 1) \n
		Configures the inner loop power control test steps E and F. \n
			:param length: Number of TPC bits per test step
			:param statistics: Number of slots at the end of test step E (F) , where the minimum (maximum) output power results are measured.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('length', length, DataType.Integer), ArgSingle('statistics', statistics, DataType.Integer))
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:ILPControl:TSEF {param}'.rstrip())

	# noinspection PyTypeChecker
	class TsefStruct(StructBase):
		"""Response structure. Fields: \n
			- Length: int: Number of TPC bits per test step
			- Statistics: int: Number of slots at the end of test step E (F) , where the minimum (maximum) output power results are measured."""
		__meta_args_list = [
			ArgStruct.scalar_int('Length'),
			ArgStruct.scalar_int('Statistics')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Length: int = None
			self.Statistics: int = None

	def get(self) -> TsefStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:ILPControl:TSEF \n
		Snippet: value: TsefStruct = driver.configure.wcdmaMeas.tpc.ilpControl.tsef.get() \n
		Configures the inner loop power control test steps E and F. \n
			:return: structure: for return value, see the help for TsefStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:ILPControl:TSEF?', self.__class__.TsefStruct())
