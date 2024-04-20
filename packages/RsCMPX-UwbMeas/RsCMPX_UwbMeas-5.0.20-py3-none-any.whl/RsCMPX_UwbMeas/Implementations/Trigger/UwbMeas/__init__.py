from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UwbMeasCls:
	"""UwbMeas commands group definition. 7 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uwbMeas", core, parent)

	@property
	def multiEval(self):
		"""multiEval commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_multiEval'):
			from .MultiEval import MultiEvalCls
			self._multiEval = MultiEvalCls(self._core, self._cmd_group)
		return self._multiEval

	def clone(self) -> 'UwbMeasCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UwbMeasCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
