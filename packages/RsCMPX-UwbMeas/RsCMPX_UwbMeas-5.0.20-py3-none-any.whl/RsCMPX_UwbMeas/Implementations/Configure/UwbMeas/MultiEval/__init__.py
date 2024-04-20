from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiEvalCls:
	"""MultiEval commands group definition. 44 total commands, 16 Subgroups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("multiEval", core, parent)

	@property
	def ppdu(self):
		"""ppdu commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_ppdu'):
			from .Ppdu import PpduCls
			self._ppdu = PpduCls(self._core, self._cmd_group)
		return self._ppdu

	@property
	def phr(self):
		"""phr commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_phr'):
			from .Phr import PhrCls
			self._phr = PhrCls(self._core, self._cmd_group)
		return self._phr

	@property
	def psdu(self):
		"""psdu commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_psdu'):
			from .Psdu import PsduCls
			self._psdu = PsduCls(self._core, self._cmd_group)
		return self._psdu

	@property
	def mprFrequency(self):
		"""mprFrequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mprFrequency'):
			from .MprFrequency import MprFrequencyCls
			self._mprFrequency = MprFrequencyCls(self._core, self._cmd_group)
		return self._mprFrequency

	@property
	def prfMode(self):
		"""prfMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prfMode'):
			from .PrfMode import PrfModeCls
			self._prfMode = PrfModeCls(self._core, self._cmd_group)
		return self._prfMode

	@property
	def psFormat(self):
		"""psFormat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_psFormat'):
			from .PsFormat import PsFormatCls
			self._psFormat = PsFormatCls(self._core, self._cmd_group)
		return self._psFormat

	@property
	def ppLength(self):
		"""ppLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ppLength'):
			from .PpLength import PpLengthCls
			self._ppLength = PpLengthCls(self._core, self._cmd_group)
		return self._ppLength

	@property
	def stSegments(self):
		"""stSegments commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stSegments'):
			from .StSegments import StSegmentsCls
			self._stSegments = StSegmentsCls(self._core, self._cmd_group)
		return self._stSegments

	@property
	def stsLength(self):
		"""stsLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stsLength'):
			from .StsLength import StsLengthCls
			self._stsLength = StsLengthCls(self._core, self._cmd_group)
		return self._stsLength

	@property
	def stsGap(self):
		"""stsGap commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_stsGap'):
			from .StsGap import StsGapCls
			self._stsGap = StsGapCls(self._core, self._cmd_group)
		return self._stsGap

	@property
	def spectrum(self):
		"""spectrum commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_spectrum'):
			from .Spectrum import SpectrumCls
			self._spectrum = SpectrumCls(self._core, self._cmd_group)
		return self._spectrum

	@property
	def phrRate(self):
		"""phrRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phrRate'):
			from .PhrRate import PhrRateCls
			self._phrRate = PhrRateCls(self._core, self._cmd_group)
		return self._phrRate

	@property
	def result(self):
		"""result commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_result'):
			from .Result import ResultCls
			self._result = ResultCls(self._core, self._cmd_group)
		return self._result

	@property
	def modulation(self):
		"""modulation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import ModulationCls
			self._modulation = ModulationCls(self._core, self._cmd_group)
		return self._modulation

	@property
	def tsMask(self):
		"""tsMask commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tsMask'):
			from .TsMask import TsMaskCls
			self._tsMask = TsMaskCls(self._core, self._cmd_group)
		return self._tsMask

	@property
	def pmask(self):
		"""pmask commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmask'):
			from .Pmask import PmaskCls
			self._pmask = PmaskCls(self._core, self._cmd_group)
		return self._pmask

	def get_ptracking(self) -> bool:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PTRacking \n
		Snippet: value: bool = driver.configure.uwbMeas.multiEval.get_ptracking() \n
		Enables or disables phase tracking. \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:PTRacking?')
		return Conversions.str_to_bool(response)

	def set_ptracking(self, enable: bool) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PTRacking \n
		Snippet: driver.configure.uwbMeas.multiEval.set_ptracking(enable = False) \n
		Enables or disables phase tracking. \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:PTRacking {param}')

	# noinspection PyTypeChecker
	def get_pmode(self) -> enums.PpduMode:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PMODe \n
		Snippet: value: enums.PpduMode = driver.configure.uwbMeas.multiEval.get_pmode() \n
		Selects the measurement mode. \n
			:return: ppdu_mode: SPPDu: single PPDU packet analysis MPPDu: multi PPDU packet analysis
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:PMODe?')
		return Conversions.str_to_scalar_enum(response, enums.PpduMode)

	def set_pmode(self, ppdu_mode: enums.PpduMode) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PMODe \n
		Snippet: driver.configure.uwbMeas.multiEval.set_pmode(ppdu_mode = enums.PpduMode.MPPDu) \n
		Selects the measurement mode. \n
			:param ppdu_mode: SPPDu: single PPDU packet analysis MPPDu: multi PPDU packet analysis
		"""
		param = Conversions.enum_scalar_to_str(ppdu_mode, enums.PpduMode)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:PMODe {param}')

	# noinspection PyTypeChecker
	def get_scondition(self) -> enums.StopCondition:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:SCONdition \n
		Snippet: value: enums.StopCondition = driver.configure.uwbMeas.multiEval.get_scondition() \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:return: stop_condition: NONE: Continue irrespective of the limit check. SLFail: Stop the measurement on limit failure.
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:SCONdition?')
		return Conversions.str_to_scalar_enum(response, enums.StopCondition)

	def set_scondition(self, stop_condition: enums.StopCondition) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:SCONdition \n
		Snippet: driver.configure.uwbMeas.multiEval.set_scondition(stop_condition = enums.StopCondition.NONE) \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:param stop_condition: NONE: Continue irrespective of the limit check. SLFail: Stop the measurement on limit failure.
		"""
		param = Conversions.enum_scalar_to_str(stop_condition, enums.StopCondition)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:SCONdition {param}')

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:TOUT \n
		Snippet: value: float = driver.configure.uwbMeas.multiEval.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually. When the measurement has completed the first measurement
		cycle (first single shot) , the statistical depth is reached and the timer is reset. If the first measurement cycle has
		not been completed when the timer expires, the measurement is stopped. The measurement state changes to RDY.
		The reliability indicator is set to 1, indicating that a measurement timeout occurred. Still running READ, FETCh or
		CALCulate commands are completed, returning the available results. At least for some results, there are no values at all
		or the statistical depth has not been reached. A timeout of 0 s corresponds to an infinite measurement timeout. \n
			:return: tcd_timeout: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, tcd_timeout: float) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:TOUT \n
		Snippet: driver.configure.uwbMeas.multiEval.set_timeout(tcd_timeout = 1.0) \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually. When the measurement has completed the first measurement
		cycle (first single shot) , the statistical depth is reached and the timer is reset. If the first measurement cycle has
		not been completed when the timer expires, the measurement is stopped. The measurement state changes to RDY.
		The reliability indicator is set to 1, indicating that a measurement timeout occurred. Still running READ, FETCh or
		CALCulate commands are completed, returning the available results. At least for some results, there are no values at all
		or the statistical depth has not been reached. A timeout of 0 s corresponds to an infinite measurement timeout. \n
			:param tcd_timeout: No help available
		"""
		param = Conversions.decimal_value_to_str(tcd_timeout)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:TOUT {param}')

	def get_scount(self) -> int:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:SCOunt \n
		Snippet: value: int = driver.configure.uwbMeas.multiEval.get_scount() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. The statistic count applies to TX modulation and jitter measurements. \n
			:return: statistic_count: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:SCOunt?')
		return Conversions.str_to_int(response)

	def set_scount(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:SCOunt \n
		Snippet: driver.configure.uwbMeas.multiEval.set_scount(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. The statistic count applies to TX modulation and jitter measurements. \n
			:param statistic_count: No help available
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:SCOunt {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.uwbMeas.multiEval.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:return: repetition: SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:REPetition \n
		Snippet: driver.configure.uwbMeas.multiEval.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:param repetition: SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:REPetition {param}')

	def get_mo_exception(self) -> bool:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:MOEXception \n
		Snippet: value: bool = driver.configure.uwbMeas.multiEval.get_mo_exception() \n
		Specifies whether measurement results identified as faulty or inaccurate are rejected. \n
			:return: meas_on_exception: OFF: Faulty results are rejected. ON: Results are never rejected.
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:MOEXception?')
		return Conversions.str_to_bool(response)

	def set_mo_exception(self, meas_on_exception: bool) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:MOEXception \n
		Snippet: driver.configure.uwbMeas.multiEval.set_mo_exception(meas_on_exception = False) \n
		Specifies whether measurement results identified as faulty or inaccurate are rejected. \n
			:param meas_on_exception: OFF: Faulty results are rejected. ON: Results are never rejected.
		"""
		param = Conversions.bool_to_str(meas_on_exception)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:MOEXception {param}')

	def get_cap_length(self) -> float:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:CAPLength \n
		Snippet: value: float = driver.configure.uwbMeas.multiEval.get_cap_length() \n
		Defines the length to capture the signal. \n
			:return: capture_length: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:CAPLength?')
		return Conversions.str_to_float(response)

	def set_cap_length(self, capture_length: float) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:CAPLength \n
		Snippet: driver.configure.uwbMeas.multiEval.set_cap_length(capture_length = 1.0) \n
		Defines the length to capture the signal. \n
			:param capture_length: No help available
		"""
		param = Conversions.decimal_value_to_str(capture_length)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:CAPLength {param}')

	def get_eoffset(self) -> float:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:EOFFset \n
		Snippet: value: float = driver.configure.uwbMeas.multiEval.get_eoffset() \n
		Specifies which time period is excluded from the measurement at the beginning of the capture length. \n
			:return: eval_offset: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:EOFFset?')
		return Conversions.str_to_float(response)

	def set_eoffset(self, eval_offset: float) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:EOFFset \n
		Snippet: driver.configure.uwbMeas.multiEval.set_eoffset(eval_offset = 1.0) \n
		Specifies which time period is excluded from the measurement at the beginning of the capture length. \n
			:param eval_offset: No help available
		"""
		param = Conversions.decimal_value_to_str(eval_offset)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:EOFFset {param}')

	def clone(self) -> 'MultiEvalCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultiEvalCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
