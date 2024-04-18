from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SynWordCls:
	"""SynWord commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("synWord", core, parent)

	def get_low_energy(self) -> str:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:SYNWord:LENergy \n
		Snippet: value: str = driver.configure.bluetooth.measurement.inputSignal.synWord.get_low_energy() \n
		No command help available \n
			:return: synch_word: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:SYNWord:LENergy?')
		return trim_str_response(response)

	def set_low_energy(self, synch_word: str) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:SYNWord:LENergy \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.synWord.set_low_energy(synch_word = rawAbc) \n
		No command help available \n
			:param synch_word: No help available
		"""
		param = Conversions.value_to_str(synch_word)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:SYNWord:LENergy {param}')
