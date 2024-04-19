from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiEvalCls:
	"""MultiEval commands group definition. 8 total commands, 2 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("multiEval", core, parent)

	@property
	def listPy(self):
		"""listPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPyCls
			self._listPy = ListPyCls(self._core, self._cmd_group)
		return self._listPy

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import CatalogCls
			self._catalog = CatalogCls(self._core, self._cmd_group)
		return self._catalog

	def get_delay(self) -> float:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:MEValuation:DELay \n
		Snippet: value: float = driver.trigger.wcdmaMeas.multiEval.get_delay() \n
		Defines a time delaying the start of the measurement relative to the trigger event. A delay is useful if the trigger
		event and the uplink DPCH slot border are not synchronous. A measurement always starts at an uplink DPCH slot border.
		Triggering a measurement at another time can yield a synchronization error. For internal trigger sources aligned to the
		downlink DPCH, an additional delay of 1024 chips is automatically applied. It corresponds to the assumed delay between
		downlink and uplink slot. This setting has no influence on free run measurements. \n
			:return: delay: No help available
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:MEValuation:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, delay: float) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:MEValuation:DELay \n
		Snippet: driver.trigger.wcdmaMeas.multiEval.set_delay(delay = 1.0) \n
		Defines a time delaying the start of the measurement relative to the trigger event. A delay is useful if the trigger
		event and the uplink DPCH slot border are not synchronous. A measurement always starts at an uplink DPCH slot border.
		Triggering a measurement at another time can yield a synchronization error. For internal trigger sources aligned to the
		downlink DPCH, an additional delay of 1024 chips is automatically applied. It corresponds to the assumed delay between
		downlink and uplink slot. This setting has no influence on free run measurements. \n
			:param delay: No help available
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:MEValuation:DELay {param}')

	def get_mgap(self) -> float:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:MEValuation:MGAP \n
		Snippet: value: float = driver.trigger.wcdmaMeas.multiEval.get_mgap() \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. \n
			:return: minimum_gap: No help available
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:MEValuation:MGAP?')
		return Conversions.str_to_float(response)

	def set_mgap(self, minimum_gap: float) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:MEValuation:MGAP \n
		Snippet: driver.trigger.wcdmaMeas.multiEval.set_mgap(minimum_gap = 1.0) \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. \n
			:param minimum_gap: No help available
		"""
		param = Conversions.decimal_value_to_str(minimum_gap)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:MEValuation:MGAP {param}')

	def get_threshold(self) -> float:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:MEValuation:THReshold \n
		Snippet: value: float = driver.trigger.wcdmaMeas.multiEval.get_threshold() \n
		Defines the trigger threshold for power trigger sources. \n
			:return: level: No help available
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:MEValuation:THReshold?')
		return Conversions.str_to_float(response)

	def set_threshold(self, level: float) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:MEValuation:THReshold \n
		Snippet: driver.trigger.wcdmaMeas.multiEval.set_threshold(level = 1.0) \n
		Defines the trigger threshold for power trigger sources. \n
			:param level: No help available
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:MEValuation:THReshold {param}')

	# noinspection PyTypeChecker
	def get_slope(self) -> enums.SignalSlope:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:MEValuation:SLOPe \n
		Snippet: value: enums.SignalSlope = driver.trigger.wcdmaMeas.multiEval.get_slope() \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:return: slope: REDGe: Rising edge FEDGe: Falling edge
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:MEValuation:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SignalSlope)

	def set_slope(self, slope: enums.SignalSlope) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:MEValuation:SLOPe \n
		Snippet: driver.trigger.wcdmaMeas.multiEval.set_slope(slope = enums.SignalSlope.FEDGe) \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:param slope: REDGe: Rising edge FEDGe: Falling edge
		"""
		param = Conversions.enum_scalar_to_str(slope, enums.SignalSlope)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:MEValuation:SLOPe {param}')

	def get_timeout(self) -> float or bool:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:MEValuation:TOUT \n
		Snippet: value: float or bool = driver.trigger.wcdmaMeas.multiEval.get_timeout() \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. This setting has no influence on Free Run measurements. \n
			:return: timeout: (float or boolean) No help available
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:MEValuation:TOUT?')
		return Conversions.str_to_float_or_bool(response)

	def set_timeout(self, timeout: float or bool) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:MEValuation:TOUT \n
		Snippet: driver.trigger.wcdmaMeas.multiEval.set_timeout(timeout = 1.0) \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. This setting has no influence on Free Run measurements. \n
			:param timeout: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(timeout)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:MEValuation:TOUT {param}')

	def get_source(self) -> str:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:MEValuation:SOURce \n
		Snippet: value: str = driver.trigger.wcdmaMeas.multiEval.get_source() \n
		Selects the source of the trigger events. Some values are always available. They are listed below. Depending on the
		installed options, additional values are available. You can query a list of all supported values via TRIGger:...
		:CATalog:SOURce?. \n
			:return: source: 'Free Run (Standard) ': Free run (standard synchronization) 'Free Run (Fast Sync) ': Free run (fast synchronization) 'IF Power': Power trigger (normal synchronization) 'IF Power (Sync) ': Power trigger (extended synchronization)
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:MEValuation:SOURce?')
		return trim_str_response(response)

	def set_source(self, source: str) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:MEValuation:SOURce \n
		Snippet: driver.trigger.wcdmaMeas.multiEval.set_source(source = 'abc') \n
		Selects the source of the trigger events. Some values are always available. They are listed below. Depending on the
		installed options, additional values are available. You can query a list of all supported values via TRIGger:...
		:CATalog:SOURce?. \n
			:param source: 'Free Run (Standard) ': Free run (standard synchronization) 'Free Run (Fast Sync) ': Free run (fast synchronization) 'IF Power': Power trigger (normal synchronization) 'IF Power (Sync) ': Power trigger (extended synchronization)
		"""
		param = Conversions.value_to_quoted_str(source)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:MEValuation:SOURce {param}')

	def clone(self) -> 'MultiEvalCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultiEvalCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
