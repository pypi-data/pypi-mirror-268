from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	def fetch(self, timeout: float = None, target_main_state: enums.ResourceState = None, target_sync_state: enums.SyncState = None) -> enums.ResourceState:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SEARch:PER:STATe \n
		Snippet: value: enums.ResourceState = driver.bluetooth.measurement.dtMode.rxQuality.search.per.state.fetch(timeout = 1.0, target_main_state = enums.ResourceState.ACTive, target_sync_state = enums.SyncState.ADJusted) \n
		No command help available \n
			:param timeout: No help available
			:param target_main_state: No help available
			:param target_sync_state: No help available
			:return: meas_status: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('timeout', timeout, DataType.Float, None, is_optional=True), ArgSingle('target_main_state', target_main_state, DataType.Enum, enums.ResourceState, is_optional=True), ArgSingle('target_sync_state', target_sync_state, DataType.Enum, enums.SyncState, is_optional=True))
		response = self._core.io.query_str(f'FETCh:BLUetooth:MEASurement<Instance>:DTMode:RXQuality:SEARch:PER:STATe? {param}'.rstrip())
		return Conversions.str_to_scalar_enum(response, enums.ResourceState)
