from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BrateCls:
	"""Brate commands group definition. 9 total commands, 5 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("brate", core, parent)

	@property
	def powerVsTime(self):
		"""powerVsTime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_powerVsTime'):
			from .PowerVsTime import PowerVsTimeCls
			self._powerVsTime = PowerVsTimeCls(self._core, self._cmd_group)
		return self._powerVsTime

	@property
	def mratio(self):
		"""mratio commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mratio'):
			from .Mratio import MratioCls
			self._mratio = MratioCls(self._core, self._cmd_group)
		return self._mratio

	@property
	def delta(self):
		"""delta commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_delta'):
			from .Delta import DeltaCls
			self._delta = DeltaCls(self._core, self._cmd_group)
		return self._delta

	@property
	def fdrift(self):
		"""fdrift commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_fdrift'):
			from .Fdrift import FdriftCls
			self._fdrift = FdriftCls(self._core, self._cmd_group)
		return self._fdrift

	@property
	def faccuracy(self):
		"""faccuracy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_faccuracy'):
			from .Faccuracy import FaccuracyCls
			self._faccuracy = FaccuracyCls(self._core, self._cmd_group)
		return self._faccuracy

	# noinspection PyTypeChecker
	class DaverageStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Freq_Dev_F_1_Lower: float: No parameter help available
			- Freq_Dev_F_1_Upper: float: No parameter help available
			- Freq_Dev_F_2_Lower: float: No parameter help available
			- Freq_Dev_F_2_Upper: float: No parameter help available
			- Freq_Dev_F_1_Enable: List[bool]: Disable or enable limits for current, average, maximum, and minimum results (4 values) .
			- Freq_Dev_F_2_Enable: List[bool]: Disable or enable limits for current, average, maximum, and minimum results (4 values) ."""
		__meta_args_list = [
			ArgStruct.scalar_float('Freq_Dev_F_1_Lower'),
			ArgStruct.scalar_float('Freq_Dev_F_1_Upper'),
			ArgStruct.scalar_float('Freq_Dev_F_2_Lower'),
			ArgStruct.scalar_float('Freq_Dev_F_2_Upper'),
			ArgStruct('Freq_Dev_F_1_Enable', DataType.BooleanList, None, False, False, 4),
			ArgStruct('Freq_Dev_F_2_Enable', DataType.BooleanList, None, False, False, 4)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Freq_Dev_F_1_Lower: float = None
			self.Freq_Dev_F_1_Upper: float = None
			self.Freq_Dev_F_2_Lower: float = None
			self.Freq_Dev_F_2_Upper: float = None
			self.Freq_Dev_F_1_Enable: List[bool] = None
			self.Freq_Dev_F_2_Enable: List[bool] = None

	def get_daverage(self) -> DaverageStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:DAVerage \n
		Snippet: value: DaverageStruct = driver.configure.bluetooth.measurement.multiEval.limit.brate.get_daverage() \n
		Defines the lower and upper frequency deviation limits for BR bursts. The mnemonics DAVerage, DMAXimum, DMINimum
		distinguish average, maximum, and minimum frequency deviations. \n
			:return: structure: for return value, see the help for DaverageStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:DAVerage?', self.__class__.DaverageStruct())

	def set_daverage(self, value: DaverageStruct) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:DAVerage \n
		Snippet with structure: \n
		structure = driver.configure.bluetooth.measurement.multiEval.limit.brate.DaverageStruct() \n
		structure.Freq_Dev_F_1_Lower: float = 1.0 \n
		structure.Freq_Dev_F_1_Upper: float = 1.0 \n
		structure.Freq_Dev_F_2_Lower: float = 1.0 \n
		structure.Freq_Dev_F_2_Upper: float = 1.0 \n
		structure.Freq_Dev_F_1_Enable: List[bool] = [True, False, True] \n
		structure.Freq_Dev_F_2_Enable: List[bool] = [True, False, True] \n
		driver.configure.bluetooth.measurement.multiEval.limit.brate.set_daverage(value = structure) \n
		Defines the lower and upper frequency deviation limits for BR bursts. The mnemonics DAVerage, DMAXimum, DMINimum
		distinguish average, maximum, and minimum frequency deviations. \n
			:param value: see the help for DaverageStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:DAVerage', value)

	# noinspection PyTypeChecker
	class DminimumStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Freq_Dev_F_1_Lower: float: No parameter help available
			- Freq_Dev_F_1_Upper: float: No parameter help available
			- Freq_Dev_F_2_Lower: float: No parameter help available
			- Freq_Dev_F_2_Upper: float: No parameter help available
			- Freq_Dev_F_1_Enable: List[bool]: Disable or enable limits for current, average, maximum, and minimum results (4 values) .
			- Freq_Dev_F_2_Enable: List[bool]: Disable or enable limits for current, average, maximum, and minimum results (4 values) ."""
		__meta_args_list = [
			ArgStruct.scalar_float('Freq_Dev_F_1_Lower'),
			ArgStruct.scalar_float('Freq_Dev_F_1_Upper'),
			ArgStruct.scalar_float('Freq_Dev_F_2_Lower'),
			ArgStruct.scalar_float('Freq_Dev_F_2_Upper'),
			ArgStruct('Freq_Dev_F_1_Enable', DataType.BooleanList, None, False, False, 4),
			ArgStruct('Freq_Dev_F_2_Enable', DataType.BooleanList, None, False, False, 4)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Freq_Dev_F_1_Lower: float = None
			self.Freq_Dev_F_1_Upper: float = None
			self.Freq_Dev_F_2_Lower: float = None
			self.Freq_Dev_F_2_Upper: float = None
			self.Freq_Dev_F_1_Enable: List[bool] = None
			self.Freq_Dev_F_2_Enable: List[bool] = None

	def get_dminimum(self) -> DminimumStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:DMINimum \n
		Snippet: value: DminimumStruct = driver.configure.bluetooth.measurement.multiEval.limit.brate.get_dminimum() \n
		Defines the lower and upper frequency deviation limits for BR bursts. The mnemonics DAVerage, DMAXimum, DMINimum
		distinguish average, maximum, and minimum frequency deviations. \n
			:return: structure: for return value, see the help for DminimumStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:DMINimum?', self.__class__.DminimumStruct())

	def set_dminimum(self, value: DminimumStruct) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:DMINimum \n
		Snippet with structure: \n
		structure = driver.configure.bluetooth.measurement.multiEval.limit.brate.DminimumStruct() \n
		structure.Freq_Dev_F_1_Lower: float = 1.0 \n
		structure.Freq_Dev_F_1_Upper: float = 1.0 \n
		structure.Freq_Dev_F_2_Lower: float = 1.0 \n
		structure.Freq_Dev_F_2_Upper: float = 1.0 \n
		structure.Freq_Dev_F_1_Enable: List[bool] = [True, False, True] \n
		structure.Freq_Dev_F_2_Enable: List[bool] = [True, False, True] \n
		driver.configure.bluetooth.measurement.multiEval.limit.brate.set_dminimum(value = structure) \n
		Defines the lower and upper frequency deviation limits for BR bursts. The mnemonics DAVerage, DMAXimum, DMINimum
		distinguish average, maximum, and minimum frequency deviations. \n
			:param value: see the help for DminimumStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:DMINimum', value)

	# noinspection PyTypeChecker
	class DmaximumStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Freq_Dev_F_1_Lower: float: No parameter help available
			- Freq_Dev_F_1_Upper: float: No parameter help available
			- Freq_Dev_F_2_Lower: float: No parameter help available
			- Freq_Dev_F_2_Upper: float: No parameter help available
			- Freq_Dev_F_1_Enable: List[bool]: Disable or enable limits for current, average, maximum, and minimum results (4 values) .
			- Freq_Dev_F_2_Enable: List[bool]: Disable or enable limits for current, average, maximum, and minimum results (4 values) ."""
		__meta_args_list = [
			ArgStruct.scalar_float('Freq_Dev_F_1_Lower'),
			ArgStruct.scalar_float('Freq_Dev_F_1_Upper'),
			ArgStruct.scalar_float('Freq_Dev_F_2_Lower'),
			ArgStruct.scalar_float('Freq_Dev_F_2_Upper'),
			ArgStruct('Freq_Dev_F_1_Enable', DataType.BooleanList, None, False, False, 4),
			ArgStruct('Freq_Dev_F_2_Enable', DataType.BooleanList, None, False, False, 4)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Freq_Dev_F_1_Lower: float = None
			self.Freq_Dev_F_1_Upper: float = None
			self.Freq_Dev_F_2_Lower: float = None
			self.Freq_Dev_F_2_Upper: float = None
			self.Freq_Dev_F_1_Enable: List[bool] = None
			self.Freq_Dev_F_2_Enable: List[bool] = None

	def get_dmaximum(self) -> DmaximumStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:DMAXimum \n
		Snippet: value: DmaximumStruct = driver.configure.bluetooth.measurement.multiEval.limit.brate.get_dmaximum() \n
		Defines the lower and upper frequency deviation limits for BR bursts. The mnemonics DAVerage, DMAXimum, DMINimum
		distinguish average, maximum, and minimum frequency deviations. \n
			:return: structure: for return value, see the help for DmaximumStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:DMAXimum?', self.__class__.DmaximumStruct())

	def set_dmaximum(self, value: DmaximumStruct) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:DMAXimum \n
		Snippet with structure: \n
		structure = driver.configure.bluetooth.measurement.multiEval.limit.brate.DmaximumStruct() \n
		structure.Freq_Dev_F_1_Lower: float = 1.0 \n
		structure.Freq_Dev_F_1_Upper: float = 1.0 \n
		structure.Freq_Dev_F_2_Lower: float = 1.0 \n
		structure.Freq_Dev_F_2_Upper: float = 1.0 \n
		structure.Freq_Dev_F_1_Enable: List[bool] = [True, False, True] \n
		structure.Freq_Dev_F_2_Enable: List[bool] = [True, False, True] \n
		driver.configure.bluetooth.measurement.multiEval.limit.brate.set_dmaximum(value = structure) \n
		Defines the lower and upper frequency deviation limits for BR bursts. The mnemonics DAVerage, DMAXimum, DMINimum
		distinguish average, maximum, and minimum frequency deviations. \n
			:param value: see the help for DmaximumStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:DMAXimum', value)

	def clone(self) -> 'BrateCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BrateCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
