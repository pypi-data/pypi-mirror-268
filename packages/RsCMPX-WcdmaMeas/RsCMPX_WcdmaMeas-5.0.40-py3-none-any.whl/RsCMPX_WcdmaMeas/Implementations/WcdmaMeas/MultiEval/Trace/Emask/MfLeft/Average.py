from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:WCDMa:MEASurement<instance>:MEValuation:TRACe:EMASk:MFLeft:AVERage \n
		Snippet: value: List[float] = driver.wcdmaMeas.multiEval.trace.emask.mfLeft.average.read() \n
		Returns the values of the spectrum emission 1 MHz traces. The left section and the right section of each trace are
		retrieved by separate commands (distinguished by the terms MFLeft and MFRight) . The results of the current, average and
		maximum traces can be retrieved. \n
		Suppressed linked return values: reliability \n
			:return: emask_1_mleft: Comma-separated list of values, the covered frequency range differs for single and dual uplink carrier: Single carrier: n = 89 values correspond to test points that are separated by 90 kHz. The covered frequency ranges are: Left section: -11970 kHz to -4050 kHz from the center carrier frequency Right section: 4050 kHz to 11970 kHz from the center carrier frequency Dual carrier in uplink: n = 144 values correspond to test points that are separated by 90 kHz. The covered frequency ranges are: Left section: -19440 kHz to -6570 kHz from the center frequency of both carriers, e.g. from f = (fC2 - fC1) /2. Right section: 6570 kHz to 19440 kHz from the center frequency of both carriers"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WCDMa:MEASurement<Instance>:MEValuation:TRACe:EMASk:MFLeft:AVERage?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:TRACe:EMASk:MFLeft:AVERage \n
		Snippet: value: List[float] = driver.wcdmaMeas.multiEval.trace.emask.mfLeft.average.fetch() \n
		Returns the values of the spectrum emission 1 MHz traces. The left section and the right section of each trace are
		retrieved by separate commands (distinguished by the terms MFLeft and MFRight) . The results of the current, average and
		maximum traces can be retrieved. \n
		Suppressed linked return values: reliability \n
			:return: emask_1_mleft: Comma-separated list of values, the covered frequency range differs for single and dual uplink carrier: Single carrier: n = 89 values correspond to test points that are separated by 90 kHz. The covered frequency ranges are: Left section: -11970 kHz to -4050 kHz from the center carrier frequency Right section: 4050 kHz to 11970 kHz from the center carrier frequency Dual carrier in uplink: n = 144 values correspond to test points that are separated by 90 kHz. The covered frequency ranges are: Left section: -19440 kHz to -6570 kHz from the center frequency of both carriers, e.g. from f = (fC2 - fC1) /2. Right section: 6570 kHz to 19440 kHz from the center frequency of both carriers"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:TRACe:EMASk:MFLeft:AVERage?', suppressed)
		return response
