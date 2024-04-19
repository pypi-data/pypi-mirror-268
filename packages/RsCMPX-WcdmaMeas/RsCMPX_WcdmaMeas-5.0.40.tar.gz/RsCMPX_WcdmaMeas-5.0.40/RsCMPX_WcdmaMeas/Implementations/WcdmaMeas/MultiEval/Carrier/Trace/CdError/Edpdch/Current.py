from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ........Internal.Types import DataType
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def read(self, carrier=repcap.Carrier.Default, edpdChannel=repcap.EdpdChannel.Default) -> List[float]:
		"""SCPI: READ:WCDMa:MEASurement<instance>:MEValuation:CARRier<carrier>:TRACe:CDERror:EDPDch<nr>:CURRent \n
		Snippet: value: List[float] = driver.wcdmaMeas.multiEval.carrier.trace.cdError.edpdch.current.read(carrier = repcap.Carrier.Default, edpdChannel = repcap.EdpdChannel.Default) \n
		Returns the values of the RMS CDE vs slot traces for the E-DPDCH 1 to 4. Each current value is averaged over a half-slot
		or a full-slot, depending on the measurement period (see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Mperiod.
		modulation) . The number of results depends on the measurement length (see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.
		MultiEval.msCount) . The results of the current, average, maximum and standard deviation traces can be retrieved.
		The standard deviation trace cannot be displayed at the GUI. \n
		Suppressed linked return values: reliability \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:param edpdChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Edpdch')
			:return: edpdch: RMS CDE trace results, one result per measured slot or half-slot"""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		edpdChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(edpdChannel, repcap.EdpdChannel)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WCDMa:MEASurement<Instance>:MEValuation:CARRier{carrier_cmd_val}:TRACe:CDERror:EDPDch{edpdChannel_cmd_val}:CURRent?', suppressed)
		return response

	def fetch(self, carrier=repcap.Carrier.Default, edpdChannel=repcap.EdpdChannel.Default) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:CARRier<carrier>:TRACe:CDERror:EDPDch<nr>:CURRent \n
		Snippet: value: List[float] = driver.wcdmaMeas.multiEval.carrier.trace.cdError.edpdch.current.fetch(carrier = repcap.Carrier.Default, edpdChannel = repcap.EdpdChannel.Default) \n
		Returns the values of the RMS CDE vs slot traces for the E-DPDCH 1 to 4. Each current value is averaged over a half-slot
		or a full-slot, depending on the measurement period (see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Mperiod.
		modulation) . The number of results depends on the measurement length (see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.
		MultiEval.msCount) . The results of the current, average, maximum and standard deviation traces can be retrieved.
		The standard deviation trace cannot be displayed at the GUI. \n
		Suppressed linked return values: reliability \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:param edpdChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Edpdch')
			:return: edpdch: RMS CDE trace results, one result per measured slot or half-slot"""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		edpdChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(edpdChannel, repcap.EdpdChannel)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:CARRier{carrier_cmd_val}:TRACe:CDERror:EDPDch{edpdChannel_cmd_val}:CURRent?', suppressed)
		return response
