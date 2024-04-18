from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerVsTimeCls:
	"""PowerVsTime commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("powerVsTime", core, parent)

	def set(self, nom_pow_lower: float, nom_pow_upper: float, peak_pow_upper: float, nom_pow_enabled: List[bool], peak_pow_enabled: List[bool]) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:PVTime \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.limit.brate.powerVsTime.set(nom_pow_lower = 1.0, nom_pow_upper = 1.0, peak_pow_upper = 1.0, nom_pow_enabled = [True, False, True], peak_pow_enabled = [True, False, True]) \n
		Defines the power limits for BR: lower and upper average power limits, upper peak power limit, limit check enabling. \n
			:param nom_pow_lower: No help available
			:param nom_pow_upper: No help available
			:param peak_pow_upper: No help available
			:param nom_pow_enabled: Disables or enables the limit check for the average power, 4 values, corresponding to the current, average, maximum and minimum results.
			:param peak_pow_enabled: Disables or enables the limit check for the peak power, 4 values, corresponding to the current, average, maximum and minimum results.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('nom_pow_lower', nom_pow_lower, DataType.Float), ArgSingle('nom_pow_upper', nom_pow_upper, DataType.Float), ArgSingle('peak_pow_upper', peak_pow_upper, DataType.Float), ArgSingle('nom_pow_enabled', nom_pow_enabled, DataType.BooleanList, None, False, False, 4), ArgSingle('peak_pow_enabled', peak_pow_enabled, DataType.BooleanList, None, False, False, 4))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:PVTime {param}'.rstrip())

	# noinspection PyTypeChecker
	class PowerVsTimeStruct(StructBase):
		"""Response structure. Fields: \n
			- Nom_Pow_Lower: float: No parameter help available
			- Nom_Pow_Upper: float: No parameter help available
			- Peak_Pow_Upper: float: No parameter help available
			- Nom_Pow_Enabled: List[bool]: Disables or enables the limit check for the average power, 4 values, corresponding to the current, average, maximum and minimum results.
			- Peak_Pow_Enabled: List[bool]: Disables or enables the limit check for the peak power, 4 values, corresponding to the current, average, maximum and minimum results."""
		__meta_args_list = [
			ArgStruct.scalar_float('Nom_Pow_Lower'),
			ArgStruct.scalar_float('Nom_Pow_Upper'),
			ArgStruct.scalar_float('Peak_Pow_Upper'),
			ArgStruct('Nom_Pow_Enabled', DataType.BooleanList, None, False, False, 4),
			ArgStruct('Peak_Pow_Enabled', DataType.BooleanList, None, False, False, 4)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Nom_Pow_Lower: float = None
			self.Nom_Pow_Upper: float = None
			self.Peak_Pow_Upper: float = None
			self.Nom_Pow_Enabled: List[bool] = None
			self.Peak_Pow_Enabled: List[bool] = None

	def get(self) -> PowerVsTimeStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:PVTime \n
		Snippet: value: PowerVsTimeStruct = driver.configure.bluetooth.measurement.multiEval.limit.brate.powerVsTime.get() \n
		Defines the power limits for BR: lower and upper average power limits, upper peak power limit, limit check enabling. \n
			:return: structure: for return value, see the help for PowerVsTimeStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:PVTime?', self.__class__.PowerVsTimeStruct())
