from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpectrumCls:
	"""Spectrum commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spectrum", core, parent)

	def get_scount(self) -> int:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:SPECtrum:SCOunt \n
		Snippet: value: int = driver.configure.uwbMeas.multiEval.spectrum.get_scount() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. The statistic count applies to spectrum measurements. \n
			:return: statistic_count: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:SPECtrum:SCOunt?')
		return Conversions.str_to_int(response)

	def set_scount(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:SPECtrum:SCOunt \n
		Snippet: driver.configure.uwbMeas.multiEval.spectrum.set_scount(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. The statistic count applies to spectrum measurements. \n
			:param statistic_count: No help available
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:SPECtrum:SCOunt {param}')

	# noinspection PyTypeChecker
	def get_msp_length(self) -> enums.MaxSpecPowLen:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:SPECtrum:MSPLength \n
		Snippet: value: enums.MaxSpecPowLen = driver.configure.uwbMeas.multiEval.spectrum.get_msp_length() \n
		Selects the time interval for measuring the maximum spectral power. \n
			:return: max_spec_pow_len: PPDU: entire PPDU MS1: 1 ms, starting with the PPDU
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:SPECtrum:MSPLength?')
		return Conversions.str_to_scalar_enum(response, enums.MaxSpecPowLen)

	def set_msp_length(self, max_spec_pow_len: enums.MaxSpecPowLen) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:SPECtrum:MSPLength \n
		Snippet: driver.configure.uwbMeas.multiEval.spectrum.set_msp_length(max_spec_pow_len = enums.MaxSpecPowLen.MS1) \n
		Selects the time interval for measuring the maximum spectral power. \n
			:param max_spec_pow_len: PPDU: entire PPDU MS1: 1 ms, starting with the PPDU
		"""
		param = Conversions.enum_scalar_to_str(max_spec_pow_len, enums.MaxSpecPowLen)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:SPECtrum:MSPLength {param}')
