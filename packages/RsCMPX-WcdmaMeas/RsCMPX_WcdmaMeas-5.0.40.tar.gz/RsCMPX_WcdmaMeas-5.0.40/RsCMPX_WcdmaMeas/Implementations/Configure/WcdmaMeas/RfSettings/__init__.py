from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettingsCls:
	"""RfSettings commands group definition. 5 total commands, 2 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfSettings", core, parent)

	@property
	def dcarrier(self):
		"""dcarrier commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dcarrier'):
			from .Dcarrier import DcarrierCls
			self._dcarrier = DcarrierCls(self._core, self._cmd_group)
		return self._dcarrier

	@property
	def carrier(self):
		"""carrier commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .Carrier import CarrierCls
			self._carrier = CarrierCls(self._core, self._cmd_group)
		return self._carrier

	def get_eattenuation(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:RFSettings:EATTenuation \n
		Snippet: value: float = driver.configure.wcdmaMeas.rfSettings.get_eattenuation() \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the input connector. \n
			:return: rf_input_ext_att: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:RFSettings:EATTenuation?')
		return Conversions.str_to_float(response)

	def set_eattenuation(self, rf_input_ext_att: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:RFSettings:EATTenuation \n
		Snippet: driver.configure.wcdmaMeas.rfSettings.set_eattenuation(rf_input_ext_att = 1.0) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the input connector. \n
			:param rf_input_ext_att: No help available
		"""
		param = Conversions.decimal_value_to_str(rf_input_ext_att)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:RFSettings:EATTenuation {param}')

	def get_umargin(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:RFSettings:UMARgin \n
		Snippet: value: float = driver.configure.wcdmaMeas.rfSettings.get_umargin() \n
		Sets the margin that the measurement adds to the expected nominal power to determine the reference power. The reference
		power minus the external input attenuation must be within the power range of the selected input connector. Refer to the
		specifications document. \n
			:return: user_margin: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:RFSettings:UMARgin?')
		return Conversions.str_to_float(response)

	def set_umargin(self, user_margin: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:RFSettings:UMARgin \n
		Snippet: driver.configure.wcdmaMeas.rfSettings.set_umargin(user_margin = 1.0) \n
		Sets the margin that the measurement adds to the expected nominal power to determine the reference power. The reference
		power minus the external input attenuation must be within the power range of the selected input connector. Refer to the
		specifications document. \n
			:param user_margin: No help available
		"""
		param = Conversions.decimal_value_to_str(user_margin)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:RFSettings:UMARgin {param}')

	def get_envelope_power(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:RFSettings:ENPower \n
		Snippet: value: float = driver.configure.wcdmaMeas.rfSettings.get_envelope_power() \n
		Sets the expected nominal power of the measured RF signal. \n
			:return: exp_nom_power: The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the specifications document.
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:RFSettings:ENPower?')
		return Conversions.str_to_float(response)

	def set_envelope_power(self, exp_nom_power: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:RFSettings:ENPower \n
		Snippet: driver.configure.wcdmaMeas.rfSettings.set_envelope_power(exp_nom_power = 1.0) \n
		Sets the expected nominal power of the measured RF signal. \n
			:param exp_nom_power: The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the specifications document.
		"""
		param = Conversions.decimal_value_to_str(exp_nom_power)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:RFSettings:ENPower {param}')

	def clone(self) -> 'RfSettingsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RfSettingsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
