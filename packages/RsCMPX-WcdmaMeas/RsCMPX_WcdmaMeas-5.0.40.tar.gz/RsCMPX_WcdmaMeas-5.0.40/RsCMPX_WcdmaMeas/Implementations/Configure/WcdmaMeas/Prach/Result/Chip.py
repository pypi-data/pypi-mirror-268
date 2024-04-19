from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChipCls:
	"""Chip commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("chip", core, parent)

	def get_ue_power(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult:CHIP:UEPower \n
		Snippet: value: bool = driver.configure.wcdmaMeas.prach.result.chip.get_ue_power() \n
		Enables or disables the evaluation of results of the PRACH measurement identified by the last command mnemonics: UE power,
		power steps, frequency error, error vector magnitude (EVM) , magnitude error, phase error, UE power vs chip, EVM vs chip,
		magnitude error vs chip, phase error vs chip, and I/Q constellation measurements. \n
			:return: enable_ue_pchip: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:CHIP:UEPower?')
		return Conversions.str_to_bool(response)

	def set_ue_power(self, enable_ue_pchip: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult:CHIP:UEPower \n
		Snippet: driver.configure.wcdmaMeas.prach.result.chip.set_ue_power(enable_ue_pchip = False) \n
		Enables or disables the evaluation of results of the PRACH measurement identified by the last command mnemonics: UE power,
		power steps, frequency error, error vector magnitude (EVM) , magnitude error, phase error, UE power vs chip, EVM vs chip,
		magnitude error vs chip, phase error vs chip, and I/Q constellation measurements. \n
			:param enable_ue_pchip: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_ue_pchip)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:CHIP:UEPower {param}')

	def get_perror(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult:CHIP:PERRor \n
		Snippet: value: bool = driver.configure.wcdmaMeas.prach.result.chip.get_perror() \n
		Enables or disables the evaluation of results of the PRACH measurement identified by the last command mnemonics: UE power,
		power steps, frequency error, error vector magnitude (EVM) , magnitude error, phase error, UE power vs chip, EVM vs chip,
		magnitude error vs chip, phase error vs chip, and I/Q constellation measurements. \n
			:return: enable_ph_err_chip: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:CHIP:PERRor?')
		return Conversions.str_to_bool(response)

	def set_perror(self, enable_ph_err_chip: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult:CHIP:PERRor \n
		Snippet: driver.configure.wcdmaMeas.prach.result.chip.set_perror(enable_ph_err_chip = False) \n
		Enables or disables the evaluation of results of the PRACH measurement identified by the last command mnemonics: UE power,
		power steps, frequency error, error vector magnitude (EVM) , magnitude error, phase error, UE power vs chip, EVM vs chip,
		magnitude error vs chip, phase error vs chip, and I/Q constellation measurements. \n
			:param enable_ph_err_chip: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_ph_err_chip)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:CHIP:PERRor {param}')

	def get_merror(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult:CHIP:MERRor \n
		Snippet: value: bool = driver.configure.wcdmaMeas.prach.result.chip.get_merror() \n
		Enables or disables the evaluation of results of the PRACH measurement identified by the last command mnemonics: UE power,
		power steps, frequency error, error vector magnitude (EVM) , magnitude error, phase error, UE power vs chip, EVM vs chip,
		magnitude error vs chip, phase error vs chip, and I/Q constellation measurements. \n
			:return: enable_merr_chip: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:CHIP:MERRor?')
		return Conversions.str_to_bool(response)

	def set_merror(self, enable_merr_chip: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult:CHIP:MERRor \n
		Snippet: driver.configure.wcdmaMeas.prach.result.chip.set_merror(enable_merr_chip = False) \n
		Enables or disables the evaluation of results of the PRACH measurement identified by the last command mnemonics: UE power,
		power steps, frequency error, error vector magnitude (EVM) , magnitude error, phase error, UE power vs chip, EVM vs chip,
		magnitude error vs chip, phase error vs chip, and I/Q constellation measurements. \n
			:param enable_merr_chip: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_merr_chip)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:CHIP:MERRor {param}')

	def get_evm(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult:CHIP:EVM \n
		Snippet: value: bool = driver.configure.wcdmaMeas.prach.result.chip.get_evm() \n
		Enables or disables the evaluation of results of the PRACH measurement identified by the last command mnemonics: UE power,
		power steps, frequency error, error vector magnitude (EVM) , magnitude error, phase error, UE power vs chip, EVM vs chip,
		magnitude error vs chip, phase error vs chip, and I/Q constellation measurements. \n
			:return: enable_evm_chip: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:CHIP:EVM?')
		return Conversions.str_to_bool(response)

	def set_evm(self, enable_evm_chip: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:RESult:CHIP:EVM \n
		Snippet: driver.configure.wcdmaMeas.prach.result.chip.set_evm(enable_evm_chip = False) \n
		Enables or disables the evaluation of results of the PRACH measurement identified by the last command mnemonics: UE power,
		power steps, frequency error, error vector magnitude (EVM) , magnitude error, phase error, UE power vs chip, EVM vs chip,
		magnitude error vs chip, phase error vs chip, and I/Q constellation measurements. \n
			:param enable_evm_chip: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_evm_chip)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:RESult:CHIP:EVM {param}')
