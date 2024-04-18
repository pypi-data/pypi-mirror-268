from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MeasurementCls:
	"""Measurement commands group definition. 903 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	@property
	def bhRate(self):
		"""bhRate commands group. 7 Sub-classes, 3 commands."""
		if not hasattr(self, '_bhRate'):
			from .BhRate import BhRateCls
			self._bhRate = BhRateCls(self._core, self._cmd_group)
		return self._bhRate

	@property
	def hdrp(self):
		"""hdrp commands group. 6 Sub-classes, 3 commands."""
		if not hasattr(self, '_hdrp'):
			from .Hdrp import HdrpCls
			self._hdrp = HdrpCls(self._core, self._cmd_group)
		return self._hdrp

	@property
	def hdr(self):
		"""hdr commands group. 7 Sub-classes, 3 commands."""
		if not hasattr(self, '_hdr'):
			from .Hdr import HdrCls
			self._hdr = HdrCls(self._core, self._cmd_group)
		return self._hdr

	@property
	def multiEval(self):
		"""multiEval commands group. 10 Sub-classes, 3 commands."""
		if not hasattr(self, '_multiEval'):
			from .MultiEval import MultiEvalCls
			self._multiEval = MultiEvalCls(self._core, self._cmd_group)
		return self._multiEval

	@property
	def inputSignal(self):
		"""inputSignal commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_inputSignal'):
			from .InputSignal import InputSignalCls
			self._inputSignal = InputSignalCls(self._core, self._cmd_group)
		return self._inputSignal

	@property
	def dtMode(self):
		"""dtMode commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dtMode'):
			from .DtMode import DtModeCls
			self._dtMode = DtModeCls(self._core, self._cmd_group)
		return self._dtMode

	@property
	def rxQuality(self):
		"""rxQuality commands group. 5 Sub-classes, 3 commands."""
		if not hasattr(self, '_rxQuality'):
			from .RxQuality import RxQualityCls
			self._rxQuality = RxQualityCls(self._core, self._cmd_group)
		return self._rxQuality

	@property
	def trx(self):
		"""trx commands group. 5 Sub-classes, 3 commands."""
		if not hasattr(self, '_trx'):
			from .Trx import TrxCls
			self._trx = TrxCls(self._core, self._cmd_group)
		return self._trx

	def clone(self) -> 'MeasurementCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MeasurementCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
