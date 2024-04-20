from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PsFormatCls:
	"""PsFormat commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("psFormat", core, parent)

	def set(self, ppdu_sts_format: int, record=repcap.Record.Nr1) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PSFormat<Record> \n
		Snippet: driver.configure.uwbMeas.multiEval.psFormat.set(ppdu_sts_format = 1, record = repcap.Record.Nr1) \n
		Specifies the PPDU STS packet structure configuration. See also 'HRP-ERDEV'. \n
			:param ppdu_sts_format: No help available
			:param record: optional repeated capability selector. Default value: Nr1
		"""
		param = Conversions.decimal_value_to_str(ppdu_sts_format)
		record_cmd_val = self._cmd_group.get_repcap_cmd_value(record, repcap.Record)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:PSFormat{record_cmd_val} {param}')

	def get(self, record=repcap.Record.Nr1) -> int:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PSFormat<Record> \n
		Snippet: value: int = driver.configure.uwbMeas.multiEval.psFormat.get(record = repcap.Record.Nr1) \n
		Specifies the PPDU STS packet structure configuration. See also 'HRP-ERDEV'. \n
			:param record: optional repeated capability selector. Default value: Nr1
			:return: ppdu_sts_format: No help available"""
		record_cmd_val = self._cmd_group.get_repcap_cmd_value(record, repcap.Record)
		response = self._core.io.query_str(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:PSFormat{record_cmd_val}?')
		return Conversions.str_to_int(response)
