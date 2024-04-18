from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PtypeCls:
	"""Ptype commands group definition. 5 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ptype", core, parent)

	@property
	def lowEnergy(self):
		"""lowEnergy commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_lowEnergy'):
			from .LowEnergy import LowEnergyCls
			self._lowEnergy = LowEnergyCls(self._core, self._cmd_group)
		return self._lowEnergy

	@property
	def edrate(self):
		"""edrate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_edrate'):
			from .Edrate import EdrateCls
			self._edrate = EdrateCls(self._core, self._cmd_group)
		return self._edrate

	@property
	def brate(self):
		"""brate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_brate'):
			from .Brate import BrateCls
			self._brate = BrateCls(self._core, self._cmd_group)
		return self._brate

	def clone(self) -> 'PtypeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PtypeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
