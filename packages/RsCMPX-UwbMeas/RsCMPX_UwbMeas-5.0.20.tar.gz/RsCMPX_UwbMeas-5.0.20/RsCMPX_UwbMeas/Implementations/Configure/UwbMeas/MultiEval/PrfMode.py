from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrfModeCls:
	"""PrfMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prfMode", core, parent)

	def get(self, record=repcap.Record.Nr1) -> str:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PRFMode<Record> \n
		Snippet: value: str = driver.configure.uwbMeas.multiEval.prfMode.get(record = repcap.Record.Nr1) \n
		Queries the pulse repetition frequency mode. \n
			:param record: optional repeated capability selector. Default value: Nr1
			:return: prf_mode: 'BPRF', 'HPRF' or '---'"""
		record_cmd_val = self._cmd_group.get_repcap_cmd_value(record, repcap.Record)
		response = self._core.io.query_str(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:PRFMode{record_cmd_val}?')
		return trim_str_response(response)
