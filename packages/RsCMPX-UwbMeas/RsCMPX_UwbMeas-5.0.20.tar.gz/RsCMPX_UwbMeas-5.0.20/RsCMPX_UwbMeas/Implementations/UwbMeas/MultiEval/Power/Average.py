from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

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

	def fetch(self, ppdu=repcap.Ppdu.Nr1) -> ResultData:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:POWer:AVERage<PPDU> \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.power.average.fetch(ppdu = repcap.Ppdu.Nr1) \n
		Return the current, average, extreme and standard deviation single value power results. \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: structure: for return value, see the help for ResultData structure arguments."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'FETCh:UWB:MEASurement<Instance>:MEValuation:POWer:AVERage{ppdu_cmd_val}?', self.__class__.ResultData())

	def read(self, ppdu=repcap.Ppdu.Nr1) -> ResultData:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:POWer:AVERage<PPDU> \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.power.average.read(ppdu = repcap.Ppdu.Nr1) \n
		Return the current, average, extreme and standard deviation single value power results. \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: structure: for return value, see the help for ResultData structure arguments."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'READ:UWB:MEASurement<Instance>:MEValuation:POWer:AVERage{ppdu_cmd_val}?', self.__class__.ResultData())
