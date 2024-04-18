from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RdevicesCls:
	"""Rdevices commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rdevices", core, parent)

	def set(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CALL:BLUetooth:MEASurement<Instance>:DTMode:LENergy:RDEVices \n
		Snippet: driver.call.bluetooth.measurement.dtMode.lowEnergy.rdevices.set() \n
		No command help available \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALL:BLUetooth:MEASurement<Instance>:DTMode:LENergy:RDEVices', opc_timeout_ms)
