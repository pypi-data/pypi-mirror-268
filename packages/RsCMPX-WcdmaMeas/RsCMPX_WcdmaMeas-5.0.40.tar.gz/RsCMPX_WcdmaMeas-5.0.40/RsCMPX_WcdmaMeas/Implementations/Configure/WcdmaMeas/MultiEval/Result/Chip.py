from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChipCls:
	"""Chip commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("chip", core, parent)

	def get_perror(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:CHIP:PERRor \n
		Snippet: value: bool = driver.configure.wcdmaMeas.multiEval.result.chip.get_perror() \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:return: enable_ph_err_chip: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:CHIP:PERRor?')
		return Conversions.str_to_bool(response)

	def set_perror(self, enable_ph_err_chip: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:CHIP:PERRor \n
		Snippet: driver.configure.wcdmaMeas.multiEval.result.chip.set_perror(enable_ph_err_chip = False) \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:param enable_ph_err_chip: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_ph_err_chip)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:CHIP:PERRor {param}')

	def get_merror(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:CHIP:MERRor \n
		Snippet: value: bool = driver.configure.wcdmaMeas.multiEval.result.chip.get_merror() \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:return: enable_merr_chip: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:CHIP:MERRor?')
		return Conversions.str_to_bool(response)

	def set_merror(self, enable_merr_chip: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:CHIP:MERRor \n
		Snippet: driver.configure.wcdmaMeas.multiEval.result.chip.set_merror(enable_merr_chip = False) \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:param enable_merr_chip: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_merr_chip)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:CHIP:MERRor {param}')

	def get_evm(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:CHIP:EVM \n
		Snippet: value: bool = driver.configure.wcdmaMeas.multiEval.result.chip.get_evm() \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:return: enable_evm_chip: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:CHIP:EVM?')
		return Conversions.str_to_bool(response)

	def set_evm(self, enable_evm_chip: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:CHIP:EVM \n
		Snippet: driver.configure.wcdmaMeas.multiEval.result.chip.set_evm(enable_evm_chip = False) \n
		Enables or disables the evaluation of results of the multi-evaluation measurement identified by the last command
		mnemonics: error vector magnitude (EVM) , magnitude error, phase error, adjacent channel leakage power ratio, spectrum
		emission mask, code domain monitor, code domain power, code domain error (CDE) , EVM vs chip, magnitude error vs chip,
		phase error vs chip, UE power, frequency error, phase discontinuity, power steps, bit error rate, I/Q constellation, and
		relative CDE results. \n
			:param enable_evm_chip: OFF: Do not evaluate results. ON: Evaluate the results.
		"""
		param = Conversions.bool_to_str(enable_evm_chip)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:CHIP:EVM {param}')
