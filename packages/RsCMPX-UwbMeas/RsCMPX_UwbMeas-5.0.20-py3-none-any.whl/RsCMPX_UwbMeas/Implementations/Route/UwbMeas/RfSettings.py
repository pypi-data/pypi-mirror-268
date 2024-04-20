from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettingsCls:
	"""RfSettings commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfSettings", core, parent)

	# noinspection PyTypeChecker
	def get_connector(self) -> enums.Connector:
		"""SCPI: ROUTe:UWB:MEASurement<Instance>:RFSettings:CONNector \n
		Snippet: value: enums.Connector = driver.route.uwbMeas.rfSettings.get_connector() \n
		No command help available \n
			:return: connector: No help available
		"""
		response = self._core.io.query_str('ROUTe:UWB:MEASurement<Instance>:RFSettings:CONNector?')
		return Conversions.str_to_scalar_enum(response, enums.Connector)

	def set_connector(self, connector: enums.Connector) -> None:
		"""SCPI: ROUTe:UWB:MEASurement<Instance>:RFSettings:CONNector \n
		Snippet: driver.route.uwbMeas.rfSettings.set_connector(connector = enums.Connector.I11I) \n
		No command help available \n
			:param connector: No help available
		"""
		param = Conversions.enum_scalar_to_str(connector, enums.Connector)
		self._core.io.write(f'ROUTe:UWB:MEASurement<Instance>:RFSettings:CONNector {param}')
