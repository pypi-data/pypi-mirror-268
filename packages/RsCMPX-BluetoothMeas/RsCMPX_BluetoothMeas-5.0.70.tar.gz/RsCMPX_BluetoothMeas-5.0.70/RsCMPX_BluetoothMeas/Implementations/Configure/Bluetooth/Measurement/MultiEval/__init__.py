from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiEvalCls:
	"""MultiEval commands group definition. 154 total commands, 14 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("multiEval", core, parent)

	@property
	def qhsl(self):
		"""qhsl commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_qhsl'):
			from .Qhsl import QhslCls
			self._qhsl = QhslCls(self._core, self._cmd_group)
		return self._qhsl

	@property
	def sacp(self):
		"""sacp commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_sacp'):
			from .Sacp import SacpCls
			self._sacp = SacpCls(self._core, self._cmd_group)
		return self._sacp

	@property
	def limit(self):
		"""limit commands group. 9 Sub-classes, 1 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import LimitCls
			self._limit = LimitCls(self._core, self._cmd_group)
		return self._limit

	@property
	def measurement(self):
		"""measurement commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_measurement'):
			from .Measurement import MeasurementCls
			self._measurement = MeasurementCls(self._core, self._cmd_group)
		return self._measurement

	@property
	def listPy(self):
		"""listPy commands group. 2 Sub-classes, 5 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPyCls
			self._listPy = ListPyCls(self._core, self._cmd_group)
		return self._listPy

	@property
	def malgorithm(self):
		"""malgorithm commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_malgorithm'):
			from .Malgorithm import MalgorithmCls
			self._malgorithm = MalgorithmCls(self._core, self._cmd_group)
		return self._malgorithm

	@property
	def lowEnergy(self):
		"""lowEnergy commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_lowEnergy'):
			from .LowEnergy import LowEnergyCls
			self._lowEnergy = LowEnergyCls(self._core, self._cmd_group)
		return self._lowEnergy

	@property
	def edrate(self):
		"""edrate commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_edrate'):
			from .Edrate import EdrateCls
			self._edrate = EdrateCls(self._core, self._cmd_group)
		return self._edrate

	@property
	def brate(self):
		"""brate commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_brate'):
			from .Brate import BrateCls
			self._brate = BrateCls(self._core, self._cmd_group)
		return self._brate

	@property
	def scount(self):
		"""scount commands group. 0 Sub-classes, 7 commands."""
		if not hasattr(self, '_scount'):
			from .Scount import ScountCls
			self._scount = ScountCls(self._core, self._cmd_group)
		return self._scount

	@property
	def result(self):
		"""result commands group. 0 Sub-classes, 17 commands."""
		if not hasattr(self, '_result'):
			from .Result import ResultCls
			self._result = ResultCls(self._core, self._cmd_group)
		return self._result

	@property
	def frange(self):
		"""frange commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_frange'):
			from .Frange import FrangeCls
			self._frange = FrangeCls(self._core, self._cmd_group)
		return self._frange

	@property
	def sgacp(self):
		"""sgacp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sgacp'):
			from .Sgacp import SgacpCls
			self._sgacp = SgacpCls(self._core, self._cmd_group)
		return self._sgacp

	@property
	def synchronise(self):
		"""synchronise commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_synchronise'):
			from .Synchronise import SynchroniseCls
			self._synchronise = SynchroniseCls(self._core, self._cmd_group)
		return self._synchronise

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:TOUT \n
		Snippet: value: float = driver.configure.bluetooth.measurement.multiEval.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually. When the measurement has completed the first measurement
		cycle (first single shot) , the statistical depth is reached and the timer is reset. If the first measurement cycle has
		not been completed when the timer expires, the measurement is stopped. The measurement state changes to RDY.
		The reliability indicator is set to 1, indicating that a measurement timeout occurred. Still running READ, FETCh or
		CALCulate commands are completed, returning the available results. At least for some results, there are no values at all
		or the statistical depth has not been reached. A timeout of 0 s corresponds to an infinite measurement timeout. \n
			:return: timeout: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:TOUT \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.set_timeout(timeout = 1.0) \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually. When the measurement has completed the first measurement
		cycle (first single shot) , the statistical depth is reached and the timer is reset. If the first measurement cycle has
		not been completed when the timer expires, the measurement is stopped. The measurement state changes to RDY.
		The reliability indicator is set to 1, indicating that a measurement timeout occurred. Still running READ, FETCh or
		CALCulate commands are completed, returning the available results. At least for some results, there are no values at all
		or the statistical depth has not been reached. A timeout of 0 s corresponds to an infinite measurement timeout. \n
			:param timeout: No help available
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:TOUT {param}')

	def get_mo_exception(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:MOEXception \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.multiEval.get_mo_exception() \n
		Specifies whether measurement results that are identified as faulty or inaccurate are rejected. \n
			:return: meas_on_exception: ON: Results are never rejected. OFF: Faulty results are rejected.
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:MOEXception?')
		return Conversions.str_to_bool(response)

	def set_mo_exception(self, meas_on_exception: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:MOEXception \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.set_mo_exception(meas_on_exception = False) \n
		Specifies whether measurement results that are identified as faulty or inaccurate are rejected. \n
			:param meas_on_exception: ON: Results are never rejected. OFF: Faulty results are rejected.
		"""
		param = Conversions.bool_to_str(meas_on_exception)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:MOEXception {param}')

	# noinspection PyTypeChecker
	def get_scondition(self) -> enums.StopCondition:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCONdition \n
		Snippet: value: enums.StopCondition = driver.configure.bluetooth.measurement.multiEval.get_scondition() \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:return: stop_condition: NONE: Continue measurement irrespective of the limit check. SLFail: Stop measurement on limit failure.
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCONdition?')
		return Conversions.str_to_scalar_enum(response, enums.StopCondition)

	def set_scondition(self, stop_condition: enums.StopCondition) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCONdition \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.set_scondition(stop_condition = enums.StopCondition.NONE) \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:param stop_condition: NONE: Continue measurement irrespective of the limit check. SLFail: Stop measurement on limit failure.
		"""
		param = Conversions.enum_scalar_to_str(stop_condition, enums.StopCondition)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:SCONdition {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.bluetooth.measurement.multiEval.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:return: repetition: SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:REPetition \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:param repetition: SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:REPetition {param}')

	def clone(self) -> 'MultiEvalCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultiEvalCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
