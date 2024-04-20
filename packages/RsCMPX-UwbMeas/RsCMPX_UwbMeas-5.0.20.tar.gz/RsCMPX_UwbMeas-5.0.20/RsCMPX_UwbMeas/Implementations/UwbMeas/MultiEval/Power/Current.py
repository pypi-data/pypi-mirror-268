from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


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
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Preamble_Power: float: No parameter help available
			- Pre_Peak_Power: float: No parameter help available
			- Data_Power: float: No parameter help available
			- Data_Peak_Power: float: No parameter help available
			- Max_Spec_Power: float: No parameter help available
			- Max_Spec_50_Power: float: No parameter help available
			- Ppdu_Power: float: Mean power of the PPDU.
			- Ppdu_Peak_Power: float: Peak power of the PPDU."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Preamble_Power'),
			ArgStruct.scalar_float('Pre_Peak_Power'),
			ArgStruct.scalar_float('Data_Power'),
			ArgStruct.scalar_float('Data_Peak_Power'),
			ArgStruct.scalar_float('Max_Spec_Power'),
			ArgStruct.scalar_float('Max_Spec_50_Power'),
			ArgStruct.scalar_float('Ppdu_Power'),
			ArgStruct.scalar_float('Ppdu_Peak_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Preamble_Power: float = None
			self.Pre_Peak_Power: float = None
			self.Data_Power: float = None
			self.Data_Peak_Power: float = None
			self.Max_Spec_Power: float = None
			self.Max_Spec_50_Power: float = None
			self.Ppdu_Power: float = None
			self.Ppdu_Peak_Power: float = None

	def fetch(self, ppdu=repcap.Ppdu.Default) -> ResultData:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:POWer:CURRent<PPDU> \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.power.current.fetch(ppdu = repcap.Ppdu.Default) \n
		Return the current, average, extreme and standard deviation single value power results. \n
			:param ppdu: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Current')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'FETCh:UWB:MEASurement<Instance>:MEValuation:POWer:CURRent{ppdu_cmd_val}?', self.__class__.ResultData())

	def read(self, ppdu=repcap.Ppdu.Default) -> ResultData:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:POWer:CURRent<PPDU> \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.power.current.read(ppdu = repcap.Ppdu.Default) \n
		Return the current, average, extreme and standard deviation single value power results. \n
			:param ppdu: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Current')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'READ:UWB:MEASurement<Instance>:MEValuation:POWer:CURRent{ppdu_cmd_val}?', self.__class__.ResultData())

	def clone(self) -> 'CurrentCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CurrentCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
