from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LowEnergyCls:
	"""LowEnergy commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lowEnergy", core, parent)

	@property
	def rdevices(self):
		"""rdevices commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rdevices'):
			from .Rdevices import RdevicesCls
			self._rdevices = RdevicesCls(self._core, self._cmd_group)
		return self._rdevices

	# noinspection PyTypeChecker
	def get_rresult(self) -> enums.Result:
		"""SCPI: CALL:BLUetooth:MEASurement<Instance>:DTMode:LENergy:RRESult \n
		Snippet: value: enums.Result = driver.call.bluetooth.measurement.dtMode.lowEnergy.get_rresult() \n
		No command help available \n
			:return: result: No help available
		"""
		response = self._core.io.query_str('CALL:BLUetooth:MEASurement<Instance>:DTMode:LENergy:RRESult?')
		return Conversions.str_to_scalar_enum(response, enums.Result)

	def reset(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CALL:BLUetooth:MEASurement<Instance>:DTMode:LENergy:RESet \n
		Snippet: driver.call.bluetooth.measurement.dtMode.lowEnergy.reset() \n
		No command help available \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALL:BLUetooth:MEASurement<Instance>:DTMode:LENergy:RESet', opc_timeout_ms)

	def clone(self) -> 'LowEnergyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LowEnergyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
