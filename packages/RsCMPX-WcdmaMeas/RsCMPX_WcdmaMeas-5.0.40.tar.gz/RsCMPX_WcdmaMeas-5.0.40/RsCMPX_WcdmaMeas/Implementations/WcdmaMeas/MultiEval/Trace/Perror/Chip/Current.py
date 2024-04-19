from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:TRACe:PERRor:CHIP:CURRent \n
		Snippet: value: List[float] = driver.wcdmaMeas.multiEval.trace.perror.chip.current.fetch() \n
		Returns the values of the RMS phase error vs chip traces, measured in the preselected slot (see method RsCMPX_WcdmaMeas.
		Configure.WcdmaMeas.MultiEval.pslot) . One value per chip is returned. The results of the current, average and maximum
		traces can be retrieved. \n
		Suppressed linked return values: reliability \n
			:return: phase_error_chip: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:TRACe:PERRor:CHIP:CURRent?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:WCDMa:MEASurement<instance>:MEValuation:TRACe:PERRor:CHIP:CURRent \n
		Snippet: value: List[float] = driver.wcdmaMeas.multiEval.trace.perror.chip.current.read() \n
		Returns the values of the RMS phase error vs chip traces, measured in the preselected slot (see method RsCMPX_WcdmaMeas.
		Configure.WcdmaMeas.MultiEval.pslot) . One value per chip is returned. The results of the current, average and maximum
		traces can be retrieved. \n
		Suppressed linked return values: reliability \n
			:return: phase_error_chip: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WCDMa:MEASurement<Instance>:MEValuation:TRACe:PERRor:CHIP:CURRent?', suppressed)
		return response
