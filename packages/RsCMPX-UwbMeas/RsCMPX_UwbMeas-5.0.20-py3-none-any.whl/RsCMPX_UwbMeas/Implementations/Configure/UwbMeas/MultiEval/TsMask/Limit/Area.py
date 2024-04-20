from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


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

	def set(self, enable: bool, area_limit: float = None, area=repcap.Area.Default) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:TSMask:LIMit:AREA<nr> \n
		Snippet: driver.configure.uwbMeas.multiEval.tsMask.limit.area.set(enable = False, area_limit = 1.0, area = repcap.Area.Default) \n
		Activates and defines an upper limit for the two areas of the spectral mask. \n
			:param enable: No help available
			:param area_limit: No help available
			:param area: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('area_limit', area_limit, DataType.Float, None, is_optional=True))
		area_cmd_val = self._cmd_group.get_repcap_cmd_value(area, repcap.Area)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:TSMask:LIMit:AREA{area_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class AreaStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: No parameter help available
			- Area_Limit: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Area_Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Area_Limit: float = None

	def get(self, area=repcap.Area.Default) -> AreaStruct:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:TSMask:LIMit:AREA<nr> \n
		Snippet: value: AreaStruct = driver.configure.uwbMeas.multiEval.tsMask.limit.area.get(area = repcap.Area.Default) \n
		Activates and defines an upper limit for the two areas of the spectral mask. \n
			:param area: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
			:return: structure: for return value, see the help for AreaStruct structure arguments."""
		area_cmd_val = self._cmd_group.get_repcap_cmd_value(area, repcap.Area)
		return self._core.io.query_struct(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:TSMask:LIMit:AREA{area_cmd_val}?', self.__class__.AreaStruct())

	def clone(self) -> 'AreaCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AreaCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
