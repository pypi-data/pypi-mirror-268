from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeChannelsCls:
	"""UeChannels commands group definition. 7 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ueChannels", core, parent)

	@property
	def carrier(self):
		"""carrier commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .Carrier import CarrierCls
			self._carrier = CarrierCls(self._core, self._cmd_group)
		return self._carrier

	# noinspection PyTypeChecker
	def get_bsf_selection(self) -> enums.AutoManualMode:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:UECHannels:BSFSelection \n
		Snippet: value: enums.AutoManualMode = driver.configure.wcdmaMeas.ueChannels.get_bsf_selection() \n
		No command help available \n
			:return: selection: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:UECHannels:BSFSelection?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)

	def set_bsf_selection(self, selection: enums.AutoManualMode) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:UECHannels:BSFSelection \n
		Snippet: driver.configure.wcdmaMeas.ueChannels.set_bsf_selection(selection = enums.AutoManualMode.AUTO) \n
		No command help available \n
			:param selection: No help available
		"""
		param = Conversions.enum_scalar_to_str(selection, enums.AutoManualMode)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:UECHannels:BSFSelection {param}')

	def clone(self) -> 'UeChannelsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeChannelsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
