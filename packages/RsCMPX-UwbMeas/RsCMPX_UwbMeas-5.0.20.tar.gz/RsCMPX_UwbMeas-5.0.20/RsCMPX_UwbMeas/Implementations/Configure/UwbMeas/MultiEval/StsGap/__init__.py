from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StsGapCls:
	"""StsGap commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stsGap", core, parent)

	@property
	def chip(self):
		"""chip commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_chip'):
			from .Chip import ChipCls
			self._chip = ChipCls(self._core, self._cmd_group)
		return self._chip

	def set(self, sts_gap: int, record=repcap.Record.Nr1) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:STSGap<Record> \n
		Snippet: driver.configure.uwbMeas.multiEval.stsGap.set(sts_gap = 1, record = repcap.Record.Nr1) \n
		Specifies additional gaps between the payload and the STS in units of 4 chips. This setting is only relevant for PPDU STS
		packet structure configuration two set via CONFigure:UWB:MEAS<i>:MEValuation:PSFormat<Record>) . \n
			:param sts_gap: No help available
			:param record: optional repeated capability selector. Default value: Nr1
		"""
		param = Conversions.decimal_value_to_str(sts_gap)
		record_cmd_val = self._cmd_group.get_repcap_cmd_value(record, repcap.Record)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:STSGap{record_cmd_val} {param}')

	def get(self, record=repcap.Record.Nr1) -> int:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:STSGap<Record> \n
		Snippet: value: int = driver.configure.uwbMeas.multiEval.stsGap.get(record = repcap.Record.Nr1) \n
		Specifies additional gaps between the payload and the STS in units of 4 chips. This setting is only relevant for PPDU STS
		packet structure configuration two set via CONFigure:UWB:MEAS<i>:MEValuation:PSFormat<Record>) . \n
			:param record: optional repeated capability selector. Default value: Nr1
			:return: sts_gap: No help available"""
		record_cmd_val = self._cmd_group.get_repcap_cmd_value(record, repcap.Record)
		response = self._core.io.query_str(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:STSGap{record_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'StsGapCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = StsGapCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
