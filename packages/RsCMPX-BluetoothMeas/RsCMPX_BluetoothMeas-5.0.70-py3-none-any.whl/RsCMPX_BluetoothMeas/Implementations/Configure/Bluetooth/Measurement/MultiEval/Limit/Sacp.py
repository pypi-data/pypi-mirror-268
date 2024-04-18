from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SacpCls:
	"""Sacp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sacp", core, parent)

	def set(self, ptx_limit: float, exc_ptx_limit: float, no_of_ex_limit: int, ptx_enable: bool, no_of_exc_enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:SACP \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.limit.sacp.set(ptx_limit = 1.0, exc_ptx_limit = 1.0, no_of_ex_limit = 1, ptx_enable = False, no_of_exc_enable = False) \n
		These commands define and enable the Spectrum ACP limits for BR (...:LIMit:SACP) , LE 1M PHY ( ...:LE1M...) , LE 2M PHY (.
		..:LE2M...) , and LE coded PHY (...:LRANge...) , respectively. \n
			:param ptx_limit: Power limit for 1 MHz channels fTX± 2 MHz
			:param exc_ptx_limit: Power limit for 1 MHz channels fTX±3 MHz, fTX±4 MHz, ...
			:param no_of_ex_limit: Maximum number of tolerable exceptions, i.e. 1 MHz channels fTX±3 MHz, fTX±4 MHz, ... whose power is above ExcPTxLimit, but below PTxLimit.
			:param ptx_enable: Disables | enables the PTxLimit limit for 1 MHz channels fTX± 2 MHz.
			:param no_of_exc_enable: Disables | enables the ExcPTxLimit limit for 1 MHz channels fTX±3 MHz, fTX±4 MHz, ... with NoOfExLimit tolerable exceptions (per statistic cycle) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ptx_limit', ptx_limit, DataType.Float), ArgSingle('exc_ptx_limit', exc_ptx_limit, DataType.Float), ArgSingle('no_of_ex_limit', no_of_ex_limit, DataType.Integer), ArgSingle('ptx_enable', ptx_enable, DataType.Boolean), ArgSingle('no_of_exc_enable', no_of_exc_enable, DataType.Boolean))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:SACP {param}'.rstrip())

	# noinspection PyTypeChecker
	class SacpStruct(StructBase):
		"""Response structure. Fields: \n
			- Ptx_Limit: float: Power limit for 1 MHz channels fTX± 2 MHz
			- Exc_Ptx_Limit: float: Power limit for 1 MHz channels fTX±3 MHz, fTX±4 MHz, ...
			- No_Of_Ex_Limit: int: Maximum number of tolerable exceptions, i.e. 1 MHz channels fTX±3 MHz, fTX±4 MHz, ... whose power is above ExcPTxLimit, but below PTxLimit.
			- Ptx_Enable: bool: Disables | enables the PTxLimit limit for 1 MHz channels fTX± 2 MHz.
			- No_Of_Exc_Enable: bool: Disables | enables the ExcPTxLimit limit for 1 MHz channels fTX±3 MHz, fTX±4 MHz, ... with NoOfExLimit tolerable exceptions (per statistic cycle) ."""
		__meta_args_list = [
			ArgStruct.scalar_float('Ptx_Limit'),
			ArgStruct.scalar_float('Exc_Ptx_Limit'),
			ArgStruct.scalar_int('No_Of_Ex_Limit'),
			ArgStruct.scalar_bool('Ptx_Enable'),
			ArgStruct.scalar_bool('No_Of_Exc_Enable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ptx_Limit: float = None
			self.Exc_Ptx_Limit: float = None
			self.No_Of_Ex_Limit: int = None
			self.Ptx_Enable: bool = None
			self.No_Of_Exc_Enable: bool = None

	def get(self) -> SacpStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:SACP \n
		Snippet: value: SacpStruct = driver.configure.bluetooth.measurement.multiEval.limit.sacp.get() \n
		These commands define and enable the Spectrum ACP limits for BR (...:LIMit:SACP) , LE 1M PHY ( ...:LE1M...) , LE 2M PHY (.
		..:LE2M...) , and LE coded PHY (...:LRANge...) , respectively. \n
			:return: structure: for return value, see the help for SacpStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:SACP?', self.__class__.SacpStruct())
