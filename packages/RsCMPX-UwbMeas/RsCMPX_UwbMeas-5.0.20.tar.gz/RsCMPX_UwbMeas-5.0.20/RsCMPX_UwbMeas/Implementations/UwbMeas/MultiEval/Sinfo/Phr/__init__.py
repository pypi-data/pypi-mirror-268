from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PhrCls:
	"""Phr commands group definition. 6 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phr", core, parent)

	@property
	def crc(self):
		"""crc commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_crc'):
			from .Crc import CrcCls
			self._crc = CrcCls(self._core, self._cmd_group)
		return self._crc

	@property
	def asSymbols(self):
		"""asSymbols commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_asSymbols'):
			from .AsSymbols import AsSymbolsCls
			self._asSymbols = AsSymbolsCls(self._core, self._cmd_group)
		return self._asSymbols

	@property
	def bitrate(self):
		"""bitrate commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_bitrate'):
			from .Bitrate import BitrateCls
			self._bitrate = BitrateCls(self._core, self._cmd_group)
		return self._bitrate

	def clone(self) -> 'PhrCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PhrCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
