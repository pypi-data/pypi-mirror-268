from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrachCls:
	"""Prach commands group definition. 7 total commands, 1 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prach", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import CatalogCls
			self._catalog = CatalogCls(self._core, self._cmd_group)
		return self._catalog

	def get_delay(self) -> float:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:PRACh:DELay \n
		Snippet: value: float = driver.trigger.wcdmaMeas.prach.get_delay() \n
		Defines a time delaying the start of the measurement relative to the trigger event. \n
			:return: delay: No help available
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:PRACh:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, delay: float) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:PRACh:DELay \n
		Snippet: driver.trigger.wcdmaMeas.prach.set_delay(delay = 1.0) \n
		Defines a time delaying the start of the measurement relative to the trigger event. \n
			:param delay: No help available
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:PRACh:DELay {param}')

	def get_mgap(self) -> float:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:PRACh:MGAP \n
		Snippet: value: float = driver.trigger.wcdmaMeas.prach.get_mgap() \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. \n
			:return: minimum_gap: No help available
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:PRACh:MGAP?')
		return Conversions.str_to_float(response)

	def set_mgap(self, minimum_gap: float) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:PRACh:MGAP \n
		Snippet: driver.trigger.wcdmaMeas.prach.set_mgap(minimum_gap = 1.0) \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. \n
			:param minimum_gap: No help available
		"""
		param = Conversions.decimal_value_to_str(minimum_gap)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:PRACh:MGAP {param}')

	def get_threshold(self) -> float:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:PRACh:THReshold \n
		Snippet: value: float = driver.trigger.wcdmaMeas.prach.get_threshold() \n
		Defines the trigger threshold for power trigger sources. \n
			:return: level: No help available
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:PRACh:THReshold?')
		return Conversions.str_to_float(response)

	def set_threshold(self, level: float) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:PRACh:THReshold \n
		Snippet: driver.trigger.wcdmaMeas.prach.set_threshold(level = 1.0) \n
		Defines the trigger threshold for power trigger sources. \n
			:param level: No help available
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:PRACh:THReshold {param}')

	# noinspection PyTypeChecker
	def get_slope(self) -> enums.SignalSlope:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:PRACh:SLOPe \n
		Snippet: value: enums.SignalSlope = driver.trigger.wcdmaMeas.prach.get_slope() \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:return: slope: REDGe: Rising edge FEDGe: Falling edge
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:PRACh:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SignalSlope)

	def set_slope(self, slope: enums.SignalSlope) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:PRACh:SLOPe \n
		Snippet: driver.trigger.wcdmaMeas.prach.set_slope(slope = enums.SignalSlope.FEDGe) \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:param slope: REDGe: Rising edge FEDGe: Falling edge
		"""
		param = Conversions.enum_scalar_to_str(slope, enums.SignalSlope)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:PRACh:SLOPe {param}')

	def get_timeout(self) -> float or bool:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:PRACh:TOUT \n
		Snippet: value: float or bool = driver.trigger.wcdmaMeas.prach.get_timeout() \n
		Selects the maximum time that the CMP180 waits for a trigger event before it stops the measurement in remote control mode
		or indicates a trigger timeout in manual operation mode. \n
			:return: timeout: (float or boolean) No help available
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:PRACh:TOUT?')
		return Conversions.str_to_float_or_bool(response)

	def set_timeout(self, timeout: float or bool) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:PRACh:TOUT \n
		Snippet: driver.trigger.wcdmaMeas.prach.set_timeout(timeout = 1.0) \n
		Selects the maximum time that the CMP180 waits for a trigger event before it stops the measurement in remote control mode
		or indicates a trigger timeout in manual operation mode. \n
			:param timeout: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(timeout)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:PRACh:TOUT {param}')

	def get_source(self) -> str:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:PRACh:SOURce \n
		Snippet: value: str = driver.trigger.wcdmaMeas.prach.get_source() \n
		Selects the source of the trigger events. Some values are always available. They are listed below. Depending on the
		installed options, additional values are available. You can query a list of all supported values via TRIGger:...
		:CATalog:SOURce?. \n
			:return: source: 'IF Power (Sync) ': Power trigger (extended synchronization)
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:PRACh:SOURce?')
		return trim_str_response(response)

	def set_source(self, source: str) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:PRACh:SOURce \n
		Snippet: driver.trigger.wcdmaMeas.prach.set_source(source = 'abc') \n
		Selects the source of the trigger events. Some values are always available. They are listed below. Depending on the
		installed options, additional values are available. You can query a list of all supported values via TRIGger:...
		:CATalog:SOURce?. \n
			:param source: 'IF Power (Sync) ': Power trigger (extended synchronization)
		"""
		param = Conversions.value_to_quoted_str(source)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:PRACh:SOURce {param}')

	def clone(self) -> 'PrachCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PrachCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
