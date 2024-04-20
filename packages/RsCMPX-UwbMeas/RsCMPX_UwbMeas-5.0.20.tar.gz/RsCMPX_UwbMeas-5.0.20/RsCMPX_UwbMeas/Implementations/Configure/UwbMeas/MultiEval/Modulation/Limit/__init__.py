from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LimitCls:
	"""Limit commands group definition. 10 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)

	@property
	def foffset(self):
		"""foffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_foffset'):
			from .Foffset import FoffsetCls
			self._foffset = FoffsetCls(self._core, self._cmd_group)
		return self._foffset

	@property
	def ccError(self):
		"""ccError commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ccError'):
			from .CcError import CcErrorCls
			self._ccError = CcErrorCls(self._core, self._cmd_group)
		return self._ccError

	@property
	def smAccuracy(self):
		"""smAccuracy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_smAccuracy'):
			from .SmAccuracy import SmAccuracyCls
			self._smAccuracy = SmAccuracyCls(self._core, self._cmd_group)
		return self._smAccuracy

	@property
	def slPeak(self):
		"""slPeak commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slPeak'):
			from .SlPeak import SlPeakCls
			self._slPeak = SlPeakCls(self._core, self._cmd_group)
		return self._slPeak

	@property
	def pmlWidth(self):
		"""pmlWidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmlWidth'):
			from .PmlWidth import PmlWidthCls
			self._pmlWidth = PmlWidthCls(self._core, self._cmd_group)
		return self._pmlWidth

	@property
	def shr(self):
		"""shr commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_shr'):
			from .Shr import ShrCls
			self._shr = ShrCls(self._core, self._cmd_group)
		return self._shr

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
	def sts(self):
		"""sts commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sts'):
			from .Sts import StsCls
			self._sts = StsCls(self._core, self._cmd_group)
		return self._sts

	@property
	def plevel(self):
		"""plevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_plevel'):
			from .Plevel import PlevelCls
			self._plevel = PlevelCls(self._core, self._cmd_group)
		return self._plevel

	def clone(self) -> 'LimitCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LimitCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
