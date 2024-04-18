from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MscalarCls:
	"""Mscalar commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mscalar", core, parent)

	def set(self, enable_mod_scalar: bool, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:RESults:MSCalar \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.listPy.segment.results.mscalar.set(enable_mod_scalar = False, segment = repcap.Segment.Default) \n
		Enables or disables the evaluation of results for the segment<no> in list mode. The last mnemonic denotes the measurement
		type: statistical modulation results, statistical power results, spectrum ACP (BR, LE) , spectrum gated ACP (EDR) ,
		spectrum 20 dB bandwidth (BR) . \n
			:param enable_mod_scalar: No help available
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
		"""
		param = Conversions.bool_to_str(enable_mod_scalar)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:RESults:MSCalar {param}')

	def get(self, segment=repcap.Segment.Default) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:RESults:MSCalar \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.multiEval.listPy.segment.results.mscalar.get(segment = repcap.Segment.Default) \n
		Enables or disables the evaluation of results for the segment<no> in list mode. The last mnemonic denotes the measurement
		type: statistical modulation results, statistical power results, spectrum ACP (BR, LE) , spectrum gated ACP (EDR) ,
		spectrum 20 dB bandwidth (BR) . \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: enable_mod_scalar: No help available"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		response = self._core.io.query_str(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:RESults:MSCalar?')
		return Conversions.str_to_bool(response)
