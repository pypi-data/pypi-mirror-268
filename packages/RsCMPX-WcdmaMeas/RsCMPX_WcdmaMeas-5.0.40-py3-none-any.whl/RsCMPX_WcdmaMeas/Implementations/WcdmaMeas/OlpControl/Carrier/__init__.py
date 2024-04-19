from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CarrierCls:
	"""Carrier commands group definition. 2 total commands, 1 Subgroups, 0 group commands
	Repeated Capability: CARRierExt, default value after init: CARRierExt.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("carrier", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_cARRierExt_get', 'repcap_cARRierExt_set', repcap.CARRierExt.Nr1)

	def repcap_cARRierExt_set(self, cARRierExt: repcap.CARRierExt) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to CARRierExt.Default
		Default value after init: CARRierExt.Nr1"""
		self._cmd_group.set_repcap_enum_value(cARRierExt)

	def repcap_cARRierExt_get(self) -> repcap.CARRierExt:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def uepPower(self):
		"""uepPower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_uepPower'):
			from .UepPower import UepPowerCls
			self._uepPower = UepPowerCls(self._core, self._cmd_group)
		return self._uepPower

	def clone(self) -> 'CarrierCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CarrierCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
