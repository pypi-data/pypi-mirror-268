from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HsdpcchCls:
	"""Hsdpcch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hsdpcch", core, parent)

	def set(self, enable: bool, dtx_to_nack: float, nack_to_cqi: float, cqi_to_dtx: float, test_case: enums.TestCase = None) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:PCONtrol:HSDPcch \n
		Snippet: driver.configure.wcdmaMeas.multiEval.limit.pcontrol.hsdpcch.set(enable = False, dtx_to_nack = 1.0, nack_to_cqi = 1.0, cqi_to_dtx = 1.0, test_case = enums.TestCase.T0DB) \n
		Defines nominal power steps for the HS-DPCCH limit set. Measurements at maximum UE power and below maximum UE power are
		supported. Separate values can be defined for the boundaries DTX > (N) ACK, (N) ACK > CQI and CQI > DTX. Also the limit
		check can be enabled or disabled. \n
			:param enable: Disables | enables the limit check.
			:param dtx_to_nack: No help available
			:param nack_to_cqi: No help available
			:param cqi_to_dtx: No help available
			:param test_case: T0DB: measurement below maximum UE power with TPC command = 0 dB T1DB: measurement at maximum UE power with TPC command = 1 dB
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('dtx_to_nack', dtx_to_nack, DataType.Float), ArgSingle('nack_to_cqi', nack_to_cqi, DataType.Float), ArgSingle('cqi_to_dtx', cqi_to_dtx, DataType.Float), ArgSingle('test_case', test_case, DataType.Enum, enums.TestCase, is_optional=True))
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:PCONtrol:HSDPcch {param}'.rstrip())

	# noinspection PyTypeChecker
	class HsdpcchStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: Disables | enables the limit check.
			- Dtx_To_Nack: float: No parameter help available
			- Nack_To_Cqi: float: No parameter help available
			- Cqi_To_Dtx: float: No parameter help available
			- Test_Case: enums.TestCase: T0DB: measurement below maximum UE power with TPC command = 0 dB T1DB: measurement at maximum UE power with TPC command = 1 dB"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Dtx_To_Nack'),
			ArgStruct.scalar_float('Nack_To_Cqi'),
			ArgStruct.scalar_float('Cqi_To_Dtx'),
			ArgStruct.scalar_enum('Test_Case', enums.TestCase)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Dtx_To_Nack: float = None
			self.Nack_To_Cqi: float = None
			self.Cqi_To_Dtx: float = None
			self.Test_Case: enums.TestCase = None

	def get(self) -> HsdpcchStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:PCONtrol:HSDPcch \n
		Snippet: value: HsdpcchStruct = driver.configure.wcdmaMeas.multiEval.limit.pcontrol.hsdpcch.get() \n
		Defines nominal power steps for the HS-DPCCH limit set. Measurements at maximum UE power and below maximum UE power are
		supported. Separate values can be defined for the boundaries DTX > (N) ACK, (N) ACK > CQI and CQI > DTX. Also the limit
		check can be enabled or disabled. \n
			:return: structure: for return value, see the help for HsdpcchStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:PCONtrol:HSDPcch?', self.__class__.HsdpcchStruct())
