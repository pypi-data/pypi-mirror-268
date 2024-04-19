from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AclrCls:
	"""Aclr commands group definition. 6 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aclr", core, parent)

	@property
	def m(self):
		"""m commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_m'):
			from .M import MCls
			self._m = MCls(self._core, self._cmd_group)
		return self._m

	@property
	def p(self):
		"""p commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_p'):
			from .P import PCls
			self._p = PCls(self._core, self._cmd_group)
		return self._p

	def clone(self) -> 'AclrCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AclrCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
