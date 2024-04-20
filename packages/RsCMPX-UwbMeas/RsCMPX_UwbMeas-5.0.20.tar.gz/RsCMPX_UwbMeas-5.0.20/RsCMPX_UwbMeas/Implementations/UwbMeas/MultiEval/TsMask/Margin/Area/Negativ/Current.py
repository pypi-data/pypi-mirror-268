from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


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
			- Margin_Curr_Neg_X: float: No parameter help available
			- Margin_Curr_Neg_Y: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Margin_Curr_Neg_X'),
			ArgStruct.scalar_float('Margin_Curr_Neg_Y')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Margin_Curr_Neg_X: float = None
			self.Margin_Curr_Neg_Y: float = None

	def fetch(self, area=repcap.Area.Default, ppdu=repcap.Ppdu.Default) -> ResultData:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:TSMask:MARGin:AREA<nr>:NEGativ:CURRent<PPDU> \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.tsMask.margin.area.negativ.current.fetch(area = repcap.Area.Default, ppdu = repcap.Ppdu.Default) \n
		Returns the margin values between the result trace and the transmit spectrum mask for the area <no> with negative
		frequency offset. A negative margin indicates that the trace is located above the limit line, i.e. the limit is exceeded.
		The current and average values can be retrieved. See also 'Narrowband results'. \n
			:param area: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
			:param ppdu: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Current')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		area_cmd_val = self._cmd_group.get_repcap_cmd_value(area, repcap.Area)
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'FETCh:UWB:MEASurement<Instance>:MEValuation:TSMask:MARGin:AREA{area_cmd_val}:NEGativ:CURRent{ppdu_cmd_val}?', self.__class__.ResultData())

	def read(self, area=repcap.Area.Default, ppdu=repcap.Ppdu.Default) -> ResultData:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:TSMask:MARGin:AREA<nr>:NEGativ:CURRent<PPDU> \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.tsMask.margin.area.negativ.current.read(area = repcap.Area.Default, ppdu = repcap.Ppdu.Default) \n
		Returns the margin values between the result trace and the transmit spectrum mask for the area <no> with negative
		frequency offset. A negative margin indicates that the trace is located above the limit line, i.e. the limit is exceeded.
		The current and average values can be retrieved. See also 'Narrowband results'. \n
			:param area: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
			:param ppdu: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Current')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		area_cmd_val = self._cmd_group.get_repcap_cmd_value(area, repcap.Area)
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'READ:UWB:MEASurement<Instance>:MEValuation:TSMask:MARGin:AREA{area_cmd_val}:NEGativ:CURRent{ppdu_cmd_val}?', self.__class__.ResultData())

	def clone(self) -> 'CurrentCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CurrentCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
