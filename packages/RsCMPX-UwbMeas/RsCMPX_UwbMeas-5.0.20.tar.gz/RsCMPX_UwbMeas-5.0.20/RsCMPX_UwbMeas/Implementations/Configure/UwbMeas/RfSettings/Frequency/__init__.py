from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	@property
	def range(self):
		"""range commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_range'):
			from .Range import RangeCls
			self._range = RangeCls(self._core, self._cmd_group)
		return self._range

	def get_value(self) -> float:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:RFSettings:FREQuency \n
		Snippet: value: float = driver.configure.uwbMeas.rfSettings.frequency.get_value() \n
		Selects the center frequency of the measured carrier for UWB signals. For the supported frequency range, see 'Frequency
		ranges'. \n
			:return: analyzer_freq: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:RFSettings:FREQuency?')
		return Conversions.str_to_float(response)

	def set_value(self, analyzer_freq: float) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:RFSettings:FREQuency \n
		Snippet: driver.configure.uwbMeas.rfSettings.frequency.set_value(analyzer_freq = 1.0) \n
		Selects the center frequency of the measured carrier for UWB signals. For the supported frequency range, see 'Frequency
		ranges'. \n
			:param analyzer_freq: No help available
		"""
		param = Conversions.decimal_value_to_str(analyzer_freq)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:RFSettings:FREQuency {param}')

	def clone(self) -> 'FrequencyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FrequencyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
