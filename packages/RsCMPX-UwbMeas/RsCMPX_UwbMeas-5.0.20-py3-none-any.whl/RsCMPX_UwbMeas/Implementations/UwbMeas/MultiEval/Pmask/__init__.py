from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PmaskCls:
	"""Pmask commands group definition. 11 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pmask", core, parent)

	@property
	def margin(self):
		"""margin commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_margin'):
			from .Margin import MarginCls
			self._margin = MarginCls(self._core, self._cmd_group)
		return self._margin

	@property
	def lower(self):
		"""lower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lower'):
			from .Lower import LowerCls
			self._lower = LowerCls(self._core, self._cmd_group)
		return self._lower

	@property
	def upper(self):
		"""upper commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_upper'):
			from .Upper import UpperCls
			self._upper = UpperCls(self._core, self._cmd_group)
		return self._upper

	@property
	def otolerance(self):
		"""otolerance commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_otolerance'):
			from .Otolerance import OtoleranceCls
			self._otolerance = OtoleranceCls(self._core, self._cmd_group)
		return self._otolerance

	def clone(self) -> 'PmaskCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PmaskCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
