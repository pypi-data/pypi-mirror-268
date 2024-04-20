from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TdbBandwidthCls:
	"""TdbBandwidth commands group definition. 5 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tdbBandwidth", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def psPower(self):
		"""psPower commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_psPower'):
			from .PsPower import PsPowerCls
			self._psPower = PsPowerCls(self._core, self._cmd_group)
		return self._psPower

	def clone(self) -> 'TdbBandwidthCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TdbBandwidthCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
