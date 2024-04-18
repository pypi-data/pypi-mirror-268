from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPyCls:
	"""FilterPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("filterPy", core, parent)

	def set(self, meas_filter: enums.FilterWidth, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:FILTer \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.filterPy.set(meas_filter = enums.FilterWidth.NARRow, segment = repcap.Segment.Default) \n
		Specifies the measurement filter bandwidth for the segment. \n
			:param meas_filter: NARRow: Narrowband filter WIDE: Wideband filter
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
		"""
		param = Conversions.enum_scalar_to_str(meas_filter, enums.FilterWidth)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:FILTer {param}')

	# noinspection PyTypeChecker
	def get(self, segment=repcap.Segment.Default) -> enums.FilterWidth:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:FILTer \n
		Snippet: value: enums.FilterWidth = driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.filterPy.get(segment = repcap.Segment.Default) \n
		Specifies the measurement filter bandwidth for the segment. \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: meas_filter: NARRow: Narrowband filter WIDE: Wideband filter"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		response = self._core.io.query_str(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:FILTer?')
		return Conversions.str_to_scalar_enum(response, enums.FilterWidth)
