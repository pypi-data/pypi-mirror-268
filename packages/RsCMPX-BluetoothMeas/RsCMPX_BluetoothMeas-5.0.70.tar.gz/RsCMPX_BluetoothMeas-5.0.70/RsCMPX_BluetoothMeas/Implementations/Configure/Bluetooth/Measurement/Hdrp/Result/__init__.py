from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 6 total commands, 1 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	def get_power_vs_time(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult:PVTime \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.hdrp.result.get_power_vs_time() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult:PVTime?')
		return Conversions.str_to_bool(response)

	def set_power_vs_time(self, state: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult:PVTime \n
		Snippet: driver.configure.bluetooth.measurement.hdrp.result.set_power_vs_time(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult:PVTime {param}')

	def get_sacp(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult:SACP \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.hdrp.result.get_sacp() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult:SACP?')
		return Conversions.str_to_bool(response)

	def set_sacp(self, state: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult:SACP \n
		Snippet: driver.configure.bluetooth.measurement.hdrp.result.set_sacp(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult:SACP {param}')

	def get_iq(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult:IQ \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.hdrp.result.get_iq() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult:IQ?')
		return Conversions.str_to_bool(response)

	def set_iq(self, state: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult:IQ \n
		Snippet: driver.configure.bluetooth.measurement.hdrp.result.set_iq(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult:IQ {param}')

	def get_ev_magnitude(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult:EVMagnitude \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.hdrp.result.get_ev_magnitude() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult:EVMagnitude?')
		return Conversions.str_to_bool(response)

	def set_ev_magnitude(self, state: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult:EVMagnitude \n
		Snippet: driver.configure.bluetooth.measurement.hdrp.result.set_ev_magnitude(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult:EVMagnitude {param}')

	def get_tx_scalar(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult:TXSCalar \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.hdrp.result.get_tx_scalar() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult:TXSCalar?')
		return Conversions.str_to_bool(response)

	def set_tx_scalar(self, state: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult:TXSCalar \n
		Snippet: driver.configure.bluetooth.measurement.hdrp.result.set_tx_scalar(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDRP:RESult:TXSCalar {param}')

	def clone(self) -> 'ResultCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ResultCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
