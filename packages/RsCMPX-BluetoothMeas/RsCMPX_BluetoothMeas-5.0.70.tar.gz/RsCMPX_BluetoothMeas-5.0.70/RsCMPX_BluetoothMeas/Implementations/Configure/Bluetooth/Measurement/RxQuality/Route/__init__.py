from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RouteCls:
	"""Route commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("route", core, parent)

	@property
	def usage(self):
		"""usage commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_usage'):
			from .Usage import UsageCls
			self._usage = UsageCls(self._core, self._cmd_group)
		return self._usage

	def set(self, tx_connector: enums.TxConnector, rf_converter: enums.TxConverter) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:ROUTe \n
		Snippet: driver.configure.bluetooth.measurement.rxQuality.route.set(tx_connector = enums.TxConnector.I12O, rf_converter = enums.TxConverter.ITX1) \n
		No command help available \n
			:param tx_connector: No help available
			:param rf_converter: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('tx_connector', tx_connector, DataType.Enum, enums.TxConnector), ArgSingle('rf_converter', rf_converter, DataType.Enum, enums.TxConverter))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:ROUTe {param}'.rstrip())

	# noinspection PyTypeChecker
	class RouteStruct(StructBase):
		"""Response structure. Fields: \n
			- Tx_Connector: enums.TxConnector: No parameter help available
			- Rf_Converter: enums.TxConverter: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Rf_Converter', enums.TxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Tx_Connector: enums.TxConnector = None
			self.Rf_Converter: enums.TxConverter = None

	def get(self) -> RouteStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:ROUTe \n
		Snippet: value: RouteStruct = driver.configure.bluetooth.measurement.rxQuality.route.get() \n
		No command help available \n
			:return: structure: for return value, see the help for RouteStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:ROUTe?', self.__class__.RouteStruct())

	def clone(self) -> 'RouteCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RouteCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
