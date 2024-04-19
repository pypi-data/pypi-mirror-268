from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TraceCls:
	"""Trace commands group definition. 6 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trace", core, parent)

	@property
	def uePower(self):
		"""uePower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_uePower'):
			from .UePower import UePowerCls
			self._uePower = UePowerCls(self._core, self._cmd_group)
		return self._uePower

	@property
	def psteps(self):
		"""psteps commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_psteps'):
			from .Psteps import PstepsCls
			self._psteps = PstepsCls(self._core, self._cmd_group)
		return self._psteps

	def clone(self) -> 'TraceCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TraceCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
