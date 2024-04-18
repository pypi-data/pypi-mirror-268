from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AdetectedCls:
	"""Adetected commands group definition. 39 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("adetected", core, parent)

	@property
	def qhsl(self):
		"""qhsl commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_qhsl'):
			from .Qhsl import QhslCls
			self._qhsl = QhslCls(self._core, self._cmd_group)
		return self._qhsl

	@property
	def plength(self):
		"""plength commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_plength'):
			from .Plength import PlengthCls
			self._plength = PlengthCls(self._core, self._cmd_group)
		return self._plength

	@property
	def cte(self):
		"""cte commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cte'):
			from .Cte import CteCls
			self._cte = CteCls(self._core, self._cmd_group)
		return self._cte

	@property
	def coding(self):
		"""coding commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_coding'):
			from .Coding import CodingCls
			self._coding = CodingCls(self._core, self._cmd_group)
		return self._coding

	@property
	def ptype(self):
		"""ptype commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ptype'):
			from .Ptype import PtypeCls
			self._ptype = PtypeCls(self._core, self._cmd_group)
		return self._ptype

	@property
	def pattern(self):
		"""pattern commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import PatternCls
			self._pattern = PatternCls(self._core, self._cmd_group)
		return self._pattern

	@property
	def aaddress(self):
		"""aaddress commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_aaddress'):
			from .Aaddress import AaddressCls
			self._aaddress = AaddressCls(self._core, self._cmd_group)
		return self._aaddress

	@property
	def pduType(self):
		"""pduType commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pduType'):
			from .PduType import PduTypeCls
			self._pduType = PduTypeCls(self._core, self._cmd_group)
		return self._pduType

	@property
	def noSlots(self):
		"""noSlots commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_noSlots'):
			from .NoSlots import NoSlotsCls
			self._noSlots = NoSlotsCls(self._core, self._cmd_group)
		return self._noSlots

	def clone(self) -> 'AdetectedCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AdetectedCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
