from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DppduCls:
	"""Dppdu commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dppdu", core, parent)

	def fetch(self) -> int:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo:DPPDu \n
		Snippet: value: int = driver.uwbMeas.multiEval.sinfo.dppdu.fetch() \n
		Returns the number of detected PPDUs in the capture length. \n
		Suppressed linked return values: reliability \n
			:return: detected_ppdu: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo:DPPDu?', suppressed)
		return Conversions.str_to_int(response)

	def read(self) -> int:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:SINFo:DPPDu \n
		Snippet: value: int = driver.uwbMeas.multiEval.sinfo.dppdu.read() \n
		Returns the number of detected PPDUs in the capture length. \n
		Suppressed linked return values: reliability \n
			:return: detected_ppdu: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:SINFo:DPPDu?', suppressed)
		return Conversions.str_to_int(response)
