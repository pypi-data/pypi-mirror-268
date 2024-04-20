from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MarginCls:
	"""Margin commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("margin", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Margin_Lower_X: float: X-position of the margin for the upper area no
			- Margin_Lower_Y: float: Y-value of the margin for the upper area no"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Margin_Lower_X'),
			ArgStruct.scalar_float('Margin_Lower_Y')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Margin_Lower_X: float = None
			self.Margin_Lower_Y: float = None

	def fetch(self, area=repcap.Area.Default, ppdu=repcap.Ppdu.Nr1) -> ResultData:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:PMASk:UPPer:AREA<nr>:MARGin<PPDU> \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.pmask.upper.area.margin.fetch(area = repcap.Area.Default, ppdu = repcap.Ppdu.Nr1) \n
		Returns the margin values between the transmitted pulse trace and the pulse mask for the upper area <no>. A negative
		margin indicates that the trace is located above the limit line, i.e. the limit is exceeded. See also 'Pulse Mask square'. \n
			:param area: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: structure: for return value, see the help for ResultData structure arguments."""
		area_cmd_val = self._cmd_group.get_repcap_cmd_value(area, repcap.Area)
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'FETCh:UWB:MEASurement<Instance>:MEValuation:PMASk:UPPer:AREA{area_cmd_val}:MARGin{ppdu_cmd_val}?', self.__class__.ResultData())

	def read(self, area=repcap.Area.Default, ppdu=repcap.Ppdu.Nr1) -> ResultData:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:PMASk:UPPer:AREA<nr>:MARGin<PPDU> \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.pmask.upper.area.margin.read(area = repcap.Area.Default, ppdu = repcap.Ppdu.Nr1) \n
		Returns the margin values between the transmitted pulse trace and the pulse mask for the upper area <no>. A negative
		margin indicates that the trace is located above the limit line, i.e. the limit is exceeded. See also 'Pulse Mask square'. \n
			:param area: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: structure: for return value, see the help for ResultData structure arguments."""
		area_cmd_val = self._cmd_group.get_repcap_cmd_value(area, repcap.Area)
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'READ:UWB:MEASurement<Instance>:MEValuation:PMASk:UPPer:AREA{area_cmd_val}:MARGin{ppdu_cmd_val}?', self.__class__.ResultData())
