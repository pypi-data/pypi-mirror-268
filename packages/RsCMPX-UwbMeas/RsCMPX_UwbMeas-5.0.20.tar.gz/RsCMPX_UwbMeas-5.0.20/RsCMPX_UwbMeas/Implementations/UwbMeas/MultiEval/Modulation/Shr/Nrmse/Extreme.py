from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExtremeCls:
	"""Extreme commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("extreme", core, parent)

	def fetch(self, ppdu=repcap.Ppdu.Nr1) -> float:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:MODulation:SHR:NRMSe:EXTReme<PPDU> \n
		Snippet: value: float = driver.uwbMeas.multiEval.modulation.shr.nrmse.extreme.fetch(ppdu = repcap.Ppdu.Nr1) \n
		Returns the NRMSE for SHR, according to FIRA specification. \n
		Suppressed linked return values: reliability \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: error: No help available"""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:UWB:MEASurement<Instance>:MEValuation:MODulation:SHR:NRMSe:EXTReme{ppdu_cmd_val}?', suppressed)
		return Conversions.str_to_float(response)

	def read(self, ppdu=repcap.Ppdu.Nr1) -> float:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:MODulation:SHR:NRMSe:EXTReme<PPDU> \n
		Snippet: value: float = driver.uwbMeas.multiEval.modulation.shr.nrmse.extreme.read(ppdu = repcap.Ppdu.Nr1) \n
		Returns the NRMSE for SHR, according to FIRA specification. \n
		Suppressed linked return values: reliability \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: error: No help available"""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:MODulation:SHR:NRMSe:EXTReme{ppdu_cmd_val}?', suppressed)
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def calculate(self, ppdu=repcap.Ppdu.Nr1) -> enums.ResultStatus2:
		"""SCPI: CALCulate:UWB:MEASurement<Instance>:MEValuation:MODulation:SHR:NRMSe:EXTReme<PPDU> \n
		Snippet: value: enums.ResultStatus2 = driver.uwbMeas.multiEval.modulation.shr.nrmse.extreme.calculate(ppdu = repcap.Ppdu.Nr1) \n
		Returns the NRMSE for SHR, according to FIRA specification. \n
		Suppressed linked return values: reliability \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: error: No help available"""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:UWB:MEASurement<Instance>:MEValuation:MODulation:SHR:NRMSe:EXTReme{ppdu_cmd_val}?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.ResultStatus2)
