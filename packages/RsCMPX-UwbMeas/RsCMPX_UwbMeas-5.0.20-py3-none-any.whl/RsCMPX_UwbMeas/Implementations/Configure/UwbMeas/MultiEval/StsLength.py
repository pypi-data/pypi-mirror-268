from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StsLengthCls:
	"""StsLength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stsLength", core, parent)

	def set(self, sts_segment_len: enums.StsSegmentLen, record=repcap.Record.Nr1) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:STSLength<Record> \n
		Snippet: driver.configure.uwbMeas.multiEval.stsLength.set(sts_segment_len = enums.StsSegmentLen.L128, record = repcap.Record.Nr1) \n
		Specifies the length of the STS segment in units of 512 chips. \n
			:param sts_segment_len: No help available
			:param record: optional repeated capability selector. Default value: Nr1
		"""
		param = Conversions.enum_scalar_to_str(sts_segment_len, enums.StsSegmentLen)
		record_cmd_val = self._cmd_group.get_repcap_cmd_value(record, repcap.Record)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:STSLength{record_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, record=repcap.Record.Nr1) -> enums.StsSegmentLen:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:STSLength<Record> \n
		Snippet: value: enums.StsSegmentLen = driver.configure.uwbMeas.multiEval.stsLength.get(record = repcap.Record.Nr1) \n
		Specifies the length of the STS segment in units of 512 chips. \n
			:param record: optional repeated capability selector. Default value: Nr1
			:return: sts_segment_len: No help available"""
		record_cmd_val = self._cmd_group.get_repcap_cmd_value(record, repcap.Record)
		response = self._core.io.query_str(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:STSLength{record_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.StsSegmentLen)
