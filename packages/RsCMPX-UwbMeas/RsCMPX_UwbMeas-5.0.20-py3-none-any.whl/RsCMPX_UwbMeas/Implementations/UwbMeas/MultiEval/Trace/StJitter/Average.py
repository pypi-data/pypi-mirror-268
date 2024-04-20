from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:TRACe:STJitter:AVERage \n
		Snippet: value: List[float] = driver.uwbMeas.multiEval.trace.stJitter.average.fetch() \n
		Returns the y-values of the average symbol time jitter trace. See also 'Symbol Jitter square'. \n
		Suppressed linked return values: reliability \n
			:return: jitter: Comma-separated list of symbol jitter values."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:UWB:MEASurement<Instance>:MEValuation:TRACe:STJitter:AVERage?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:TRACe:STJitter:AVERage \n
		Snippet: value: List[float] = driver.uwbMeas.multiEval.trace.stJitter.average.read() \n
		Returns the y-values of the average symbol time jitter trace. See also 'Symbol Jitter square'. \n
		Suppressed linked return values: reliability \n
			:return: jitter: Comma-separated list of symbol jitter values."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:TRACe:STJitter:AVERage?', suppressed)
		return response
