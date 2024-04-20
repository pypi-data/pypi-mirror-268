from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BitrateCls:
	"""Bitrate commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bitrate", core, parent)

	def fetch(self, ppdu=repcap.Ppdu.Nr1) -> float:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo:PHR:BITRate<PPDU> \n
		Snippet: value: float = driver.uwbMeas.multiEval.sinfo.phr.bitrate.fetch(ppdu = repcap.Ppdu.Nr1) \n
		Returns the data rate of the PHR. \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: phr_bitrate: No help available"""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		response = self._core.io.query_str(f'FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo:PHR:BITRate{ppdu_cmd_val}?')
		return Conversions.str_to_float(response)

	def read(self, ppdu=repcap.Ppdu.Nr1) -> float:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:SINFo:PHR:BITRate<PPDU> \n
		Snippet: value: float = driver.uwbMeas.multiEval.sinfo.phr.bitrate.read(ppdu = repcap.Ppdu.Nr1) \n
		Returns the data rate of the PHR. \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: phr_bitrate: No help available"""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		response = self._core.io.query_str(f'READ:UWB:MEASurement<Instance>:MEValuation:SINFo:PHR:BITRate{ppdu_cmd_val}?')
		return Conversions.str_to_float(response)
