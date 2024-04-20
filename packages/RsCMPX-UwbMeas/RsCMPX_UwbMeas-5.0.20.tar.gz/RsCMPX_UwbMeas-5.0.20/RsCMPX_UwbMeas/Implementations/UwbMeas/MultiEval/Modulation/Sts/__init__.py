from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StsCls:
	"""Sts commands group definition. 30 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sts", core, parent)

	@property
	def nrmse(self):
		"""nrmse commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_nrmse'):
			from .Nrmse import NrmseCls
			self._nrmse = NrmseCls(self._core, self._cmd_group)
		return self._nrmse

	@property
	def plPolarity(self):
		"""plPolarity commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_plPolarity'):
			from .PlPolarity import PlPolarityCls
			self._plPolarity = PlPolarityCls(self._core, self._cmd_group)
		return self._plPolarity

	@property
	def plevel(self):
		"""plevel commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_plevel'):
			from .Plevel import PlevelCls
			self._plevel = PlevelCls(self._core, self._cmd_group)
		return self._plevel

	def clone(self) -> 'StsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = StsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
