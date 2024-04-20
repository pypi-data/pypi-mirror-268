from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TraceCls:
	"""Trace commands group definition. 58 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trace", core, parent)

	@property
	def ncCorr(self):
		"""ncCorr commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ncCorr'):
			from .NcCorr import NcCorrCls
			self._ncCorr = NcCorrCls(self._core, self._cmd_group)
		return self._ncCorr

	@property
	def pmask(self):
		"""pmask commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmask'):
			from .Pmask import PmaskCls
			self._pmask = PmaskCls(self._core, self._cmd_group)
		return self._pmask

	@property
	def tsMask(self):
		"""tsMask commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tsMask'):
			from .TsMask import TsMaskCls
			self._tsMask = TsMaskCls(self._core, self._cmd_group)
		return self._tsMask

	@property
	def stJitter(self):
		"""stJitter commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_stJitter'):
			from .StJitter import StJitterCls
			self._stJitter = StJitterCls(self._core, self._cmd_group)
		return self._stJitter

	@property
	def spJitter(self):
		"""spJitter commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_spJitter'):
			from .SpJitter import SpJitterCls
			self._spJitter = SpJitterCls(self._core, self._cmd_group)
		return self._spJitter

	@property
	def ctJitter(self):
		"""ctJitter commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ctJitter'):
			from .CtJitter import CtJitterCls
			self._ctJitter = CtJitterCls(self._core, self._cmd_group)
		return self._ctJitter

	@property
	def cpJitter(self):
		"""cpJitter commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cpJitter'):
			from .CpJitter import CpJitterCls
			self._cpJitter = CpJitterCls(self._core, self._cmd_group)
		return self._cpJitter

	@property
	def sbws(self):
		"""sbws commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_sbws'):
			from .Sbws import SbwsCls
			self._sbws = SbwsCls(self._core, self._cmd_group)
		return self._sbws

	@property
	def sbwl(self):
		"""sbwl commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_sbwl'):
			from .Sbwl import SbwlCls
			self._sbwl = SbwlCls(self._core, self._cmd_group)
		return self._sbwl

	@property
	def powerVsTime(self):
		"""powerVsTime commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_powerVsTime'):
			from .PowerVsTime import PowerVsTimeCls
			self._powerVsTime = PowerVsTimeCls(self._core, self._cmd_group)
		return self._powerVsTime

	def clone(self) -> 'TraceCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TraceCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
