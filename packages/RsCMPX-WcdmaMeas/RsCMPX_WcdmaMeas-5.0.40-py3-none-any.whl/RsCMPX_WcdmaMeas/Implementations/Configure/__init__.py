from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConfigureCls:
	"""Configure commands group definition. 164 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("configure", core, parent)

	@property
	def wcdmaMeas(self):
		"""wcdmaMeas commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_wcdmaMeas'):
			from .WcdmaMeas import WcdmaMeasCls
			self._wcdmaMeas = WcdmaMeasCls(self._core, self._cmd_group)
		return self._wcdmaMeas

	def clone(self) -> 'ConfigureCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ConfigureCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
