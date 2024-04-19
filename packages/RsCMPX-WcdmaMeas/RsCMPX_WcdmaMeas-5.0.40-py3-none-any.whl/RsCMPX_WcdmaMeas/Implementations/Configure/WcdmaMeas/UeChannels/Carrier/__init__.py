from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CarrierCls:
	"""Carrier commands group definition. 6 total commands, 5 Subgroups, 0 group commands
	Repeated Capability: Carrier, default value after init: Carrier.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("carrier", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_carrier_get', 'repcap_carrier_set', repcap.Carrier.Nr1)

	def repcap_carrier_set(self, carrier: repcap.Carrier) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Carrier.Default
		Default value after init: Carrier.Nr1"""
		self._cmd_group.set_repcap_enum_value(carrier)

	def repcap_carrier_get(self) -> repcap.Carrier:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def edpdch(self):
		"""edpdch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_edpdch'):
			from .Edpdch import EdpdchCls
			self._edpdch = EdpdchCls(self._core, self._cmd_group)
		return self._edpdch

	@property
	def edpcch(self):
		"""edpcch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_edpcch'):
			from .Edpcch import EdpcchCls
			self._edpcch = EdpcchCls(self._core, self._cmd_group)
		return self._edpcch

	@property
	def hsdpcch(self):
		"""hsdpcch commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_hsdpcch'):
			from .Hsdpcch import HsdpcchCls
			self._hsdpcch = HsdpcchCls(self._core, self._cmd_group)
		return self._hsdpcch

	@property
	def dpdch(self):
		"""dpdch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dpdch'):
			from .Dpdch import DpdchCls
			self._dpdch = DpdchCls(self._core, self._cmd_group)
		return self._dpdch

	@property
	def dpcch(self):
		"""dpcch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dpcch'):
			from .Dpcch import DpcchCls
			self._dpcch = DpcchCls(self._core, self._cmd_group)
		return self._dpcch

	def clone(self) -> 'CarrierCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CarrierCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
