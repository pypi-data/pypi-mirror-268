from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StSegmentsCls:
	"""StSegments commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stSegments", core, parent)

	def set(self, no_sts_segments: int, record=repcap.Record.Nr1) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:STSegments<Record> \n
		Snippet: driver.configure.uwbMeas.multiEval.stSegments.set(no_sts_segments = 1, record = repcap.Record.Nr1) \n
		Specifies the number of STS segments inserted according to the STS packet configuration. \n
			:param no_sts_segments: No help available
			:param record: optional repeated capability selector. Default value: Nr1
		"""
		param = Conversions.decimal_value_to_str(no_sts_segments)
		record_cmd_val = self._cmd_group.get_repcap_cmd_value(record, repcap.Record)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:STSegments{record_cmd_val} {param}')

	def get(self, record=repcap.Record.Nr1) -> int:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:STSegments<Record> \n
		Snippet: value: int = driver.configure.uwbMeas.multiEval.stSegments.get(record = repcap.Record.Nr1) \n
		Specifies the number of STS segments inserted according to the STS packet configuration. \n
			:param record: optional repeated capability selector. Default value: Nr1
			:return: no_sts_segments: No help available"""
		record_cmd_val = self._cmd_group.get_repcap_cmd_value(record, repcap.Record)
		response = self._core.io.query_str(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:STSegments{record_cmd_val}?')
		return Conversions.str_to_int(response)
