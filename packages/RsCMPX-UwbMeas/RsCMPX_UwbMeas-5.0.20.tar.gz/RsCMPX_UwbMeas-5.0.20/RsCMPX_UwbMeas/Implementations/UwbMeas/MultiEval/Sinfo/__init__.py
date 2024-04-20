from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SinfoCls:
	"""Sinfo commands group definition. 36 total commands, 14 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sinfo", core, parent)

	@property
	def drate(self):
		"""drate commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_drate'):
			from .Drate import DrateCls
			self._drate = DrateCls(self._core, self._cmd_group)
		return self._drate

	@property
	def phr(self):
		"""phr commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_phr'):
			from .Phr import PhrCls
			self._phr = PhrCls(self._core, self._cmd_group)
		return self._phr

	@property
	def asSymbols(self):
		"""asSymbols commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_asSymbols'):
			from .AsSymbols import AsSymbolsCls
			self._asSymbols = AsSymbolsCls(self._core, self._cmd_group)
		return self._asSymbols

	@property
	def csLength(self):
		"""csLength commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_csLength'):
			from .CsLength import CsLengthCls
			self._csLength = CsLengthCls(self._core, self._cmd_group)
		return self._csLength

	@property
	def psdu(self):
		"""psdu commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_psdu'):
			from .Psdu import PsduCls
			self._psdu = PsduCls(self._core, self._cmd_group)
		return self._psdu

	@property
	def dlength(self):
		"""dlength commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dlength'):
			from .Dlength import DlengthCls
			self._dlength = DlengthCls(self._core, self._cmd_group)
		return self._dlength

	@property
	def cindex(self):
		"""cindex commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_cindex'):
			from .Cindex import CindexCls
			self._cindex = CindexCls(self._core, self._cmd_group)
		return self._cindex

	@property
	def dppdu(self):
		"""dppdu commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dppdu'):
			from .Dppdu import DppduCls
			self._dppdu = DppduCls(self._core, self._cmd_group)
		return self._dppdu

	@property
	def pstGap(self):
		"""pstGap commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_pstGap'):
			from .PstGap import PstGapCls
			self._pstGap = PstGapCls(self._core, self._cmd_group)
		return self._pstGap

	@property
	def reBit(self):
		"""reBit commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_reBit'):
			from .ReBit import ReBitCls
			self._reBit = ReBitCls(self._core, self._cmd_group)
		return self._reBit

	@property
	def raBit(self):
		"""raBit commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_raBit'):
			from .RaBit import RaBitCls
			self._raBit = RaBitCls(self._core, self._cmd_group)
		return self._raBit

	@property
	def fcsCheck(self):
		"""fcsCheck commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_fcsCheck'):
			from .FcsCheck import FcsCheckCls
			self._fcsCheck = FcsCheckCls(self._core, self._cmd_group)
		return self._fcsCheck

	@property
	def sfd(self):
		"""sfd commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_sfd'):
			from .Sfd import SfdCls
			self._sfd = SfdCls(self._core, self._cmd_group)
		return self._sfd

	@property
	def sfdLength(self):
		"""sfdLength commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_sfdLength'):
			from .SfdLength import SfdLengthCls
			self._sfdLength = SfdLengthCls(self._core, self._cmd_group)
		return self._sfdLength

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Psdu_Bitrate: float: No parameter help available
			- Phr_Crc: enums.Result: Verification of PHR checksum (SECDED)
			- Analysed_Sync_Sym: int: No parameter help available
			- Cs_Length: int: Length of the code sequence
			- Psdu_Length: int: Length of the PSDU
			- Delta_Length: int: No parameter help available
			- Code_Index: int: No parameter help available
			- Detected_Ppdus: int: No parameter help available
			- Payload_Sts_Gap_A_0: int: No parameter help available
			- Payload_Sts_Gap_A_1: int: No parameter help available
			- Ranging_Bit: int: Decoded ranging bit of the PHR
			- Reserved_Bit: int: Decoded reserved bit of the PHR
			- Fcs_Check: enums.Result: Verification of MAC FCS checksum
			- Sync_Sym_Phr: int: Number of symbols in the SYNC field, read from the PHR
			- Sfd_Value: int: SFD value as defined in IEEE Std 802.15.4z‐2020
			- Sfd_Length: int: Length of the SFD sequence
			- Phr_Bitrate: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Psdu_Bitrate'),
			ArgStruct.scalar_enum('Phr_Crc', enums.Result),
			ArgStruct.scalar_int('Analysed_Sync_Sym'),
			ArgStruct.scalar_int('Cs_Length'),
			ArgStruct.scalar_int('Psdu_Length'),
			ArgStruct.scalar_int('Delta_Length'),
			ArgStruct.scalar_int('Code_Index'),
			ArgStruct.scalar_int('Detected_Ppdus'),
			ArgStruct.scalar_int('Payload_Sts_Gap_A_0'),
			ArgStruct.scalar_int('Payload_Sts_Gap_A_1'),
			ArgStruct.scalar_int('Ranging_Bit'),
			ArgStruct.scalar_int('Reserved_Bit'),
			ArgStruct.scalar_enum('Fcs_Check', enums.Result),
			ArgStruct.scalar_int('Sync_Sym_Phr'),
			ArgStruct.scalar_int('Sfd_Value'),
			ArgStruct.scalar_int('Sfd_Length'),
			ArgStruct.scalar_float('Phr_Bitrate')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Psdu_Bitrate: float = None
			self.Phr_Crc: enums.Result = None
			self.Analysed_Sync_Sym: int = None
			self.Cs_Length: int = None
			self.Psdu_Length: int = None
			self.Delta_Length: int = None
			self.Code_Index: int = None
			self.Detected_Ppdus: int = None
			self.Payload_Sts_Gap_A_0: int = None
			self.Payload_Sts_Gap_A_1: int = None
			self.Ranging_Bit: int = None
			self.Reserved_Bit: int = None
			self.Fcs_Check: enums.Result = None
			self.Sync_Sym_Phr: int = None
			self.Sfd_Value: int = None
			self.Sfd_Length: int = None
			self.Phr_Bitrate: float = None

	def fetch(self, ppdu=repcap.Ppdu.Nr1) -> ResultData:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo<PPDU> \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.sinfo.fetch(ppdu = repcap.Ppdu.Nr1) \n
		Return the current single value signal information results. \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: structure: for return value, see the help for ResultData structure arguments."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo{ppdu_cmd_val}?', self.__class__.ResultData())

	def read(self, ppdu=repcap.Ppdu.Nr1) -> ResultData:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:SINFo<PPDU> \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.sinfo.read(ppdu = repcap.Ppdu.Nr1) \n
		Return the current single value signal information results. \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: structure: for return value, see the help for ResultData structure arguments."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'READ:UWB:MEASurement<Instance>:MEValuation:SINFo{ppdu_cmd_val}?', self.__class__.ResultData())

	def clone(self) -> 'SinfoCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SinfoCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
