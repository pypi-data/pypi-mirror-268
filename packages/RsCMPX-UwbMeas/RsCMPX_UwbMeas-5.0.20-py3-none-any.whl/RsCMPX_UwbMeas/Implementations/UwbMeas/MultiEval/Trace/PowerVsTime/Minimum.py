from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MinimumCls:
	"""Minimum commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	def fetch(self, ppdu=repcap.Ppdu.Nr1) -> List[float]:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:TRACe:PVTime:MINimum<PPDU> \n
		Snippet: value: List[float] = driver.uwbMeas.multiEval.trace.powerVsTime.minimum.fetch(ppdu = repcap.Ppdu.Nr1) \n
		Returns the y-values of the power vs time trace. The minimum and maximum values can be retrieved. See also 'Power vs Time
		square'. \n
		Suppressed linked return values: reliability \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: power: Comma-separated list of power values."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:UWB:MEASurement<Instance>:MEValuation:TRACe:PVTime:MINimum{ppdu_cmd_val}?', suppressed)
		return response

	def read(self, ppdu=repcap.Ppdu.Nr1) -> List[float]:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:TRACe:PVTime:MINimum<PPDU> \n
		Snippet: value: List[float] = driver.uwbMeas.multiEval.trace.powerVsTime.minimum.read(ppdu = repcap.Ppdu.Nr1) \n
		Returns the y-values of the power vs time trace. The minimum and maximum values can be retrieved. See also 'Power vs Time
		square'. \n
		Suppressed linked return values: reliability \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: power: Comma-separated list of power values."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:TRACe:PVTime:MINimum{ppdu_cmd_val}?', suppressed)
		return response
