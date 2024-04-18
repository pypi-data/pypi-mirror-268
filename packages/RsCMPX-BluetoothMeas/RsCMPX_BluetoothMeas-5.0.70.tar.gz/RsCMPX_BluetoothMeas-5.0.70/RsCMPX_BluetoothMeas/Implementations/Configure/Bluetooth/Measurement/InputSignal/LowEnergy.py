from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LowEnergyCls:
	"""LowEnergy commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lowEnergy", core, parent)

	def get_syn_word(self) -> str:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:LENergy:SYNWord \n
		Snippet: value: str = driver.configure.bluetooth.measurement.inputSignal.lowEnergy.get_syn_word() \n
		Specifies the synchronization word used during direct test mode. \n
			:return: synch_word: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:LENergy:SYNWord?')
		return trim_str_response(response)

	def set_syn_word(self, synch_word: str) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:LENergy:SYNWord \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.lowEnergy.set_syn_word(synch_word = rawAbc) \n
		Specifies the synchronization word used during direct test mode. \n
			:param synch_word: No help available
		"""
		param = Conversions.value_to_str(synch_word)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:LENergy:SYNWord {param}')

	# noinspection PyTypeChecker
	def get_phy(self) -> enums.LePhysicalType:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:LENergy:PHY \n
		Snippet: value: enums.LePhysicalType = driver.configure.bluetooth.measurement.inputSignal.lowEnergy.get_phy() \n
		Selects the physical layer used for LE measurements. \n
			:return: phy: LE1M: LE 1 Msymbol/s uncoded PHY LE2M: LE 2 Msymbol/s uncoded PHY LELR: LE 1 Msymbol/s long range (LE coded PHY)
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:LENergy:PHY?')
		return Conversions.str_to_scalar_enum(response, enums.LePhysicalType)

	def set_phy(self, phy: enums.LePhysicalType) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:LENergy:PHY \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.lowEnergy.set_phy(phy = enums.LePhysicalType.LE1M) \n
		Selects the physical layer used for LE measurements. \n
			:param phy: LE1M: LE 1 Msymbol/s uncoded PHY LE2M: LE 2 Msymbol/s uncoded PHY LELR: LE 1 Msymbol/s long range (LE coded PHY)
		"""
		param = Conversions.enum_scalar_to_str(phy, enums.LePhysicalType)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:LENergy:PHY {param}')
