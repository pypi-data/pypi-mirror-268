from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ........Internal.Types import DataType
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HsdpcchCls:
	"""Hsdpcch commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hsdpcch", core, parent)

	def read(self, carrier=repcap.Carrier.Default) -> List[int]:
		"""SCPI: READ:WCDMa:MEASurement<instance>:MEValuation:CARRier<carrier>:TRACe:RCDerror:SF:HSDPcch \n
		Snippet: value: List[int] = driver.wcdmaMeas.multiEval.carrier.trace.rcdError.sf.hsdpcch.read(carrier = repcap.Carrier.Default) \n
		Returns the current spreading factors for the E-DPCCH and the HS-DPCCH. Each value refers to a half-slot or a full-slot,
		depending on the measurement period (see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Mperiod.modulation) . The
		number of results depends on the measurement length (see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.msCount) . \n
		Suppressed linked return values: reliability \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: hsdpcch: Spreading factors, one result per measured slot or half-slot."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'READ:WCDMa:MEASurement<Instance>:MEValuation:CARRier{carrier_cmd_val}:TRACe:RCDerror:SF:HSDPcch?', suppressed)
		return response

	def fetch(self, carrier=repcap.Carrier.Default) -> List[int]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:CARRier<carrier>:TRACe:RCDerror:SF:HSDPcch \n
		Snippet: value: List[int] = driver.wcdmaMeas.multiEval.carrier.trace.rcdError.sf.hsdpcch.fetch(carrier = repcap.Carrier.Default) \n
		Returns the current spreading factors for the E-DPCCH and the HS-DPCCH. Each value refers to a half-slot or a full-slot,
		depending on the measurement period (see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Mperiod.modulation) . The
		number of results depends on the measurement length (see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.msCount) . \n
		Suppressed linked return values: reliability \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: hsdpcch: Spreading factors, one result per measured slot or half-slot."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:CARRier{carrier_cmd_val}:TRACe:RCDerror:SF:HSDPcch?', suppressed)
		return response
