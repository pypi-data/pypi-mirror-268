from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:WCDMa:MEASurement<instance>:MEValuation:TRACe:EMASk:KFILter:MAXimum \n
		Snippet: value: List[float] = driver.wcdmaMeas.multiEval.trace.emask.kfilter.maximum.read() \n
		Returns the values of the spectrum emission 30 kHz traces. The results of the current, average and maximum traces can be
		retrieved. \n
		Suppressed linked return values: reliability \n
			:return: emask_30_k: Comma-separated list of values, the covered frequency range differs for single and dual uplink carrier: Single carrier: n = 1665 values correspond to test points that are separated by 15 kHz and cover the frequency range between -12480 kHz and 12480 kHz from the center carrier frequency. Dual carrier in uplink: n = 2665 values correspond to test points that are separated by 15 kHz. The results cover the frequency range between -19980 kHz and 19980 kHz from the center frequency of both carriers, e.g. from f = (fC2 - fC1) /2."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WCDMa:MEASurement<Instance>:MEValuation:TRACe:EMASk:KFILter:MAXimum?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:TRACe:EMASk:KFILter:MAXimum \n
		Snippet: value: List[float] = driver.wcdmaMeas.multiEval.trace.emask.kfilter.maximum.fetch() \n
		Returns the values of the spectrum emission 30 kHz traces. The results of the current, average and maximum traces can be
		retrieved. \n
		Suppressed linked return values: reliability \n
			:return: emask_30_k: Comma-separated list of values, the covered frequency range differs for single and dual uplink carrier: Single carrier: n = 1665 values correspond to test points that are separated by 15 kHz and cover the frequency range between -12480 kHz and 12480 kHz from the center carrier frequency. Dual carrier in uplink: n = 2665 values correspond to test points that are separated by 15 kHz. The results cover the frequency range between -19980 kHz and 19980 kHz from the center frequency of both carriers, e.g. from f = (fC2 - fC1) /2."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:TRACe:EMASk:KFILter:MAXimum?', suppressed)
		return response
