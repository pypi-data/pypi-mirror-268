from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PcontrolCls:
	"""Pcontrol commands group definition. 7 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pcontrol", core, parent)

	@property
	def maxPower(self):
		"""maxPower commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_maxPower'):
			from .MaxPower import MaxPowerCls
			self._maxPower = MaxPowerCls(self._core, self._cmd_group)
		return self._maxPower

	@property
	def pstep(self):
		"""pstep commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pstep'):
			from .Pstep import PstepCls
			self._pstep = PstepCls(self._core, self._cmd_group)
		return self._pstep

	@property
	def olPower(self):
		"""olPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_olPower'):
			from .OlPower import OlPowerCls
			self._olPower = OlPowerCls(self._core, self._cmd_group)
		return self._olPower

	def get_off_power(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:LIMit:PCONtrol:OFFPower \n
		Snippet: value: float or bool = driver.configure.wcdmaMeas.prach.limit.pcontrol.get_off_power() \n
		Defines an upper OFF power limit. It also enables or disables the limit check. \n
			:return: limit: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:PRACh:LIMit:PCONtrol:OFFPower?')
		return Conversions.str_to_float_or_bool(response)

	def set_off_power(self, limit: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:LIMit:PCONtrol:OFFPower \n
		Snippet: driver.configure.wcdmaMeas.prach.limit.pcontrol.set_off_power(limit = 1.0) \n
		Defines an upper OFF power limit. It also enables or disables the limit check. \n
			:param limit: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(limit)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:LIMit:PCONtrol:OFFPower {param}')

	def clone(self) -> 'PcontrolCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PcontrolCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
