from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class QhslCls:
	"""Qhsl commands group definition. 10 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qhsl", core, parent)

	@property
	def p2Q(self):
		"""p2Q commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_p2Q'):
			from .P2Q import P2QCls
			self._p2Q = P2QCls(self._core, self._cmd_group)
		return self._p2Q

	@property
	def p3Q(self):
		"""p3Q commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_p3Q'):
			from .P3Q import P3QCls
			self._p3Q = P3QCls(self._core, self._cmd_group)
		return self._p3Q

	@property
	def p4Q(self):
		"""p4Q commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_p4Q'):
			from .P4Q import P4QCls
			self._p4Q = P4QCls(self._core, self._cmd_group)
		return self._p4Q

	@property
	def p5Q(self):
		"""p5Q commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_p5Q'):
			from .P5Q import P5QCls
			self._p5Q = P5QCls(self._core, self._cmd_group)
		return self._p5Q

	@property
	def p6Q(self):
		"""p6Q commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_p6Q'):
			from .P6Q import P6QCls
			self._p6Q = P6QCls(self._core, self._cmd_group)
		return self._p6Q

	def clone(self) -> 'QhslCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = QhslCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
