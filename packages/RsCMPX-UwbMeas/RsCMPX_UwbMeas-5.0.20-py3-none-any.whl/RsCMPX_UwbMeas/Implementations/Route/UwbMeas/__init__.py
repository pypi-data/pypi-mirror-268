from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UwbMeasCls:
	"""UwbMeas commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uwbMeas", core, parent)

	@property
	def rfSettings(self):
		"""rfSettings commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rfSettings'):
			from .RfSettings import RfSettingsCls
			self._rfSettings = RfSettingsCls(self._core, self._cmd_group)
		return self._rfSettings

	def get_spath(self) -> str:
		"""SCPI: ROUTe:UWB:MEAS<instance>:SPATh \n
		Snippet: value: str = driver.route.uwbMeas.get_spath() \n
		Selects the RF connection (signal input path) for the measured signal. For possible connection names, see method
		RsCMPX_UwbMeas.Catalog.UwbMeas.spath. \n
			:return: signal_path: No help available
		"""
		response = self._core.io.query_str('ROUTe:UWB:MEAS<Instance>:SPATh?')
		return trim_str_response(response)

	def set_spath(self, signal_path: str) -> None:
		"""SCPI: ROUTe:UWB:MEAS<instance>:SPATh \n
		Snippet: driver.route.uwbMeas.set_spath(signal_path = 'abc') \n
		Selects the RF connection (signal input path) for the measured signal. For possible connection names, see method
		RsCMPX_UwbMeas.Catalog.UwbMeas.spath. \n
			:param signal_path: No help available
		"""
		param = Conversions.value_to_quoted_str(signal_path)
		self._core.io.write(f'ROUTe:UWB:MEAS<Instance>:SPATh {param}')

	def clone(self) -> 'UwbMeasCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UwbMeasCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
