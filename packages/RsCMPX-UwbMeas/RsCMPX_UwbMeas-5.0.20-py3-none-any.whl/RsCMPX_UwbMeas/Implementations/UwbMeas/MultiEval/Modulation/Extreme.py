from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExtremeCls:
	"""Extreme commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("extreme", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Freq_Offset_Hz: float: No parameter help available
			- Freq_Offset: float: No parameter help available
			- Chip_Clock_Error: float: No parameter help available
			- Pulse_Nsme: float: No parameter help available
			- Sym_Mod_Accuracy: float: No parameter help available
			- Side_Lobe_Peak: float: No parameter help available
			- Pulse_Ml_Width: float: No parameter help available
			- Sym_Time_Jitter: float: No parameter help available
			- Sym_Phase_Jitter: float: No parameter help available
			- Chip_Time_Jitter: float: No parameter help available
			- Chip_Phase_Jitter: float: No parameter help available
			- Symbol_Evm: float: No parameter help available
			- Chip_Evm: float: No parameter help available
			- Rmarker: float: RMARKER time
			- Shr_Nrmse: float: NRMSE for SHR
			- Phr_Nrmse: float: NRMSE for PHR
			- Psdu_Nrmse: float: NRMSE for PSDU
			- Sts_Nrmse: float: NRMSE for STS
			- Sync_Pulse_Loc_Pol: enums.Result: No parameter help available
			- Sfd_Pulse_Loc_Pol: enums.Result: No parameter help available
			- Sts_Pulse_Loc_Pol: enums.Result: No parameter help available
			- Iq_Offset: float: I/Q offset"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Freq_Offset_Hz'),
			ArgStruct.scalar_float('Freq_Offset'),
			ArgStruct.scalar_float('Chip_Clock_Error'),
			ArgStruct.scalar_float('Pulse_Nsme'),
			ArgStruct.scalar_float('Sym_Mod_Accuracy'),
			ArgStruct.scalar_float('Side_Lobe_Peak'),
			ArgStruct.scalar_float('Pulse_Ml_Width'),
			ArgStruct.scalar_float('Sym_Time_Jitter'),
			ArgStruct.scalar_float('Sym_Phase_Jitter'),
			ArgStruct.scalar_float('Chip_Time_Jitter'),
			ArgStruct.scalar_float('Chip_Phase_Jitter'),
			ArgStruct.scalar_float('Symbol_Evm'),
			ArgStruct.scalar_float('Chip_Evm'),
			ArgStruct.scalar_float('Rmarker'),
			ArgStruct.scalar_float('Shr_Nrmse'),
			ArgStruct.scalar_float('Phr_Nrmse'),
			ArgStruct.scalar_float('Psdu_Nrmse'),
			ArgStruct.scalar_float('Sts_Nrmse'),
			ArgStruct.scalar_enum('Sync_Pulse_Loc_Pol', enums.Result),
			ArgStruct.scalar_enum('Sfd_Pulse_Loc_Pol', enums.Result),
			ArgStruct.scalar_enum('Sts_Pulse_Loc_Pol', enums.Result),
			ArgStruct.scalar_float('Iq_Offset')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Freq_Offset_Hz: float = None
			self.Freq_Offset: float = None
			self.Chip_Clock_Error: float = None
			self.Pulse_Nsme: float = None
			self.Sym_Mod_Accuracy: float = None
			self.Side_Lobe_Peak: float = None
			self.Pulse_Ml_Width: float = None
			self.Sym_Time_Jitter: float = None
			self.Sym_Phase_Jitter: float = None
			self.Chip_Time_Jitter: float = None
			self.Chip_Phase_Jitter: float = None
			self.Symbol_Evm: float = None
			self.Chip_Evm: float = None
			self.Rmarker: float = None
			self.Shr_Nrmse: float = None
			self.Phr_Nrmse: float = None
			self.Psdu_Nrmse: float = None
			self.Sts_Nrmse: float = None
			self.Sync_Pulse_Loc_Pol: enums.Result = None
			self.Sfd_Pulse_Loc_Pol: enums.Result = None
			self.Sts_Pulse_Loc_Pol: enums.Result = None
			self.Iq_Offset: float = None

	def fetch(self, ppdu=repcap.Ppdu.Nr1) -> ResultData:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:MODulation:EXTReme<PPDU> \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.modulation.extreme.fetch(ppdu = repcap.Ppdu.Nr1) \n
		Return the current, average, extreme and standard deviation single value modulation results. \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: structure: for return value, see the help for ResultData structure arguments."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'FETCh:UWB:MEASurement<Instance>:MEValuation:MODulation:EXTReme{ppdu_cmd_val}?', self.__class__.ResultData())

	def read(self, ppdu=repcap.Ppdu.Nr1) -> ResultData:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:MODulation:EXTReme<PPDU> \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.modulation.extreme.read(ppdu = repcap.Ppdu.Nr1) \n
		Return the current, average, extreme and standard deviation single value modulation results. \n
			:param ppdu: optional repeated capability selector. Default value: Nr1
			:return: structure: for return value, see the help for ResultData structure arguments."""
		ppdu_cmd_val = self._cmd_group.get_repcap_cmd_value(ppdu, repcap.Ppdu)
		return self._core.io.query_struct(f'READ:UWB:MEASurement<Instance>:MEValuation:MODulation:EXTReme{ppdu_cmd_val}?', self.__class__.ResultData())
