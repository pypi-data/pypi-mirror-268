from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MalgorithmCls:
	"""Malgorithm commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("malgorithm", core, parent)

	# noinspection PyTypeChecker
	def get_low_energy(self) -> enums.PatternIndependent:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:MALGorithm:LENergy \n
		Snippet: value: enums.PatternIndependent = driver.configure.bluetooth.measurement.multiEval.malgorithm.get_low_energy() \n
		No command help available \n
			:return: pattern_independent: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:MALGorithm:LENergy?')
		return Conversions.str_to_scalar_enum(response, enums.PatternIndependent)

	def set_low_energy(self, pattern_independent: enums.PatternIndependent) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:MALGorithm:LENergy \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.malgorithm.set_low_energy(pattern_independent = enums.PatternIndependent.PINDependent) \n
		No command help available \n
			:param pattern_independent: No help available
		"""
		param = Conversions.enum_scalar_to_str(pattern_independent, enums.PatternIndependent)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:MALGorithm:LENergy {param}')

	# noinspection PyTypeChecker
	def get_brate(self) -> enums.PatternIndependent:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:MALGorithm:BRATe \n
		Snippet: value: enums.PatternIndependent = driver.configure.bluetooth.measurement.multiEval.malgorithm.get_brate() \n
		No command help available \n
			:return: pattern_independent: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:MALGorithm:BRATe?')
		return Conversions.str_to_scalar_enum(response, enums.PatternIndependent)

	def set_brate(self, pattern_independent: enums.PatternIndependent) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:MALGorithm:BRATe \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.malgorithm.set_brate(pattern_independent = enums.PatternIndependent.PINDependent) \n
		No command help available \n
			:param pattern_independent: No help available
		"""
		param = Conversions.enum_scalar_to_str(pattern_independent, enums.PatternIndependent)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:MALGorithm:BRATe {param}')
