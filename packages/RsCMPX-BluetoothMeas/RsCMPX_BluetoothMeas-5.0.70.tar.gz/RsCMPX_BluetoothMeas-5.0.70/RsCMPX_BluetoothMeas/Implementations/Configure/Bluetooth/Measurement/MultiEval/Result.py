from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 17 total commands, 0 Subgroups, 17 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get_spower(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:SPOWer \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.multiEval.result.get_spower() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:SPOWer?')
		return Conversions.str_to_bool(response)

	def set_spower(self, enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:SPOWer \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.result.set_spower(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:SPOWer {param}')

	def get_pencoding(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:PENCoding \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.multiEval.result.get_pencoding() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:PENCoding?')
		return Conversions.str_to_bool(response)

	def set_pencoding(self, enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:PENCoding \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.result.set_pencoding(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:PENCoding {param}')

	def get_frange(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:FRANge \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.multiEval.result.get_frange() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:return: enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:FRANge?')
		return Conversions.str_to_bool(response)

	def set_frange(self, enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:FRANge \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.result.set_frange(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:param enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:FRANge {param}')

	def get_sgacp(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:SGACp \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.multiEval.result.get_sgacp() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:return: enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:SGACp?')
		return Conversions.str_to_bool(response)

	def set_sgacp(self, enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:SGACp \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.result.set_sgacp(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:param enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:SGACp {param}')

	def get_so_bw(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:SOBW \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.multiEval.result.get_so_bw() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:return: enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:SOBW?')
		return Conversions.str_to_bool(response)

	def set_so_bw(self, enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:SOBW \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.result.set_so_bw(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:param enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:SOBW {param}')

	def get_sacp(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:SACP \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.multiEval.result.get_sacp() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:return: enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:SACP?')
		return Conversions.str_to_bool(response)

	def set_sacp(self, enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:SACP \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.result.set_sacp(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:param enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:SACP {param}')

	# noinspection PyTypeChecker
	class AllStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Devm: bool: Differential error vector magnitude (only for EDR) ON: Evaluate the results. OFF: Do not evaluate results.
			- Phase_Diff: bool: Phase difference (only for EDR)
			- Mod_Scalars: bool: Statistical modulation results
			- Iq_Absolute: bool: I/Q constellation absolute (only for EDR)
			- Iq_Differential: bool: I/Q constellation differential (only for EDR)
			- Iq_Error: bool: I/Q constellation error (only for EDR)
			- Freq_Dev: bool: Frequency deviation (only for BR and LE)
			- Power_Vs_Time: bool: Power vs time
			- Power_Scalars: bool: Statistical power results
			- Spectrum_Obw: bool: Spectrum 20 dB bandwidth (only for BR)
			- Spectrum_Acp: bool: Spectrum ACP (only for BR and LE)
			- Spectrum_Gat_Acp: bool: Spectrum gated ACP (only for EDR)
			- Spec_Freq_Range: bool: Optional setting parameter. Spectrum frequency range (only for BR)
			- Phase_Encoding: bool: No parameter help available
			- Power_Vs_Slot: bool: Optional setting parameter. Power versus slot (only for LE with CTE)"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Devm'),
			ArgStruct.scalar_bool('Phase_Diff'),
			ArgStruct.scalar_bool('Mod_Scalars'),
			ArgStruct.scalar_bool('Iq_Absolute'),
			ArgStruct.scalar_bool('Iq_Differential'),
			ArgStruct.scalar_bool('Iq_Error'),
			ArgStruct.scalar_bool('Freq_Dev'),
			ArgStruct.scalar_bool('Power_Vs_Time'),
			ArgStruct.scalar_bool('Power_Scalars'),
			ArgStruct.scalar_bool('Spectrum_Obw'),
			ArgStruct.scalar_bool('Spectrum_Acp'),
			ArgStruct.scalar_bool('Spectrum_Gat_Acp'),
			ArgStruct.scalar_bool_optional('Spec_Freq_Range'),
			ArgStruct.scalar_bool_optional('Phase_Encoding'),
			ArgStruct.scalar_bool_optional('Power_Vs_Slot')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Devm: bool = None
			self.Phase_Diff: bool = None
			self.Mod_Scalars: bool = None
			self.Iq_Absolute: bool = None
			self.Iq_Differential: bool = None
			self.Iq_Error: bool = None
			self.Freq_Dev: bool = None
			self.Power_Vs_Time: bool = None
			self.Power_Scalars: bool = None
			self.Spectrum_Obw: bool = None
			self.Spectrum_Acp: bool = None
			self.Spectrum_Gat_Acp: bool = None
			self.Spec_Freq_Range: bool = None
			self.Phase_Encoding: bool = None
			self.Power_Vs_Slot: bool = None

	def get_all(self) -> AllStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult[:ALL] \n
		Snippet: value: AllStruct = driver.configure.bluetooth.measurement.multiEval.result.get_all() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. This command combines all other
		CONFigure:BLUetooth:MEAS<i>:MEValuation:RESult... commands. \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:ALL?', self.__class__.AllStruct())

	def set_all(self, value: AllStruct) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult[:ALL] \n
		Snippet with structure: \n
		structure = driver.configure.bluetooth.measurement.multiEval.result.AllStruct() \n
		structure.Devm: bool = False \n
		structure.Phase_Diff: bool = False \n
		structure.Mod_Scalars: bool = False \n
		structure.Iq_Absolute: bool = False \n
		structure.Iq_Differential: bool = False \n
		structure.Iq_Error: bool = False \n
		structure.Freq_Dev: bool = False \n
		structure.Power_Vs_Time: bool = False \n
		structure.Power_Scalars: bool = False \n
		structure.Spectrum_Obw: bool = False \n
		structure.Spectrum_Acp: bool = False \n
		structure.Spectrum_Gat_Acp: bool = False \n
		structure.Spec_Freq_Range: bool = False \n
		structure.Phase_Encoding: bool = False \n
		structure.Power_Vs_Slot: bool = False \n
		driver.configure.bluetooth.measurement.multiEval.result.set_all(value = structure) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. This command combines all other
		CONFigure:BLUetooth:MEAS<i>:MEValuation:RESult... commands. \n
			:param value: see the help for AllStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:ALL', value)

	def get_pscalar(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:PSCalar \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.multiEval.result.get_pscalar() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:return: enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:PSCalar?')
		return Conversions.str_to_bool(response)

	def set_pscalar(self, enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:PSCalar \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.result.set_pscalar(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:param enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:PSCalar {param}')

	def get_iq_absolute(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:IQABsolute \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.multiEval.result.get_iq_absolute() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:return: enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:IQABsolute?')
		return Conversions.str_to_bool(response)

	def set_iq_absolute(self, enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:IQABsolute \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.result.set_iq_absolute(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:param enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:IQABsolute {param}')

	def get_iq_error(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:IQERror \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.multiEval.result.get_iq_error() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:return: enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:IQERror?')
		return Conversions.str_to_bool(response)

	def set_iq_error(self, enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:IQERror \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.result.set_iq_error(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:param enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:IQERror {param}')

	def get_iq_difference(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:IQDiff \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.multiEval.result.get_iq_difference() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:return: enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:IQDiff?')
		return Conversions.str_to_bool(response)

	def set_iq_difference(self, enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:IQDiff \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.result.set_iq_difference(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:param enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:IQDiff {param}')

	def get_power_vs_time(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:PVTime \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.multiEval.result.get_power_vs_time() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:return: enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:PVTime?')
		return Conversions.str_to_bool(response)

	def set_power_vs_time(self, enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:PVTime \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.result.set_power_vs_time(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:param enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:PVTime {param}')

	def get_dev_magnitude(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:DEVMagnitude \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.multiEval.result.get_dev_magnitude() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:return: enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:DEVMagnitude?')
		return Conversions.str_to_bool(response)

	def set_dev_magnitude(self, enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:DEVMagnitude \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.result.set_dev_magnitude(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:param enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:DEVMagnitude {param}')

	def get_pdifference(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:PDIFference \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.multiEval.result.get_pdifference() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:return: enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:PDIFference?')
		return Conversions.str_to_bool(response)

	def set_pdifference(self, enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:PDIFference \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.result.set_pdifference(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:param enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:PDIFference {param}')

	def get_mscalar(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:MSCalar \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.multiEval.result.get_mscalar() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:return: enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:MSCalar?')
		return Conversions.str_to_bool(response)

	def set_mscalar(self, enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:MSCalar \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.result.set_mscalar(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:param enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:MSCalar {param}')

	def get_fdeviation(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:FDEViation \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.multiEval.result.get_fdeviation() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:return: enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:FDEViation?')
		return Conversions.str_to_bool(response)

	def set_fdeviation(self, enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:FDEViation \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.result.set_fdeviation(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:param enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:FDEViation {param}')

	def get_pv_slot(self) -> bool:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:PVSLot \n
		Snippet: value: bool = driver.configure.bluetooth.measurement.multiEval.result.get_pv_slot() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:return: enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:PVSLot?')
		return Conversions.str_to_bool(response)

	def set_pv_slot(self, enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:PVSLot \n
		Snippet: driver.configure.bluetooth.measurement.multiEval.result.set_pv_slot(enable = False) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. The last mnemonic denotes the
		measurement type: Statistical modulation results, statistical power results, power vs time results, power vs slot results
		(LE with CTE) , DEVM (EDR) , phase difference (EDR) , I/Q constellation absolute (EDR) , I/Q constellation differential
		(EDR) , I/Q constellation error (EDR) , frequency deviation (BR, LE) , frequency range results (BR) , spectrum 20 dB
		bandwidth (BR) , spectrum ACP (BR, LE) , spectrum gated ACP (EDR) . Use method RsCMPX_BluetoothMeas.Configure.Bluetooth.
		Measurement.MultiEval.Result.all to enable/disable all result types. Tip: Use READ...? queries to retrieve results for
		disabled measurements. \n
			:param enable: ON: Evaluate the results. OFF: Do not evaluate results.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:RESult:PVSLot {param}')
