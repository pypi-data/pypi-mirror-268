from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TraceCls:
	"""Trace commands group definition. 72 total commands, 13 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trace", core, parent)

	@property
	def frange(self):
		"""frange commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_frange'):
			from .Frange import FrangeCls
			self._frange = FrangeCls(self._core, self._cmd_group)
		return self._frange

	@property
	def soBw(self):
		"""soBw commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_soBw'):
			from .SoBw import SoBwCls
			self._soBw = SoBwCls(self._core, self._cmd_group)
		return self._soBw

	@property
	def sacp(self):
		"""sacp commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_sacp'):
			from .Sacp import SacpCls
			self._sacp = SacpCls(self._core, self._cmd_group)
		return self._sacp

	@property
	def sgacp(self):
		"""sgacp commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_sgacp'):
			from .Sgacp import SgacpCls
			self._sgacp = SgacpCls(self._core, self._cmd_group)
		return self._sgacp

	@property
	def devMagnitude(self):
		"""devMagnitude commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_devMagnitude'):
			from .DevMagnitude import DevMagnitudeCls
			self._devMagnitude = DevMagnitudeCls(self._core, self._cmd_group)
		return self._devMagnitude

	@property
	def pdifference(self):
		"""pdifference commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdifference'):
			from .Pdifference import PdifferenceCls
			self._pdifference = PdifferenceCls(self._core, self._cmd_group)
		return self._pdifference

	@property
	def iqAbs(self):
		"""iqAbs commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_iqAbs'):
			from .IqAbs import IqAbsCls
			self._iqAbs = IqAbsCls(self._core, self._cmd_group)
		return self._iqAbs

	@property
	def iqDifference(self):
		"""iqDifference commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_iqDifference'):
			from .IqDifference import IqDifferenceCls
			self._iqDifference = IqDifferenceCls(self._core, self._cmd_group)
		return self._iqDifference

	@property
	def iqError(self):
		"""iqError commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_iqError'):
			from .IqError import IqErrorCls
			self._iqError = IqErrorCls(self._core, self._cmd_group)
		return self._iqError

	@property
	def fdeviation(self):
		"""fdeviation commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_fdeviation'):
			from .Fdeviation import FdeviationCls
			self._fdeviation = FdeviationCls(self._core, self._cmd_group)
		return self._fdeviation

	@property
	def spower(self):
		"""spower commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_spower'):
			from .Spower import SpowerCls
			self._spower = SpowerCls(self._core, self._cmd_group)
		return self._spower

	@property
	def pdeviation(self):
		"""pdeviation commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdeviation'):
			from .Pdeviation import PdeviationCls
			self._pdeviation = PdeviationCls(self._core, self._cmd_group)
		return self._pdeviation

	@property
	def powerVsTime(self):
		"""powerVsTime commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_powerVsTime'):
			from .PowerVsTime import PowerVsTimeCls
			self._powerVsTime = PowerVsTimeCls(self._core, self._cmd_group)
		return self._powerVsTime

	def clone(self) -> 'TraceCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TraceCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
