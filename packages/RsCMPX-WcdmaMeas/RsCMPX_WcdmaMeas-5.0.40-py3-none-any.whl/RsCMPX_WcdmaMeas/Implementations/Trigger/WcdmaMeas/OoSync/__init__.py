from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OoSyncCls:
	"""OoSync commands group definition. 7 total commands, 1 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ooSync", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import CatalogCls
			self._catalog = CatalogCls(self._core, self._cmd_group)
		return self._catalog

	def get_delay(self) -> float:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:DELay \n
		Snippet: value: float = driver.trigger.wcdmaMeas.ooSync.get_delay() \n
		No command help available \n
			:return: delay: No help available
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, delay: float) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:DELay \n
		Snippet: driver.trigger.wcdmaMeas.ooSync.set_delay(delay = 1.0) \n
		No command help available \n
			:param delay: No help available
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:DELay {param}')

	def get_mgap(self) -> float:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:MGAP \n
		Snippet: value: float = driver.trigger.wcdmaMeas.ooSync.get_mgap() \n
		No command help available \n
			:return: minimum_gap: No help available
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:MGAP?')
		return Conversions.str_to_float(response)

	def set_mgap(self, minimum_gap: float) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:MGAP \n
		Snippet: driver.trigger.wcdmaMeas.ooSync.set_mgap(minimum_gap = 1.0) \n
		No command help available \n
			:param minimum_gap: No help available
		"""
		param = Conversions.decimal_value_to_str(minimum_gap)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:MGAP {param}')

	def get_threshold(self) -> float:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:THReshold \n
		Snippet: value: float = driver.trigger.wcdmaMeas.ooSync.get_threshold() \n
		No command help available \n
			:return: level: No help available
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:THReshold?')
		return Conversions.str_to_float(response)

	def set_threshold(self, level: float) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:THReshold \n
		Snippet: driver.trigger.wcdmaMeas.ooSync.set_threshold(level = 1.0) \n
		No command help available \n
			:param level: No help available
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:THReshold {param}')

	# noinspection PyTypeChecker
	def get_slope(self) -> enums.SignalSlope:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:SLOPe \n
		Snippet: value: enums.SignalSlope = driver.trigger.wcdmaMeas.ooSync.get_slope() \n
		No command help available \n
			:return: slope: No help available
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SignalSlope)

	def set_slope(self, slope: enums.SignalSlope) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:SLOPe \n
		Snippet: driver.trigger.wcdmaMeas.ooSync.set_slope(slope = enums.SignalSlope.FEDGe) \n
		No command help available \n
			:param slope: No help available
		"""
		param = Conversions.enum_scalar_to_str(slope, enums.SignalSlope)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:SLOPe {param}')

	def get_timeout(self) -> float or bool:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:TOUT \n
		Snippet: value: float or bool = driver.trigger.wcdmaMeas.ooSync.get_timeout() \n
		No command help available \n
			:return: timeout: (float or boolean) No help available
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:TOUT?')
		return Conversions.str_to_float_or_bool(response)

	def set_timeout(self, timeout: float or bool) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:TOUT \n
		Snippet: driver.trigger.wcdmaMeas.ooSync.set_timeout(timeout = 1.0) \n
		No command help available \n
			:param timeout: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(timeout)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:TOUT {param}')

	def get_source(self) -> str:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:SOURce \n
		Snippet: value: str = driver.trigger.wcdmaMeas.ooSync.get_source() \n
		No command help available \n
			:return: source: No help available
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:SOURce?')
		return trim_str_response(response)

	def set_source(self, source: str) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:SOURce \n
		Snippet: driver.trigger.wcdmaMeas.ooSync.set_source(source = 'abc') \n
		No command help available \n
			:param source: No help available
		"""
		param = Conversions.value_to_quoted_str(source)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:SOURce {param}')

	def clone(self) -> 'OoSyncCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = OoSyncCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
