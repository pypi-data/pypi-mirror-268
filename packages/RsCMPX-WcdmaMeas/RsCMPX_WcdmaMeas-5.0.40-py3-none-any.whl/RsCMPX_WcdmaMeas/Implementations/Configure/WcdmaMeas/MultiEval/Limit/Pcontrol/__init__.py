from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PcontrolCls:
	"""Pcontrol commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pcontrol", core, parent)

	@property
	def hsdpcch(self):
		"""hsdpcch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hsdpcch'):
			from .Hsdpcch import HsdpcchCls
			self._hsdpcch = HsdpcchCls(self._core, self._cmd_group)
		return self._hsdpcch

	@property
	def epStep(self):
		"""epStep commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_epStep'):
			from .EpStep import EpStepCls
			self._epStep = EpStepCls(self._core, self._cmd_group)
		return self._epStep

	def clone(self) -> 'PcontrolCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PcontrolCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
