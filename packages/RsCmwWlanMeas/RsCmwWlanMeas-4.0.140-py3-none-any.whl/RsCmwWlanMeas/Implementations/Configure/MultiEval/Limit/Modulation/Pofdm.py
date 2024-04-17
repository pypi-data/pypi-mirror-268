from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PofdmCls:
	"""Pofdm commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pofdm", core, parent)

	# noinspection PyTypeChecker
	class EvmStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Bpsk_12: float or bool: numeric | ON | OFF Limit for data rate BPSK modulation and coding rate 1/2 Range: -100 dB to 0 dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Bpsk_34: float or bool: numeric | ON | OFF Limit for data rate BPSK modulation and coding rate 3/4 Range: -100 dB to 0 dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Qpsk_12: float or bool: numeric | ON | OFF Limit for data rate QPSK modulation and coding rate 1/2 Range: -100 dB to 0 dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Qpsk_34: float or bool: numeric | ON | OFF Limit for data rate QPSK modulation and coding rate 3/4 Range: -100 dB to 0 dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Q_16_Am_12: float or bool: numeric | ON | OFF Limit for data rate 16-QAM modulation and coding rate 1/2 Range: -100 dB to 0 dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Q_16_Am_34: float or bool: numeric | ON | OFF Limit for data rate 16-QAM modulation and coding rate 3/4 Range: -100 dB to 0 dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Q_64_Am_23: float or bool: numeric | ON | OFF Limit for data rate 64-QAM modulation and coding rate 2/3 Additional parameters: OFF | ON (disables | enables the limit check)
			- Q_64_Am_34: float or bool: numeric | ON | OFF Limit for data rate 64-QAM modulation and coding rate 3/4 Additional parameters: OFF | ON (disables | enables the limit check)"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Bpsk_12'),
			ArgStruct.scalar_float_ext('Bpsk_34'),
			ArgStruct.scalar_float_ext('Qpsk_12'),
			ArgStruct.scalar_float_ext('Qpsk_34'),
			ArgStruct.scalar_float_ext('Q_16_Am_12'),
			ArgStruct.scalar_float_ext('Q_16_Am_34'),
			ArgStruct.scalar_float_ext('Q_64_Am_23'),
			ArgStruct.scalar_float_ext('Q_64_Am_34')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Bpsk_12: float or bool = None
			self.Bpsk_34: float or bool = None
			self.Qpsk_12: float or bool = None
			self.Qpsk_34: float or bool = None
			self.Q_16_Am_12: float or bool = None
			self.Q_16_Am_34: float or bool = None
			self.Q_64_Am_23: float or bool = None
			self.Q_64_Am_34: float or bool = None

	def get_evm(self) -> EvmStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:POFDm:EVM \n
		Snippet: value: EvmStruct = driver.configure.multiEval.limit.modulation.pofdm.get_evm() \n
		Defines and activates upper limits for the error vector magnitude (EVM) of the data carriers in 802.11p signals. \n
			:return: structure: for return value, see the help for EvmStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:POFDm:EVM?', self.__class__.EvmStruct())

	def set_evm(self, value: EvmStruct) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:POFDm:EVM \n
		Snippet with structure: \n
		structure = driver.configure.multiEval.limit.modulation.pofdm.EvmStruct() \n
		structure.Bpsk_12: float or bool = 1.0 \n
		structure.Bpsk_34: float or bool = 1.0 \n
		structure.Qpsk_12: float or bool = 1.0 \n
		structure.Qpsk_34: float or bool = 1.0 \n
		structure.Q_16_Am_12: float or bool = 1.0 \n
		structure.Q_16_Am_34: float or bool = 1.0 \n
		structure.Q_64_Am_23: float or bool = 1.0 \n
		structure.Q_64_Am_34: float or bool = 1.0 \n
		driver.configure.multiEval.limit.modulation.pofdm.set_evm(value = structure) \n
		Defines and activates upper limits for the error vector magnitude (EVM) of the data carriers in 802.11p signals. \n
			:param value: see the help for EvmStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:POFDm:EVM', value)

	def get_evm_pilot(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:POFDm:EVMPilot \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.modulation.pofdm.get_evm_pilot() \n
		Defines and activates an upper limit for the error vector magnitude (EVM) of 802.11p pilot carriers. \n
			:return: evm_pilot: (float or boolean) numeric | ON | OFF Range: -100 dB to 0 dB Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:POFDm:EVMPilot?')
		return Conversions.str_to_float_or_bool(response)

	def set_evm_pilot(self, evm_pilot: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:POFDm:EVMPilot \n
		Snippet: driver.configure.multiEval.limit.modulation.pofdm.set_evm_pilot(evm_pilot = 1.0) \n
		Defines and activates an upper limit for the error vector magnitude (EVM) of 802.11p pilot carriers. \n
			:param evm_pilot: (float or boolean) numeric | ON | OFF Range: -100 dB to 0 dB Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		param = Conversions.decimal_or_bool_value_to_str(evm_pilot)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:POFDm:EVMPilot {param}')

	def get_iq_offset(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:POFDm:IQOFfset \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.modulation.pofdm.get_iq_offset() \n
		Defines and activates an upper limit for the I/Q origin offset of 802.11p signals. \n
			:return: iq_offset: (float or boolean) numeric | ON | OFF Range: -100 dB to 0 dB Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:POFDm:IQOFfset?')
		return Conversions.str_to_float_or_bool(response)

	def set_iq_offset(self, iq_offset: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:POFDm:IQOFfset \n
		Snippet: driver.configure.multiEval.limit.modulation.pofdm.set_iq_offset(iq_offset = 1.0) \n
		Defines and activates an upper limit for the I/Q origin offset of 802.11p signals. \n
			:param iq_offset: (float or boolean) numeric | ON | OFF Range: -100 dB to 0 dB Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		param = Conversions.decimal_or_bool_value_to_str(iq_offset)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:POFDm:IQOFfset {param}')

	def get_cf_error(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:POFDm:CFERror \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.modulation.pofdm.get_cf_error() \n
		Defines and activates an upper limit for the center frequency error (802.11p) . \n
			:return: center_freq_error: (float or boolean) numeric | ON | OFF Range: 0 Hz to 100 MHz Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:POFDm:CFERror?')
		return Conversions.str_to_float_or_bool(response)

	def set_cf_error(self, center_freq_error: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:POFDm:CFERror \n
		Snippet: driver.configure.multiEval.limit.modulation.pofdm.set_cf_error(center_freq_error = 1.0) \n
		Defines and activates an upper limit for the center frequency error (802.11p) . \n
			:param center_freq_error: (float or boolean) numeric | ON | OFF Range: 0 Hz to 100 MHz Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		param = Conversions.decimal_or_bool_value_to_str(center_freq_error)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:POFDm:CFERror {param}')

	def get_sc_error(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:POFDm:SCERror \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.modulation.pofdm.get_sc_error() \n
		Defines and activates an upper limit for the symbol clock error (802.11p) . \n
			:return: clock_error: (float or boolean) numeric | ON | OFF Range: 0 ppm to 100 ppm, Unit: ppm Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:POFDm:SCERror?')
		return Conversions.str_to_float_or_bool(response)

	def set_sc_error(self, clock_error: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:POFDm:SCERror \n
		Snippet: driver.configure.multiEval.limit.modulation.pofdm.set_sc_error(clock_error = 1.0) \n
		Defines and activates an upper limit for the symbol clock error (802.11p) . \n
			:param clock_error: (float or boolean) numeric | ON | OFF Range: 0 ppm to 100 ppm, Unit: ppm Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		param = Conversions.decimal_or_bool_value_to_str(clock_error)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:POFDm:SCERror {param}')
