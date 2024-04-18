from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FdriftCls:
	"""Fdrift commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fdrift", core, parent)

	def set(self, frequency_drift: float, max_drift_rate: float, freq_drift_enable: List[bool], max_drift_rate_enb: List[bool]) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:FDRift \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.limit.brate.fdrift.set(frequency_drift = 1.0, max_drift_rate = 1.0, freq_drift_enable = [True, False, True], max_drift_rate_enb = [True, False, True]) \n
		Defines the frequency drift limit for DH1 packets and the maximum drift rate limit for all BR packets. Since V2.1.
		20, this command is superseded by the command method RsCMPX_BluetoothMeas.Configure.Bluetooth.Measurement.MultiEval.Limit.
		Brate.Fdrift.apackets that allows to set different limits for different packet types. \n
			:param frequency_drift: No help available
			:param max_drift_rate: No help available
			:param freq_drift_enable: Disable or enable limit check for current, average, and maximum results (3 values) .
			:param max_drift_rate_enb: Disable or enable limit check for current, average, and maximum results (3 values) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('frequency_drift', frequency_drift, DataType.Float), ArgSingle('max_drift_rate', max_drift_rate, DataType.Float), ArgSingle('freq_drift_enable', freq_drift_enable, DataType.BooleanList, None, False, False, 3), ArgSingle('max_drift_rate_enb', max_drift_rate_enb, DataType.BooleanList, None, False, False, 3))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:FDRift {param}'.rstrip())

	# noinspection PyTypeChecker
	class FdriftStruct(StructBase):
		"""Response structure. Fields: \n
			- Frequency_Drift: float: No parameter help available
			- Max_Drift_Rate: float: No parameter help available
			- Freq_Drift_Enable: List[bool]: Disable or enable limit check for current, average, and maximum results (3 values) .
			- Max_Drift_Rate_Enb: List[bool]: Disable or enable limit check for current, average, and maximum results (3 values) ."""
		__meta_args_list = [
			ArgStruct.scalar_float('Frequency_Drift'),
			ArgStruct.scalar_float('Max_Drift_Rate'),
			ArgStruct('Freq_Drift_Enable', DataType.BooleanList, None, False, False, 3),
			ArgStruct('Max_Drift_Rate_Enb', DataType.BooleanList, None, False, False, 3)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Frequency_Drift: float = None
			self.Max_Drift_Rate: float = None
			self.Freq_Drift_Enable: List[bool] = None
			self.Max_Drift_Rate_Enb: List[bool] = None

	def get(self) -> FdriftStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:FDRift \n
		Snippet: value: FdriftStruct = driver.configure.bluetooth.measurement.multiEval.limit.brate.fdrift.get() \n
		Defines the frequency drift limit for DH1 packets and the maximum drift rate limit for all BR packets. Since V2.1.
		20, this command is superseded by the command method RsCMPX_BluetoothMeas.Configure.Bluetooth.Measurement.MultiEval.Limit.
		Brate.Fdrift.apackets that allows to set different limits for different packet types. \n
			:return: structure: for return value, see the help for FdriftStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:FDRift?', self.__class__.FdriftStruct())

	# noinspection PyTypeChecker
	class ApacketsStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Freq_Drift_Dh_1: float: No parameter help available
			- Freq_Drift_Dh_3: float: No parameter help available
			- Freq_Drift_Dh_5: float: No parameter help available
			- Max_Drift_Rate: float: No parameter help available
			- Freq_Drift_Dh_1_Enb: List[bool]: Disable or enable limit check for current, average, and maximum results (3 values) .
			- Freq_Drift_Dh_3_Enb: List[bool]: Disable or enable limit check for current, average, and maximum results (3 values) .
			- Freq_Drift_Dh_5_Enb: List[bool]: Disable or enable limit check for current, average, and maximum results (3 values) .
			- Max_Drift_Rate_Enb: List[bool]: Disable or enable limit check for current, average, and maximum results (3 values) ."""
		__meta_args_list = [
			ArgStruct.scalar_float('Freq_Drift_Dh_1'),
			ArgStruct.scalar_float('Freq_Drift_Dh_3'),
			ArgStruct.scalar_float('Freq_Drift_Dh_5'),
			ArgStruct.scalar_float('Max_Drift_Rate'),
			ArgStruct('Freq_Drift_Dh_1_Enb', DataType.BooleanList, None, False, False, 3),
			ArgStruct('Freq_Drift_Dh_3_Enb', DataType.BooleanList, None, False, False, 3),
			ArgStruct('Freq_Drift_Dh_5_Enb', DataType.BooleanList, None, False, False, 3),
			ArgStruct('Max_Drift_Rate_Enb', DataType.BooleanList, None, False, False, 3)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Freq_Drift_Dh_1: float = None
			self.Freq_Drift_Dh_3: float = None
			self.Freq_Drift_Dh_5: float = None
			self.Max_Drift_Rate: float = None
			self.Freq_Drift_Dh_1_Enb: List[bool] = None
			self.Freq_Drift_Dh_3_Enb: List[bool] = None
			self.Freq_Drift_Dh_5_Enb: List[bool] = None
			self.Max_Drift_Rate_Enb: List[bool] = None

	def get_apackets(self) -> ApacketsStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:FDRift:APACkets \n
		Snippet: value: ApacketsStruct = driver.configure.bluetooth.measurement.multiEval.limit.brate.fdrift.get_apackets() \n
		Defines the limits for the frequency drift and the maximum drift rate for BR. For each packet type (DH1, DH3, DH5) a
		different frequency drift limit can be specified. \n
			:return: structure: for return value, see the help for ApacketsStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:FDRift:APACkets?', self.__class__.ApacketsStruct())

	def set_apackets(self, value: ApacketsStruct) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:FDRift:APACkets \n
		Snippet with structure: \n
		structure = driver.configure.bluetooth.measurement.multiEval.limit.brate.fdrift.ApacketsStruct() \n
		structure.Freq_Drift_Dh_1: float = 1.0 \n
		structure.Freq_Drift_Dh_3: float = 1.0 \n
		structure.Freq_Drift_Dh_5: float = 1.0 \n
		structure.Max_Drift_Rate: float = 1.0 \n
		structure.Freq_Drift_Dh_1_Enb: List[bool] = [True, False, True] \n
		structure.Freq_Drift_Dh_3_Enb: List[bool] = [True, False, True] \n
		structure.Freq_Drift_Dh_5_Enb: List[bool] = [True, False, True] \n
		structure.Max_Drift_Rate_Enb: List[bool] = [True, False, True] \n
		driver.configure.bluetooth.measurement.multiEval.limit.brate.fdrift.set_apackets(value = structure) \n
		Defines the limits for the frequency drift and the maximum drift rate for BR. For each packet type (DH1, DH3, DH5) a
		different frequency drift limit can be specified. \n
			:param value: see the help for ApacketsStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:BRATe:FDRift:APACkets', value)
