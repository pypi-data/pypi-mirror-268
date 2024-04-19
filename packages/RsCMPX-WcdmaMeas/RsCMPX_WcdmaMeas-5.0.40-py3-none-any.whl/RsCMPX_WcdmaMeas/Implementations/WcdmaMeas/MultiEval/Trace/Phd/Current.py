from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:TRACe:PHD:CURRent \n
		Snippet: value: List[float] = driver.wcdmaMeas.multiEval.trace.phd.current.fetch() \n
		Returns the values of the phase discontinuity traces for up to 120 slots. One value per measured slot is returned (see
		method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.msCount) .
			INTRO_CMD_HELP: The meaning of the value depends on the measurement period (see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Mperiod.modulation) : \n
			- For full-slot measurements, each value indicates the phase discontinuity at the boundary between a slot and the previous slot. As there is no previous slot for slot 0, the first returned phase discontinuity value equals NCAP.
			- For half-slot measurements, each value indicates the phase discontinuity at the boundary between the first and second half-slot of a slot. This value can be measured for all slots, including slot 0.  \n
		Suppressed linked return values: reliability \n
			:return: phase_disc: One value per measured slot"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:TRACe:PHD:CURRent?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:WCDMa:MEASurement<instance>:MEValuation:TRACe:PHD:CURRent \n
		Snippet: value: List[float] = driver.wcdmaMeas.multiEval.trace.phd.current.read() \n
		Returns the values of the phase discontinuity traces for up to 120 slots. One value per measured slot is returned (see
		method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.msCount) .
			INTRO_CMD_HELP: The meaning of the value depends on the measurement period (see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Mperiod.modulation) : \n
			- For full-slot measurements, each value indicates the phase discontinuity at the boundary between a slot and the previous slot. As there is no previous slot for slot 0, the first returned phase discontinuity value equals NCAP.
			- For half-slot measurements, each value indicates the phase discontinuity at the boundary between the first and second half-slot of a slot. This value can be measured for all slots, including slot 0.  \n
		Suppressed linked return values: reliability \n
			:return: phase_disc: One value per measured slot"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WCDMa:MEASurement<Instance>:MEValuation:TRACe:PHD:CURRent?', suppressed)
		return response
