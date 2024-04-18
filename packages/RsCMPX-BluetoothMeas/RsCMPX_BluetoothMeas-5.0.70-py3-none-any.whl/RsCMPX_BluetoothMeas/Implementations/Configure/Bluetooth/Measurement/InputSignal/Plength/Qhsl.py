from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class QhslCls:
	"""Qhsl commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qhsl", core, parent)

	def get_p_2_q(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:QHSL:P2Q \n
		Snippet: value: int = driver.configure.bluetooth.measurement.inputSignal.plength.qhsl.get_p_2_q() \n
		No command help available \n
			:return: payload_length: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:QHSL:P2Q?')
		return Conversions.str_to_int(response)

	def set_p_2_q(self, payload_length: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:QHSL:P2Q \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.plength.qhsl.set_p_2_q(payload_length = 1) \n
		No command help available \n
			:param payload_length: No help available
		"""
		param = Conversions.decimal_value_to_str(payload_length)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:QHSL:P2Q {param}')

	def get_p_3_q(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:QHSL:P3Q \n
		Snippet: value: int = driver.configure.bluetooth.measurement.inputSignal.plength.qhsl.get_p_3_q() \n
		No command help available \n
			:return: payload_length: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:QHSL:P3Q?')
		return Conversions.str_to_int(response)

	def set_p_3_q(self, payload_length: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:QHSL:P3Q \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.plength.qhsl.set_p_3_q(payload_length = 1) \n
		No command help available \n
			:param payload_length: No help available
		"""
		param = Conversions.decimal_value_to_str(payload_length)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:QHSL:P3Q {param}')

	def get_p_4_q(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:QHSL:P4Q \n
		Snippet: value: int = driver.configure.bluetooth.measurement.inputSignal.plength.qhsl.get_p_4_q() \n
		No command help available \n
			:return: payload_length: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:QHSL:P4Q?')
		return Conversions.str_to_int(response)

	def set_p_4_q(self, payload_length: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:QHSL:P4Q \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.plength.qhsl.set_p_4_q(payload_length = 1) \n
		No command help available \n
			:param payload_length: No help available
		"""
		param = Conversions.decimal_value_to_str(payload_length)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:QHSL:P4Q {param}')

	def get_p_5_q(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:QHSL:P5Q \n
		Snippet: value: int = driver.configure.bluetooth.measurement.inputSignal.plength.qhsl.get_p_5_q() \n
		No command help available \n
			:return: payload_length: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:QHSL:P5Q?')
		return Conversions.str_to_int(response)

	def set_p_5_q(self, payload_length: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:QHSL:P5Q \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.plength.qhsl.set_p_5_q(payload_length = 1) \n
		No command help available \n
			:param payload_length: No help available
		"""
		param = Conversions.decimal_value_to_str(payload_length)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:QHSL:P5Q {param}')

	def get_p_6_q(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:QHSL:P6Q \n
		Snippet: value: int = driver.configure.bluetooth.measurement.inputSignal.plength.qhsl.get_p_6_q() \n
		No command help available \n
			:return: payload_length: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:QHSL:P6Q?')
		return Conversions.str_to_int(response)

	def set_p_6_q(self, payload_length: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:QHSL:P6Q \n
		Snippet: driver.configure.bluetooth.measurement.inputSignal.plength.qhsl.set_p_6_q(payload_length = 1) \n
		No command help available \n
			:param payload_length: No help available
		"""
		param = Conversions.decimal_value_to_str(payload_length)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:QHSL:P6Q {param}')
