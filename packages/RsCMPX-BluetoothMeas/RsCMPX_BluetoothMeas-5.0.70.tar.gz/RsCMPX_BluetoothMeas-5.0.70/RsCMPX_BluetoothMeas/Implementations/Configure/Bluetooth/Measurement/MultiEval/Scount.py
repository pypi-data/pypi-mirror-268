from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScountCls:
	"""Scount commands group definition. 7 total commands, 0 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scount", core, parent)

	def get_pencoding(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:PENCoding \n
		Snippet: value: int = driver.configure.bluetooth.measurement.multiEval.scount.get_pencoding() \n
		No command help available \n
			:return: statistic_count: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:PENCoding?')
		return Conversions.str_to_int(response)

	def set_pencoding(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:PENCoding \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.scount.set_pencoding(statistic_count = 1) \n
		No command help available \n
			:param statistic_count: No help available
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:PENCoding {param}')

	def get_frange(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:FRANge \n
		Snippet: value: int = driver.configure.bluetooth.measurement.multiEval.scount.get_frange() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. The last mnemonic denotes the measurement type: spectrum frequency range, spectrum ACP and spectrum gated
		ACP. \n
			:return: statistic_count: Statistic count for the measurement
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:FRANge?')
		return Conversions.str_to_int(response)

	def set_frange(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:FRANge \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.scount.set_frange(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. The last mnemonic denotes the measurement type: spectrum frequency range, spectrum ACP and spectrum gated
		ACP. \n
			:param statistic_count: Statistic count for the measurement
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:FRANge {param}')

	def get_sgacp(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:SGACp \n
		Snippet: value: int = driver.configure.bluetooth.measurement.multiEval.scount.get_sgacp() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. The last mnemonic denotes the measurement type: spectrum frequency range, spectrum ACP and spectrum gated
		ACP. \n
			:return: statistic_count: Statistic count for the measurement
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:SGACp?')
		return Conversions.str_to_int(response)

	def set_sgacp(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:SGACp \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.scount.set_sgacp(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. The last mnemonic denotes the measurement type: spectrum frequency range, spectrum ACP and spectrum gated
		ACP. \n
			:param statistic_count: Statistic count for the measurement
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:SGACp {param}')

	def get_so_bw(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:SOBW \n
		Snippet: value: int = driver.configure.bluetooth.measurement.multiEval.scount.get_so_bw() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. The last mnemonic denotes the measurement type: statistical modulation, statistical power, and spectrum 20
		dB bandwidth (occupied bandwidth) measurement. \n
			:return: statistic_count: Number of measurement intervals
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:SOBW?')
		return Conversions.str_to_int(response)

	def set_so_bw(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:SOBW \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.scount.set_so_bw(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. The last mnemonic denotes the measurement type: statistical modulation, statistical power, and spectrum 20
		dB bandwidth (occupied bandwidth) measurement. \n
			:param statistic_count: Number of measurement intervals
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:SOBW {param}')

	def get_sacp(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:SACP \n
		Snippet: value: int = driver.configure.bluetooth.measurement.multiEval.scount.get_sacp() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. The last mnemonic denotes the measurement type: spectrum frequency range, spectrum ACP and spectrum gated
		ACP. \n
			:return: statistic_count: Statistic count for the measurement
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:SACP?')
		return Conversions.str_to_int(response)

	def set_sacp(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:SACP \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.scount.set_sacp(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. The last mnemonic denotes the measurement type: spectrum frequency range, spectrum ACP and spectrum gated
		ACP. \n
			:param statistic_count: Statistic count for the measurement
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:SACP {param}')

	def get_power_vs_time(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:PVTime \n
		Snippet: value: int = driver.configure.bluetooth.measurement.multiEval.scount.get_power_vs_time() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. The last mnemonic denotes the measurement type: statistical modulation, statistical power, and spectrum 20
		dB bandwidth (occupied bandwidth) measurement. \n
			:return: statistic_count: Number of measurement intervals
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:PVTime?')
		return Conversions.str_to_int(response)

	def set_power_vs_time(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:PVTime \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.scount.set_power_vs_time(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. The last mnemonic denotes the measurement type: statistical modulation, statistical power, and spectrum 20
		dB bandwidth (occupied bandwidth) measurement. \n
			:param statistic_count: Number of measurement intervals
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:PVTime {param}')

	def get_modulation(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:MODulation \n
		Snippet: value: int = driver.configure.bluetooth.measurement.multiEval.scount.get_modulation() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. The last mnemonic denotes the measurement type: statistical modulation, statistical power, and spectrum 20
		dB bandwidth (occupied bandwidth) measurement. \n
			:return: statistic_count: Number of measurement intervals
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:MODulation?')
		return Conversions.str_to_int(response)

	def set_modulation(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:MODulation \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.scount.set_modulation(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. The last mnemonic denotes the measurement type: statistical modulation, statistical power, and spectrum 20
		dB bandwidth (occupied bandwidth) measurement. \n
			:param statistic_count: Number of measurement intervals
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCOunt:MODulation {param}')
