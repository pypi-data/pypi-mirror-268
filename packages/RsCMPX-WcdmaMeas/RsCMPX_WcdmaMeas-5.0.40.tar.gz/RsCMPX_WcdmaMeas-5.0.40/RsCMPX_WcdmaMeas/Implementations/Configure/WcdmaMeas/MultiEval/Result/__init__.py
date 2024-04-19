from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 20 total commands, 1 Subgroups, 17 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	@property
	def chip(self):
		"""chip commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_chip'):
			from .Chip import ChipCls
			self._chip = ChipCls(self._core, self._cmd_group)
		return self._chip

	def get_txm(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:TXM \n
		Snippet: value: bool = driver.configure.wcdmaMeas.multiEval.result.get_txm() \n
		No command help available \n
			:return: enable_txm: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:TXM?')
		return Conversions.str_to_bool(response)

	def set_txm(self, enable_txm: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:TXM \n
		Snippet: driver.configure.wcdmaMeas.multiEval.result.set_txm(enable_txm = False) \n
		No command help available \n
			:param enable_txm: No help available
		"""
		param = Conversions.bool_to_str(enable_txm)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:TXM {param}')

	def get_rcd_error(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:RCDerror \n
		Snippet: value: bool = driver.configure.wcdmaMeas.multiEval.result.get_rcd_error() \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:return: enable_rcde: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:RCDerror?')
		return Conversions.str_to_bool(response)

	def set_rcd_error(self, enable_rcde: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:RCDerror \n
		Snippet: driver.configure.wcdmaMeas.multiEval.result.set_rcd_error(enable_rcde = False) \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:param enable_rcde: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_rcde)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:RCDerror {param}')

	def get_iq(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:IQ \n
		Snippet: value: bool = driver.configure.wcdmaMeas.multiEval.result.get_iq() \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:return: enable_iq: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:IQ?')
		return Conversions.str_to_bool(response)

	def set_iq(self, enable_iq: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:IQ \n
		Snippet: driver.configure.wcdmaMeas.multiEval.result.set_iq(enable_iq = False) \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:param enable_iq: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_iq)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:IQ {param}')

	def get_ber(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:BER \n
		Snippet: value: bool = driver.configure.wcdmaMeas.multiEval.result.get_ber() \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:return: enable_ber: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:BER?')
		return Conversions.str_to_bool(response)

	def set_ber(self, enable_ber: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:BER \n
		Snippet: driver.configure.wcdmaMeas.multiEval.result.set_ber(enable_ber = False) \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:param enable_ber: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_ber)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:BER {param}')

	def get_psteps(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:PSTeps \n
		Snippet: value: bool = driver.configure.wcdmaMeas.multiEval.result.get_psteps() \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:return: enable_pow_steps: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:PSTeps?')
		return Conversions.str_to_bool(response)

	def set_psteps(self, enable_pow_steps: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:PSTeps \n
		Snippet: driver.configure.wcdmaMeas.multiEval.result.set_psteps(enable_pow_steps = False) \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:param enable_pow_steps: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_pow_steps)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:PSTeps {param}')

	def get_phd(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:PHD \n
		Snippet: value: bool = driver.configure.wcdmaMeas.multiEval.result.get_phd() \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:return: enable_phase_disc: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:PHD?')
		return Conversions.str_to_bool(response)

	def set_phd(self, enable_phase_disc: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:PHD \n
		Snippet: driver.configure.wcdmaMeas.multiEval.result.set_phd(enable_phase_disc = False) \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:param enable_phase_disc: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_phase_disc)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:PHD {param}')

	def get_freq_error(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:FERRor \n
		Snippet: value: bool = driver.configure.wcdmaMeas.multiEval.result.get_freq_error() \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:return: enable_freq_error: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:FERRor?')
		return Conversions.str_to_bool(response)

	def set_freq_error(self, enable_freq_error: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:FERRor \n
		Snippet: driver.configure.wcdmaMeas.multiEval.result.set_freq_error(enable_freq_error = False) \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:param enable_freq_error: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_freq_error)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:FERRor {param}')

	def get_ue_power(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:UEPower \n
		Snippet: value: bool = driver.configure.wcdmaMeas.multiEval.result.get_ue_power() \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:return: enable_ue_power: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:UEPower?')
		return Conversions.str_to_bool(response)

	def set_ue_power(self, enable_ue_power: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:UEPower \n
		Snippet: driver.configure.wcdmaMeas.multiEval.result.set_ue_power(enable_ue_power = False) \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:param enable_ue_power: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_ue_power)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:UEPower {param}')

	# noinspection PyTypeChecker
	class AllStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Enable_Evm: bool: Error vector magnitude OFF: Do not evaluate results. ON: Evaluate results
			- Enable_Mag_Error: bool: Magnitude error
			- Enable_Phase_Err: bool: Phase error
			- Enable_Aclr: bool: Adjacent channel leakage power ratio
			- Enable_Emask: bool: Spectrum emission mask
			- Enable_Cd_Monitor: bool: Code domain monitor
			- Enable_Cdp: bool: Code domain power
			- Enable_Cde: bool: Code domain error
			- Enable_Evm_Chip: bool: EVM vs chip
			- Enable_Merr_Chip: bool: Magnitude error vs chip
			- Enable_Ph_Err_Chip: bool: Phase error vs chip
			- Enable_Ue_Power: bool: UE power
			- Enable_Freq_Error: bool: Frequency error
			- Enable_Phase_Disc: bool: Phase discontinuity
			- Enable_Pow_Steps: bool: Power steps
			- Enable_Ber: bool: Bit error rate
			- Enable_Iq: bool: Optional setting parameter. I/Q constellation diagram
			- Enable_Rcde: bool: Optional setting parameter. Relative CDE
			- Enable_Txm: bool: Optional setting parameter. TX measurement scalar results"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable_Evm'),
			ArgStruct.scalar_bool('Enable_Mag_Error'),
			ArgStruct.scalar_bool('Enable_Phase_Err'),
			ArgStruct.scalar_bool('Enable_Aclr'),
			ArgStruct.scalar_bool('Enable_Emask'),
			ArgStruct.scalar_bool('Enable_Cd_Monitor'),
			ArgStruct.scalar_bool('Enable_Cdp'),
			ArgStruct.scalar_bool('Enable_Cde'),
			ArgStruct.scalar_bool('Enable_Evm_Chip'),
			ArgStruct.scalar_bool('Enable_Merr_Chip'),
			ArgStruct.scalar_bool('Enable_Ph_Err_Chip'),
			ArgStruct.scalar_bool('Enable_Ue_Power'),
			ArgStruct.scalar_bool('Enable_Freq_Error'),
			ArgStruct.scalar_bool('Enable_Phase_Disc'),
			ArgStruct.scalar_bool('Enable_Pow_Steps'),
			ArgStruct.scalar_bool('Enable_Ber'),
			ArgStruct.scalar_bool_optional('Enable_Iq'),
			ArgStruct.scalar_bool_optional('Enable_Rcde'),
			ArgStruct.scalar_bool_optional('Enable_Txm')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable_Evm: bool = None
			self.Enable_Mag_Error: bool = None
			self.Enable_Phase_Err: bool = None
			self.Enable_Aclr: bool = None
			self.Enable_Emask: bool = None
			self.Enable_Cd_Monitor: bool = None
			self.Enable_Cdp: bool = None
			self.Enable_Cde: bool = None
			self.Enable_Evm_Chip: bool = None
			self.Enable_Merr_Chip: bool = None
			self.Enable_Ph_Err_Chip: bool = None
			self.Enable_Ue_Power: bool = None
			self.Enable_Freq_Error: bool = None
			self.Enable_Phase_Disc: bool = None
			self.Enable_Pow_Steps: bool = None
			self.Enable_Ber: bool = None
			self.Enable_Iq: bool = None
			self.Enable_Rcde: bool = None
			self.Enable_Txm: bool = None

	def get_all(self) -> AllStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult[:ALL] \n
		Snippet: value: AllStruct = driver.configure.wcdmaMeas.multiEval.result.get_all() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. This command combines all other
		CONFigure:WCDMa:MEAS<i>:MEValuation:RESult... commands. \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:ALL?', self.__class__.AllStruct())

	def set_all(self, value: AllStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult[:ALL] \n
		Snippet with structure: \n
		structure = driver.configure.wcdmaMeas.multiEval.result.AllStruct() \n
		structure.Enable_Evm: bool = False \n
		structure.Enable_Mag_Error: bool = False \n
		structure.Enable_Phase_Err: bool = False \n
		structure.Enable_Aclr: bool = False \n
		structure.Enable_Emask: bool = False \n
		structure.Enable_Cd_Monitor: bool = False \n
		structure.Enable_Cdp: bool = False \n
		structure.Enable_Cde: bool = False \n
		structure.Enable_Evm_Chip: bool = False \n
		structure.Enable_Merr_Chip: bool = False \n
		structure.Enable_Ph_Err_Chip: bool = False \n
		structure.Enable_Ue_Power: bool = False \n
		structure.Enable_Freq_Error: bool = False \n
		structure.Enable_Phase_Disc: bool = False \n
		structure.Enable_Pow_Steps: bool = False \n
		structure.Enable_Ber: bool = False \n
		structure.Enable_Iq: bool = False \n
		structure.Enable_Rcde: bool = False \n
		structure.Enable_Txm: bool = False \n
		driver.configure.wcdmaMeas.multiEval.result.set_all(value = structure) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. This command combines all other
		CONFigure:WCDMa:MEAS<i>:MEValuation:RESult... commands. \n
			:param value: see the help for AllStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:ALL', value)

	def get_cd_error(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:CDERror \n
		Snippet: value: bool = driver.configure.wcdmaMeas.multiEval.result.get_cd_error() \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:return: enable_cde: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:CDERror?')
		return Conversions.str_to_bool(response)

	def set_cd_error(self, enable_cde: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:CDERror \n
		Snippet: driver.configure.wcdmaMeas.multiEval.result.set_cd_error(enable_cde = False) \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:param enable_cde: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_cde)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:CDERror {param}')

	def get_cd_power(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:CDPower \n
		Snippet: value: bool = driver.configure.wcdmaMeas.multiEval.result.get_cd_power() \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:return: enable_cdp: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:CDPower?')
		return Conversions.str_to_bool(response)

	def set_cd_power(self, enable_cdp: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:CDPower \n
		Snippet: driver.configure.wcdmaMeas.multiEval.result.set_cd_power(enable_cdp = False) \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:param enable_cdp: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_cdp)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:CDPower {param}')

	def get_cdp_monitor(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:CDPMonitor \n
		Snippet: value: bool = driver.configure.wcdmaMeas.multiEval.result.get_cdp_monitor() \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:return: enable_cd_monitor: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:CDPMonitor?')
		return Conversions.str_to_bool(response)

	def set_cdp_monitor(self, enable_cd_monitor: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:CDPMonitor \n
		Snippet: driver.configure.wcdmaMeas.multiEval.result.set_cdp_monitor(enable_cd_monitor = False) \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:param enable_cd_monitor: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_cd_monitor)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:CDPMonitor {param}')

	def get_emask(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:EMASk \n
		Snippet: value: bool = driver.configure.wcdmaMeas.multiEval.result.get_emask() \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:return: enable_emask: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:EMASk?')
		return Conversions.str_to_bool(response)

	def set_emask(self, enable_emask: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:EMASk \n
		Snippet: driver.configure.wcdmaMeas.multiEval.result.set_emask(enable_emask = False) \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:param enable_emask: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_emask)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:EMASk {param}')

	def get_aclr(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:ACLR \n
		Snippet: value: bool = driver.configure.wcdmaMeas.multiEval.result.get_aclr() \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:return: enable_aclr: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:ACLR?')
		return Conversions.str_to_bool(response)

	def set_aclr(self, enable_aclr: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:ACLR \n
		Snippet: driver.configure.wcdmaMeas.multiEval.result.set_aclr(enable_aclr = False) \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:param enable_aclr: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_aclr)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:ACLR {param}')

	def get_perror(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:PERRor \n
		Snippet: value: bool = driver.configure.wcdmaMeas.multiEval.result.get_perror() \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:return: enable_phase_err: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:PERRor?')
		return Conversions.str_to_bool(response)

	def set_perror(self, enable_phase_err: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:PERRor \n
		Snippet: driver.configure.wcdmaMeas.multiEval.result.set_perror(enable_phase_err = False) \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:param enable_phase_err: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_phase_err)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:PERRor {param}')

	def get_ev_magnitude(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:EVMagnitude \n
		Snippet: value: bool = driver.configure.wcdmaMeas.multiEval.result.get_ev_magnitude() \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:return: enable_evm: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:EVMagnitude?')
		return Conversions.str_to_bool(response)

	def set_ev_magnitude(self, enable_evm: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:EVMagnitude \n
		Snippet: driver.configure.wcdmaMeas.multiEval.result.set_ev_magnitude(enable_evm = False) \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:param enable_evm: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_evm)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:EVMagnitude {param}')

	def get_merror(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:MERRor \n
		Snippet: value: bool = driver.configure.wcdmaMeas.multiEval.result.get_merror() \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:return: enable_mag_error: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:MERRor?')
		return Conversions.str_to_bool(response)

	def set_merror(self, enable_mag_error: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:MERRor \n
		Snippet: driver.configure.wcdmaMeas.multiEval.result.set_merror(enable_mag_error = False) \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:param enable_mag_error: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_mag_error)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:MERRor {param}')

	def clone(self) -> 'ResultCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ResultCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
