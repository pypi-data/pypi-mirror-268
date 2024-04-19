from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrachCls:
	"""Prach commands group definition. 30 total commands, 2 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prach", core, parent)

	@property
	def limit(self):
		"""limit commands group. 4 Sub-classes, 3 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import LimitCls
			self._limit = LimitCls(self._core, self._cmd_group)
		return self._limit

	@property
	def result(self):
		"""result commands group. 1 Sub-classes, 8 commands."""
		if not hasattr(self, '_result'):
			from .Result import ResultCls
			self._result = ResultCls(self._core, self._cmd_group)
		return self._result

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:TOUT \n
		Snippet: value: float = driver.configure.wcdmaMeas.prach.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually. When the measurement has completed the first measurement
		cycle (first single shot) , the statistical depth is reached and the timer is reset. If the first measurement cycle has
		not been completed when the timer expires, the measurement is stopped. The measurement state changes to RDY.
		The reliability indicator is set to 1, indicating that a measurement timeout occurred. Still running READ, FETCh or
		CALCulate commands are completed, returning the available results. At least for some results, there are no values at all
		or the statistical depth has not been reached. A timeout of 0 s corresponds to an infinite measurement timeout. \n
			:return: timeout: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:PRACh:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:TOUT \n
		Snippet: driver.configure.wcdmaMeas.prach.set_timeout(timeout = 1.0) \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually. When the measurement has completed the first measurement
		cycle (first single shot) , the statistical depth is reached and the timer is reset. If the first measurement cycle has
		not been completed when the timer expires, the measurement is stopped. The measurement state changes to RDY.
		The reliability indicator is set to 1, indicating that a measurement timeout occurred. Still running READ, FETCh or
		CALCulate commands are completed, returning the available results. At least for some results, there are no values at all
		or the statistical depth has not been reached. A timeout of 0 s corresponds to an infinite measurement timeout. \n
			:param timeout: No help available
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:TOUT {param}')

	def get_mpreamble(self) -> int:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:MPReamble \n
		Snippet: value: int = driver.configure.wcdmaMeas.prach.get_mpreamble() \n
		Specifies the number of preambles to be measured. \n
			:return: preambles: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:PRACh:MPReamble?')
		return Conversions.str_to_int(response)

	def set_mpreamble(self, preambles: int) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:MPReamble \n
		Snippet: driver.configure.wcdmaMeas.prach.set_mpreamble(preambles = 1) \n
		Specifies the number of preambles to be measured. \n
			:param preambles: No help available
		"""
		param = Conversions.decimal_value_to_str(preambles)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:MPReamble {param}')

	def get_ppreamble(self) -> int:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:PPReamble \n
		Snippet: value: int = driver.configure.wcdmaMeas.prach.get_ppreamble() \n
		Selects the preamble used to determine the single preamble results, i.e. the ... vs Chip results and the I/Q diagram. The
		number of the preselected preamble must be smaller than the number of measured preambles (method RsCMPX_WcdmaMeas.
		Configure.WcdmaMeas.Prach.mpreamble) . \n
			:return: preamble: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:PRACh:PPReamble?')
		return Conversions.str_to_int(response)

	def set_ppreamble(self, preamble: int) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:PPReamble \n
		Snippet: driver.configure.wcdmaMeas.prach.set_ppreamble(preamble = 1) \n
		Selects the preamble used to determine the single preamble results, i.e. the ... vs Chip results and the I/Q diagram. The
		number of the preselected preamble must be smaller than the number of measured preambles (method RsCMPX_WcdmaMeas.
		Configure.WcdmaMeas.Prach.mpreamble) . \n
			:param preamble: No help available
		"""
		param = Conversions.decimal_value_to_str(preamble)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:PPReamble {param}')

	def get_off_power(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:OFFPower \n
		Snippet: value: bool = driver.configure.wcdmaMeas.prach.get_off_power() \n
		Enables or disables the measurement of the off power before and after the last preamble. \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:PRACh:OFFPower?')
		return Conversions.str_to_bool(response)

	def set_off_power(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:OFFPower \n
		Snippet: driver.configure.wcdmaMeas.prach.set_off_power(enable = False) \n
		Enables or disables the measurement of the off power before and after the last preamble. \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:OFFPower {param}')

	def get_mo_exception(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:MOEXception \n
		Snippet: value: bool = driver.configure.wcdmaMeas.prach.get_mo_exception() \n
		Specifies whether measurement results that the CMP180 identifies as faulty or inaccurate are rejected. \n
			:return: meas_on_exception: OFF: Faulty results are rejected. ON: Results are never rejected.
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:PRACh:MOEXception?')
		return Conversions.str_to_bool(response)

	def set_mo_exception(self, meas_on_exception: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:MOEXception \n
		Snippet: driver.configure.wcdmaMeas.prach.set_mo_exception(meas_on_exception = False) \n
		Specifies whether measurement results that the CMP180 identifies as faulty or inaccurate are rejected. \n
			:param meas_on_exception: OFF: Faulty results are rejected. ON: Results are never rejected.
		"""
		param = Conversions.bool_to_str(meas_on_exception)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:MOEXception {param}')

	def clone(self) -> 'PrachCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PrachCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
