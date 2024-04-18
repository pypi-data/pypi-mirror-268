from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnvelopePowerCls:
	"""EnvelopePower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("envelopePower", core, parent)

	def set(self, level: float, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:ENPower \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.envelopePower.set(level = 1.0, segment = repcap.Segment.Default) \n
		Specifies the expected nominal power in the segment. The range of the expected nominal power can be calculated as
		follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin \n
			:param level: The input power range is stated in the specifications document.
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
		"""
		param = Conversions.decimal_value_to_str(level)
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:ENPower {param}')

	def get(self, segment=repcap.Segment.Default) -> float:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:SETup]:ENPower \n
		Snippet: value: float = driver.configure.bluetooth.measurement.multiEval.listPy.segment.setup.envelopePower.get(segment = repcap.Segment.Default) \n
		Specifies the expected nominal power in the segment. The range of the expected nominal power can be calculated as
		follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: level: The input power range is stated in the specifications document."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		response = self._core.io.query_str(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup:ENPower?')
		return Conversions.str_to_float(response)
