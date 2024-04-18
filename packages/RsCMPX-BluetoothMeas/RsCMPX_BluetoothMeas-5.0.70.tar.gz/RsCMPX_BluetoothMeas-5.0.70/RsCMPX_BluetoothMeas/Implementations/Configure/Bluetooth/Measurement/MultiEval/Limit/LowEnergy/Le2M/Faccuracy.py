from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FaccuracyCls:
	"""Faccuracy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("faccuracy", core, parent)

	def set(self, freq_accuracy: float, freq_acc_enabled: List[bool]) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy:LE2M:FACCuracy \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.limit.lowEnergy.le2M.faccuracy.set(freq_accuracy = 1.0, freq_acc_enabled = [True, False, True]) \n
		Defines the limit for the frequency accuracy. Commands for uncoded LE 1M PHY (..:LE1M..) , LE 2M PHY (..:LE2M..) , and LE
		coded PHY (..:LRANge..) are available. \n
			:param freq_accuracy: No help available
			:param freq_acc_enabled: Disable or enable limit check for current, average, and maximum results (3 values) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('freq_accuracy', freq_accuracy, DataType.Float), ArgSingle('freq_acc_enabled', freq_acc_enabled, DataType.BooleanList, None, False, False, 3))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy:LE2M:FACCuracy {param}'.rstrip())

	# noinspection PyTypeChecker
	class FaccuracyStruct(StructBase):
		"""Response structure. Fields: \n
			- Freq_Accuracy: float: No parameter help available
			- Freq_Acc_Enabled: List[bool]: Disable or enable limit check for current, average, and maximum results (3 values) ."""
		__meta_args_list = [
			ArgStruct.scalar_float('Freq_Accuracy'),
			ArgStruct('Freq_Acc_Enabled', DataType.BooleanList, None, False, False, 3)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Freq_Accuracy: float = None
			self.Freq_Acc_Enabled: List[bool] = None

	def get(self) -> FaccuracyStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy:LE2M:FACCuracy \n
		Snippet: value: FaccuracyStruct = driver.configure.bluetooth.measurement.multiEval.limit.lowEnergy.le2M.faccuracy.get() \n
		Defines the limit for the frequency accuracy. Commands for uncoded LE 1M PHY (..:LE1M..) , LE 2M PHY (..:LE2M..) , and LE
		coded PHY (..:LRANge..) are available. \n
			:return: structure: for return value, see the help for FaccuracyStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy:LE2M:FACCuracy?', self.__class__.FaccuracyStruct())
