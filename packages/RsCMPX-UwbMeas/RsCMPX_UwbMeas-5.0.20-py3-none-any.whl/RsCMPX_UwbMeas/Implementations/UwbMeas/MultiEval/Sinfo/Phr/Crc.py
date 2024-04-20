from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CrcCls:
	"""Crc commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("crc", core, parent)

	# noinspection PyTypeChecker
	def fetch(self, ppdu=repcap.Ppdu.Nr1) -> enums.Result:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo:PHR:CRC<PPDU> \n
		Snippet: value: enums.Result = driver.uwbMeas.multiEval.sinfo.phr.crc.fetch(ppdu = repcap.Ppdu.Nr1) \n
		Returns the result of the PHR checksum (SECDED) verification. \n
		Suppressed linked return values: reliability \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: crc: No help available"""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo:PHR:CRC{ppdu_cmd_val}?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.Result)

	# noinspection PyTypeChecker
	def read(self, ppdu=repcap.Ppdu.Nr1) -> enums.Result:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:SINFo:PHR:CRC<PPDU> \n
		Snippet: value: enums.Result = driver.uwbMeas.multiEval.sinfo.phr.crc.read(ppdu = repcap.Ppdu.Nr1) \n
		Returns the result of the PHR checksum (SECDED) verification. \n
		Suppressed linked return values: reliability \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: crc: No help available"""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:SINFo:PHR:CRC{ppdu_cmd_val}?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.Result)
