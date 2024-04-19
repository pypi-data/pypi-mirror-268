from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OlpControlCls:
	"""OlpControl commands group definition. 10 total commands, 2 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("olpControl", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def carrier(self):
		"""carrier commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .Carrier import CarrierCls
			self._carrier = CarrierCls(self._core, self._cmd_group)
		return self._carrier

	def stop(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: STOP:WCDMa:MEASurement<instance>:OLPControl \n
		Snippet: driver.wcdmaMeas.olpControl.stop() \n
		No command help available \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:WCDMa:MEASurement<Instance>:OLPControl', opc_timeout_ms)

	def abort(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: ABORt:WCDMa:MEASurement<instance>:OLPControl \n
		Snippet: driver.wcdmaMeas.olpControl.abort() \n
		No command help available \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:WCDMa:MEASurement<Instance>:OLPControl', opc_timeout_ms)

	def initiate(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate:WCDMa:MEASurement<instance>:OLPControl \n
		Snippet: driver.wcdmaMeas.olpControl.initiate() \n
		No command help available \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:WCDMa:MEASurement<Instance>:OLPControl', opc_timeout_ms)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Ue_Pwr_C_1: float: No parameter help available
			- Olpc_1: float: No parameter help available
			- Slot_No_C_1: int: No parameter help available
			- Olpc_2: float: No parameter help available
			- Slot_No_C_2: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Ue_Pwr_C_1'),
			ArgStruct.scalar_float('Olpc_1'),
			ArgStruct.scalar_int('Slot_No_C_1'),
			ArgStruct.scalar_float('Olpc_2'),
			ArgStruct.scalar_int('Slot_No_C_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ue_Pwr_C_1: float = None
			self.Olpc_1: float = None
			self.Slot_No_C_1: int = None
			self.Olpc_2: float = None
			self.Slot_No_C_2: int = None

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:OLPControl \n
		Snippet: value: ResultData = driver.wcdmaMeas.olpControl.read() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:OLPControl?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:OLPControl \n
		Snippet: value: ResultData = driver.wcdmaMeas.olpControl.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:OLPControl?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Olpc_1: float or bool: No parameter help available
			- Olpc_2: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Olpc_1'),
			ArgStruct.scalar_float_ext('Olpc_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Olpc_1: float or bool = None
			self.Olpc_2: float or bool = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WCDMa:MEASurement<instance>:OLPControl \n
		Snippet: value: CalculateStruct = driver.wcdmaMeas.olpControl.calculate() \n
		No command help available \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WCDMa:MEASurement<Instance>:OLPControl?', self.__class__.CalculateStruct())

	def clone(self) -> 'OlpControlCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = OlpControlCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
