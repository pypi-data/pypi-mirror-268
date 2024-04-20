from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CrcCls:
	"""Crc commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("crc", core, parent)

	def fetch(self, ppdu=repcap.Ppdu.Nr1) -> bool:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo:PSDU:CRC<PPDU> \n
		Snippet: value: bool = driver.uwbMeas.multiEval.sinfo.psdu.crc.fetch(ppdu = repcap.Ppdu.Nr1) \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: crc: No help available"""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo:PSDU:CRC{ppdu_cmd_val}?', suppressed)
		return Conversions.str_to_bool(response)

	def read(self, ppdu=repcap.Ppdu.Nr1) -> bool:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:SINFo:PSDU:CRC<PPDU> \n
		Snippet: value: bool = driver.uwbMeas.multiEval.sinfo.psdu.crc.read(ppdu = repcap.Ppdu.Nr1) \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: crc: No help available"""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:SINFo:PSDU:CRC{ppdu_cmd_val}?', suppressed)
		return Conversions.str_to_bool(response)
