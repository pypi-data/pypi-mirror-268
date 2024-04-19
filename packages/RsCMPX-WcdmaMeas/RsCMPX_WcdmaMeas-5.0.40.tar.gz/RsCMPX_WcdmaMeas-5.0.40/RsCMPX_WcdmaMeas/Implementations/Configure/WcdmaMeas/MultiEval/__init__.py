from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiEvalCls:
	"""MultiEval commands group definition. 75 total commands, 11 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("multiEval", core, parent)

	@property
	def scount(self):
		"""scount commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_scount'):
			from .Scount import ScountCls
			self._scount = ScountCls(self._core, self._cmd_group)
		return self._scount

	@property
	def limit(self):
		"""limit commands group. 9 Sub-classes, 3 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import LimitCls
			self._limit = LimitCls(self._core, self._cmd_group)
		return self._limit

	@property
	def rotation(self):
		"""rotation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rotation'):
			from .Rotation import RotationCls
			self._rotation = RotationCls(self._core, self._cmd_group)
		return self._rotation

	@property
	def dsFactor(self):
		"""dsFactor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dsFactor'):
			from .DsFactor import DsFactorCls
			self._dsFactor = DsFactorCls(self._core, self._cmd_group)
		return self._dsFactor

	@property
	def sscalar(self):
		"""sscalar commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sscalar'):
			from .Sscalar import SscalarCls
			self._sscalar = SscalarCls(self._core, self._cmd_group)
		return self._sscalar

	@property
	def cdThreshold(self):
		"""cdThreshold commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cdThreshold'):
			from .CdThreshold import CdThresholdCls
			self._cdThreshold = CdThresholdCls(self._core, self._cmd_group)
		return self._cdThreshold

	@property
	def dmode(self):
		"""dmode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dmode'):
			from .Dmode import DmodeCls
			self._dmode = DmodeCls(self._core, self._cmd_group)
		return self._dmode

	@property
	def amode(self):
		"""amode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_amode'):
			from .Amode import AmodeCls
			self._amode = AmodeCls(self._core, self._cmd_group)
		return self._amode

	@property
	def mperiod(self):
		"""mperiod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mperiod'):
			from .Mperiod import MperiodCls
			self._mperiod = MperiodCls(self._core, self._cmd_group)
		return self._mperiod

	@property
	def result(self):
		"""result commands group. 1 Sub-classes, 17 commands."""
		if not hasattr(self, '_result'):
			from .Result import ResultCls
			self._result = ResultCls(self._core, self._cmd_group)
		return self._result

	@property
	def listPy(self):
		"""listPy commands group. 2 Sub-classes, 6 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPyCls
			self._listPy = ListPyCls(self._core, self._cmd_group)
		return self._listPy

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:TOUT \n
		Snippet: value: float = driver.configure.wcdmaMeas.multiEval.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually. When the measurement has completed the first measurement
		cycle (first single shot) , the statistical depth is reached and the timer is reset. If the first measurement cycle has
		not been completed when the timer expires, the measurement is stopped. The measurement state changes to RDY.
		The reliability indicator is set to 1, indicating that a measurement timeout occurred. Still running READ, FETCh or
		CALCulate commands are completed, returning the available results. At least for some results, there are no values at all
		or the statistical depth has not been reached. A timeout of 0 s corresponds to an infinite measurement timeout. \n
			:return: timeout: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:TOUT \n
		Snippet: driver.configure.wcdmaMeas.multiEval.set_timeout(timeout = 1.0) \n
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
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:TOUT {param}')

	def get_ms_count(self) -> int:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:MSCount \n
		Snippet: value: int = driver.configure.wcdmaMeas.multiEval.get_ms_count() \n
		Selects the total number of measured slots. \n
			:return: slot_count: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:MSCount?')
		return Conversions.str_to_int(response)

	def set_ms_count(self, slot_count: int) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:MSCount \n
		Snippet: driver.configure.wcdmaMeas.multiEval.set_ms_count(slot_count = 1) \n
		Selects the total number of measured slots. \n
			:param slot_count: No help available
		"""
		param = Conversions.decimal_value_to_str(slot_count)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:MSCount {param}')

	def get_pslot(self) -> int:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:PSLot \n
		Snippet: value: int = driver.configure.wcdmaMeas.multiEval.get_pslot() \n
		Selects the slot where the CMP180 calculates the results of single slot measurements: ACLR, emission mask, EVM vs chip,
		CD monitor. The number of the preselected slot must be smaller than the number of measured slots (method RsCMPX_WcdmaMeas.
		Configure.WcdmaMeas.MultiEval.msCount) . \n
			:return: slot_number: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:PSLot?')
		return Conversions.str_to_int(response)

	def set_pslot(self, slot_number: int) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:PSLot \n
		Snippet: driver.configure.wcdmaMeas.multiEval.set_pslot(slot_number = 1) \n
		Selects the slot where the CMP180 calculates the results of single slot measurements: ACLR, emission mask, EVM vs chip,
		CD monitor. The number of the preselected slot must be smaller than the number of measured slots (method RsCMPX_WcdmaMeas.
		Configure.WcdmaMeas.MultiEval.msCount) . \n
			:param slot_number: No help available
		"""
		param = Conversions.decimal_value_to_str(slot_number)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:PSLot {param}')

	# noinspection PyTypeChecker
	def get_synch(self) -> enums.SlotNumber:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:SYNCh \n
		Snippet: value: enums.SlotNumber = driver.configure.wcdmaMeas.multiEval.get_synch() \n
		Selects a slot number within the UL WCDMA frames (0 to 14) that the CMP180 displays as the first slot in the measurement
		interval. \n
			:return: slot_number: ANY: No frame synchronization SL0 ... SL14: First slot = slot 0 ... slot 14
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:SYNCh?')
		return Conversions.str_to_scalar_enum(response, enums.SlotNumber)

	def set_synch(self, slot_number: enums.SlotNumber) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:SYNCh \n
		Snippet: driver.configure.wcdmaMeas.multiEval.set_synch(slot_number = enums.SlotNumber.ANY) \n
		Selects a slot number within the UL WCDMA frames (0 to 14) that the CMP180 displays as the first slot in the measurement
		interval. \n
			:param slot_number: ANY: No frame synchronization SL0 ... SL14: First slot = slot 0 ... slot 14
		"""
		param = Conversions.enum_scalar_to_str(slot_number, enums.SlotNumber)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:SYNCh {param}')

	def get_mo_exception(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:MOEXception \n
		Snippet: value: bool = driver.configure.wcdmaMeas.multiEval.get_mo_exception() \n
		Specifies whether measurement results that the CMP180 identifies as faulty or inaccurate are rejected. \n
			:return: meas_on_exception: OFF: Faulty results are rejected. ON: Results are never rejected.
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:MOEXception?')
		return Conversions.str_to_bool(response)

	def set_mo_exception(self, meas_on_exception: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:MOEXception \n
		Snippet: driver.configure.wcdmaMeas.multiEval.set_mo_exception(meas_on_exception = False) \n
		Specifies whether measurement results that the CMP180 identifies as faulty or inaccurate are rejected. \n
			:param meas_on_exception: OFF: Faulty results are rejected. ON: Results are never rejected.
		"""
		param = Conversions.bool_to_str(meas_on_exception)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:MOEXception {param}')

	# noinspection PyTypeChecker
	def get_scondition(self) -> enums.StopCondition:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:SCONdition \n
		Snippet: value: enums.StopCondition = driver.configure.wcdmaMeas.multiEval.get_scondition() \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:return: stop_condition: NONE: Continue measurement irrespective of the limit check SLFail: Stop measurement on limit failure
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:SCONdition?')
		return Conversions.str_to_scalar_enum(response, enums.StopCondition)

	def set_scondition(self, stop_condition: enums.StopCondition) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:SCONdition \n
		Snippet: driver.configure.wcdmaMeas.multiEval.set_scondition(stop_condition = enums.StopCondition.NONE) \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:param stop_condition: NONE: Continue measurement irrespective of the limit check SLFail: Stop measurement on limit failure
		"""
		param = Conversions.enum_scalar_to_str(stop_condition, enums.StopCondition)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:SCONdition {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.wcdmaMeas.multiEval.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:return: repetition: SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:REPetition \n
		Snippet: driver.configure.wcdmaMeas.multiEval.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:param repetition: SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:REPetition {param}')

	def clone(self) -> 'MultiEvalCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultiEvalCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
