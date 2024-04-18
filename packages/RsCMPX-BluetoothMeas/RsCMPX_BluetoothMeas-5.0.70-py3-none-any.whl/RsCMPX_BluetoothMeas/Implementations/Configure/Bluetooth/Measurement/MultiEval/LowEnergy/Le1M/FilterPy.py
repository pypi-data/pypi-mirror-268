from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPyCls:
	"""FilterPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("filterPy", core, parent)

	# noinspection PyTypeChecker
	def get_bandwidth(self) -> enums.FilterWidth:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LENergy[:LE1M]:FILTer:BWIDth \n
		Snippet: value: enums.FilterWidth = driver.configure.bluetooth.measurement.multiEval.lowEnergy.le1M.filterPy.get_bandwidth() \n
		Selects the filter bandwidth. Commands for uncoded LE 1M PHY (..:LE1M..) , LE 2M PHY (..:LE2M..) , and LE coded PHY (..
		:LRANge..) are available. \n
			:return: filter_bandwidth: NARRow: Narrowband filter WIDE: Wideband filter
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LENergy:LE1M:FILTer:BWIDth?')
		return Conversions.str_to_scalar_enum(response, enums.FilterWidth)

	def set_bandwidth(self, filter_bandwidth: enums.FilterWidth) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LENergy[:LE1M]:FILTer:BWIDth \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.lowEnergy.le1M.filterPy.set_bandwidth(filter_bandwidth = enums.FilterWidth.NARRow) \n
		Selects the filter bandwidth. Commands for uncoded LE 1M PHY (..:LE1M..) , LE 2M PHY (..:LE2M..) , and LE coded PHY (..
		:LRANge..) are available. \n
			:param filter_bandwidth: NARRow: Narrowband filter WIDE: Wideband filter
		"""
		param = Conversions.enum_scalar_to_str(filter_bandwidth, enums.FilterWidth)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LENergy:LE1M:FILTer:BWIDth {param}')
