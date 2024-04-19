from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ........Internal.Types import DataType
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def read(self, carrier=repcap.Carrier.Default) -> List[float]:
		"""SCPI: READ:WCDMa:MEASurement<instance>:MEValuation:TRACe:CARRier<carrier>:PERRor[:RMS]:CURRent \n
		Snippet: value: List[float] = driver.wcdmaMeas.multiEval.trace.carrier.perror.rms.current.read(carrier = repcap.Carrier.Default) \n
		Returns the values of the RMS phase error traces for up to 120 slots. Each current value is averaged over a half-slot or
		a full-slot, depending on the measurement period (see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Mperiod.
		modulation) . The number of results depends on the measurement length (see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.
		MultiEval.msCount) . The results of the current, average, maximum and standard deviation traces can be retrieved.
		The standard deviation trace cannot be displayed at the GUI. \n
		Suppressed linked return values: reliability \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: phase_error: RMS phase error trace results, one result per measured slot or half-slot"""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WCDMa:MEASurement<Instance>:MEValuation:TRACe:CARRier{carrier_cmd_val}:PERRor:RMS:CURRent?', suppressed)
		return response
