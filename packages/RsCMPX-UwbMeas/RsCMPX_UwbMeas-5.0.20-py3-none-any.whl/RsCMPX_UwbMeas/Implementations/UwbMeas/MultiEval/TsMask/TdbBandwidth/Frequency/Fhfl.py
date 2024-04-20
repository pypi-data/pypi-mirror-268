from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FhflCls:
	"""Fhfl commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fhfl", core, parent)

	# noinspection PyTypeChecker
	def calculate(self, ppdu=repcap.Ppdu.Nr1) -> enums.ResultStatus2:
		"""SCPI: CALCulate:UWB:MEASurement<Instance>:MEValuation:TSMask:TDBBandwidth:FREQuency:FHFL<PPDU> \n
		Snippet: value: enums.ResultStatus2 = driver.uwbMeas.multiEval.tsMask.tdbBandwidth.frequency.fhfl.calculate(ppdu = repcap.Ppdu.Nr1) \n
		Returns the limit check result for the −10 dB bandwidth (fH − fL) ≧ 500 MHz. \n
		Suppressed linked return values: reliability \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: frequency: No help available"""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:UWB:MEASurement<Instance>:MEValuation:TSMask:TDBBandwidth:FREQuency:FHFL{ppdu_cmd_val}?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.ResultStatus2)
