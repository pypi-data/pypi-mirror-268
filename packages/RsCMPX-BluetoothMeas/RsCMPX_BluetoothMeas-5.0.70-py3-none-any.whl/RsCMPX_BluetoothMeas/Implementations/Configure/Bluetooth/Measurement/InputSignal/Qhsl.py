from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class QhslCls:
	"""Qhsl commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qhsl", core, parent)

	# noinspection PyTypeChecker
	def get_phy(self) -> enums.DetectedPhyType:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:QHSL:PHY \n
		Snippet: value: enums.DetectedPhyType = driver.configure.bluetooth.measurement.inputSignal.qhsl.get_phy() \n
		No command help available \n
			:return: phy: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:QHSL:PHY?')
		return Conversions.str_to_scalar_enum(response, enums.DetectedPhyType)

	def set_phy(self, phy: enums.DetectedPhyType) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:QHSL:PHY \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.qhsl.set_phy(phy = enums.DetectedPhyType.P2Q) \n
		No command help available \n
			:param phy: No help available
		"""
		param = Conversions.enum_scalar_to_str(phy, enums.DetectedPhyType)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:QHSL:PHY {param}')
