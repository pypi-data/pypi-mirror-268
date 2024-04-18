from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Le1MCls:
	"""Le1M commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("le1M", core, parent)

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.CtePacketType:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:CTE:LENergy:LE1M:TYPE \n
		Snippet: value: enums.CtePacketType = driver.configure.bluetooth.measurement.inputSignal.cte.lowEnergy.le1M.get_type_py() \n
		Specifies the CTE slot type for LE with CTE. Commands for uncoded LE 1M PHY (..:LE1M..) and LE 2M PHY (..:LE2M..
		) are available. \n
			:return: cte_type: AOD1us, AOD2us: CTE type angle of departure, 1 µs or 2 µs slot AOAus, AOA2us: CTE type angle of arrival, 2 µs slot AOA1us: CTE type angle of arrival, 1 µs slot
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:CTE:LENergy:LE1M:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.CtePacketType)

	def set_type_py(self, cte_type: enums.CtePacketType) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:CTE:LENergy:LE1M:TYPE \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.cte.lowEnergy.le1M.set_type_py(cte_type = enums.CtePacketType.AOA1us) \n
		Specifies the CTE slot type for LE with CTE. Commands for uncoded LE 1M PHY (..:LE1M..) and LE 2M PHY (..:LE2M..
		) are available. \n
			:param cte_type: AOD1us, AOD2us: CTE type angle of departure, 1 µs or 2 µs slot AOAus, AOA2us: CTE type angle of arrival, 2 µs slot AOA1us: CTE type angle of arrival, 1 µs slot
		"""
		param = Conversions.enum_scalar_to_str(cte_type, enums.CtePacketType)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:CTE:LENergy:LE1M:TYPE {param}')

	def get_units(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:CTE:LENergy:LE1M:UNITs \n
		Snippet: value: int = driver.configure.bluetooth.measurement.inputSignal.cte.lowEnergy.le1M.get_units() \n
		Specifies the number of CTE units for LE with CTE. Commands for uncoded LE 1M PHY (..:LE1M..) and LE 2M PHY (..:LE2M..
		) are available. \n
			:return: cte_units: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:CTE:LENergy:LE1M:UNITs?')
		return Conversions.str_to_int(response)

	def set_units(self, cte_units: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:CTE:LENergy:LE1M:UNITs \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.cte.lowEnergy.le1M.set_units(cte_units = 1) \n
		Specifies the number of CTE units for LE with CTE. Commands for uncoded LE 1M PHY (..:LE1M..) and LE 2M PHY (..:LE2M..
		) are available. \n
			:param cte_units: No help available
		"""
		param = Conversions.decimal_value_to_str(cte_units)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:CTE:LENergy:LE1M:UNITs {param}')
