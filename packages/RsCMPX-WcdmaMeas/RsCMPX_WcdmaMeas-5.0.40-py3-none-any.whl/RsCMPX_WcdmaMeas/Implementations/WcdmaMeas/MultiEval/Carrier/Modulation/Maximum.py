from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Evm_Rms: float or bool: Error vector magnitude RMS and peak value.
			- Evm_Peak: float or bool: Error vector magnitude RMS and peak value.
			- Mag_Error_Rms: float or bool: Magnitude error RMS value.
			- Mag_Error_Peak: float or bool: Magnitude error peak value.
			- Phase_Error_Rms: float or bool: No parameter help available
			- Phase_Error_Peak: float or bool: No parameter help available
			- Iq_Offset: float or bool: I/Q origin offset.
			- Iq_Imbalance: float or bool: I/Q imbalance.
			- Carrier_Freq_Err: float or bool: No parameter help available
			- Transmit_Time_Err: float or bool: No parameter help available
			- Ue_Power: float or bool: User equipment power.
			- Power_Steps: float or bool: User equipment power step.
			- Phase_Disc: enums.ResultStatus2: Phase discontinuity."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Evm_Rms'),
			ArgStruct.scalar_float_ext('Evm_Peak'),
			ArgStruct.scalar_float_ext('Mag_Error_Rms'),
			ArgStruct.scalar_float_ext('Mag_Error_Peak'),
			ArgStruct.scalar_float_ext('Phase_Error_Rms'),
			ArgStruct.scalar_float_ext('Phase_Error_Peak'),
			ArgStruct.scalar_float_ext('Iq_Offset'),
			ArgStruct.scalar_float_ext('Iq_Imbalance'),
			ArgStruct.scalar_float_ext('Carrier_Freq_Err'),
			ArgStruct.scalar_float_ext('Transmit_Time_Err'),
			ArgStruct.scalar_float_ext('Ue_Power'),
			ArgStruct.scalar_float_ext('Power_Steps'),
			ArgStruct.scalar_enum('Phase_Disc', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Evm_Rms: float or bool = None
			self.Evm_Peak: float or bool = None
			self.Mag_Error_Rms: float or bool = None
			self.Mag_Error_Peak: float or bool = None
			self.Phase_Error_Rms: float or bool = None
			self.Phase_Error_Peak: float or bool = None
			self.Iq_Offset: float or bool = None
			self.Iq_Imbalance: float or bool = None
			self.Carrier_Freq_Err: float or bool = None
			self.Transmit_Time_Err: float or bool = None
			self.Ue_Power: float or bool = None
			self.Power_Steps: float or bool = None
			self.Phase_Disc: enums.ResultStatus2 = None

	def calculate(self, carrier=repcap.Carrier.Default) -> CalculateStruct:
		"""SCPI: CALCulate:WCDMa:MEASurement<instance>:MEValuation:CARRier<carrier>:MODulation:MAXimum \n
		Snippet: value: CalculateStruct = driver.wcdmaMeas.multiEval.carrier.modulation.maximum.calculate(carrier = repcap.Carrier.Default) \n
		Return the current, average, maximum and standard deviation single value results. The return values described below are
		returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each of the
		first 14 results listed below. The TX time alignment is only returned by FETCh and READ commands. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'CALCulate:WCDMa:MEASurement<Instance>:MEValuation:CARRier{carrier_cmd_val}:MODulation:MAXimum?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Evm_Rms: float: Error vector magnitude RMS and peak value.
			- Evm_Peak: float: Error vector magnitude RMS and peak value.
			- Mag_Error_Rms: float: Magnitude error RMS value.
			- Mag_Error_Peak: float: Magnitude error peak value.
			- Phase_Error_Rms: float: No parameter help available
			- Phase_Error_Peak: float: No parameter help available
			- Iq_Offset: float: I/Q origin offset.
			- Iq_Imbalance: float: I/Q imbalance.
			- Carrier_Freq_Err: float: No parameter help available
			- Transmit_Time_Err: float: No parameter help available
			- Ue_Power: float: User equipment power.
			- Power_Steps: float: User equipment power step.
			- Phase_Disc: float: Phase discontinuity.
			- Tx_Time_Alignment: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Evm_Rms'),
			ArgStruct.scalar_float('Evm_Peak'),
			ArgStruct.scalar_float('Mag_Error_Rms'),
			ArgStruct.scalar_float('Mag_Error_Peak'),
			ArgStruct.scalar_float('Phase_Error_Rms'),
			ArgStruct.scalar_float('Phase_Error_Peak'),
			ArgStruct.scalar_float('Iq_Offset'),
			ArgStruct.scalar_float('Iq_Imbalance'),
			ArgStruct.scalar_float('Carrier_Freq_Err'),
			ArgStruct.scalar_float('Transmit_Time_Err'),
			ArgStruct.scalar_float('Ue_Power'),
			ArgStruct.scalar_float('Power_Steps'),
			ArgStruct.scalar_float('Phase_Disc'),
			ArgStruct.scalar_float('Tx_Time_Alignment')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Evm_Rms: float = None
			self.Evm_Peak: float = None
			self.Mag_Error_Rms: float = None
			self.Mag_Error_Peak: float = None
			self.Phase_Error_Rms: float = None
			self.Phase_Error_Peak: float = None
			self.Iq_Offset: float = None
			self.Iq_Imbalance: float = None
			self.Carrier_Freq_Err: float = None
			self.Transmit_Time_Err: float = None
			self.Ue_Power: float = None
			self.Power_Steps: float = None
			self.Phase_Disc: float = None
			self.Tx_Time_Alignment: float = None

	def read(self, carrier=repcap.Carrier.Default) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:MEValuation:CARRier<carrier>:MODulation:MAXimum \n
		Snippet: value: ResultData = driver.wcdmaMeas.multiEval.carrier.modulation.maximum.read(carrier = repcap.Carrier.Default) \n
		Return the current, average, maximum and standard deviation single value results. The return values described below are
		returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each of the
		first 14 results listed below. The TX time alignment is only returned by FETCh and READ commands. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:MEValuation:CARRier{carrier_cmd_val}:MODulation:MAXimum?', self.__class__.ResultData())

	def fetch(self, carrier=repcap.Carrier.Default) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:CARRier<carrier>:MODulation:MAXimum \n
		Snippet: value: ResultData = driver.wcdmaMeas.multiEval.carrier.modulation.maximum.fetch(carrier = repcap.Carrier.Default) \n
		Return the current, average, maximum and standard deviation single value results. The return values described below are
		returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each of the
		first 14 results listed below. The TX time alignment is only returned by FETCh and READ commands. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:CARRier{carrier_cmd_val}:MODulation:MAXimum?', self.__class__.ResultData())
