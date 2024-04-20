from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChipCls:
	"""Chip commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("chip", core, parent)

	def get(self, record=repcap.Record.Nr1) -> int:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:STSGap:CHIP<Record> \n
		Snippet: value: int = driver.configure.uwbMeas.multiEval.stsGap.chip.get(record = repcap.Record.Nr1) \n
		Queries the number of chips for the configured STS gap, resulting from CONFigure:UWB:MEAS<i>:MEValuation:STSGap<Record>. \n
			:param record: optional repeated capability selector. Default value: Nr1
			:return: sts_gap_chip: No help available"""
		record_cmd_val = self._cmd_group.get_repcap_cmd_value(record, repcap.Record)
		response = self._core.io.query_str(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:STSGap:CHIP{record_cmd_val}?')
		return Conversions.str_to_int(response)
