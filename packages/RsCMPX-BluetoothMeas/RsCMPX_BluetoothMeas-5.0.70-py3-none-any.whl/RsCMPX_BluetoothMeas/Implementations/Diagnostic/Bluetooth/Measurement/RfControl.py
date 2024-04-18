from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfControlCls:
	"""RfControl commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfControl", core, parent)

	def get_tx_enable(self) -> bool:
		"""SCPI: DIAGnostic:BLUetooth:MEASurement<Instance>:RFControl:TXENable \n
		Snippet: value: bool = driver.diagnostic.bluetooth.measurement.rfControl.get_tx_enable() \n
		No command help available \n
			:return: set_ctrl_bit: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:BLUetooth:MEASurement<Instance>:RFControl:TXENable?')
		return Conversions.str_to_bool(response)

	def set_tx_enable(self, set_ctrl_bit: bool) -> None:
		"""SCPI: DIAGnostic:BLUetooth:MEASurement<Instance>:RFControl:TXENable \n
		Snippet: driver.diagnostic.bluetooth.measurement.rfControl.set_tx_enable(set_ctrl_bit = False) \n
		No command help available \n
			:param set_ctrl_bit: No help available
		"""
		param = Conversions.bool_to_str(set_ctrl_bit)
		self._core.io.write(f'DIAGnostic:BLUetooth:MEASurement<Instance>:RFControl:TXENable {param}')
