from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 12 total commands, 1 Subgroups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	@property
	def chip(self):
		"""chip commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_chip'):
			from .Chip import ChipCls
			self._chip = ChipCls(self._core, self._cmd_group)
		return self._chip

	def get_ue_power(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult:UEPower \n
		Snippet: value: bool = driver.configure.wcdmaMeas.prach.result.get_ue_power() \n
		Enables or disables the evaluation of results of the PRACH measurement identified by the last command mnemonics: UE power,
		power steps, frequency error, error vector magnitude (EVM) , magnitude error, phase error, UE power vs chip, EVM vs chip,
		magnitude error vs chip, phase error vs chip, and I/Q constellation measurements. \n
			:return: enable_ue_power: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:UEPower?')
		return Conversions.str_to_bool(response)

	def set_ue_power(self, enable_ue_power: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult:UEPower \n
		Snippet: driver.configure.wcdmaMeas.prach.result.set_ue_power(enable_ue_power = False) \n
		Enables or disables the evaluation of results of the PRACH measurement identified by the last command mnemonics: UE power,
		power steps, frequency error, error vector magnitude (EVM) , magnitude error, phase error, UE power vs chip, EVM vs chip,
		magnitude error vs chip, phase error vs chip, and I/Q constellation measurements. \n
			:param enable_ue_power: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_ue_power)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:UEPower {param}')

	def get_psteps(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult:PSTeps \n
		Snippet: value: bool = driver.configure.wcdmaMeas.prach.result.get_psteps() \n
		Enables or disables the evaluation of results of the PRACH measurement identified by the last command mnemonics: UE power,
		power steps, frequency error, error vector magnitude (EVM) , magnitude error, phase error, UE power vs chip, EVM vs chip,
		magnitude error vs chip, phase error vs chip, and I/Q constellation measurements. \n
			:return: enable_pow_steps: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:PSTeps?')
		return Conversions.str_to_bool(response)

	def set_psteps(self, enable_pow_steps: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult:PSTeps \n
		Snippet: driver.configure.wcdmaMeas.prach.result.set_psteps(enable_pow_steps = False) \n
		Enables or disables the evaluation of results of the PRACH measurement identified by the last command mnemonics: UE power,
		power steps, frequency error, error vector magnitude (EVM) , magnitude error, phase error, UE power vs chip, EVM vs chip,
		magnitude error vs chip, phase error vs chip, and I/Q constellation measurements. \n
			:param enable_pow_steps: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_pow_steps)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:PSTeps {param}')

	def get_freq_error(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult:FERRor \n
		Snippet: value: bool = driver.configure.wcdmaMeas.prach.result.get_freq_error() \n
		Enables or disables the evaluation of results of the PRACH measurement identified by the last command mnemonics: UE power,
		power steps, frequency error, error vector magnitude (EVM) , magnitude error, phase error, UE power vs chip, EVM vs chip,
		magnitude error vs chip, phase error vs chip, and I/Q constellation measurements. \n
			:return: enable_freq_error: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:FERRor?')
		return Conversions.str_to_bool(response)

	def set_freq_error(self, enable_freq_error: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult:FERRor \n
		Snippet: driver.configure.wcdmaMeas.prach.result.set_freq_error(enable_freq_error = False) \n
		Enables or disables the evaluation of results of the PRACH measurement identified by the last command mnemonics: UE power,
		power steps, frequency error, error vector magnitude (EVM) , magnitude error, phase error, UE power vs chip, EVM vs chip,
		magnitude error vs chip, phase error vs chip, and I/Q constellation measurements. \n
			:param enable_freq_error: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_freq_error)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:FERRor {param}')

	# noinspection PyTypeChecker
	class AllStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Enable_Ue_Power: bool: UE power OFF: Do not evaluate results. ON: Evaluate the results.
			- Enable_Pow_Steps: bool: Power steps
			- Enable_Freq_Error: bool: Frequency error
			- Enable_Evm: bool: Error vector magnitude
			- Enable_Mag_Error: bool: Magnitude error
			- Enable_Phase_Err: bool: Phase error
			- Enable_Ue_Pchip: bool: UE power vs chip
			- Enable_Evm_Chip: bool: EVM vs chip
			- Enable_Merr_Chip: bool: Magnitude error vs chip
			- Enable_Ph_Err_Chip: bool: Phase error vs chip
			- Enable_Iq: bool: I/Q constellation diagram"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable_Ue_Power'),
			ArgStruct.scalar_bool('Enable_Pow_Steps'),
			ArgStruct.scalar_bool('Enable_Freq_Error'),
			ArgStruct.scalar_bool('Enable_Evm'),
			ArgStruct.scalar_bool('Enable_Mag_Error'),
			ArgStruct.scalar_bool('Enable_Phase_Err'),
			ArgStruct.scalar_bool('Enable_Ue_Pchip'),
			ArgStruct.scalar_bool('Enable_Evm_Chip'),
			ArgStruct.scalar_bool('Enable_Merr_Chip'),
			ArgStruct.scalar_bool('Enable_Ph_Err_Chip'),
			ArgStruct.scalar_bool('Enable_Iq')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable_Ue_Power: bool = None
			self.Enable_Pow_Steps: bool = None
			self.Enable_Freq_Error: bool = None
			self.Enable_Evm: bool = None
			self.Enable_Mag_Error: bool = None
			self.Enable_Phase_Err: bool = None
			self.Enable_Ue_Pchip: bool = None
			self.Enable_Evm_Chip: bool = None
			self.Enable_Merr_Chip: bool = None
			self.Enable_Ph_Err_Chip: bool = None
			self.Enable_Iq: bool = None

	def get_all(self) -> AllStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult[:ALL] \n
		Snippet: value: AllStruct = driver.configure.wcdmaMeas.prach.result.get_all() \n
		Enables or disables the evaluation of results of the PRACH measurement.
		This command combines all other CONFigure:WCDMa:MEAS<i>:PRACh:RESult... commands. \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:ALL?', self.__class__.AllStruct())

	def set_all(self, value: AllStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult[:ALL] \n
		Snippet with structure: \n
		structure = driver.configure.wcdmaMeas.prach.result.AllStruct() \n
		structure.Enable_Ue_Power: bool = False \n
		structure.Enable_Pow_Steps: bool = False \n
		structure.Enable_Freq_Error: bool = False \n
		structure.Enable_Evm: bool = False \n
		structure.Enable_Mag_Error: bool = False \n
		structure.Enable_Phase_Err: bool = False \n
		structure.Enable_Ue_Pchip: bool = False \n
		structure.Enable_Evm_Chip: bool = False \n
		structure.Enable_Merr_Chip: bool = False \n
		structure.Enable_Ph_Err_Chip: bool = False \n
		structure.Enable_Iq: bool = False \n
		driver.configure.wcdmaMeas.prach.result.set_all(value = structure) \n
		Enables or disables the evaluation of results of the PRACH measurement.
		This command combines all other CONFigure:WCDMa:MEAS<i>:PRACh:RESult... commands. \n
			:param value: see the help for AllStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:ALL', value)

	def get_perror(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult:PERRor \n
		Snippet: value: bool = driver.configure.wcdmaMeas.prach.result.get_perror() \n
		Enables or disables the evaluation of results of the PRACH measurement identified by the last command mnemonics: UE power,
		power steps, frequency error, error vector magnitude (EVM) , magnitude error, phase error, UE power vs chip, EVM vs chip,
		magnitude error vs chip, phase error vs chip, and I/Q constellation measurements. \n
			:return: enable_phase_err: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:PERRor?')
		return Conversions.str_to_bool(response)

	def set_perror(self, enable_phase_err: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult:PERRor \n
		Snippet: driver.configure.wcdmaMeas.prach.result.set_perror(enable_phase_err = False) \n
		Enables or disables the evaluation of results of the PRACH measurement identified by the last command mnemonics: UE power,
		power steps, frequency error, error vector magnitude (EVM) , magnitude error, phase error, UE power vs chip, EVM vs chip,
		magnitude error vs chip, phase error vs chip, and I/Q constellation measurements. \n
			:param enable_phase_err: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_phase_err)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:PERRor {param}')

	def get_ev_magnitude(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult:EVMagnitude \n
		Snippet: value: bool = driver.configure.wcdmaMeas.prach.result.get_ev_magnitude() \n
		Enables or disables the evaluation of results of the PRACH measurement identified by the last command mnemonics: UE power,
		power steps, frequency error, error vector magnitude (EVM) , magnitude error, phase error, UE power vs chip, EVM vs chip,
		magnitude error vs chip, phase error vs chip, and I/Q constellation measurements. \n
			:return: enable_evm: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:EVMagnitude?')
		return Conversions.str_to_bool(response)

	def set_ev_magnitude(self, enable_evm: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult:EVMagnitude \n
		Snippet: driver.configure.wcdmaMeas.prach.result.set_ev_magnitude(enable_evm = False) \n
		Enables or disables the evaluation of results of the PRACH measurement identified by the last command mnemonics: UE power,
		power steps, frequency error, error vector magnitude (EVM) , magnitude error, phase error, UE power vs chip, EVM vs chip,
		magnitude error vs chip, phase error vs chip, and I/Q constellation measurements. \n
			:param enable_evm: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_evm)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:EVMagnitude {param}')

	def get_merror(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult:MERRor \n
		Snippet: value: bool = driver.configure.wcdmaMeas.prach.result.get_merror() \n
		Enables or disables the evaluation of results of the PRACH measurement identified by the last command mnemonics: UE power,
		power steps, frequency error, error vector magnitude (EVM) , magnitude error, phase error, UE power vs chip, EVM vs chip,
		magnitude error vs chip, phase error vs chip, and I/Q constellation measurements. \n
			:return: enable_mag_error: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:MERRor?')
		return Conversions.str_to_bool(response)

	def set_merror(self, enable_mag_error: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult:MERRor \n
		Snippet: driver.configure.wcdmaMeas.prach.result.set_merror(enable_mag_error = False) \n
		Enables or disables the evaluation of results of the PRACH measurement identified by the last command mnemonics: UE power,
		power steps, frequency error, error vector magnitude (EVM) , magnitude error, phase error, UE power vs chip, EVM vs chip,
		magnitude error vs chip, phase error vs chip, and I/Q constellation measurements. \n
			:param enable_mag_error: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_mag_error)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:MERRor {param}')

	def get_iq(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult:IQ \n
		Snippet: value: bool = driver.configure.wcdmaMeas.prach.result.get_iq() \n
		Enables or disables the evaluation of results of the PRACH measurement identified by the last command mnemonics: UE power,
		power steps, frequency error, error vector magnitude (EVM) , magnitude error, phase error, UE power vs chip, EVM vs chip,
		magnitude error vs chip, phase error vs chip, and I/Q constellation measurements. \n
			:return: enable_iq: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:IQ?')
		return Conversions.str_to_bool(response)

	def set_iq(self, enable_iq: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult:IQ \n
		Snippet: driver.configure.wcdmaMeas.prach.result.set_iq(enable_iq = False) \n
		Enables or disables the evaluation of results of the PRACH measurement identified by the last command mnemonics: UE power,
		power steps, frequency error, error vector magnitude (EVM) , magnitude error, phase error, UE power vs chip, EVM vs chip,
		magnitude error vs chip, phase error vs chip, and I/Q constellation measurements. \n
			:param enable_iq: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_iq)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:IQ {param}')

	def clone(self) -> 'ResultCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ResultCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
