from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DdecodingCls:
	"""Ddecoding commands group definition. 6 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ddecoding", core, parent)

	@property
	def rsParity(self):
		"""rsParity commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rsParity'):
			from .RsParity import RsParityCls
			self._rsParity = RsParityCls(self._core, self._cmd_group)
		return self._rsParity

	@property
	def clength(self):
		"""clength commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_clength'):
			from .Clength import ClengthCls
			self._clength = ClengthCls(self._core, self._cmd_group)
		return self._clength

	@property
	def content(self):
		"""content commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_content'):
			from .Content import ContentCls
			self._content = ContentCls(self._core, self._cmd_group)
		return self._content

	def clone(self) -> 'DdecodingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DdecodingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
