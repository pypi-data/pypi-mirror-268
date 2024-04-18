from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LrStartCls:
	"""LrStart commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lrStart", core, parent)

	def set(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:LRSTart \n
		Snippet: driver.configure.bluetooth.measurement.rfSettings.lrStart.set() \n
		Starts level adjustment. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:LRSTart', opc_timeout_ms)
