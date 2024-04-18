from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MratioCls:
	"""Mratio commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mratio", core, parent)

	def set(self, mod_ratio: float, mod_ratio_enabled: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy[:LE1M]:MRATio \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.limit.lowEnergy.le1M.mratio.set(mod_ratio = 1.0, mod_ratio_enabled = False) \n
		Sets or queries the modulation ratio limit Δf2 avg / Δf1 avg for LE 1M PHY (...:LE1M...) and LE 2M PHY (...:LE2M...) . \n
			:param mod_ratio: No help available
			:param mod_ratio_enabled: Disable/enable limit checking
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('mod_ratio', mod_ratio, DataType.Float), ArgSingle('mod_ratio_enabled', mod_ratio_enabled, DataType.Boolean))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy:LE1M:MRATio {param}'.rstrip())

	# noinspection PyTypeChecker
	class MratioStruct(StructBase):
		"""Response structure. Fields: \n
			- Mod_Ratio: float: No parameter help available
			- Mod_Ratio_Enabled: bool: Disable/enable limit checking"""
		__meta_args_list = [
			ArgStruct.scalar_float('Mod_Ratio'),
			ArgStruct.scalar_bool('Mod_Ratio_Enabled')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mod_Ratio: float = None
			self.Mod_Ratio_Enabled: bool = None

	def get(self) -> MratioStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy[:LE1M]:MRATio \n
		Snippet: value: MratioStruct = driver.configure.bluetooth.measurement.multiEval.limit.lowEnergy.le1M.mratio.get() \n
		Sets or queries the modulation ratio limit Δf2 avg / Δf1 avg for LE 1M PHY (...:LE1M...) and LE 2M PHY (...:LE2M...) . \n
			:return: structure: for return value, see the help for MratioStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy:LE1M:MRATio?', self.__class__.MratioStruct())
