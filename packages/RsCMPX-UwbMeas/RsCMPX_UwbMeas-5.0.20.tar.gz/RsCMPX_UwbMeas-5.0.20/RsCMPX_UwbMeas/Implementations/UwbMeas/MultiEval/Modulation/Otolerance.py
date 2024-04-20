from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OtoleranceCls:
	"""Otolerance commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("otolerance", core, parent)

	def read(self) -> float:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:MODulation:OTOLerance \n
		Snippet: value: float = driver.uwbMeas.multiEval.modulation.otolerance.read() \n
		Returns the out of tolerance result for modulation measurements. It indicates the percentage of measurement intervals of
		the statistic count for modulation measurements exceeding the specified TX Modulation limits or Pulse Mask limits. \n
		Suppressed linked return values: reliability \n
			:return: out_of_tolerance: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:MODulation:OTOLerance?', suppressed)
		return Conversions.str_to_float(response)

	def fetch(self) -> float:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:MODulation:OTOLerance \n
		Snippet: value: float = driver.uwbMeas.multiEval.modulation.otolerance.fetch() \n
		Returns the out of tolerance result for modulation measurements. It indicates the percentage of measurement intervals of
		the statistic count for modulation measurements exceeding the specified TX Modulation limits or Pulse Mask limits. \n
		Suppressed linked return values: reliability \n
			:return: out_of_tolerance: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:UWB:MEASurement<Instance>:MEValuation:MODulation:OTOLerance?', suppressed)
		return Conversions.str_to_float(response)
