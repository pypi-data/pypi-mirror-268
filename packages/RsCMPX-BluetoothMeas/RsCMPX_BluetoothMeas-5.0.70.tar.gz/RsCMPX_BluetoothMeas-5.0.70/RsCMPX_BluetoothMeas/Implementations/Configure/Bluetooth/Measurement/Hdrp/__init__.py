from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HdrpCls:
	"""Hdrp commands group definition. 23 total commands, 5 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hdrp", core, parent)

	@property
	def limit(self):
		"""limit commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import LimitCls
			self._limit = LimitCls(self._core, self._cmd_group)
		return self._limit

	@property
	def inputSignal(self):
		"""inputSignal commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_inputSignal'):
			from .InputSignal import InputSignalCls
			self._inputSignal = InputSignalCls(self._core, self._cmd_group)
		return self._inputSignal

	@property
	def result(self):
		"""result commands group. 1 Sub-classes, 5 commands."""
		if not hasattr(self, '_result'):
			from .Result import ResultCls
			self._result = ResultCls(self._core, self._cmd_group)
		return self._result

	@property
	def scount(self):
		"""scount commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_scount'):
			from .Scount import ScountCls
			self._scount = ScountCls(self._core, self._cmd_group)
		return self._scount

	@property
	def sacp(self):
		"""sacp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sacp'):
			from .Sacp import SacpCls
			self._sacp = SacpCls(self._core, self._cmd_group)
		return self._sacp

	def get_mo_exception(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:MOEXception \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.hdrp.get_mo_exception() \n
		No command help available \n
			:return: meas_on_exception: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HDRP:MOEXception?')
		return Conversions.str_to_bool(response)

	def set_mo_exception(self, meas_on_exception: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:MOEXception \n
		Snippet: driver.configure.bluetooth.measurement.hdrp.set_mo_exception(meas_on_exception = False) \n
		No command help available \n
			:param meas_on_exception: No help available
		"""
		param = Conversions.bool_to_str(meas_on_exception)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDRP:MOEXception {param}')

	# noinspection PyTypeChecker
	def get_scondition(self) -> enums.StopCondition:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:SCONdition \n
		Snippet: value: enums.StopCondition = driver.configure.bluetooth.measurement.hdrp.get_scondition() \n
		No command help available \n
			:return: stop_condition: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HDRP:SCONdition?')
		return Conversions.str_to_scalar_enum(response, enums.StopCondition)

	def set_scondition(self, stop_condition: enums.StopCondition) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:SCONdition \n
		Snippet: driver.configure.bluetooth.measurement.hdrp.set_scondition(stop_condition = enums.StopCondition.NONE) \n
		No command help available \n
			:param stop_condition: No help available
		"""
		param = Conversions.enum_scalar_to_str(stop_condition, enums.StopCondition)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDRP:SCONdition {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.bluetooth.measurement.hdrp.get_repetition() \n
		No command help available \n
			:return: repetition: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:HDRP:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:HDRP:REPetition \n
		Snippet: driver.configure.bluetooth.measurement.hdrp.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		No command help available \n
			:param repetition: No help available
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:HDRP:REPetition {param}')

	def clone(self) -> 'HdrpCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HdrpCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
