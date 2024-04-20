from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class XvaluesCls:
	"""Xvalues commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("xvalues", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:TRACe:TSMask:XVALues \n
		Snippet: value: List[float] = driver.uwbMeas.multiEval.trace.tsMask.xvalues.fetch() \n
		Returns the x-values of the transmit spectrum trace. \n
		Suppressed linked return values: reliability \n
			:return: values: Comma-separated list of frequency values."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:UWB:MEASurement<Instance>:MEValuation:TRACe:TSMask:XVALues?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:TRACe:TSMask:XVALues \n
		Snippet: value: List[float] = driver.uwbMeas.multiEval.trace.tsMask.xvalues.read() \n
		Returns the x-values of the transmit spectrum trace. \n
		Suppressed linked return values: reliability \n
			:return: values: Comma-separated list of frequency values."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:TRACe:TSMask:XVALues?', suppressed)
		return response
