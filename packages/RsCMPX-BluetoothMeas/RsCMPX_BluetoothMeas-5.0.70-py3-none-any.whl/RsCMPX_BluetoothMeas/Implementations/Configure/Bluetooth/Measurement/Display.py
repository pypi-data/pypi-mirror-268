from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DisplayCls:
	"""Display commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("display", core, parent)

	def set(self, measurement: enums.DisplayMeasurement, view: enums.DisplayView = None) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DISPlay \n
		Snippet: driver.configure.bluetooth.measurement.display.set(measurement = enums.DisplayMeasurement.MEV, view = enums.DisplayView.DEVM) \n
		No command help available \n
			:param measurement: No help available
			:param view: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('measurement', measurement, DataType.Enum, enums.DisplayMeasurement), ArgSingle('view', view, DataType.Enum, enums.DisplayView, is_optional=True))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:DISPlay {param}'.rstrip())

	# noinspection PyTypeChecker
	class DisplayStruct(StructBase):
		"""Response structure. Fields: \n
			- Measurement: enums.DisplayMeasurement: No parameter help available
			- View: enums.DisplayView: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Measurement', enums.DisplayMeasurement),
			ArgStruct.scalar_enum('View', enums.DisplayView)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Measurement: enums.DisplayMeasurement = None
			self.View: enums.DisplayView = None

	def get(self) -> DisplayStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DISPlay \n
		Snippet: value: DisplayStruct = driver.configure.bluetooth.measurement.display.get() \n
		No command help available \n
			:return: structure: for return value, see the help for DisplayStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:DISPlay?', self.__class__.DisplayStruct())
