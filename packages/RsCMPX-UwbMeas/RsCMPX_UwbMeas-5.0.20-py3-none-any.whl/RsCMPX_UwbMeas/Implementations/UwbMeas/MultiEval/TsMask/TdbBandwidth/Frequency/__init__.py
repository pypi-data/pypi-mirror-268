from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	@property
	def fhfl(self):
		"""fhfl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fhfl'):
			from .Fhfl import FhflCls
			self._fhfl = FhflCls(self._core, self._cmd_group)
		return self._fhfl

	def fetch(self, ppdu=repcap.Ppdu.Nr1) -> List[float]:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:TSMask:TDBBandwidth:FREQuency<PPDU> \n
		Snippet: value: List[float] = driver.uwbMeas.multiEval.tsMask.tdbBandwidth.frequency.fetch(ppdu = repcap.Ppdu.Nr1) \n
		Returns the frequency values fM, fL, fH, fH − fL for the -10 dB bandwidth limit as defined in ANSI C63.10-2013, chapter
		10.1 'Evaluation of -10 dB bandwidth'. \n
		Suppressed linked return values: reliability \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: frequency: Comma-separated list of frequencies in the order fM, fL, fH, fH − fL."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:UWB:MEASurement<Instance>:MEValuation:TSMask:TDBBandwidth:FREQuency{ppdu_cmd_val}?', suppressed)
		return response

	def read(self, ppdu=repcap.Ppdu.Nr1) -> List[float]:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:TSMask:TDBBandwidth:FREQuency<PPDU> \n
		Snippet: value: List[float] = driver.uwbMeas.multiEval.tsMask.tdbBandwidth.frequency.read(ppdu = repcap.Ppdu.Nr1) \n
		Returns the frequency values fM, fL, fH, fH − fL for the -10 dB bandwidth limit as defined in ANSI C63.10-2013, chapter
		10.1 'Evaluation of -10 dB bandwidth'. \n
		Suppressed linked return values: reliability \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: frequency: Comma-separated list of frequencies in the order fM, fL, fH, fH − fL."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:TSMask:TDBBandwidth:FREQuency{ppdu_cmd_val}?', suppressed)
		return response

	def clone(self) -> 'FrequencyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FrequencyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
