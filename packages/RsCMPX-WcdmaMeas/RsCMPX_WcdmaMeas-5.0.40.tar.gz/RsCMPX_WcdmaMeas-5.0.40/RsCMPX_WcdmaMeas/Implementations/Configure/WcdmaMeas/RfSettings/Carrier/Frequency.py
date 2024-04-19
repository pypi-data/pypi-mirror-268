from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, frequency: float, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:RFSettings:CARRier<carrier>:FREQuency \n
		Snippet: driver.configure.wcdmaMeas.rfSettings.carrier.frequency.set(frequency = 1.0, carrier = repcap.Carrier.Default) \n
		Selects the center frequency of the RF analyzer. For the supported frequency range, see 'Frequency ranges'. \n
			:param frequency: No help available
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:RFSettings:CARRier{carrier_cmd_val}:FREQuency {param}')

	def get(self, carrier=repcap.Carrier.Default) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:RFSettings:CARRier<carrier>:FREQuency \n
		Snippet: value: float = driver.configure.wcdmaMeas.rfSettings.carrier.frequency.get(carrier = repcap.Carrier.Default) \n
		Selects the center frequency of the RF analyzer. For the supported frequency range, see 'Frequency ranges'. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: frequency: No help available"""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		response = self._core.io.query_str(f'CONFigure:WCDMa:MEASurement<Instance>:RFSettings:CARRier{carrier_cmd_val}:FREQuency?')
		return Conversions.str_to_float(response)
