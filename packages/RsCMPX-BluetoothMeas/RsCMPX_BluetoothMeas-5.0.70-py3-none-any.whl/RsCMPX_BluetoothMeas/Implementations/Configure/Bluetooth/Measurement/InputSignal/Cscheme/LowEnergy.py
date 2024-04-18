from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LowEnergyCls:
	"""LowEnergy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lowEnergy", core, parent)

	# noinspection PyTypeChecker
	def get_lrange(self) -> enums.CodingScheme:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:CSCHeme:LENergy:LRANge \n
		Snippet: value: enums.CodingScheme = driver.configure.bluetooth.measurement.inputSignal.cscheme.lowEnergy.get_lrange() \n
		No command help available \n
			:return: coding_scheme: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:CSCHeme:LENergy:LRANge?')
		return Conversions.str_to_scalar_enum(response, enums.CodingScheme)

	def set_lrange(self, coding_scheme: enums.CodingScheme) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:CSCHeme:LENergy:LRANge \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.cscheme.lowEnergy.set_lrange(coding_scheme = enums.CodingScheme.S2) \n
		No command help available \n
			:param coding_scheme: No help available
		"""
		param = Conversions.enum_scalar_to_str(coding_scheme, enums.CodingScheme)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:CSCHeme:LENergy:LRANge {param}')
