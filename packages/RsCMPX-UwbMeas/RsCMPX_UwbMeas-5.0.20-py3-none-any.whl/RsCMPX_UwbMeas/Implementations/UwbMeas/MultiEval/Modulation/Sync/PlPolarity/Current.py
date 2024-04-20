from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 2 total commands, 0 Subgroups, 2 group commands
	Repeated Capability: Ppdu, default value after init: Ppdu.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_ppdu_get', 'repcap_ppdu_set', repcap.Ppdu.Nr1)

	def repcap_ppdu_set(self, ppdu: repcap.Ppdu) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Ppdu.Default
		Default value after init: Ppdu.Nr1"""
		self._cmd_group.set_repcap_enum_value(ppdu)

	def repcap_ppdu_get(self) -> repcap.Ppdu:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

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

	def fetch(self, ppdu=repcap.Ppdu.Default) -> FetchStruct:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:MODulation:SYNC:PLPolarity:CURRent<PPDU> \n
		Snippet: value: FetchStruct = driver.uwbMeas.multiEval.modulation.sync.plPolarity.current.fetch(ppdu = repcap.Ppdu.Default) \n
		Returns the result of the check for correct pulse location and polarity, for SYNC. \n
			:param ppdu: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Current')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'FETCh:UWB:MEASurement<Instance>:MEValuation:MODulation:SYNC:PLPolarity:CURRent{ppdu_cmd_val}?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	def read(self, ppdu=repcap.Ppdu.Default) -> enums.Result:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:MODulation:SYNC:PLPolarity:CURRent<PPDU> \n
		Snippet: value: enums.Result = driver.uwbMeas.multiEval.modulation.sync.plPolarity.current.read(ppdu = repcap.Ppdu.Default) \n
		Returns the result of the check for correct pulse location and polarity, for SYNC. \n
		Suppressed linked return values: reliability \n
			:param ppdu: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Current')
			:return: sync_pulse_loc_pol: No help available"""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:MODulation:SYNC:PLPolarity:CURRent{ppdu_cmd_val}?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.Result)

	def clone(self) -> 'CurrentCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CurrentCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
