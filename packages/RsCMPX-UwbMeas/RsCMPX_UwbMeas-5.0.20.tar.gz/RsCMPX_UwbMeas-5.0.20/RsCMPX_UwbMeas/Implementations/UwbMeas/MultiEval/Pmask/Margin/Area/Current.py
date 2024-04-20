from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 1 total commands, 0 Subgroups, 1 group commands
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
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Margin_Upper_Y: enums.ResultStatus2: Limit check result for upper area no.
			- Margin_Lower_Y: enums.ResultStatus2: Limit check result for lower area no."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Margin_Upper_Y', enums.ResultStatus2),
			ArgStruct.scalar_enum('Margin_Lower_Y', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Margin_Upper_Y: enums.ResultStatus2 = None
			self.Margin_Lower_Y: enums.ResultStatus2 = None

	def calculate(self, area=repcap.Area.Default, ppdu=repcap.Ppdu.Default) -> CalculateStruct:
		"""SCPI: CALCulate:UWB:MEASurement<Instance>:MEValuation:PMASk:MARGin:AREA<nr>:CURRent<PPDU> \n
		Snippet: value: CalculateStruct = driver.uwbMeas.multiEval.pmask.margin.area.current.calculate(area = repcap.Area.Default, ppdu = repcap.Ppdu.Default) \n
		Returns the limit check results for the pulse mask measurement, for the pulse mask area <no>. See also 'Pulse Mask
		square'. \n
			:param area: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
			:param ppdu: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Current')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		area_cmd_val = self._cmd_group.get_repcap_cmd_value(area, repcap.Area)
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'CALCulate:UWB:MEASurement<Instance>:MEValuation:PMASk:MARGin:AREA{area_cmd_val}:CURRent{ppdu_cmd_val}?', self.__class__.CalculateStruct())

	def clone(self) -> 'CurrentCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CurrentCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
