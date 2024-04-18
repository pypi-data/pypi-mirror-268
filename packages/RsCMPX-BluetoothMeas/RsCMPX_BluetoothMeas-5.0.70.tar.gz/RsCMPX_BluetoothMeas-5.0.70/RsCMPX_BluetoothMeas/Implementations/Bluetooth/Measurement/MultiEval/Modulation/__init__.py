from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModulationCls:
	"""Modulation commands group definition. 288 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	@property
	def qhsl(self):
		"""qhsl commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_qhsl'):
			from .Qhsl import QhslCls
			self._qhsl = QhslCls(self._core, self._cmd_group)
		return self._qhsl

	@property
	def nmode(self):
		"""nmode commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_nmode'):
			from .Nmode import NmodeCls
			self._nmode = NmodeCls(self._core, self._cmd_group)
		return self._nmode

	@property
	def brate(self):
		"""brate commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_brate'):
			from .Brate import BrateCls
			self._brate = BrateCls(self._core, self._cmd_group)
		return self._brate

	@property
	def edrate(self):
		"""edrate commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_edrate'):
			from .Edrate import EdrateCls
			self._edrate = EdrateCls(self._core, self._cmd_group)
		return self._edrate

	@property
	def cte(self):
		"""cte commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cte'):
			from .Cte import CteCls
			self._cte = CteCls(self._core, self._cmd_group)
		return self._cte

	@property
	def lowEnergy(self):
		"""lowEnergy commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_lowEnergy'):
			from .LowEnergy import LowEnergyCls
			self._lowEnergy = LowEnergyCls(self._core, self._cmd_group)
		return self._lowEnergy

	def clone(self) -> 'ModulationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ModulationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
