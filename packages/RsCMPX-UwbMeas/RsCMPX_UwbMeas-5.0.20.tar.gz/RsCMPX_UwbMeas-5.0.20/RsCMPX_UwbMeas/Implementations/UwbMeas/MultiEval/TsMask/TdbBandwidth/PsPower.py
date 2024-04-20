from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PsPowerCls:
	"""PsPower commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("psPower", core, parent)

	def fetch(self, ppdu=repcap.Ppdu.Nr1) -> List[float]:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:TSMask:TDBBandwidth:PSPower<PPDU> \n
		Snippet: value: List[float] = driver.uwbMeas.multiEval.tsMask.tdbBandwidth.psPower.fetch(ppdu = repcap.Ppdu.Nr1) \n
		Returns the peak spectral power results at the frequencies fM, fL, fH for the -10 dB bandwidth limit as defined in ANSI
		C63.10-2013, chapter 10.1 'Evaluation of -10 dB bandwidth'. \n
		Suppressed linked return values: reliability \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: peak_spectr_power: Comma-separated list of peak spectral power values at fM, fL, fH, NAV for fH − fL."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:UWB:MEASurement<Instance>:MEValuation:TSMask:TDBBandwidth:PSPower{ppdu_cmd_val}?', suppressed)
		return response

	def read(self, ppdu=repcap.Ppdu.Nr1) -> List[float]:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:TSMask:TDBBandwidth:PSPower<PPDU> \n
		Snippet: value: List[float] = driver.uwbMeas.multiEval.tsMask.tdbBandwidth.psPower.read(ppdu = repcap.Ppdu.Nr1) \n
		Returns the peak spectral power results at the frequencies fM, fL, fH for the -10 dB bandwidth limit as defined in ANSI
		C63.10-2013, chapter 10.1 'Evaluation of -10 dB bandwidth'. \n
		Suppressed linked return values: reliability \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: peak_spectr_power: Comma-separated list of peak spectral power values at fM, fL, fH, NAV for fH − fL."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:TSMask:TDBBandwidth:PSPower{ppdu_cmd_val}?', suppressed)
		return response
