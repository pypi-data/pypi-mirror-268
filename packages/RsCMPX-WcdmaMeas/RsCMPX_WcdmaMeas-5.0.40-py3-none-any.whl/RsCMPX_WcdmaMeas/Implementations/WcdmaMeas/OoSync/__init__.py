from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OoSyncCls:
	"""OoSync commands group definition. 8 total commands, 1 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ooSync", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Out_Pow_Ab_Max: enums.ResultStatus2: No parameter help available
			- Out_Pow_Ab_Min: enums.ResultStatus2: No parameter help available
			- Out_Pow_Ccurrent: enums.ResultStatus2: No parameter help available
			- Out_Pow_Cd_Max: enums.ResultStatus2: No parameter help available
			- Out_Pow_Cd_Min: enums.ResultStatus2: No parameter help available
			- Out_Pow_De_Max: enums.ResultStatus2: No parameter help available
			- Out_Pow_De_Min: enums.ResultStatus2: No parameter help available
			- Out_Pow_Fcurrent: enums.ResultStatus2: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Out_Pow_Ab_Max', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Pow_Ab_Min', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Pow_Ccurrent', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Pow_Cd_Max', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Pow_Cd_Min', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Pow_De_Max', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Pow_De_Min', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Pow_Fcurrent', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Pow_Ab_Max: enums.ResultStatus2 = None
			self.Out_Pow_Ab_Min: enums.ResultStatus2 = None
			self.Out_Pow_Ccurrent: enums.ResultStatus2 = None
			self.Out_Pow_Cd_Max: enums.ResultStatus2 = None
			self.Out_Pow_Cd_Min: enums.ResultStatus2 = None
			self.Out_Pow_De_Max: enums.ResultStatus2 = None
			self.Out_Pow_De_Min: enums.ResultStatus2 = None
			self.Out_Pow_Fcurrent: enums.ResultStatus2 = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WCDMa:MEASurement<instance>:OOSYnc \n
		Snippet: value: CalculateStruct = driver.wcdmaMeas.ooSync.calculate() \n
		No command help available \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WCDMa:MEASurement<Instance>:OOSYnc?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Out_Pow_Ab_Max: float: No parameter help available
			- Out_Pow_Ab_Min: float: No parameter help available
			- Out_Pow_Ccurrent: float: No parameter help available
			- Out_Powc_State: enums.OutPowFstate: No parameter help available
			- Out_Pow_Cd_Max: float: No parameter help available
			- Out_Pow_Cd_Min: float: No parameter help available
			- Out_Pow_De_Max: float: No parameter help available
			- Out_Pow_De_Min: float: No parameter help available
			- Out_Pow_Fcurrent: float: No parameter help available
			- Out_Pow_Fstate: enums.OutPowFstate: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Out_Pow_Ab_Max'),
			ArgStruct.scalar_float('Out_Pow_Ab_Min'),
			ArgStruct.scalar_float('Out_Pow_Ccurrent'),
			ArgStruct.scalar_enum('Out_Powc_State', enums.OutPowFstate),
			ArgStruct.scalar_float('Out_Pow_Cd_Max'),
			ArgStruct.scalar_float('Out_Pow_Cd_Min'),
			ArgStruct.scalar_float('Out_Pow_De_Max'),
			ArgStruct.scalar_float('Out_Pow_De_Min'),
			ArgStruct.scalar_float('Out_Pow_Fcurrent'),
			ArgStruct.scalar_enum('Out_Pow_Fstate', enums.OutPowFstate)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Pow_Ab_Max: float = None
			self.Out_Pow_Ab_Min: float = None
			self.Out_Pow_Ccurrent: float = None
			self.Out_Powc_State: enums.OutPowFstate = None
			self.Out_Pow_Cd_Max: float = None
			self.Out_Pow_Cd_Min: float = None
			self.Out_Pow_De_Max: float = None
			self.Out_Pow_De_Min: float = None
			self.Out_Pow_Fcurrent: float = None
			self.Out_Pow_Fstate: enums.OutPowFstate = None

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:OOSYnc \n
		Snippet: value: ResultData = driver.wcdmaMeas.ooSync.read() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:OOSYnc?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:OOSYnc \n
		Snippet: value: ResultData = driver.wcdmaMeas.ooSync.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:OOSYnc?', self.__class__.ResultData())

	def stop(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: STOP:WCDMa:MEASurement<instance>:OOSYnc \n
		Snippet: driver.wcdmaMeas.ooSync.stop() \n
		No command help available \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:WCDMa:MEASurement<Instance>:OOSYnc', opc_timeout_ms)

	def abort(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: ABORt:WCDMa:MEASurement<instance>:OOSYnc \n
		Snippet: driver.wcdmaMeas.ooSync.abort() \n
		No command help available \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:WCDMa:MEASurement<Instance>:OOSYnc', opc_timeout_ms)

	def initiate(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate:WCDMa:MEASurement<instance>:OOSYnc \n
		Snippet: driver.wcdmaMeas.ooSync.initiate() \n
		No command help available \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:WCDMa:MEASurement<Instance>:OOSYnc', opc_timeout_ms)

	def clone(self) -> 'OoSyncCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = OoSyncCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
