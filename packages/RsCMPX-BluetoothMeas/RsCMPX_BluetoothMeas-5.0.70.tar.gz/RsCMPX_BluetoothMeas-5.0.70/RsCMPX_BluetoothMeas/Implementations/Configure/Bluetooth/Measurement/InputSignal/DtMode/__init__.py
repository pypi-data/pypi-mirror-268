from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DtModeCls:
	"""DtMode commands group definition. 9 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dtMode", core, parent)

	@property
	def rxQuality(self):
		"""rxQuality commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rxQuality'):
			from .RxQuality import RxQualityCls
			self._rxQuality = RxQualityCls(self._core, self._cmd_group)
		return self._rxQuality

	@property
	def plength(self):
		"""plength commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_plength'):
			from .Plength import PlengthCls
			self._plength = PlengthCls(self._core, self._cmd_group)
		return self._plength

	@property
	def pattern(self):
		"""pattern commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import PatternCls
			self._pattern = PatternCls(self._core, self._cmd_group)
		return self._pattern

	def clone(self) -> 'DtModeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DtModeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
