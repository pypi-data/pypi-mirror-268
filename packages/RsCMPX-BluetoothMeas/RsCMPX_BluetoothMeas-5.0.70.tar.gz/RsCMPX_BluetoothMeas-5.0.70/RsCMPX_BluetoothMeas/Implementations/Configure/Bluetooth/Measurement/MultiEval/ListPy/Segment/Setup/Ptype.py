from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PtypeCls:
	"""Ptype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ptype", core, parent)

	def set(self, packet_type: enums.SegmentPacketType, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:PTYPe \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.ptype.set(packet_type = enums.SegmentPacketType.ADVertiser, segment = repcap.Segment.Default) \n
		Specifies the packet type expected in the segment. \n
			:param packet_type: DH1, DH3, DH5: BR packet E21P, E23P, E25P, E31P, E33P, E35P: 2-DH1, 2-DH3, 2-DH5, 3-DH1, 3-DH3, 3-DH5 EDR packet RFPHytest: LE test packet ADVertiser: LE advertiser RFCTe: LE with CTE test packet
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
		"""
		param = Conversions.enum_scalar_to_str(packet_type, enums.SegmentPacketType)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:PTYPe {param}')

	# noinspection PyTypeChecker
	def get(self, segment=repcap.Segment.Default) -> enums.SegmentPacketType:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:PTYPe \n
		Snippet: value: enums.SegmentPacketType = driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.ptype.get(segment = repcap.Segment.Default) \n
		Specifies the packet type expected in the segment. \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: packet_type: DH1, DH3, DH5: BR packet E21P, E23P, E25P, E31P, E33P, E35P: 2-DH1, 2-DH3, 2-DH5, 3-DH1, 3-DH3, 3-DH5 EDR packet RFPHytest: LE test packet ADVertiser: LE advertiser RFCTe: LE with CTE test packet"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		response = self._core.io.query_str(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:PTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.SegmentPacketType)
