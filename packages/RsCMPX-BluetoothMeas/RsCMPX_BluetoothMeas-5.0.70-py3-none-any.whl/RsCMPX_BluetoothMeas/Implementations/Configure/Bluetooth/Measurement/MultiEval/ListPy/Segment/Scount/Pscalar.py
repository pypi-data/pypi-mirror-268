from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PscalarCls:
	"""Pscalar commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pscalar", core, parent)

	def set(self, power_stat_count: int, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SCOunt:PSCalar \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.listPy.segment.scount.pscalar.set(power_stat_count = 1, segment = repcap.Segment.Default) \n
		Defines the statistic count in the segment. The last mnemonic denotes the measurement type: statistical modulation
		measurement, statistical power measurement, spectrum ACP measurement (BR, LE) , spectrum gated ACP measurement (EDR) ,
		spectrum 20 dB bandwidth (occupied bandwidth) measurement (BR) . \n
			:param power_stat_count: Statistic count
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
		"""
		param = Conversions.decimal_value_to_str(power_stat_count)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SCOunt:PSCalar {param}')

	def get(self, segment=repcap.Segment.Default) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SCOunt:PSCalar \n
		Snippet: value: int = driver.configure.bluetooth.measurement.multiEval.listPy.segment.scount.pscalar.get(segment = repcap.Segment.Default) \n
		Defines the statistic count in the segment. The last mnemonic denotes the measurement type: statistical modulation
		measurement, statistical power measurement, spectrum ACP measurement (BR, LE) , spectrum gated ACP measurement (EDR) ,
		spectrum 20 dB bandwidth (occupied bandwidth) measurement (BR) . \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: power_stat_count: Statistic count"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		response = self._core.io.query_str(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SCOunt:PSCalar?')
		return Conversions.str_to_int(response)
