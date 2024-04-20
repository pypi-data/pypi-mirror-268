from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PstGapCls:
	"""PstGap commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pstGap", core, parent)

	# noinspection PyTypeChecker
	class ReadStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliabiltiy: int: No parameter help available
			- Payload_Sts_Gap_A_0: int: No parameter help available
			- Payload_Sts_Gap_A_1: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliabiltiy'),
			ArgStruct.scalar_int('Payload_Sts_Gap_A_0'),
			ArgStruct.scalar_int('Payload_Sts_Gap_A_1')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliabiltiy: int = None
			self.Payload_Sts_Gap_A_0: int = None
			self.Payload_Sts_Gap_A_1: int = None

	def read(self, ppdu=repcap.Ppdu.Nr1) -> ReadStruct:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:SINFo:PSTGap<PPDU> \n
		Snippet: value: ReadStruct = driver.uwbMeas.multiEval.sinfo.pstGap.read(ppdu = repcap.Ppdu.Nr1) \n
		Returns the decoded bits A0 and A1 of the PHR. \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: structure: for return value, see the help for ReadStruct structure arguments."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'READ:UWB:MEASurement<Instance>:MEValuation:SINFo:PSTGap{ppdu_cmd_val}?', self.__class__.ReadStruct())

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Payload_Sts_Gap_A_0: int: No parameter help available
			- Payload_Sts_Gap_A_1: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Payload_Sts_Gap_A_0'),
			ArgStruct.scalar_int('Payload_Sts_Gap_A_1')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Payload_Sts_Gap_A_0: int = None
			self.Payload_Sts_Gap_A_1: int = None

	def fetch(self, ppdu=repcap.Ppdu.Nr1) -> FetchStruct:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo:PSTGap<PPDU> \n
		Snippet: value: FetchStruct = driver.uwbMeas.multiEval.sinfo.pstGap.fetch(ppdu = repcap.Ppdu.Nr1) \n
		Returns the decoded bits A0 and A1 of the PHR. \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo:PSTGap{ppdu_cmd_val}?', self.__class__.FetchStruct())
