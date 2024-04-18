from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PhyCls:
	"""Phy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phy", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.DetectedPhyType:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:ISIGnal:ADETected:QHSL:PHY \n
		Snippet: value: enums.DetectedPhyType = driver.bluetooth.measurement.inputSignal.adetected.qhsl.phy.fetch() \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:return: detected_phy_type: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:BLUetooth:MEASurement<Instance>:ISIGnal:ADETected:QHSL:PHY?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.DetectedPhyType)
