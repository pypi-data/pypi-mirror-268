from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ContentCls:
	"""Content commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("content", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliabiltiy: int: 'Reliability indicator'
			- Content: List[str]: Comma-separated list of hexadecimal values. The number of values can be queried via [CMDLINKRESOLVED UwbMeas.MultiEval.Ddecoding.Clength#Read CMDLINKRESOLVED]."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliabiltiy'),
			ArgStruct('Content', DataType.RawStringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliabiltiy: int = None
			self.Content: List[str] = None

	def fetch(self, ppdu=repcap.Ppdu.Nr1) -> ResultData:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:DDECoding:CONTent<PPDU> \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.ddecoding.content.fetch(ppdu = repcap.Ppdu.Nr1) \n
		Returns the binary data content as a list of hexadecimal values. \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: structure: for return value, see the help for ResultData structure arguments."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'FETCh:UWB:MEASurement<Instance>:MEValuation:DDECoding:CONTent{ppdu_cmd_val}?', self.__class__.ResultData())

	def read(self, ppdu=repcap.Ppdu.Nr1) -> ResultData:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:DDECoding:CONTent<PPDU> \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.ddecoding.content.read(ppdu = repcap.Ppdu.Nr1) \n
		Returns the binary data content as a list of hexadecimal values. \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: structure: for return value, see the help for ResultData structure arguments."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'READ:UWB:MEASurement<Instance>:MEValuation:DDECoding:CONTent{ppdu_cmd_val}?', self.__class__.ResultData())
