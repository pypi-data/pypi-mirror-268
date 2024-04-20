from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LimitCls:
	"""Limit commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)

	@property
	def area(self):
		"""area commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_area'):
			from .Area import AreaCls
			self._area = AreaCls(self._core, self._cmd_group)
		return self._area

	@property
	def upper(self):
		"""upper commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_upper'):
			from .Upper import UpperCls
			self._upper = UpperCls(self._core, self._cmd_group)
		return self._upper

	@property
	def lower(self):
		"""lower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lower'):
			from .Lower import LowerCls
			self._lower = LowerCls(self._core, self._cmd_group)
		return self._lower

	def clone(self) -> 'LimitCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LimitCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
