from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AccAddressCls:
	"""AccAddress commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("accAddress", core, parent)

	def get_low_energy(self) -> str:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:ACCaddress:LENergy \n
		Snippet: value: str = driver.configure.bluetooth.measurement.inputSignal.accAddress.get_low_energy() \n
		Specifies the access address of the advertiser for standalone LE measurements. \n
			:return: access_address: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:ACCaddress:LENergy?')
		return trim_str_response(response)

	def set_low_energy(self, access_address: str) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:ACCaddress:LENergy \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.accAddress.set_low_energy(access_address = rawAbc) \n
		Specifies the access address of the advertiser for standalone LE measurements. \n
			:param access_address: No help available
		"""
		param = Conversions.value_to_str(access_address)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:ACCaddress:LENergy {param}')
