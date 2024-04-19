from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> List[enums.PcdErrorPhase]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:LIST:PCDE:PHASe:MAXimum \n
		Snippet: value: List[enums.PcdErrorPhase] = driver.wcdmaMeas.multiEval.listPy.pcde.phase.maximum.fetch() \n
		Return the phase where the peak code domain error was measured, for all measured list mode segments. \n
		Suppressed linked return values: reliability \n
			:return: pcd_error_phase: Comma-separated list of values, one per measured segment IPHase: I-Signal QPHase: Q-Signal"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:LIST:PCDE:PHASe:MAXimum?', suppressed)
		return Conversions.str_to_list_enum(response, enums.PcdErrorPhase)
