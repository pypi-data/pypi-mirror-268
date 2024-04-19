from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MlengthCls:
	"""Mlength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mlength", core, parent)

	def set(self, nr_steps: int) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:CTFC:MLENgth \n
		Snippet: driver.configure.wcdmaMeas.tpc.ctfc.mlength.set(nr_steps = 1) \n
		Specifies the number of power steps to be measured per step direction (n up steps + n down steps) . A query returns the
		configured number of steps and the resulting measurement length. \n
			:param nr_steps: Number of steps to be measured per direction.
		"""
		param = Conversions.decimal_value_to_str(nr_steps)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:CTFC:MLENgth {param}')

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Nr_Steps: int: Number of steps to be measured per direction.
			- Meas_Length: int: Number of slots to be measured."""
		__meta_args_list = [
			ArgStruct.scalar_int('Nr_Steps'),
			ArgStruct.scalar_int('Meas_Length')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Nr_Steps: int = None
			self.Meas_Length: int = None

	def get(self) -> GetStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:CTFC:MLENgth \n
		Snippet: value: GetStruct = driver.configure.wcdmaMeas.tpc.ctfc.mlength.get() \n
		Specifies the number of power steps to be measured per step direction (n up steps + n down steps) . A query returns the
		configured number of steps and the resulting measurement length. \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:CTFC:MLENgth?', self.__class__.GetStruct())
