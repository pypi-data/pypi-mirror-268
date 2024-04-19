from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BandCls:
	"""Band commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("band", core, parent)

	def set(self, band: enums.Band, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:CARRier<carrier>:BAND \n
		Snippet: driver.configure.wcdmaMeas.carrier.band.set(band = enums.Band.OB1, carrier = repcap.Carrier.Default) \n
		Selects the operating band (OB) . \n
			:param band: OB1, ..., OB22: operating band I to XXII OB25, OB26: operating band XXV and XXVI OBS1: operating band S OBS2: operating band S 170 MHz OBS3: operating band S 190 MHz OBL1: operating band L
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
		"""
		param = Conversions.enum_scalar_to_str(band, enums.Band)
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:CARRier{carrier_cmd_val}:BAND {param}')

	# noinspection PyTypeChecker
	def get(self, carrier=repcap.Carrier.Default) -> enums.Band:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:CARRier<carrier>:BAND \n
		Snippet: value: enums.Band = driver.configure.wcdmaMeas.carrier.band.get(carrier = repcap.Carrier.Default) \n
		Selects the operating band (OB) . \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: band: OB1, ..., OB22: operating band I to XXII OB25, OB26: operating band XXV and XXVI OBS1: operating band S OBS2: operating band S 170 MHz OBS3: operating band S 190 MHz OBL1: operating band L"""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		response = self._core.io.query_str(f'CONFigure:WCDMa:MEASurement<Instance>:CARRier{carrier_cmd_val}:BAND?')
		return Conversions.str_to_scalar_enum(response, enums.Band)
