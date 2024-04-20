from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TsMaskCls:
	"""TsMask commands group definition. 17 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsMask", core, parent)

	@property
	def margin(self):
		"""margin commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_margin'):
			from .Margin import MarginCls
			self._margin = MarginCls(self._core, self._cmd_group)
		return self._margin

	@property
	def otolerance(self):
		"""otolerance commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_otolerance'):
			from .Otolerance import OtoleranceCls
			self._otolerance = OtoleranceCls(self._core, self._cmd_group)
		return self._otolerance

	@property
	def tdbBandwidth(self):
		"""tdbBandwidth commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tdbBandwidth'):
			from .TdbBandwidth import TdbBandwidthCls
			self._tdbBandwidth = TdbBandwidthCls(self._core, self._cmd_group)
		return self._tdbBandwidth

	def clone(self) -> 'TsMaskCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TsMaskCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
