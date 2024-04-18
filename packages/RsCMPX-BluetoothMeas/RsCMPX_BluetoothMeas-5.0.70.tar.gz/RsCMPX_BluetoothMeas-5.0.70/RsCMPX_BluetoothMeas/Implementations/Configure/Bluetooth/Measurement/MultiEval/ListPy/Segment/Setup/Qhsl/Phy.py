from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PhyCls:
	"""Phy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phy", core, parent)

	def set(self, le_phy_type: enums.LePhyType, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:QHSL:PHY \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.qhsl.phy.set(le_phy_type = enums.LePhyType.LE1M, segment = repcap.Segment.Default) \n
		No command help available \n
			:param le_phy_type: No help available
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
		"""
		param = Conversions.enum_scalar_to_str(le_phy_type, enums.LePhyType)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:QHSL:PHY {param}')

	# noinspection PyTypeChecker
	def get(self, segment=repcap.Segment.Default) -> enums.LePhyType:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:QHSL:PHY \n
		Snippet: value: enums.LePhyType = driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.qhsl.phy.get(segment = repcap.Segment.Default) \n
		No command help available \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: le_phy_type: No help available"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		response = self._core.io.query_str(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:QHSL:PHY?')
		return Conversions.str_to_scalar_enum(response, enums.LePhyType)
