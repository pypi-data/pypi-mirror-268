from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LowEnergyCls:
	"""LowEnergy commands group definition. 9 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lowEnergy", core, parent)

	@property
	def le1M(self):
		"""le1M commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_le1M'):
			from .Le1M import Le1MCls
			self._le1M = Le1MCls(self._core, self._cmd_group)
		return self._le1M

	@property
	def le2M(self):
		"""le2M commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_le2M'):
			from .Le2M import Le2MCls
			self._le2M = Le2MCls(self._core, self._cmd_group)
		return self._le2M

	@property
	def lrange(self):
		"""lrange commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_lrange'):
			from .Lrange import LrangeCls
			self._lrange = LrangeCls(self._core, self._cmd_group)
		return self._lrange

	def clone(self) -> 'LowEnergyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LowEnergyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
