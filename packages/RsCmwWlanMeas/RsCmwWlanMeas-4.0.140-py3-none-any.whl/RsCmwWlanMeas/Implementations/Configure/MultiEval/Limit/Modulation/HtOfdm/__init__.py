from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HtOfdmCls:
	"""HtOfdm commands group definition. 5 total commands, 1 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("htOfdm", core, parent)

	@property
	def iqOffset(self):
		"""iqOffset commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOffset'):
			from .IqOffset import IqOffsetCls
			self._iqOffset = IqOffsetCls(self._core, self._cmd_group)
		return self._iqOffset

	# noinspection PyTypeChecker
	class EvmStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Evm_Br_12: float or bool: numeric | ON | OFF Limits for BPSK, coding rate 1/2 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_Qr_12: float or bool: numeric | ON | OFF Limits for QPSK, coding rate 1/2 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_Qr_34: float or bool: numeric | ON | OFF Limits for QPSK, coding rate 3/4 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_Q_1_M_12: float or bool: numeric | ON | OFF Limits for 16-QAM, coding rate 1/2 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_Q_1_M_34: float or bool: numeric | ON | OFF Limits for 16-QAM, coding rate 3/4 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_Q_6_M_12: float or bool: numeric | ON | OFF Limits for 64-QAM, coding rate 1/2 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_Q_6_M_34: float or bool: numeric | ON | OFF Limits for 64-QAM, coding rate 3/4 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_Q_6_M_56: float or bool: numeric | ON | OFF Limits for 64-QAM, coding rate 5/6 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Evm_Br_12'),
			ArgStruct.scalar_float_ext('Evm_Qr_12'),
			ArgStruct.scalar_float_ext('Evm_Qr_34'),
			ArgStruct.scalar_float_ext('Evm_Q_1_M_12'),
			ArgStruct.scalar_float_ext('Evm_Q_1_M_34'),
			ArgStruct.scalar_float_ext('Evm_Q_6_M_12'),
			ArgStruct.scalar_float_ext('Evm_Q_6_M_34'),
			ArgStruct.scalar_float_ext('Evm_Q_6_M_56')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Evm_Br_12: float or bool = None
			self.Evm_Qr_12: float or bool = None
			self.Evm_Qr_34: float or bool = None
			self.Evm_Q_1_M_12: float or bool = None
			self.Evm_Q_1_M_34: float or bool = None
			self.Evm_Q_6_M_12: float or bool = None
			self.Evm_Q_6_M_34: float or bool = None
			self.Evm_Q_6_M_56: float or bool = None

	def get_evm(self) -> EvmStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HTOFdm:EVM \n
		Snippet: value: EvmStruct = driver.configure.multiEval.limit.modulation.htOfdm.get_evm() \n
		Defines and activates upper limits for the error vector magnitude (EVM) of the data carriers (802.11n) . \n
			:return: structure: for return value, see the help for EvmStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HTOFdm:EVM?', self.__class__.EvmStruct())

	def set_evm(self, value: EvmStruct) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HTOFdm:EVM \n
		Snippet with structure: \n
		structure = driver.configure.multiEval.limit.modulation.htOfdm.EvmStruct() \n
		structure.Evm_Br_12: float or bool = 1.0 \n
		structure.Evm_Qr_12: float or bool = 1.0 \n
		structure.Evm_Qr_34: float or bool = 1.0 \n
		structure.Evm_Q_1_M_12: float or bool = 1.0 \n
		structure.Evm_Q_1_M_34: float or bool = 1.0 \n
		structure.Evm_Q_6_M_12: float or bool = 1.0 \n
		structure.Evm_Q_6_M_34: float or bool = 1.0 \n
		structure.Evm_Q_6_M_56: float or bool = 1.0 \n
		driver.configure.multiEval.limit.modulation.htOfdm.set_evm(value = structure) \n
		Defines and activates upper limits for the error vector magnitude (EVM) of the data carriers (802.11n) . \n
			:param value: see the help for EvmStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HTOFdm:EVM', value)

	def get_evm_pilot(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HTOFdm:EVMPilot \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.modulation.htOfdm.get_evm_pilot() \n
		Defines and activates an upper limit for the error vector magnitude (EVM) of the pilot carriers (802.11n) . \n
			:return: evm_pilot: (float or boolean) numeric | ON | OFF Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HTOFdm:EVMPilot?')
		return Conversions.str_to_float_or_bool(response)

	def set_evm_pilot(self, evm_pilot: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HTOFdm:EVMPilot \n
		Snippet: driver.configure.multiEval.limit.modulation.htOfdm.set_evm_pilot(evm_pilot = 1.0) \n
		Defines and activates an upper limit for the error vector magnitude (EVM) of the pilot carriers (802.11n) . \n
			:param evm_pilot: (float or boolean) numeric | ON | OFF Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		param = Conversions.decimal_or_bool_value_to_str(evm_pilot)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HTOFdm:EVMPilot {param}')

	def get_cf_error(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HTOFdm:CFERror \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.modulation.htOfdm.get_cf_error() \n
		Defines and activates an upper limit for the center frequency error (802.11n) . \n
			:return: center_freq_error: (float or boolean) numeric | ON | OFF Range: 0 Hz to 100 MHz Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HTOFdm:CFERror?')
		return Conversions.str_to_float_or_bool(response)

	def set_cf_error(self, center_freq_error: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HTOFdm:CFERror \n
		Snippet: driver.configure.multiEval.limit.modulation.htOfdm.set_cf_error(center_freq_error = 1.0) \n
		Defines and activates an upper limit for the center frequency error (802.11n) . \n
			:param center_freq_error: (float or boolean) numeric | ON | OFF Range: 0 Hz to 100 MHz Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		param = Conversions.decimal_or_bool_value_to_str(center_freq_error)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HTOFdm:CFERror {param}')

	def get_sc_error(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HTOFdm:SCERror \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.modulation.htOfdm.get_sc_error() \n
		Defines and activates an upper limit for the symbol clock error (802.11n) . \n
			:return: clock_error: (float or boolean) numeric | ON | OFF Range: 0 ppm to 100 ppm, Unit: ppm Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HTOFdm:SCERror?')
		return Conversions.str_to_float_or_bool(response)

	def set_sc_error(self, clock_error: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HTOFdm:SCERror \n
		Snippet: driver.configure.multiEval.limit.modulation.htOfdm.set_sc_error(clock_error = 1.0) \n
		Defines and activates an upper limit for the symbol clock error (802.11n) . \n
			:param clock_error: (float or boolean) numeric | ON | OFF Range: 0 ppm to 100 ppm, Unit: ppm Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		param = Conversions.decimal_or_bool_value_to_str(clock_error)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HTOFdm:SCERror {param}')

	def clone(self) -> 'HtOfdmCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HtOfdmCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
