from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RsParityCls:
	"""RsParity commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rsParity", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliabiltiy: int: 'Reliability indicator'
			- Solomon_Parity: enums.Result: Indicates the passed or failed check verdict. The parity check is invalid, if no Reed-Solomon encoding is detected."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliabiltiy'),
			ArgStruct.scalar_enum('Solomon_Parity', enums.Result)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliabiltiy: int = None
			self.Solomon_Parity: enums.Result = None

	def fetch(self, ppdu=repcap.Ppdu.Nr1) -> ResultData:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:DDECoding:RSParity<PPDU> \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.ddecoding.rsParity.fetch(ppdu = repcap.Ppdu.Nr1) \n
		Returns the result of the parity check of the Reed-Solomon encoding. \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: structure: for return value, see the help for ResultData structure arguments."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'FETCh:UWB:MEASurement<Instance>:MEValuation:DDECoding:RSParity{ppdu_cmd_val}?', self.__class__.ResultData())

	def read(self, ppdu=repcap.Ppdu.Nr1) -> ResultData:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:DDECoding:RSParity<PPDU> \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.ddecoding.rsParity.read(ppdu = repcap.Ppdu.Nr1) \n
		Returns the result of the parity check of the Reed-Solomon encoding. \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: structure: for return value, see the help for ResultData structure arguments."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'READ:UWB:MEASurement<Instance>:MEValuation:DDECoding:RSParity{ppdu_cmd_val}?', self.__class__.ResultData())
