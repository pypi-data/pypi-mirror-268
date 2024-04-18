from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PencodingCls:
	"""Pencoding commands group definition. 7 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pencoding", core, parent)

	@property
	def ssequence(self):
		"""ssequence commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ssequence'):
			from .Ssequence import SsequenceCls
			self._ssequence = SsequenceCls(self._core, self._cmd_group)
		return self._ssequence

	@property
	def edrate(self):
		"""edrate commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_edrate'):
			from .Edrate import EdrateCls
			self._edrate = EdrateCls(self._core, self._cmd_group)
		return self._edrate

	def clone(self) -> 'PencodingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PencodingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
