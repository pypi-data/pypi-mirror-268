from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PpLengthCls:
	"""PpLength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ppLength", core, parent)

	def set(self, phr_payload_len: int, record=repcap.Record.Nr1) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PPLength<Record> \n
		Snippet: driver.configure.uwbMeas.multiEval.ppLength.set(phr_payload_len = 1, record = repcap.Record.Nr1) \n
		Specifies the bit length of the PHR payload length field. This setting is only relevant in HPRF mode (RHML or RHMH set
		via CONFigure:UWB:MEAS<i>:MEValuation:PHRRate<Record> ) . \n
			:param phr_payload_len: No help available
			:param record: optional repeated capability selector. Default value: Nr1
		"""
		param = Conversions.decimal_value_to_str(phr_payload_len)
		record_cmd_val = self._cmd_group.get_repcap_cmd_value(record, repcap.Record)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:PPLength{record_cmd_val} {param}')

	def get(self, record=repcap.Record.Nr1) -> int:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PPLength<Record> \n
		Snippet: value: int = driver.configure.uwbMeas.multiEval.ppLength.get(record = repcap.Record.Nr1) \n
		Specifies the bit length of the PHR payload length field. This setting is only relevant in HPRF mode (RHML or RHMH set
		via CONFigure:UWB:MEAS<i>:MEValuation:PHRRate<Record> ) . \n
			:param record: optional repeated capability selector. Default value: Nr1
			:return: phr_payload_len: No help available"""
		record_cmd_val = self._cmd_group.get_repcap_cmd_value(record, repcap.Record)
		response = self._core.io.query_str(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:PPLength{record_cmd_val}?')
		return Conversions.str_to_int(response)
