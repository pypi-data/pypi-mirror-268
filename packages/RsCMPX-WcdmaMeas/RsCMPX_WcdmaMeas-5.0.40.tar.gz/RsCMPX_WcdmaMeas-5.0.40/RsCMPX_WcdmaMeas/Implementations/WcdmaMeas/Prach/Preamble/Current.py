from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Ue_Power: float: Mean preamble power
			- Power_Steps: float: Mean preamble power minus mean power of previous preamble For the first preamble, NCAP is returned.
			- Carrier_Freq_Err: float: Carrier frequency error
			- Evm_Rms: float: Error vector magnitude RMS value
			- Evm_Peak: float: Error vector magnitude peak value
			- Mag_Error_Rms: float: Magnitude error RMS value
			- Mag_Error_Peak: float: Magnitude error peak value
			- Phase_Error_Rms: float: No parameter help available
			- Phase_Error_Peak: float: No parameter help available
			- Iq_Offset: float: I/Q origin offset
			- Iq_Imbalance: float: I/Q imbalance
			- Signature: int: Detected preamble signature"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Ue_Power'),
			ArgStruct.scalar_float('Power_Steps'),
			ArgStruct.scalar_float('Carrier_Freq_Err'),
			ArgStruct.scalar_float('Evm_Rms'),
			ArgStruct.scalar_float('Evm_Peak'),
			ArgStruct.scalar_float('Mag_Error_Rms'),
			ArgStruct.scalar_float('Mag_Error_Peak'),
			ArgStruct.scalar_float('Phase_Error_Rms'),
			ArgStruct.scalar_float('Phase_Error_Peak'),
			ArgStruct.scalar_float('Iq_Offset'),
			ArgStruct.scalar_float('Iq_Imbalance'),
			ArgStruct.scalar_int('Signature')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ue_Power: float = None
			self.Power_Steps: float = None
			self.Carrier_Freq_Err: float = None
			self.Evm_Rms: float = None
			self.Evm_Peak: float = None
			self.Mag_Error_Rms: float = None
			self.Mag_Error_Peak: float = None
			self.Phase_Error_Rms: float = None
			self.Phase_Error_Peak: float = None
			self.Iq_Offset: float = None
			self.Iq_Imbalance: float = None
			self.Signature: int = None

	def read(self, preamble=repcap.Preamble.Default) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:PRACh:PREamble<nr>:CURRent \n
		Snippet: value: ResultData = driver.wcdmaMeas.prach.preamble.current.read(preamble = repcap.Preamble.Default) \n
		Return the single value results for a selected preamble. \n
			:param preamble: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Preamble')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		preamble_cmd_val = self._cmd_group.get_repcap_cmd_value(preamble, repcap.Preamble)
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:PRACh:PREamble{preamble_cmd_val}:CURRent?', self.__class__.ResultData())

	def fetch(self, preamble=repcap.Preamble.Default) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:PRACh:PREamble<nr>:CURRent \n
		Snippet: value: ResultData = driver.wcdmaMeas.prach.preamble.current.fetch(preamble = repcap.Preamble.Default) \n
		Return the single value results for a selected preamble. \n
			:param preamble: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Preamble')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		preamble_cmd_val = self._cmd_group.get_repcap_cmd_value(preamble, repcap.Preamble)
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:PRACh:PREamble{preamble_cmd_val}:CURRent?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Ue_Power: float or bool: Mean preamble power
			- Power_Steps: float or bool: Mean preamble power minus mean power of previous preamble For the first preamble, NCAP is returned.
			- Carrier_Freq_Err: float or bool: Carrier frequency error
			- Evm_Rms: float or bool: Error vector magnitude RMS value
			- Evm_Peak: float or bool: Error vector magnitude peak value
			- Mag_Error_Rms: float or bool: Magnitude error RMS value
			- Mag_Error_Peak: float or bool: Magnitude error peak value
			- Phase_Error_Rms: float or bool: No parameter help available
			- Phase_Error_Peak: float or bool: No parameter help available
			- Iq_Offset: float or bool: I/Q origin offset
			- Iq_Imbalance: float or bool: I/Q imbalance"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Ue_Power'),
			ArgStruct.scalar_float_ext('Power_Steps'),
			ArgStruct.scalar_float_ext('Carrier_Freq_Err'),
			ArgStruct.scalar_float_ext('Evm_Rms'),
			ArgStruct.scalar_float_ext('Evm_Peak'),
			ArgStruct.scalar_float_ext('Mag_Error_Rms'),
			ArgStruct.scalar_float_ext('Mag_Error_Peak'),
			ArgStruct.scalar_float_ext('Phase_Error_Rms'),
			ArgStruct.scalar_float_ext('Phase_Error_Peak'),
			ArgStruct.scalar_float_ext('Iq_Offset'),
			ArgStruct.scalar_float_ext('Iq_Imbalance')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ue_Power: float or bool = None
			self.Power_Steps: float or bool = None
			self.Carrier_Freq_Err: float or bool = None
			self.Evm_Rms: float or bool = None
			self.Evm_Peak: float or bool = None
			self.Mag_Error_Rms: float or bool = None
			self.Mag_Error_Peak: float or bool = None
			self.Phase_Error_Rms: float or bool = None
			self.Phase_Error_Peak: float or bool = None
			self.Iq_Offset: float or bool = None
			self.Iq_Imbalance: float or bool = None

	def calculate(self, preamble=repcap.Preamble.Default) -> CalculateStruct:
		"""SCPI: CALCulate:WCDMa:MEASurement<instance>:PRACh:PREamble<nr>:CURRent \n
		Snippet: value: CalculateStruct = driver.wcdmaMeas.prach.preamble.current.calculate(preamble = repcap.Preamble.Default) \n
		Return the single value results for a selected preamble. \n
		Suppressed linked return values: reliability \n
			:param preamble: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Preamble')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		preamble_cmd_val = self._cmd_group.get_repcap_cmd_value(preamble, repcap.Preamble)
		return self._core.io.query_struct(f'CALCulate:WCDMa:MEASurement<Instance>:PRACh:PREamble{preamble_cmd_val}:CURRent?', self.__class__.CalculateStruct())
