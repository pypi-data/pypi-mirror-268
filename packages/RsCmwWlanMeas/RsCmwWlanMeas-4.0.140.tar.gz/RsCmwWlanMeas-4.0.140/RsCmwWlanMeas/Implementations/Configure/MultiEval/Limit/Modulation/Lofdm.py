from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LofdmCls:
	"""Lofdm commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lofdm", core, parent)

	# noinspection PyTypeChecker
	class EvmStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Evm_6_M: float or bool: numeric | ON | OFF Limit for data rate 6 Mbps Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_9_M: float or bool: numeric | ON | OFF Limit for data rate 9 Mbps Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_12_M: float or bool: numeric | ON | OFF Limit for data rate 12 Mbps Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_18_M: float or bool: numeric | ON | OFF Limit for data rate 18 Mbps Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_24_M: float or bool: numeric | ON | OFF Limit for data rate 24 Mbps Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_36_M: float or bool: numeric | ON | OFF Limit for data rate 36 Mbps Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_48_M: float or bool: numeric | ON | OFF Limit for data rate 48 Mbps Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_54_M: float or bool: numeric | ON | OFF Limit for data rate 54 Mbps Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Evm_6_M'),
			ArgStruct.scalar_float_ext('Evm_9_M'),
			ArgStruct.scalar_float_ext('Evm_12_M'),
			ArgStruct.scalar_float_ext('Evm_18_M'),
			ArgStruct.scalar_float_ext('Evm_24_M'),
			ArgStruct.scalar_float_ext('Evm_36_M'),
			ArgStruct.scalar_float_ext('Evm_48_M'),
			ArgStruct.scalar_float_ext('Evm_54_M')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Evm_6_M: float or bool = None
			self.Evm_9_M: float or bool = None
			self.Evm_12_M: float or bool = None
			self.Evm_18_M: float or bool = None
			self.Evm_24_M: float or bool = None
			self.Evm_36_M: float or bool = None
			self.Evm_48_M: float or bool = None
			self.Evm_54_M: float or bool = None

	def get_evm(self) -> EvmStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:LOFDm:EVM \n
		Snippet: value: EvmStruct = driver.configure.multiEval.limit.modulation.lofdm.get_evm() \n
		Defines and activates upper limits for the error vector magnitude (EVM) of the data carriers (802.11a/g, OFDM) . \n
			:return: structure: for return value, see the help for EvmStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:LOFDm:EVM?', self.__class__.EvmStruct())

	def set_evm(self, value: EvmStruct) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:LOFDm:EVM \n
		Snippet with structure: \n
		structure = driver.configure.multiEval.limit.modulation.lofdm.EvmStruct() \n
		structure.Evm_6_M: float or bool = 1.0 \n
		structure.Evm_9_M: float or bool = 1.0 \n
		structure.Evm_12_M: float or bool = 1.0 \n
		structure.Evm_18_M: float or bool = 1.0 \n
		structure.Evm_24_M: float or bool = 1.0 \n
		structure.Evm_36_M: float or bool = 1.0 \n
		structure.Evm_48_M: float or bool = 1.0 \n
		structure.Evm_54_M: float or bool = 1.0 \n
		driver.configure.multiEval.limit.modulation.lofdm.set_evm(value = structure) \n
		Defines and activates upper limits for the error vector magnitude (EVM) of the data carriers (802.11a/g, OFDM) . \n
			:param value: see the help for EvmStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:LOFDm:EVM', value)

	def get_evm_pilot(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:LOFDm:EVMPilot \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.modulation.lofdm.get_evm_pilot() \n
		Defines and activates an upper limit for the error vector magnitude (EVM) of the pilot carriers (802.11a/g, OFDM) . \n
			:return: evm_pilot: (float or boolean) numeric | ON | OFF Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:LOFDm:EVMPilot?')
		return Conversions.str_to_float_or_bool(response)

	def set_evm_pilot(self, evm_pilot: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:LOFDm:EVMPilot \n
		Snippet: driver.configure.multiEval.limit.modulation.lofdm.set_evm_pilot(evm_pilot = 1.0) \n
		Defines and activates an upper limit for the error vector magnitude (EVM) of the pilot carriers (802.11a/g, OFDM) . \n
			:param evm_pilot: (float or boolean) numeric | ON | OFF Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		param = Conversions.decimal_or_bool_value_to_str(evm_pilot)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:LOFDm:EVMPilot {param}')

	def get_iq_offset(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:LOFDm:IQOFfset \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.modulation.lofdm.get_iq_offset() \n
		Defines and activates an upper limit for the I/Q origin offset (802.11a/g, OFDM) . \n
			:return: iq_offset: (float or boolean) numeric | ON | OFF Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:LOFDm:IQOFfset?')
		return Conversions.str_to_float_or_bool(response)

	def set_iq_offset(self, iq_offset: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:LOFDm:IQOFfset \n
		Snippet: driver.configure.multiEval.limit.modulation.lofdm.set_iq_offset(iq_offset = 1.0) \n
		Defines and activates an upper limit for the I/Q origin offset (802.11a/g, OFDM) . \n
			:param iq_offset: (float or boolean) numeric | ON | OFF Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		param = Conversions.decimal_or_bool_value_to_str(iq_offset)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:LOFDm:IQOFfset {param}')

	def get_cf_error(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:LOFDm:CFERror \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.modulation.lofdm.get_cf_error() \n
		Defines and activates an upper limit for the center frequency error (802.11a/g, OFDM) . \n
			:return: center_freq_error: (float or boolean) numeric | ON | OFF Range: 0 Hz to 100 MHz Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:LOFDm:CFERror?')
		return Conversions.str_to_float_or_bool(response)

	def set_cf_error(self, center_freq_error: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:LOFDm:CFERror \n
		Snippet: driver.configure.multiEval.limit.modulation.lofdm.set_cf_error(center_freq_error = 1.0) \n
		Defines and activates an upper limit for the center frequency error (802.11a/g, OFDM) . \n
			:param center_freq_error: (float or boolean) numeric | ON | OFF Range: 0 Hz to 100 MHz Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		param = Conversions.decimal_or_bool_value_to_str(center_freq_error)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:LOFDm:CFERror {param}')

	def get_sc_error(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:LOFDm:SCERror \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.modulation.lofdm.get_sc_error() \n
		Defines and activates an upper limit for the symbol clock error (802.11a/g, OFDM) . \n
			:return: clock_error: (float or boolean) numeric | ON | OFF Range: 0 ppm to 100 ppm, Unit: ppm Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:LOFDm:SCERror?')
		return Conversions.str_to_float_or_bool(response)

	def set_sc_error(self, clock_error: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:LOFDm:SCERror \n
		Snippet: driver.configure.multiEval.limit.modulation.lofdm.set_sc_error(clock_error = 1.0) \n
		Defines and activates an upper limit for the symbol clock error (802.11a/g, OFDM) . \n
			:param clock_error: (float or boolean) numeric | ON | OFF Range: 0 ppm to 100 ppm, Unit: ppm Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		param = Conversions.decimal_or_bool_value_to_str(clock_error)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:LOFDm:SCERror {param}')
