from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VhtOfdmCls:
	"""VhtOfdm commands group definition. 5 total commands, 1 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vhtOfdm", core, parent)

	@property
	def iqOffset(self):
		"""iqOffset commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOffset'):
			from .IqOffset import IqOffsetCls
			self._iqOffset = IqOffsetCls(self._core, self._cmd_group)
		return self._iqOffset

	# noinspection PyTypeChecker
	class EvmAllStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Evm_Br_12: float or bool: numeric | ON | OFF Limits for BPSK, coding rate 1/2 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_Qr_12: float or bool: numeric | ON | OFF Limits for QPSK, coding rate 1/2 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_Qr_34: float or bool: numeric | ON | OFF Limits for QPSK, coding rate 3/4 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_16_Qam_12: float or bool: numeric | ON | OFF Limits for 16-QAM, coding rate 1/2 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_16_Qam_34: float or bool: numeric | ON | OFF Limits for 16-QAM, coding rate 3/4 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_64_Qam_12: float or bool: numeric | ON | OFF Limits for 64-QAM, coding rate 1/2 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_64_Qam_34: float or bool: numeric | ON | OFF Limits for 64-QAM, coding rate 3/4 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_64_Qam_56: float or bool: numeric | ON | OFF Limits for 64-QAM, coding rate 5/6 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_256_Qam_34: float or bool: numeric | ON | OFF Limits for 256-QAM, coding rate 3/4 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_256_Qam_56: float or bool: numeric | ON | OFF Limits for 256-QAM, coding rate 5/6 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_1024_Qam_34: float or bool: Optional setting parameter. numeric | ON | OFF Limits for 1024-QAM, coding rate 3/4 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_1024_Qam_56: float or bool: Optional setting parameter. numeric | ON | OFF Limits for 1024-QAM, coding rate 5/6 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Evm_Br_12'),
			ArgStruct.scalar_float_ext('Evm_Qr_12'),
			ArgStruct.scalar_float_ext('Evm_Qr_34'),
			ArgStruct.scalar_float_ext('Evm_16_Qam_12'),
			ArgStruct.scalar_float_ext('Evm_16_Qam_34'),
			ArgStruct.scalar_float_ext('Evm_64_Qam_12'),
			ArgStruct.scalar_float_ext('Evm_64_Qam_34'),
			ArgStruct.scalar_float_ext('Evm_64_Qam_56'),
			ArgStruct.scalar_float_ext('Evm_256_Qam_34'),
			ArgStruct.scalar_float_ext('Evm_256_Qam_56'),
			ArgStruct.scalar_float_ext_optional('Evm_1024_Qam_34'),
			ArgStruct.scalar_float_ext_optional('Evm_1024_Qam_56')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Evm_Br_12: float or bool = None
			self.Evm_Qr_12: float or bool = None
			self.Evm_Qr_34: float or bool = None
			self.Evm_16_Qam_12: float or bool = None
			self.Evm_16_Qam_34: float or bool = None
			self.Evm_64_Qam_12: float or bool = None
			self.Evm_64_Qam_34: float or bool = None
			self.Evm_64_Qam_56: float or bool = None
			self.Evm_256_Qam_34: float or bool = None
			self.Evm_256_Qam_56: float or bool = None
			self.Evm_1024_Qam_34: float or bool = None
			self.Evm_1024_Qam_56: float or bool = None

	def get_evm_all(self) -> EvmAllStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:MODulation:VHTofdm:EVMall \n
		Snippet: value: EvmAllStruct = driver.configure.multiEval.limit.modulation.vhtOfdm.get_evm_all() \n
		Defines and activates upper limits for the error vector magnitude (EVM) of 802.11ac data carriers. \n
			:return: structure: for return value, see the help for EvmAllStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:VHTofdm:EVMall?', self.__class__.EvmAllStruct())

	def set_evm_all(self, value: EvmAllStruct) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:MODulation:VHTofdm:EVMall \n
		Snippet with structure: \n
		structure = driver.configure.multiEval.limit.modulation.vhtOfdm.EvmAllStruct() \n
		structure.Evm_Br_12: float or bool = 1.0 \n
		structure.Evm_Qr_12: float or bool = 1.0 \n
		structure.Evm_Qr_34: float or bool = 1.0 \n
		structure.Evm_16_Qam_12: float or bool = 1.0 \n
		structure.Evm_16_Qam_34: float or bool = 1.0 \n
		structure.Evm_64_Qam_12: float or bool = 1.0 \n
		structure.Evm_64_Qam_34: float or bool = 1.0 \n
		structure.Evm_64_Qam_56: float or bool = 1.0 \n
		structure.Evm_256_Qam_34: float or bool = 1.0 \n
		structure.Evm_256_Qam_56: float or bool = 1.0 \n
		structure.Evm_1024_Qam_34: float or bool = 1.0 \n
		structure.Evm_1024_Qam_56: float or bool = 1.0 \n
		driver.configure.multiEval.limit.modulation.vhtOfdm.set_evm_all(value = structure) \n
		Defines and activates upper limits for the error vector magnitude (EVM) of 802.11ac data carriers. \n
			:param value: see the help for EvmAllStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:VHTofdm:EVMall', value)

	def get_evm_pilot(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:MODulation:VHTofdm:EVMPilot \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.modulation.vhtOfdm.get_evm_pilot() \n
		Defines and activates an upper limit for the error vector magnitude (EVM) of the pilot carriers in 802.11ac signals. \n
			:return: evm_pilot: (float or boolean) numeric | ON | OFF Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:VHTofdm:EVMPilot?')
		return Conversions.str_to_float_or_bool(response)

	def set_evm_pilot(self, evm_pilot: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:MODulation:VHTofdm:EVMPilot \n
		Snippet: driver.configure.multiEval.limit.modulation.vhtOfdm.set_evm_pilot(evm_pilot = 1.0) \n
		Defines and activates an upper limit for the error vector magnitude (EVM) of the pilot carriers in 802.11ac signals. \n
			:param evm_pilot: (float or boolean) numeric | ON | OFF Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		param = Conversions.decimal_or_bool_value_to_str(evm_pilot)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:VHTofdm:EVMPilot {param}')

	def get_cf_error(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:VHTofdm:CFERror \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.modulation.vhtOfdm.get_cf_error() \n
		Defines and activates an upper limit for the center frequency error in 802.11ac signals. \n
			:return: center_freq_error: (float or boolean) numeric | ON | OFF Note that the reset value is identical for all standards Range: 0 Hz to 100 MHz Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:VHTofdm:CFERror?')
		return Conversions.str_to_float_or_bool(response)

	def set_cf_error(self, center_freq_error: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:VHTofdm:CFERror \n
		Snippet: driver.configure.multiEval.limit.modulation.vhtOfdm.set_cf_error(center_freq_error = 1.0) \n
		Defines and activates an upper limit for the center frequency error in 802.11ac signals. \n
			:param center_freq_error: (float or boolean) numeric | ON | OFF Note that the reset value is identical for all standards Range: 0 Hz to 100 MHz Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		param = Conversions.decimal_or_bool_value_to_str(center_freq_error)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:VHTofdm:CFERror {param}')

	def get_sc_error(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:VHTofdm:SCERror \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.modulation.vhtOfdm.get_sc_error() \n
		Defines and activates an upper limit for the symbol clock error in 802.11ac signals. \n
			:return: clock_error: (float or boolean) numeric | ON | OFF Range: 0 ppm to 100 ppm, Unit: ppm Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:VHTofdm:SCERror?')
		return Conversions.str_to_float_or_bool(response)

	def set_sc_error(self, clock_error: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:VHTofdm:SCERror \n
		Snippet: driver.configure.multiEval.limit.modulation.vhtOfdm.set_sc_error(clock_error = 1.0) \n
		Defines and activates an upper limit for the symbol clock error in 802.11ac signals. \n
			:param clock_error: (float or boolean) numeric | ON | OFF Range: 0 ppm to 100 ppm, Unit: ppm Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		param = Conversions.decimal_or_bool_value_to_str(clock_error)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:VHTofdm:SCERror {param}')

	def clone(self) -> 'VhtOfdmCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = VhtOfdmCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
