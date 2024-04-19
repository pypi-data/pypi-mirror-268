from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ........Internal.Types import DataType
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EdpdchCls:
	"""Edpdch commands group definition. 2 total commands, 0 Subgroups, 2 group commands
	Repeated Capability: EdpdChannel, default value after init: EdpdChannel.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("edpdch", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_edpdChannel_get', 'repcap_edpdChannel_set', repcap.EdpdChannel.Nr1)

	def repcap_edpdChannel_set(self, edpdChannel: repcap.EdpdChannel) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to EdpdChannel.Default
		Default value after init: EdpdChannel.Nr1"""
		self._cmd_group.set_repcap_enum_value(edpdChannel)

	def repcap_edpdChannel_get(self) -> repcap.EdpdChannel:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def fetch(self, carrier=repcap.Carrier.Default, edpdChannel=repcap.EdpdChannel.Default) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:CARRier<carrier>:TRACe:RCDerror:SF:EDPDch<nr> \n
		Snippet: value: List[float] = driver.wcdmaMeas.multiEval.carrier.trace.rcdError.sf.edpdch.fetch(carrier = repcap.Carrier.Default, edpdChannel = repcap.EdpdChannel.Default) \n
		Returns the spreading factors for the E-DPDCH 1 to 4. Each current value refers to a half-slot or a full-slot, depending
		on the measurement period (see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Mperiod.modulation) . The number of
		results depends on the measurement length (see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.msCount) . \n
		Suppressed linked return values: reliability \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:param edpdChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Edpdch')
			:return: edpdch: Spreading factors, one result per measured slot or half-slot"""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		edpdChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(edpdChannel, repcap.EdpdChannel)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:CARRier{carrier_cmd_val}:TRACe:RCDerror:SF:EDPDch{edpdChannel_cmd_val}?', suppressed)
		return response

	def read(self, carrier=repcap.Carrier.Default, edpdChannel=repcap.EdpdChannel.Default) -> List[float]:
		"""SCPI: READ:WCDMa:MEASurement<instance>:MEValuation:CARRier<carrier>:TRACe:RCDerror:SF:EDPDch<nr> \n
		Snippet: value: List[float] = driver.wcdmaMeas.multiEval.carrier.trace.rcdError.sf.edpdch.read(carrier = repcap.Carrier.Default, edpdChannel = repcap.EdpdChannel.Default) \n
		Returns the spreading factors for the E-DPDCH 1 to 4. Each current value refers to a half-slot or a full-slot, depending
		on the measurement period (see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.Mperiod.modulation) . The number of
		results depends on the measurement length (see method RsCMPX_WcdmaMeas.Configure.WcdmaMeas.MultiEval.msCount) . \n
		Suppressed linked return values: reliability \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:param edpdChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Edpdch')
			:return: edpdch: Spreading factors, one result per measured slot or half-slot"""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		edpdChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(edpdChannel, repcap.EdpdChannel)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WCDMa:MEASurement<Instance>:MEValuation:CARRier{carrier_cmd_val}:TRACe:RCDerror:SF:EDPDch{edpdChannel_cmd_val}?', suppressed)
		return response

	def clone(self) -> 'EdpdchCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EdpdchCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
