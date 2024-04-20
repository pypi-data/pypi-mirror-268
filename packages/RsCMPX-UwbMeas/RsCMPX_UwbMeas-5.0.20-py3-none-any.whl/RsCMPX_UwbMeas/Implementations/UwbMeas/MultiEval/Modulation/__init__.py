from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModulationCls:
	"""Modulation commands group definition. 267 total commands, 27 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	@property
	def otolerance(self):
		"""otolerance commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_otolerance'):
			from .Otolerance import OtoleranceCls
			self._otolerance = OtoleranceCls(self._core, self._cmd_group)
		return self._otolerance

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_current'):
			from .Current import CurrentCls
			self._current = CurrentCls(self._core, self._cmd_group)
		return self._current

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_average'):
			from .Average import AverageCls
			self._average = AverageCls(self._core, self._cmd_group)
		return self._average

	@property
	def extreme(self):
		"""extreme commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_extreme'):
			from .Extreme import ExtremeCls
			self._extreme = ExtremeCls(self._core, self._cmd_group)
		return self._extreme

	@property
	def standardDev(self):
		"""standardDev commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_standardDev'):
			from .StandardDev import StandardDevCls
			self._standardDev = StandardDevCls(self._core, self._cmd_group)
		return self._standardDev

	@property
	def foffset(self):
		"""foffset commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_foffset'):
			from .Foffset import FoffsetCls
			self._foffset = FoffsetCls(self._core, self._cmd_group)
		return self._foffset

	@property
	def ccError(self):
		"""ccError commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccError'):
			from .CcError import CcErrorCls
			self._ccError = CcErrorCls(self._core, self._cmd_group)
		return self._ccError

	@property
	def smAccuracy(self):
		"""smAccuracy commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_smAccuracy'):
			from .SmAccuracy import SmAccuracyCls
			self._smAccuracy = SmAccuracyCls(self._core, self._cmd_group)
		return self._smAccuracy

	@property
	def slPeak(self):
		"""slPeak commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_slPeak'):
			from .SlPeak import SlPeakCls
			self._slPeak = SlPeakCls(self._core, self._cmd_group)
		return self._slPeak

	@property
	def pmlWidth(self):
		"""pmlWidth commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmlWidth'):
			from .PmlWidth import PmlWidthCls
			self._pmlWidth = PmlWidthCls(self._core, self._cmd_group)
		return self._pmlWidth

	@property
	def stJitter(self):
		"""stJitter commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_stJitter'):
			from .StJitter import StJitterCls
			self._stJitter = StJitterCls(self._core, self._cmd_group)
		return self._stJitter

	@property
	def spJitter(self):
		"""spJitter commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_spJitter'):
			from .SpJitter import SpJitterCls
			self._spJitter = SpJitterCls(self._core, self._cmd_group)
		return self._spJitter

	@property
	def ctJitter(self):
		"""ctJitter commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ctJitter'):
			from .CtJitter import CtJitterCls
			self._ctJitter = CtJitterCls(self._core, self._cmd_group)
		return self._ctJitter

	@property
	def cpJitter(self):
		"""cpJitter commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_cpJitter'):
			from .CpJitter import CpJitterCls
			self._cpJitter = CpJitterCls(self._core, self._cmd_group)
		return self._cpJitter

	@property
	def sevm(self):
		"""sevm commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_sevm'):
			from .Sevm import SevmCls
			self._sevm = SevmCls(self._core, self._cmd_group)
		return self._sevm

	@property
	def cevm(self):
		"""cevm commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_cevm'):
			from .Cevm import CevmCls
			self._cevm = CevmCls(self._core, self._cmd_group)
		return self._cevm

	@property
	def nmse(self):
		"""nmse commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_nmse'):
			from .Nmse import NmseCls
			self._nmse = NmseCls(self._core, self._cmd_group)
		return self._nmse

	@property
	def fofh(self):
		"""fofh commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_fofh'):
			from .Fofh import FofhCls
			self._fofh = FofhCls(self._core, self._cmd_group)
		return self._fofh

	@property
	def rmarker(self):
		"""rmarker commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_rmarker'):
			from .Rmarker import RmarkerCls
			self._rmarker = RmarkerCls(self._core, self._cmd_group)
		return self._rmarker

	@property
	def shr(self):
		"""shr commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_shr'):
			from .Shr import ShrCls
			self._shr = ShrCls(self._core, self._cmd_group)
		return self._shr

	@property
	def phr(self):
		"""phr commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_phr'):
			from .Phr import PhrCls
			self._phr = PhrCls(self._core, self._cmd_group)
		return self._phr

	@property
	def psdu(self):
		"""psdu commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_psdu'):
			from .Psdu import PsduCls
			self._psdu = PsduCls(self._core, self._cmd_group)
		return self._psdu

	@property
	def sts(self):
		"""sts commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_sts'):
			from .Sts import StsCls
			self._sts = StsCls(self._core, self._cmd_group)
		return self._sts

	@property
	def sync(self):
		"""sync commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sync'):
			from .Sync import SyncCls
			self._sync = SyncCls(self._core, self._cmd_group)
		return self._sync

	@property
	def sfd(self):
		"""sfd commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sfd'):
			from .Sfd import SfdCls
			self._sfd = SfdCls(self._core, self._cmd_group)
		return self._sfd

	@property
	def iqOffset(self):
		"""iqOffset commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOffset'):
			from .IqOffset import IqOffsetCls
			self._iqOffset = IqOffsetCls(self._core, self._cmd_group)
		return self._iqOffset

	@property
	def plevel(self):
		"""plevel commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_plevel'):
			from .Plevel import PlevelCls
			self._plevel = PlevelCls(self._core, self._cmd_group)
		return self._plevel

	def clone(self) -> 'ModulationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ModulationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
