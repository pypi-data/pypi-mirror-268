from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LimitCls:
	"""Limit commands group definition. 13 total commands, 4 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)

	@property
	def ilpControl(self):
		"""ilpControl commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_ilpControl'):
			from .IlpControl import IlpControlCls
			self._ilpControl = IlpControlCls(self._core, self._cmd_group)
		return self._ilpControl

	@property
	def mpedch(self):
		"""mpedch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mpedch'):
			from .Mpedch import MpedchCls
			self._mpedch = MpedchCls(self._core, self._cmd_group)
		return self._mpedch

	@property
	def ctfc(self):
		"""ctfc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ctfc'):
			from .Ctfc import CtfcCls
			self._ctfc = CtfcCls(self._core, self._cmd_group)
		return self._ctfc

	@property
	def ulcm(self):
		"""ulcm commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ulcm'):
			from .Ulcm import UlcmCls
			self._ulcm = UlcmCls(self._core, self._cmd_group)
		return self._ulcm

	def get_dhib(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:DHIB \n
		Snippet: value: float = driver.configure.wcdmaMeas.tpc.limit.get_dhib() \n
		No command help available \n
			:return: min_power: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:DHIB?')
		return Conversions.str_to_float(response)

	def set_dhib(self, min_power: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:DHIB \n
		Snippet: driver.configure.wcdmaMeas.tpc.limit.set_dhib(min_power = 1.0) \n
		No command help available \n
			:param min_power: No help available
		"""
		param = Conversions.decimal_value_to_str(min_power)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:DHIB {param}')

	def clone(self) -> 'LimitCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LimitCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
