from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BhRateCls:
	"""BhRate commands group definition. 71 total commands, 7 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bhRate", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def trace(self):
		"""trace commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import TraceCls
			self._trace = TraceCls(self._core, self._cmd_group)
		return self._trace

	@property
	def pencoding(self):
		"""pencoding commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pencoding'):
			from .Pencoding import PencodingCls
			self._pencoding = PencodingCls(self._core, self._cmd_group)
		return self._pencoding

	@property
	def sgacp(self):
		"""sgacp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sgacp'):
			from .Sgacp import SgacpCls
			self._sgacp = SgacpCls(self._core, self._cmd_group)
		return self._sgacp

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
		"""SCPI: ABORt:BLUetooth:MEASurement<Instance>:BHRate \n
		Snippet: driver.bluetooth.measurement.bhRate.abort() \n
		No command help available \n
		"""
		self._core.io.write(f'ABORt:BLUetooth:MEASurement<Instance>:BHRate')

	def abort_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: ABORt:BLUetooth:MEASurement<Instance>:BHRate \n
		Snippet: driver.bluetooth.measurement.bhRate.abort_with_opc() \n
		No command help available \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCMPX_BluetoothMeas.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:BLUetooth:MEASurement<Instance>:BHRate', opc_timeout_ms)

	def stop(self) -> None:
		"""SCPI: STOP:BLUetooth:MEASurement<Instance>:BHRate \n
		Snippet: driver.bluetooth.measurement.bhRate.stop() \n
		No command help available \n
		"""
		self._core.io.write(f'STOP:BLUetooth:MEASurement<Instance>:BHRate')

	def stop_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: STOP:BLUetooth:MEASurement<Instance>:BHRate \n
		Snippet: driver.bluetooth.measurement.bhRate.stop_with_opc() \n
		No command help available \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCMPX_BluetoothMeas.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:BLUetooth:MEASurement<Instance>:BHRate', opc_timeout_ms)

	def initiate(self) -> None:
		"""SCPI: INITiate:BLUetooth:MEASurement<Instance>:BHRate \n
		Snippet: driver.bluetooth.measurement.bhRate.initiate() \n
		No command help available \n
		"""
		self._core.io.write(f'INITiate:BLUetooth:MEASurement<Instance>:BHRate')

	def initiate_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate:BLUetooth:MEASurement<Instance>:BHRate \n
		Snippet: driver.bluetooth.measurement.bhRate.initiate_with_opc() \n
		No command help available \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCMPX_BluetoothMeas.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:BLUetooth:MEASurement<Instance>:BHRate', opc_timeout_ms)

	def clone(self) -> 'BhRateCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BhRateCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
