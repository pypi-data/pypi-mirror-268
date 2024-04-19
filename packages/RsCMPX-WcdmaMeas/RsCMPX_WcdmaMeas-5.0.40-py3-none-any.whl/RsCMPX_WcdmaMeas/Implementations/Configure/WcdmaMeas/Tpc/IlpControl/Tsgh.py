from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TsghCls:
	"""Tsgh commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsgh", core, parent)

	def set(self, length: int, statistics: int) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:ILPControl:TSGH \n
		Snippet: driver.configure.wcdmaMeas.tpc.ilpControl.tsgh.set(length = 1, statistics = 1) \n
		Configures the inner loop power control test steps G and H. For Signal Path = Network, usemethod RsCMPX_WcdmaMeas.
		Configure.WcdmaMeas.Tpc.IlpControl.Tsgh.set. \n
			:param length: Number of TPC bits per test step
			:param statistics: Number of slots at the end of test step G (H) , where the minimum (maximum) output power results are measured.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('length', length, DataType.Integer), ArgSingle('statistics', statistics, DataType.Integer))
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:ILPControl:TSGH {param}'.rstrip())

	# noinspection PyTypeChecker
	class TsghStruct(StructBase):
		"""Response structure. Fields: \n
			- Length: int: Number of TPC bits per test step
			- Statistics: int: Number of slots at the end of test step G (H) , where the minimum (maximum) output power results are measured."""
		__meta_args_list = [
			ArgStruct.scalar_int('Length'),
			ArgStruct.scalar_int('Statistics')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Length: int = None
			self.Statistics: int = None

	def get(self) -> TsghStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:ILPControl:TSGH \n
		Snippet: value: TsghStruct = driver.configure.wcdmaMeas.tpc.ilpControl.tsgh.get() \n
		Configures the inner loop power control test steps G and H. For Signal Path = Network, usemethod RsCMPX_WcdmaMeas.
		Configure.WcdmaMeas.Tpc.IlpControl.Tsgh.set. \n
			:return: structure: for return value, see the help for TsghStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:ILPControl:TSGH?', self.__class__.TsghStruct())
