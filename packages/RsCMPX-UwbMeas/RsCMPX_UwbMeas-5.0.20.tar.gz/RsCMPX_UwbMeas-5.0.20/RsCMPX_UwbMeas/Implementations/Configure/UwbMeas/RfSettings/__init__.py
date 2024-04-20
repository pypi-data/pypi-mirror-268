from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettingsCls:
	"""RfSettings commands group definition. 6 total commands, 1 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfSettings", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	def get_channel(self) -> int:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:RFSettings:CHANnel \n
		Snippet: value: int = driver.configure.uwbMeas.rfSettings.get_channel() \n
		Selects the channel number. \n
			:return: analyzer_chan: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:RFSettings:CHANnel?')
		return Conversions.str_to_int(response)

	def set_channel(self, analyzer_chan: int) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:RFSettings:CHANnel \n
		Snippet: driver.configure.uwbMeas.rfSettings.set_channel(analyzer_chan = 1) \n
		Selects the channel number. \n
			:param analyzer_chan: No help available
		"""
		param = Conversions.decimal_value_to_str(analyzer_chan)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:RFSettings:CHANnel {param}')

	def get_envelope_power(self) -> float:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:RFSettings:ENPower \n
		Snippet: value: float = driver.configure.uwbMeas.rfSettings.get_envelope_power() \n
		Sets the expected nominal power of the measured UWB signal. \n
			:return: exp_nominal_power: The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the specifications document.
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:RFSettings:ENPower?')
		return Conversions.str_to_float(response)

	def set_envelope_power(self, exp_nominal_power: float) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:RFSettings:ENPower \n
		Snippet: driver.configure.uwbMeas.rfSettings.set_envelope_power(exp_nominal_power = 1.0) \n
		Sets the expected nominal power of the measured UWB signal. \n
			:param exp_nominal_power: The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the specifications document.
		"""
		param = Conversions.decimal_value_to_str(exp_nominal_power)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:RFSettings:ENPower {param}')

	def get_eattenuation(self) -> float:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:RFSettings:EATTenuation \n
		Snippet: value: float = driver.configure.uwbMeas.rfSettings.get_eattenuation() \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the input connector.
		For measurement of UWB signals. \n
			:return: rf_input_ext_att: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:RFSettings:EATTenuation?')
		return Conversions.str_to_float(response)

	def set_eattenuation(self, rf_input_ext_att: float) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:RFSettings:EATTenuation \n
		Snippet: driver.configure.uwbMeas.rfSettings.set_eattenuation(rf_input_ext_att = 1.0) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the input connector.
		For measurement of UWB signals. \n
			:param rf_input_ext_att: No help available
		"""
		param = Conversions.decimal_value_to_str(rf_input_ext_att)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:RFSettings:EATTenuation {param}')

	def get_umargin(self) -> float:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:RFSettings:UMARgin \n
		Snippet: value: float = driver.configure.uwbMeas.rfSettings.get_umargin() \n
		Sets the margin that the measurement adds to the expected nominal power to determine the reference power. The reference
		power minus the external input attenuation must be within the power range of the selected input connector. Refer to the
		specifications document. For measurement of UWB signals. \n
			:return: user_margin: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:RFSettings:UMARgin?')
		return Conversions.str_to_float(response)

	def set_umargin(self, user_margin: float) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:RFSettings:UMARgin \n
		Snippet: driver.configure.uwbMeas.rfSettings.set_umargin(user_margin = 1.0) \n
		Sets the margin that the measurement adds to the expected nominal power to determine the reference power. The reference
		power minus the external input attenuation must be within the power range of the selected input connector. Refer to the
		specifications document. For measurement of UWB signals. \n
			:param user_margin: No help available
		"""
		param = Conversions.decimal_value_to_str(user_margin)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:RFSettings:UMARgin {param}')

	def clone(self) -> 'RfSettingsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RfSettingsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
