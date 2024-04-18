from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EloggingCls:
	"""Elogging commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("elogging", core, parent)

	def set(self) -> None:
		"""SCPI: CLEan:BLUetooth:MEASurement<Instance>:ELOGging \n
		Snippet: driver.clean.bluetooth.measurement.elogging.set() \n
		No command help available \n
		"""
		self._core.io.write(f'CLEan:BLUetooth:MEASurement<Instance>:ELOGging')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CLEan:BLUetooth:MEASurement<Instance>:ELOGging \n
		Snippet: driver.clean.bluetooth.measurement.elogging.set_with_opc() \n
		No command help available \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCMPX_BluetoothMeas.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CLEan:BLUetooth:MEASurement<Instance>:ELOGging', opc_timeout_ms)
