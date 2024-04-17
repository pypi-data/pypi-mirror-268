from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 10 total commands, 0 Subgroups, 10 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get_power_vs_time(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:PVTime \n
		Snippet: value: bool = driver.configure.multiEval.result.get_power_vs_time() \n
		Enables or disables the evaluation of power vs time results. \n
			:return: power_vs_time_enable: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:PVTime?')
		return Conversions.str_to_bool(response)

	def set_power_vs_time(self, power_vs_time_enable: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:PVTime \n
		Snippet: driver.configure.multiEval.result.set_power_vs_time(power_vs_time_enable = False) \n
		Enables or disables the evaluation of power vs time results. \n
			:param power_vs_time_enable: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		param = Conversions.bool_to_str(power_vs_time_enable)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:PVTime {param}')

	def get_spectr_flatness(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:SFLatness \n
		Snippet: value: bool = driver.configure.multiEval.result.get_spectr_flatness() \n
		Enables or disables the evaluation of spectrum flatness results. \n
			:return: spec_flatness: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:SFLatness?')
		return Conversions.str_to_bool(response)

	def set_spectr_flatness(self, spec_flatness: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:SFLatness \n
		Snippet: driver.configure.multiEval.result.set_spectr_flatness(spec_flatness = False) \n
		Enables or disables the evaluation of spectrum flatness results. \n
			:param spec_flatness: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		param = Conversions.bool_to_str(spec_flatness)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:SFLatness {param}')

	# noinspection PyTypeChecker
	class AllStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Mod_Scalar: bool: OFF | ON Modulation scalar overview OFF: Do not evaluate results. ON: Evaluate results.
			- Power_Vs_Time: bool: OFF | ON Power vs time
			- Evm_Vs_Chip: bool: OFF | ON EVM vs chip
			- Evm_Vs_Sym: bool: OFF | ON EVM vs symbol
			- Evm_Vs_Carr: bool: OFF | ON EVM vs carrier
			- Iq_Const: bool: OFF | ON I/Q constellation diagram
			- Spec_Flatness: bool: OFF | ON Spectrum flatness
			- Tran_Spec_Mask: bool: OFF | ON Transmit spectrum mask.
			- Unused_Tone_Err: bool: Optional setting parameter. OFF | ON Unused tone error"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Mod_Scalar'),
			ArgStruct.scalar_bool('Power_Vs_Time'),
			ArgStruct.scalar_bool('Evm_Vs_Chip'),
			ArgStruct.scalar_bool('Evm_Vs_Sym'),
			ArgStruct.scalar_bool('Evm_Vs_Carr'),
			ArgStruct.scalar_bool('Iq_Const'),
			ArgStruct.scalar_bool('Spec_Flatness'),
			ArgStruct.scalar_bool('Tran_Spec_Mask'),
			ArgStruct.scalar_bool_optional('Unused_Tone_Err')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mod_Scalar: bool = None
			self.Power_Vs_Time: bool = None
			self.Evm_Vs_Chip: bool = None
			self.Evm_Vs_Sym: bool = None
			self.Evm_Vs_Carr: bool = None
			self.Iq_Const: bool = None
			self.Spec_Flatness: bool = None
			self.Tran_Spec_Mask: bool = None
			self.Unused_Tone_Err: bool = None

	def get_all(self) -> AllStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult[:ALL] \n
		Snippet: value: AllStruct = driver.configure.multiEval.result.get_all() \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. This command combines all other
		CONFigure:WLAN:MEAS<i>:MEValuation:RESult... commands. Views can only be hidden for receive mode SISO. To check which
		views are relevant for which standard, see 'Measurement results'. \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:ALL?', self.__class__.AllStruct())

	def set_all(self, value: AllStruct) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult[:ALL] \n
		Snippet with structure: \n
		structure = driver.configure.multiEval.result.AllStruct() \n
		structure.Mod_Scalar: bool = False \n
		structure.Power_Vs_Time: bool = False \n
		structure.Evm_Vs_Chip: bool = False \n
		structure.Evm_Vs_Sym: bool = False \n
		structure.Evm_Vs_Carr: bool = False \n
		structure.Iq_Const: bool = False \n
		structure.Spec_Flatness: bool = False \n
		structure.Tran_Spec_Mask: bool = False \n
		structure.Unused_Tone_Err: bool = False \n
		driver.configure.multiEval.result.set_all(value = structure) \n
		Enables or disables the evaluation of results in the multi-evaluation measurement. This command combines all other
		CONFigure:WLAN:MEAS<i>:MEValuation:RESult... commands. Views can only be hidden for receive mode SISO. To check which
		views are relevant for which standard, see 'Measurement results'. \n
			:param value: see the help for AllStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:ALL', value)

	def get_evm(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:EVM \n
		Snippet: value: bool = driver.configure.multiEval.result.get_evm() \n
		Enables or disables the evaluation of EVM vs chip results. \n
			:return: evm_enable: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:EVM?')
		return Conversions.str_to_bool(response)

	def set_evm(self, evm_enable: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:EVM \n
		Snippet: driver.configure.multiEval.result.set_evm(evm_enable = False) \n
		Enables or disables the evaluation of EVM vs chip results. \n
			:param evm_enable: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		param = Conversions.bool_to_str(evm_enable)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:EVM {param}')

	def get_evm_carrier(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:EVMCarrier \n
		Snippet: value: bool = driver.configure.multiEval.result.get_evm_carrier() \n
		Enables or disables the evaluation of EVM vs carrier results. \n
			:return: evm_enable: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:EVMCarrier?')
		return Conversions.str_to_bool(response)

	def set_evm_carrier(self, evm_enable: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:EVMCarrier \n
		Snippet: driver.configure.multiEval.result.set_evm_carrier(evm_enable = False) \n
		Enables or disables the evaluation of EVM vs carrier results. \n
			:param evm_enable: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		param = Conversions.bool_to_str(evm_enable)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:EVMCarrier {param}')

	def get_iq_constant(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:IQConst \n
		Snippet: value: bool = driver.configure.multiEval.result.get_iq_constant() \n
		Enables or disables the evaluation of I/Q constellation results. \n
			:return: iq_enable: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:IQConst?')
		return Conversions.str_to_bool(response)

	def set_iq_constant(self, iq_enable: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:IQConst \n
		Snippet: driver.configure.multiEval.result.set_iq_constant(iq_enable = False) \n
		Enables or disables the evaluation of I/Q constellation results. \n
			:param iq_enable: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		param = Conversions.bool_to_str(iq_enable)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:IQConst {param}')

	def get_ut_error(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:UTERror \n
		Snippet: value: bool = driver.configure.multiEval.result.get_ut_error() \n
		Enables or disables the evaluation unused tone error results. \n
			:return: ute_enable: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:UTERror?')
		return Conversions.str_to_bool(response)

	def set_ut_error(self, ute_enable: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:UTERror \n
		Snippet: driver.configure.multiEval.result.set_ut_error(ute_enable = False) \n
		Enables or disables the evaluation unused tone error results. \n
			:param ute_enable: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		param = Conversions.bool_to_str(ute_enable)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:UTERror {param}')

	def get_evm_symbol(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:EVMSymbol \n
		Snippet: value: bool = driver.configure.multiEval.result.get_evm_symbol() \n
		Enables or disables the evaluation of EVM vs symbol results. \n
			:return: evm_enable: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:EVMSymbol?')
		return Conversions.str_to_bool(response)

	def set_evm_symbol(self, evm_enable: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:EVMSymbol \n
		Snippet: driver.configure.multiEval.result.set_evm_symbol(evm_enable = False) \n
		Enables or disables the evaluation of EVM vs symbol results. \n
			:param evm_enable: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		param = Conversions.bool_to_str(evm_enable)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:EVMSymbol {param}')

	def get_ts_mask(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:TSMask \n
		Snippet: value: bool = driver.configure.multiEval.result.get_ts_mask() \n
		Enables or disables the evaluation of transmit spectrum mask results. \n
			:return: spec_enable: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:TSMask?')
		return Conversions.str_to_bool(response)

	def set_ts_mask(self, spec_enable: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:TSMask \n
		Snippet: driver.configure.multiEval.result.set_ts_mask(spec_enable = False) \n
		Enables or disables the evaluation of transmit spectrum mask results. \n
			:param spec_enable: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		param = Conversions.bool_to_str(spec_enable)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:TSMask {param}')

	def get_mscalar(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:MSCalar \n
		Snippet: value: bool = driver.configure.multiEval.result.get_mscalar() \n
		Enables or disables the evaluation of modulation scalar results. \n
			:return: modenable: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:MSCalar?')
		return Conversions.str_to_bool(response)

	def set_mscalar(self, modenable: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:MSCalar \n
		Snippet: driver.configure.multiEval.result.set_mscalar(modenable = False) \n
		Enables or disables the evaluation of modulation scalar results. \n
			:param modenable: OFF | ON OFF: Do not evaluate results. ON: Evaluate results.
		"""
		param = Conversions.bool_to_str(modenable)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:RESult:MSCalar {param}')
