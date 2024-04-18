from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrangeCls:
	"""Frange commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frange", core, parent)

	def set(self, flx_lower: float, fhx_upper: float, flx_lower_enable: bool, fhx_upper_enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:FRANge \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.limit.frange.set(flx_lower = 1.0, fhx_upper = 1.0, flx_lower_enable = False, fhx_upper_enable = False) \n
		Defines the limit for the frequency range measurement. \n
			:param flx_lower: Lower limit for the lowest frequency fL relative to center frequency
			:param fhx_upper: Upper limit for the highest frequency fH relative to center frequency
			:param flx_lower_enable: Disable or enable limit check for the lowest frequency fL
			:param fhx_upper_enable: Disable or enable limit check for the highest frequency fH
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('flx_lower', flx_lower, DataType.Float), ArgSingle('fhx_upper', fhx_upper, DataType.Float), ArgSingle('flx_lower_enable', flx_lower_enable, DataType.Boolean), ArgSingle('fhx_upper_enable', fhx_upper_enable, DataType.Boolean))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:FRANge {param}'.rstrip())

	# noinspection PyTypeChecker
	class FrangeStruct(StructBase):
		"""Response structure. Fields: \n
			- Flx_Lower: float: Lower limit for the lowest frequency fL relative to center frequency
			- Fhx_Upper: float: Upper limit for the highest frequency fH relative to center frequency
			- Flx_Lower_Enable: bool: Disable or enable limit check for the lowest frequency fL
			- Fhx_Upper_Enable: bool: Disable or enable limit check for the highest frequency fH"""
		__meta_args_list = [
			ArgStruct.scalar_float('Flx_Lower'),
			ArgStruct.scalar_float('Fhx_Upper'),
			ArgStruct.scalar_bool('Flx_Lower_Enable'),
			ArgStruct.scalar_bool('Fhx_Upper_Enable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Flx_Lower: float = None
			self.Fhx_Upper: float = None
			self.Flx_Lower_Enable: bool = None
			self.Fhx_Upper_Enable: bool = None

	def get(self) -> FrangeStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:FRANge \n
		Snippet: value: FrangeStruct = driver.configure.bluetooth.measurement.multiEval.limit.frange.get() \n
		Defines the limit for the frequency range measurement. \n
			:return: structure: for return value, see the help for FrangeStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:FRANge?', self.__class__.FrangeStruct())
