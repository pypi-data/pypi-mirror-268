from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HdrpCls:
	"""Hdrp commands group definition. 66 total commands, 6 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hdrp", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def trace(self):
		"""trace commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import TraceCls
			self._trace = TraceCls(self._core, self._cmd_group)
		return self._trace

	@property
	def sacp(self):
		"""sacp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sacp'):
			from .Sacp import SacpCls
			self._sacp = SacpCls(self._core, self._cmd_group)
		return self._sacp

	@property
	def powerVsTime(self):
		"""powerVsTime commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_powerVsTime'):
			from .PowerVsTime import PowerVsTimeCls
			self._powerVsTime = PowerVsTimeCls(self._core, self._cmd_group)
		return self._powerVsTime

	@property
	def modulation(self):
		"""modulation commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import ModulationCls
			self._modulation = ModulationCls(self._core, self._cmd_group)
		return self._modulation

	@property
	def inputSignal(self):
		"""inputSignal commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_inputSignal'):
			from .InputSignal import InputSignalCls
			self._inputSignal = InputSignalCls(self._core, self._cmd_group)
		return self._inputSignal

	def abort(self) -> None:
		"""SCPI: ABORt:BLUetooth:MEASurement<Instance>:HDRP \n
		Snippet: driver.bluetooth.measurement.hdrp.abort() \n
		No command help available \n
		"""
		self._core.io.write(f'ABORt:BLUetooth:MEASurement<Instance>:HDRP')

	def abort_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: ABORt:BLUetooth:MEASurement<Instance>:HDRP \n
		Snippet: driver.bluetooth.measurement.hdrp.abort_with_opc() \n
		No command help available \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCMPX_BluetoothMeas.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:BLUetooth:MEASurement<Instance>:HDRP', opc_timeout_ms)

	def stop(self) -> None:
		"""SCPI: STOP:BLUetooth:MEASurement<Instance>:HDRP \n
		Snippet: driver.bluetooth.measurement.hdrp.stop() \n
		No command help available \n
		"""
		self._core.io.write(f'STOP:BLUetooth:MEASurement<Instance>:HDRP')

	def stop_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: STOP:BLUetooth:MEASurement<Instance>:HDRP \n
		Snippet: driver.bluetooth.measurement.hdrp.stop_with_opc() \n
		No command help available \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCMPX_BluetoothMeas.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:BLUetooth:MEASurement<Instance>:HDRP', opc_timeout_ms)

	def initiate(self) -> None:
		"""SCPI: INITiate:BLUetooth:MEASurement<Instance>:HDRP \n
		Snippet: driver.bluetooth.measurement.hdrp.initiate() \n
		No command help available \n
		"""
		self._core.io.write(f'INITiate:BLUetooth:MEASurement<Instance>:HDRP')

	def initiate_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate:BLUetooth:MEASurement<Instance>:HDRP \n
		Snippet: driver.bluetooth.measurement.hdrp.initiate_with_opc() \n
		No command help available \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCMPX_BluetoothMeas.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:BLUetooth:MEASurement<Instance>:HDRP', opc_timeout_ms)

	def clone(self) -> 'HdrpCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HdrpCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
