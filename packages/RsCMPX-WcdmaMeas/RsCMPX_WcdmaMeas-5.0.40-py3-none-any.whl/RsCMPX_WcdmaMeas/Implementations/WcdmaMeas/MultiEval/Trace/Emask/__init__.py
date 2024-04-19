from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EmaskCls:
	"""Emask commands group definition. 30 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("emask", core, parent)

	@property
	def mfLeft(self):
		"""mfLeft commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mfLeft'):
			from .MfLeft import MfLeftCls
			self._mfLeft = MfLeftCls(self._core, self._cmd_group)
		return self._mfLeft

	@property
	def mfRight(self):
		"""mfRight commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mfRight'):
			from .MfRight import MfRightCls
			self._mfRight = MfRightCls(self._core, self._cmd_group)
		return self._mfRight

	@property
	def hkfLeft(self):
		"""hkfLeft commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_hkfLeft'):
			from .HkfLeft import HkfLeftCls
			self._hkfLeft = HkfLeftCls(self._core, self._cmd_group)
		return self._hkfLeft

	@property
	def hkfRight(self):
		"""hkfRight commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_hkfRight'):
			from .HkfRight import HkfRightCls
			self._hkfRight = HkfRightCls(self._core, self._cmd_group)
		return self._hkfRight

	@property
	def kfilter(self):
		"""kfilter commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_kfilter'):
			from .Kfilter import KfilterCls
			self._kfilter = KfilterCls(self._core, self._cmd_group)
		return self._kfilter

	def clone(self) -> 'EmaskCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EmaskCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
