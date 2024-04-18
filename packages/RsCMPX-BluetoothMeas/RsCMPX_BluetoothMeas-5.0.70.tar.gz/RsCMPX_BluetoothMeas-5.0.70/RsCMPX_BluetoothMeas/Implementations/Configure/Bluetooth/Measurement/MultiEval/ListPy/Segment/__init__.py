from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SegmentCls:
	"""Segment commands group definition. 35 total commands, 4 Subgroups, 0 group commands
	Repeated Capability: Segment, default value after init: Segment.S1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("segment", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_segment_get', 'repcap_segment_set', repcap.Segment.S1)

	def repcap_segment_set(self, segment: repcap.Segment) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Segment.Default
		Default value after init: Segment.S1"""
		self._cmd_group.set_repcap_enum_value(segment)

	def repcap_segment_get(self) -> repcap.Segment:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def cidx(self):
		"""cidx commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cidx'):
			from .Cidx import CidxCls
			self._cidx = CidxCls(self._core, self._cmd_group)
		return self._cidx

	@property
	def setup(self):
		"""setup commands group. 17 Sub-classes, 1 commands."""
		if not hasattr(self, '_setup'):
			from .Setup import SetupCls
			self._setup = SetupCls(self._core, self._cmd_group)
		return self._setup

	@property
	def scount(self):
		"""scount commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_scount'):
			from .Scount import ScountCls
			self._scount = ScountCls(self._core, self._cmd_group)
		return self._scount

	@property
	def results(self):
		"""results commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_results'):
			from .Results import ResultsCls
			self._results = ResultsCls(self._core, self._cmd_group)
		return self._results

	def clone(self) -> 'SegmentCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SegmentCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
