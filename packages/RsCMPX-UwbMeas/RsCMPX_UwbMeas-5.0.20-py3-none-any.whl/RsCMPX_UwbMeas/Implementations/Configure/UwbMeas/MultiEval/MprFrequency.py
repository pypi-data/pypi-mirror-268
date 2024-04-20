from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MprFrequencyCls:
	"""MprFrequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mprFrequency", core, parent)

	def get(self, record=repcap.Record.Nr1) -> str:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:MPRFrequency<Record> \n
		Snippet: value: str = driver.configure.uwbMeas.multiEval.mprFrequency.get(record = repcap.Record.Nr1) \n
		Queries the mean pulse repetition frequency. \n
			:param record: optional repeated capability selector. Default value: Nr1
			:return: mpr_frequency: No help available"""
		record_cmd_val = self._cmd_group.get_repcap_cmd_value(record, repcap.Record)
		response = self._core.io.query_str(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:MPRFrequency{record_cmd_val}?')
		return trim_str_response(response)
