from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MeasurementCls:
	"""Measurement commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	def set(self, left_channel: int, right_channel: int, threshold: float) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:FRANge:BRATe:MEASurement \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.frange.brate.measurement.set(left_channel = 1, right_channel = 1, threshold = 1.0) \n
		Specifies the number of 1 MHz channels to be measured below and above the current measured channel. The threshold is the
		level that needs to be crossed to search the frequencies fL and fH. \n
			:param left_channel: Left adjacent channel relative to the EUT center TX channel
			:param right_channel: Right adjacent channel relative to the EUT center TX channel
			:param threshold: Threshold for the spectral power density drop to search the frequencies fL and fH Specification defines - 80 dBm/Hz for equivalent isotropically radiated power or - 30 dBm if measured in a 100 kHz bandwidth.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('left_channel', left_channel, DataType.Integer), ArgSingle('right_channel', right_channel, DataType.Integer), ArgSingle('threshold', threshold, DataType.Float))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:FRANge:BRATe:MEASurement {param}'.rstrip())

	# noinspection PyTypeChecker
	class MeasurementStruct(StructBase):
		"""Response structure. Fields: \n
			- Left_Channel: int: Left adjacent channel relative to the EUT center TX channel
			- Right_Channel: int: Right adjacent channel relative to the EUT center TX channel
			- Threshold: float: Threshold for the spectral power density drop to search the frequencies fL and fH Specification defines - 80 dBm/Hz for equivalent isotropically radiated power or - 30 dBm if measured in a 100 kHz bandwidth."""
		__meta_args_list = [
			ArgStruct.scalar_int('Left_Channel'),
			ArgStruct.scalar_int('Right_Channel'),
			ArgStruct.scalar_float('Threshold')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Left_Channel: int = None
			self.Right_Channel: int = None
			self.Threshold: float = None

	def get(self) -> MeasurementStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:FRANge:BRATe:MEASurement \n
		Snippet: value: MeasurementStruct = driver.configure.bluetooth.measurement.multiEval.frange.brate.measurement.get() \n
		Specifies the number of 1 MHz channels to be measured below and above the current measured channel. The threshold is the
		level that needs to be crossed to search the frequencies fL and fH. \n
			:return: structure: for return value, see the help for MeasurementStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:FRANge:BRATe:MEASurement?', self.__class__.MeasurementStruct())
