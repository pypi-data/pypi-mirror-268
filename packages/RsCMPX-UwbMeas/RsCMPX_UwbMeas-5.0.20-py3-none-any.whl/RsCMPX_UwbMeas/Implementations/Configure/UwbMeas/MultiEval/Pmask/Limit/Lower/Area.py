from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AreaCls:
	"""Area commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Area, default value after init: Area.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("area", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_area_get', 'repcap_area_set', repcap.Area.Nr1)

	def repcap_area_set(self, area: repcap.Area) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Area.Default
		Default value after init: Area.Nr1"""
		self._cmd_group.set_repcap_enum_value(area)

	def repcap_area_get(self) -> repcap.Area:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, area_limit: float, area=repcap.Area.Default) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PMASk:LIMit:LOWer:AREA<nr> \n
		Snippet: driver.configure.uwbMeas.multiEval.pmask.limit.lower.area.set(area_limit = 1.0, area = repcap.Area.Default) \n
		Defines lower limits for the three areas of the pulse mask. \n
			:param area_limit: No help available
			:param area: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
		"""
		param = Conversions.decimal_value_to_str(area_limit)
		area_cmd_val = self._cmd_group.get_repcap_cmd_value(area, repcap.Area)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:PMASk:LIMit:LOWer:AREA{area_cmd_val} {param}')

	def get(self, area=repcap.Area.Default) -> float:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PMASk:LIMit:LOWer:AREA<nr> \n
		Snippet: value: float = driver.configure.uwbMeas.multiEval.pmask.limit.lower.area.get(area = repcap.Area.Default) \n
		Defines lower limits for the three areas of the pulse mask. \n
			:param area: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
			:return: area_limit: No help available"""
		area_cmd_val = self._cmd_group.get_repcap_cmd_value(area, repcap.Area)
		response = self._core.io.query_str(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:PMASk:LIMit:LOWer:AREA{area_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'AreaCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AreaCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
