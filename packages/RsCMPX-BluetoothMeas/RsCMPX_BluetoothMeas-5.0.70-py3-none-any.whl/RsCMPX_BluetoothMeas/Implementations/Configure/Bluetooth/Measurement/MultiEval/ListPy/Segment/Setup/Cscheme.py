from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CschemeCls:
	"""Cscheme commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cscheme", core, parent)

	def set(self, le_lr_coding: enums.CodingScheme, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:CSCHeme \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.cscheme.set(le_lr_coding = enums.CodingScheme.S2, segment = repcap.Segment.Default) \n
		Defines coding scheme S for LE coded PHY according to the core specification version 5.0 for Bluetooth wireless
		technology. \n
			:param le_lr_coding: Coding S = 8 or S = 2
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
		"""
		param = Conversions.enum_scalar_to_str(le_lr_coding, enums.CodingScheme)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:CSCHeme {param}')

	# noinspection PyTypeChecker
	def get(self, segment=repcap.Segment.Default) -> enums.CodingScheme:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:CSCHeme \n
		Snippet: value: enums.CodingScheme = driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.cscheme.get(segment = repcap.Segment.Default) \n
		Defines coding scheme S for LE coded PHY according to the core specification version 5.0 for Bluetooth wireless
		technology. \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: le_lr_coding: Coding S = 8 or S = 2"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		response = self._core.io.query_str(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:CSCHeme?')
		return Conversions.str_to_scalar_enum(response, enums.CodingScheme)
