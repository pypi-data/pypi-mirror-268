from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExtremeCls:
	"""Extreme commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("extreme", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliabiltiy: int: No parameter help available
			- Sync_Pulse_Loc_Pol: enums.Result: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliabiltiy'),
			ArgStruct.scalar_enum('Sync_Pulse_Loc_Pol', enums.Result)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliabiltiy: int = None
			self.Sync_Pulse_Loc_Pol: enums.Result = None

	def fetch(self, ppdu=repcap.Ppdu.Nr1) -> FetchStruct:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:MODulation:SYNC:PLPolarity:EXTReme<PPDU> \n
		Snippet: value: FetchStruct = driver.uwbMeas.multiEval.modulation.sync.plPolarity.extreme.fetch(ppdu = repcap.Ppdu.Nr1) \n
		Returns the result of the check for correct pulse location and polarity, for SYNC. \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'FETCh:UWB:MEASurement<Instance>:MEValuation:MODulation:SYNC:PLPolarity:EXTReme{ppdu_cmd_val}?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	def read(self, ppdu=repcap.Ppdu.Nr1) -> enums.Result:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:MODulation:SYNC:PLPolarity:EXTReme<PPDU> \n
		Snippet: value: enums.Result = driver.uwbMeas.multiEval.modulation.sync.plPolarity.extreme.read(ppdu = repcap.Ppdu.Nr1) \n
		Returns the result of the check for correct pulse location and polarity, for SYNC. \n
		Suppressed linked return values: reliability \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: sync_pulse_loc_pol: No help available"""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:MODulation:SYNC:PLPolarity:EXTReme{ppdu_cmd_val}?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.Result)
