from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RxQualityCls:
	"""RxQuality commands group definition. 10 total commands, 5 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rxQuality", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def sensitivity(self):
		"""sensitivity commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sensitivity'):
			from .Sensitivity import SensitivityCls
			self._sensitivity = SensitivityCls(self._core, self._cmd_group)
		return self._sensitivity

	@property
	def spotCheck(self):
		"""spotCheck commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spotCheck'):
			from .SpotCheck import SpotCheckCls
			self._spotCheck = SpotCheckCls(self._core, self._cmd_group)
		return self._spotCheck

	@property
	def per(self):
		"""per commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_per'):
			from .Per import PerCls
			self._per = PerCls(self._core, self._cmd_group)
		return self._per

	@property
	def adetected(self):
		"""adetected commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_adetected'):
			from .Adetected import AdetectedCls
			self._adetected = AdetectedCls(self._core, self._cmd_group)
		return self._adetected

	def initiate(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate:BLUetooth:MEASurement<Instance>:RXQuality \n
		Snippet: driver.bluetooth.measurement.rxQuality.initiate() \n
		No command help available \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:BLUetooth:MEASurement<Instance>:RXQuality', opc_timeout_ms)

	def stop(self) -> None:
		"""SCPI: STOP:BLUetooth:MEASurement<Instance>:RXQuality \n
		Snippet: driver.bluetooth.measurement.rxQuality.stop() \n
		No command help available \n
		"""
		self._core.io.write(f'STOP:BLUetooth:MEASurement<Instance>:RXQuality')

	def stop_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: STOP:BLUetooth:MEASurement<Instance>:RXQuality \n
		Snippet: driver.bluetooth.measurement.rxQuality.stop_with_opc() \n
		No command help available \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCMPX_BluetoothMeas.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:BLUetooth:MEASurement<Instance>:RXQuality', opc_timeout_ms)

	def abort(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: ABORt:BLUetooth:MEASurement<Instance>:RXQuality \n
		Snippet: driver.bluetooth.measurement.rxQuality.abort() \n
		No command help available \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:BLUetooth:MEASurement<Instance>:RXQuality', opc_timeout_ms)

	def clone(self) -> 'RxQualityCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RxQualityCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
