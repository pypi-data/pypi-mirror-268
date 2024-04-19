from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PhsDpcchCls:
	"""PhsDpcch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phsDpcch", core, parent)

	def set(self, enable: bool, measure_point_a: float, measure_point_b: float, dynamic: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:PHSDpcch \n
		Snippet: driver.configure.wcdmaMeas.multiEval.limit.phsDpcch.set(enable = False, measure_point_a = 1.0, measure_point_b = 1.0, dynamic = 1.0) \n
		Defines a dynamic limit for the phase discontinuity determined by half-slot measurements (signals with HS-DPCCH) .
		The limit is checked at point A and point B. As the phase discontinuity is measured at half-slot boundaries (x.5, not x.
		0) points A and B have to be set to half-slot positions. \n
			:param enable: Disables | enables the limit check.
			:param measure_point_a: No help available
			:param measure_point_b: No help available
			:param dynamic: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('measure_point_a', measure_point_a, DataType.Float), ArgSingle('measure_point_b', measure_point_b, DataType.Float), ArgSingle('dynamic', dynamic, DataType.Float))
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:PHSDpcch {param}'.rstrip())

	# noinspection PyTypeChecker
	class PhsDpcchStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: Disables | enables the limit check.
			- Measure_Point_A: float: No parameter help available
			- Measure_Point_B: float: No parameter help available
			- Dynamic: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Measure_Point_A'),
			ArgStruct.scalar_float('Measure_Point_B'),
			ArgStruct.scalar_float('Dynamic')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Measure_Point_A: float = None
			self.Measure_Point_B: float = None
			self.Dynamic: float = None

	def get(self) -> PhsDpcchStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:PHSDpcch \n
		Snippet: value: PhsDpcchStruct = driver.configure.wcdmaMeas.multiEval.limit.phsDpcch.get() \n
		Defines a dynamic limit for the phase discontinuity determined by half-slot measurements (signals with HS-DPCCH) .
		The limit is checked at point A and point B. As the phase discontinuity is measured at half-slot boundaries (x.5, not x.
		0) points A and B have to be set to half-slot positions. \n
			:return: structure: for return value, see the help for PhsDpcchStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:PHSDpcch?', self.__class__.PhsDpcchStruct())
