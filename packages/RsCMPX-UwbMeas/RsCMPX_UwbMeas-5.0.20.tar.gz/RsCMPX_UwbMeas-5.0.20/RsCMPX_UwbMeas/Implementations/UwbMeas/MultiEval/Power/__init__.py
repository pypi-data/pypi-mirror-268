from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerCls:
	"""Power commands group definition. 90 total commands, 13 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

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
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_maximum'):
			from .Maximum import MaximumCls
			self._maximum = MaximumCls(self._core, self._cmd_group)
		return self._maximum

	@property
	def minimum(self):
		"""minimum commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_minimum'):
			from .Minimum import MinimumCls
			self._minimum = MinimumCls(self._core, self._cmd_group)
		return self._minimum

	@property
	def standardDev(self):
		"""standardDev commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_standardDev'):
			from .StandardDev import StandardDevCls
			self._standardDev = StandardDevCls(self._core, self._cmd_group)
		return self._standardDev

	@property
	def ppower(self):
		"""ppower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_ppower'):
			from .Ppower import PpowerCls
			self._ppower = PpowerCls(self._core, self._cmd_group)
		return self._ppower

	@property
	def ppPower(self):
		"""ppPower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_ppPower'):
			from .PpPower import PpPowerCls
			self._ppPower = PpPowerCls(self._core, self._cmd_group)
		return self._ppPower

	@property
	def dpower(self):
		"""dpower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_dpower'):
			from .Dpower import DpowerCls
			self._dpower = DpowerCls(self._core, self._cmd_group)
		return self._dpower

	@property
	def dpPower(self):
		"""dpPower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_dpPower'):
			from .DpPower import DpPowerCls
			self._dpPower = DpPowerCls(self._core, self._cmd_group)
		return self._dpPower

	@property
	def msPower(self):
		"""msPower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_msPower'):
			from .MsPower import MsPowerCls
			self._msPower = MsPowerCls(self._core, self._cmd_group)
		return self._msPower

	@property
	def msfPower(self):
		"""msfPower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_msfPower'):
			from .MsfPower import MsfPowerCls
			self._msfPower = MsfPowerCls(self._core, self._cmd_group)
		return self._msfPower

	@property
	def ppdu(self):
		"""ppdu commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_ppdu'):
			from .Ppdu import PpduCls
			self._ppdu = PpduCls(self._core, self._cmd_group)
		return self._ppdu

	@property
	def ppdPeak(self):
		"""ppdPeak commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_ppdPeak'):
			from .PpdPeak import PpdPeakCls
			self._ppdPeak = PpdPeakCls(self._core, self._cmd_group)
		return self._ppdPeak

	def clone(self) -> 'PowerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PowerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
