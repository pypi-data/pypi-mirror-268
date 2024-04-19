from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModulationCls:
	"""Modulation commands group definition. 6 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	@property
	def uephd(self):
		"""uephd commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_uephd'):
			from .Uephd import UephdCls
			self._uephd = UephdCls(self._core, self._cmd_group)
		return self._uephd

	@property
	def phDhsDpcch(self):
		"""phDhsDpcch commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_phDhsDpcch'):
			from .PhDhsDpcch import PhDhsDpcchCls
			self._phDhsDpcch = PhDhsDpcchCls(self._core, self._cmd_group)
		return self._phDhsDpcch

	def clone(self) -> 'ModulationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ModulationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
