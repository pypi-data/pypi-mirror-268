from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 3 total commands, 0 Subgroups, 3 group commands
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
			- Phr_Plevel: float: PHR pulse level
			- Psdu_Plevel: float: PSDU pulse level
			- Sts_Plevel: float: STS pulse level"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Phr_Plevel'),
			ArgStruct.scalar_float('Psdu_Plevel'),
			ArgStruct.scalar_float('Sts_Plevel')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Phr_Plevel: float = None
			self.Psdu_Plevel: float = None
			self.Sts_Plevel: float = None

	def fetch(self, ppdu=repcap.Ppdu.Default) -> ResultData:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:MODulation:PLEVel:CURRent<PPDU> \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.modulation.plevel.current.fetch(ppdu = repcap.Ppdu.Default) \n
		Returns pulse levels according to the FIRA specification, relative to the SHR pulse level. \n
			:param ppdu: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Current')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'FETCh:UWB:MEASurement<Instance>:MEValuation:MODulation:PLEVel:CURRent{ppdu_cmd_val}?', self.__class__.ResultData())

	def read(self, ppdu=repcap.Ppdu.Default) -> ResultData:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:MODulation:PLEVel:CURRent<PPDU> \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.modulation.plevel.current.read(ppdu = repcap.Ppdu.Default) \n
		Returns pulse levels according to the FIRA specification, relative to the SHR pulse level. \n
			:param ppdu: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Current')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'READ:UWB:MEASurement<Instance>:MEValuation:MODulation:PLEVel:CURRent{ppdu_cmd_val}?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Phr_Plevel: enums.ResultStatus2: PHR pulse level
			- Psdu_Plevel: enums.ResultStatus2: PSDU pulse level
			- Sts_Plevel: enums.ResultStatus2: STS pulse level"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Phr_Plevel', enums.ResultStatus2),
			ArgStruct.scalar_enum('Psdu_Plevel', enums.ResultStatus2),
			ArgStruct.scalar_enum('Sts_Plevel', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Phr_Plevel: enums.ResultStatus2 = None
			self.Psdu_Plevel: enums.ResultStatus2 = None
			self.Sts_Plevel: enums.ResultStatus2 = None

	def calculate(self, ppdu=repcap.Ppdu.Default) -> CalculateStruct:
		"""SCPI: CALCulate:UWB:MEASurement<Instance>:MEValuation:MODulation:PLEVel:CURRent<PPDU> \n
		Snippet: value: CalculateStruct = driver.uwbMeas.multiEval.modulation.plevel.current.calculate(ppdu = repcap.Ppdu.Default) \n
		Returns pulse levels according to the FIRA specification, relative to the SHR pulse level. \n
			:param ppdu: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Current')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'CALCulate:UWB:MEASurement<Instance>:MEValuation:MODulation:PLEVel:CURRent{ppdu_cmd_val}?', self.__class__.CalculateStruct())

	def clone(self) -> 'CurrentCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CurrentCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
