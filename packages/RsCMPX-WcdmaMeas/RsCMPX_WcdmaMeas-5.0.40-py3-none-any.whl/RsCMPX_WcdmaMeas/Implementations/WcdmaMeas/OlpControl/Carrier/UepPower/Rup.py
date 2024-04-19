from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RupCls:
	"""Rup commands group definition. 2 total commands, 0 Subgroups, 2 group commands
	Repeated Capability: RampUpCarrier, default value after init: RampUpCarrier.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rup", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_rampUpCarrier_get', 'repcap_rampUpCarrier_set', repcap.RampUpCarrier.Nr1)

	def repcap_rampUpCarrier_set(self, rampUpCarrier: repcap.RampUpCarrier) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to RampUpCarrier.Default
		Default value after init: RampUpCarrier.Nr1"""
		self._cmd_group.set_repcap_enum_value(rampUpCarrier)

	def repcap_rampUpCarrier_get(self) -> repcap.RampUpCarrier:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def read(self, cARRierExt=repcap.CARRierExt.Default, rampUpCarrier=repcap.RampUpCarrier.Default) -> List[float]:
		"""SCPI: READ:WCDMa:MEASurement<instance>:OLPControl:CARRier<carrier>:UEPPower:RUP<rupcarrier> \n
		Snippet: value: List[float] = driver.wcdmaMeas.olpControl.carrier.uepPower.rup.read(cARRierExt = repcap.CARRierExt.Default, rampUpCarrier = repcap.RampUpCarrier.Default) \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param cARRierExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:param rampUpCarrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rup')
			:return: ue_power: No help available"""
		cARRierExt_cmd_val = self._cmd_group.get_repcap_cmd_value(cARRierExt, repcap.CARRierExt)
		rampUpCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(rampUpCarrier, repcap.RampUpCarrier)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WCDMa:MEASurement<Instance>:OLPControl:CARRier{cARRierExt_cmd_val}:UEPPower:RUP{rampUpCarrier_cmd_val}?', suppressed)
		return response

	def fetch(self, cARRierExt=repcap.CARRierExt.Default, rampUpCarrier=repcap.RampUpCarrier.Default) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:OLPControl:CARRier<carrier>:UEPPower:RUP<rupcarrier> \n
		Snippet: value: List[float] = driver.wcdmaMeas.olpControl.carrier.uepPower.rup.fetch(cARRierExt = repcap.CARRierExt.Default, rampUpCarrier = repcap.RampUpCarrier.Default) \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param cARRierExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:param rampUpCarrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rup')
			:return: ue_power: No help available"""
		cARRierExt_cmd_val = self._cmd_group.get_repcap_cmd_value(cARRierExt, repcap.CARRierExt)
		rampUpCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(rampUpCarrier, repcap.RampUpCarrier)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:OLPControl:CARRier{cARRierExt_cmd_val}:UEPPower:RUP{rampUpCarrier_cmd_val}?', suppressed)
		return response

	def clone(self) -> 'RupCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RupCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
