from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MinimumCls:
	"""Minimum commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	def fetch(self, ppdu=repcap.Ppdu.Nr1) -> float:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:POWer:PPOWer:MINimum<PPDU> \n
		Snippet: value: float = driver.uwbMeas.multiEval.power.ppower.minimum.fetch(ppdu = repcap.Ppdu.Nr1) \n
		Returns the mean power of the preamble part. \n
		Suppressed linked return values: reliability \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: power: No help available"""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:UWB:MEASurement<Instance>:MEValuation:POWer:PPOWer:MINimum{ppdu_cmd_val}?', suppressed)
		return Conversions.str_to_float(response)

	def read(self, ppdu=repcap.Ppdu.Nr1) -> float:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:POWer:PPOWer:MINimum<PPDU> \n
		Snippet: value: float = driver.uwbMeas.multiEval.power.ppower.minimum.read(ppdu = repcap.Ppdu.Nr1) \n
		Returns the mean power of the preamble part. \n
		Suppressed linked return values: reliability \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: power: No help available"""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:POWer:PPOWer:MINimum{ppdu_cmd_val}?', suppressed)
		return Conversions.str_to_float(response)
