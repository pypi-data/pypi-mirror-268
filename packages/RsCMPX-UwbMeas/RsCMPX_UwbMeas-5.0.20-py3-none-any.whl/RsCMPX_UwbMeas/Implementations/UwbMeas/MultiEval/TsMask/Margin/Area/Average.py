from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Margin_Avg_Neg_Y: enums.ResultStatus2: Limit check result for area no with negative frequency offset.
			- Margin_Avg_Pos_Y: enums.ResultStatus2: Limit check result for area no with positive frequency offset."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Margin_Avg_Neg_Y', enums.ResultStatus2),
			ArgStruct.scalar_enum('Margin_Avg_Pos_Y', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Margin_Avg_Neg_Y: enums.ResultStatus2 = None
			self.Margin_Avg_Pos_Y: enums.ResultStatus2 = None

	def calculate(self, area=repcap.Area.Default, ppdu=repcap.Ppdu.Nr1) -> CalculateStruct:
		"""SCPI: CALCulate:UWB:MEASurement<Instance>:MEValuation:TSMask:MARGin:AREA<nr>:AVERage<PPDU> \n
		Snippet: value: CalculateStruct = driver.uwbMeas.multiEval.tsMask.margin.area.average.calculate(area = repcap.Area.Default, ppdu = repcap.Ppdu.Nr1) \n
		Returns the limit check results for the current and average traces, for the transmit spectrum mask area <no>. See also
		'Narrowband results'. \n
			:param area: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		area_cmd_val = self._cmd_group.get_repcap_cmd_value(area, repcap.Area)
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'CALCulate:UWB:MEASurement<Instance>:MEValuation:TSMask:MARGin:AREA{area_cmd_val}:AVERage{ppdu_cmd_val}?', self.__class__.CalculateStruct())
