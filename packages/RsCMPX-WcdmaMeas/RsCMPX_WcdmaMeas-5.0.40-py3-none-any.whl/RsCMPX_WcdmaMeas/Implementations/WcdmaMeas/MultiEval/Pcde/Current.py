from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


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
			- Pcd_Error: float: Peak code domain error
			- Pcd_Error_Phase: enums.PcdErrorPhase: Phase where the peak code domain error was measured. IPHase: I-Signal QPHase: Q-Signal
			- Pcd_Error_Code_Nr: int: Code number for which the PCDE was measured."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Pcd_Error'),
			ArgStruct.scalar_enum('Pcd_Error_Phase', enums.PcdErrorPhase),
			ArgStruct.scalar_int('Pcd_Error_Code_Nr')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Pcd_Error: float = None
			self.Pcd_Error_Phase: enums.PcdErrorPhase = None
			self.Pcd_Error_Code_Nr: int = None

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:MEValuation:PCDE:CURRent \n
		Snippet: value: ResultData = driver.wcdmaMeas.multiEval.pcde.current.read() \n
		Returns the peak code domain error (PCDE) results. In addition to the current PCDE value, the maximum PCDE value can be
		retrieved. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:MEValuation:PCDE:CURRent?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:PCDE:CURRent \n
		Snippet: value: ResultData = driver.wcdmaMeas.multiEval.pcde.current.fetch() \n
		Returns the peak code domain error (PCDE) results. In addition to the current PCDE value, the maximum PCDE value can be
		retrieved. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:PCDE:CURRent?', self.__class__.ResultData())
