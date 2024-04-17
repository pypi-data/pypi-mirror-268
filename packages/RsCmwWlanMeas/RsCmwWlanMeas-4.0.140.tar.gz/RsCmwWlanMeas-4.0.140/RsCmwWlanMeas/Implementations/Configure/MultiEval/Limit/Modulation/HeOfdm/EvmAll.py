from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EvmAllCls:
	"""EvmAll commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("evmAll", core, parent)

	# noinspection PyTypeChecker
	class TbCoderateStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Cr_Bpsk: enums.Coderate: CR14dcm | CR38dcm | CR12 | CR23 | CR34 | CR56 Coding rate for BPSK modulation type CR14dcm: 1/4 DCM (coding rate 1/2 with DCM) CR38dcm: 3/8 DCM (coding rate 3/4 with DCM) CR12: 1/2 (coding rate 1/2 without DCM) CR23: 2/3 (coding rate 2/3 without DCM) CR34: 3/4 (coding rate 3/4 without DCM) CR56: 5/6 (coding rate 5/6 without DCM)
			- Cr_Qpsk: enums.Coderate: CR14dcm | CR38dcm | CR12 | CR23 | CR34 | CR56
			- Cr_16_Qam: enums.Coderate: CR14dcm | CR38dcm | CR12 | CR23 | CR34 | CR56
			- Cr_64_Qam: enums.Coderate: CR14dcm | CR38dcm | CR12 | CR23 | CR34 | CR56
			- Cr_256_Qam: enums.Coderate: CR14dcm | CR38dcm | CR12 | CR23 | CR34 | CR56
			- Cr_1024_Qam: enums.Coderate: CR14dcm | CR38dcm | CR12 | CR23 | CR34 | CR56"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Cr_Bpsk', enums.Coderate),
			ArgStruct.scalar_enum('Cr_Qpsk', enums.Coderate),
			ArgStruct.scalar_enum('Cr_16_Qam', enums.Coderate),
			ArgStruct.scalar_enum('Cr_64_Qam', enums.Coderate),
			ArgStruct.scalar_enum('Cr_256_Qam', enums.Coderate),
			ArgStruct.scalar_enum('Cr_1024_Qam', enums.Coderate)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cr_Bpsk: enums.Coderate = None
			self.Cr_Qpsk: enums.Coderate = None
			self.Cr_16_Qam: enums.Coderate = None
			self.Cr_64_Qam: enums.Coderate = None
			self.Cr_256_Qam: enums.Coderate = None
			self.Cr_1024_Qam: enums.Coderate = None

	def get_tb_coderate(self) -> TbCoderateStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMall:TBCoderate \n
		Snippet: value: TbCoderateStruct = driver.configure.multiEval.limit.modulation.heOfdm.evmAll.get_tb_coderate() \n
		Specifies the coding rate of HE TB PPDU per modulation type, used for the calculation of unused tone error limit line. \n
			:return: structure: for return value, see the help for TbCoderateStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMall:TBCoderate?', self.__class__.TbCoderateStruct())

	def set_tb_coderate(self, value: TbCoderateStruct) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMall:TBCoderate \n
		Snippet with structure: \n
		structure = driver.configure.multiEval.limit.modulation.heOfdm.evmAll.TbCoderateStruct() \n
		structure.Cr_Bpsk: enums.Coderate = enums.Coderate.AUTO \n
		structure.Cr_Qpsk: enums.Coderate = enums.Coderate.AUTO \n
		structure.Cr_16_Qam: enums.Coderate = enums.Coderate.AUTO \n
		structure.Cr_64_Qam: enums.Coderate = enums.Coderate.AUTO \n
		structure.Cr_256_Qam: enums.Coderate = enums.Coderate.AUTO \n
		structure.Cr_1024_Qam: enums.Coderate = enums.Coderate.AUTO \n
		driver.configure.multiEval.limit.modulation.heOfdm.evmAll.set_tb_coderate(value = structure) \n
		Specifies the coding rate of HE TB PPDU per modulation type, used for the calculation of unused tone error limit line. \n
			:param value: see the help for TbCoderateStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMall:TBCoderate', value)

	# noinspection PyTypeChecker
	class TbHighStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Evm_Bpsk: float or bool: numeric | ON | OFF EVM limit for BPSK Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_Qpsk: float or bool: numeric | ON | OFF EVM limit for QPSK Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_16_Qam: float or bool: numeric | ON | OFF EVM limit for 16-QAM Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_64_Qam: float or bool: numeric | ON | OFF EVM limit for 64-QAM Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_256_Qam: float or bool: numeric | ON | OFF EVM limit for 256-QAM Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_1024_Qam: float or bool: numeric | ON | OFF EVM limit for 1024-QAM Additional parameters: OFF | ON (disables | enables the limit check)"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Evm_Bpsk'),
			ArgStruct.scalar_float_ext('Evm_Qpsk'),
			ArgStruct.scalar_float_ext('Evm_16_Qam'),
			ArgStruct.scalar_float_ext('Evm_64_Qam'),
			ArgStruct.scalar_float_ext('Evm_256_Qam'),
			ArgStruct.scalar_float_ext('Evm_1024_Qam')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Evm_Bpsk: float or bool = None
			self.Evm_Qpsk: float or bool = None
			self.Evm_16_Qam: float or bool = None
			self.Evm_64_Qam: float or bool = None
			self.Evm_256_Qam: float or bool = None
			self.Evm_1024_Qam: float or bool = None

	def get_tb_high(self) -> TbHighStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMall:TBHigh \n
		Snippet: value: TbHighStruct = driver.configure.multiEval.limit.modulation.heOfdm.evmAll.get_tb_high() \n
		Sets EVM limits for HE TB PPDU when transmit power is larger than the maximum power of MCS 7. The default values are in
		line with standard IEEE Std 802.11ax-2021, table 27-49 Allowed relative constellation error versus constellation size and
		coding rate. \n
			:return: structure: for return value, see the help for TbHighStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMall:TBHigh?', self.__class__.TbHighStruct())

	def set_tb_high(self, value: TbHighStruct) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMall:TBHigh \n
		Snippet with structure: \n
		structure = driver.configure.multiEval.limit.modulation.heOfdm.evmAll.TbHighStruct() \n
		structure.Evm_Bpsk: float or bool = 1.0 \n
		structure.Evm_Qpsk: float or bool = 1.0 \n
		structure.Evm_16_Qam: float or bool = 1.0 \n
		structure.Evm_64_Qam: float or bool = 1.0 \n
		structure.Evm_256_Qam: float or bool = 1.0 \n
		structure.Evm_1024_Qam: float or bool = 1.0 \n
		driver.configure.multiEval.limit.modulation.heOfdm.evmAll.set_tb_high(value = structure) \n
		Sets EVM limits for HE TB PPDU when transmit power is larger than the maximum power of MCS 7. The default values are in
		line with standard IEEE Std 802.11ax-2021, table 27-49 Allowed relative constellation error versus constellation size and
		coding rate. \n
			:param value: see the help for TbHighStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMall:TBHigh', value)

	# noinspection PyTypeChecker
	class TbLowStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Evm_Bpsk: float or bool: numeric | ON | OFF EVM limit for BPSK Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_Qpsk: float or bool: numeric | ON | OFF EVM limit for QPSK Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_16_Qam: float or bool: numeric | ON | OFF EVM limit for 16-QAM Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_64_Qam: float or bool: numeric | ON | OFF EVM limit for 64-QAM Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_256_Qam: float or bool: numeric | ON | OFF EVM limit for 256-QAM Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_1024_Qam: float or bool: numeric | ON | OFF EVM limit for 1024-QAM Additional parameters: OFF | ON (disables | enables the limit check)"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Evm_Bpsk'),
			ArgStruct.scalar_float_ext('Evm_Qpsk'),
			ArgStruct.scalar_float_ext('Evm_16_Qam'),
			ArgStruct.scalar_float_ext('Evm_64_Qam'),
			ArgStruct.scalar_float_ext('Evm_256_Qam'),
			ArgStruct.scalar_float_ext('Evm_1024_Qam')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Evm_Bpsk: float or bool = None
			self.Evm_Qpsk: float or bool = None
			self.Evm_16_Qam: float or bool = None
			self.Evm_64_Qam: float or bool = None
			self.Evm_256_Qam: float or bool = None
			self.Evm_1024_Qam: float or bool = None

	def get_tb_low(self) -> TbLowStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMall:TBLow \n
		Snippet: value: TbLowStruct = driver.configure.multiEval.limit.modulation.heOfdm.evmAll.get_tb_low() \n
		Sets EVM limits for HE TB PPDU when transmit power is less than or equal to the maximum power of MCS 7. The default
		values are in line with standard IEEE Std 802.11ax-2021, table 27-49 Allowed relative constellation error versus
		constellation size and coding rate. \n
			:return: structure: for return value, see the help for TbLowStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMall:TBLow?', self.__class__.TbLowStruct())

	def set_tb_low(self, value: TbLowStruct) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMall:TBLow \n
		Snippet with structure: \n
		structure = driver.configure.multiEval.limit.modulation.heOfdm.evmAll.TbLowStruct() \n
		structure.Evm_Bpsk: float or bool = 1.0 \n
		structure.Evm_Qpsk: float or bool = 1.0 \n
		structure.Evm_16_Qam: float or bool = 1.0 \n
		structure.Evm_64_Qam: float or bool = 1.0 \n
		structure.Evm_256_Qam: float or bool = 1.0 \n
		structure.Evm_1024_Qam: float or bool = 1.0 \n
		driver.configure.multiEval.limit.modulation.heOfdm.evmAll.set_tb_low(value = structure) \n
		Sets EVM limits for HE TB PPDU when transmit power is less than or equal to the maximum power of MCS 7. The default
		values are in line with standard IEEE Std 802.11ax-2021, table 27-49 Allowed relative constellation error versus
		constellation size and coding rate. \n
			:param value: see the help for TbLowStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMall:TBLow', value)

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Evm_Br_14: float or bool: numeric | ON | OFF Limits for BPSK, coding rate 1/4, dual carrier modulation (DCM) Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_Br_12: float or bool: numeric | ON | OFF Limits for BPSK, coding rate 1/2 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_Qr_14: float or bool: numeric | ON | OFF Limits for QPSK, coding rate 1/4 DCM Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_Qr_12: float or bool: numeric | ON | OFF Limits for QPSK, coding rate 1/2 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_Qr_34: float or bool: numeric | ON | OFF Limits for QPSK, coding rate 3/4 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_16_Qam_14: float or bool: numeric | ON | OFF Limits for 16-QAM, coding rate 1/4 DCM Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_16_Qam_38: float or bool: numeric | ON | OFF Limits for 16-QAM, coding rate 3/8 DCM Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_16_Qam_12: float or bool: numeric | ON | OFF Limits for 16-QAM, coding rate 1/2 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_16_Qam_34: float or bool: numeric | ON | OFF Limits for 16-QAM, coding rate 3/4 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_64_Qam_23: float or bool: numeric | ON | OFF Limits for 64-QAM, coding rate 2/3 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_64_Qam_34: float or bool: numeric | ON | OFF Limits for 64-QAM, coding rate 3/4 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_64_Qam_56: float or bool: numeric | ON | OFF Limits for 64-QAM, coding rate 5/6 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_256_Qam_34: float or bool: numeric | ON | OFF Limits for 256-QAM, coding rate 3/4 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_256_Qam_56: float or bool: numeric | ON | OFF Limits for 256-QAM, coding rate 5/6 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_1024_Qam_34: float or bool: Optional setting parameter. numeric | ON | OFF Limits for 1024-QAM, coding rate 3/4 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)
			- Evm_1024_Qam_56: float or bool: Optional setting parameter. numeric | ON | OFF Limits for 1024-QAM, coding rate 5/6 Range: -100 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit check)"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Evm_Br_14'),
			ArgStruct.scalar_float_ext('Evm_Br_12'),
			ArgStruct.scalar_float_ext('Evm_Qr_14'),
			ArgStruct.scalar_float_ext('Evm_Qr_12'),
			ArgStruct.scalar_float_ext('Evm_Qr_34'),
			ArgStruct.scalar_float_ext('Evm_16_Qam_14'),
			ArgStruct.scalar_float_ext('Evm_16_Qam_38'),
			ArgStruct.scalar_float_ext('Evm_16_Qam_12'),
			ArgStruct.scalar_float_ext('Evm_16_Qam_34'),
			ArgStruct.scalar_float_ext('Evm_64_Qam_23'),
			ArgStruct.scalar_float_ext('Evm_64_Qam_34'),
			ArgStruct.scalar_float_ext('Evm_64_Qam_56'),
			ArgStruct.scalar_float_ext('Evm_256_Qam_34'),
			ArgStruct.scalar_float_ext('Evm_256_Qam_56'),
			ArgStruct.scalar_float_ext_optional('Evm_1024_Qam_34'),
			ArgStruct.scalar_float_ext_optional('Evm_1024_Qam_56')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Evm_Br_14: float or bool = None
			self.Evm_Br_12: float or bool = None
			self.Evm_Qr_14: float or bool = None
			self.Evm_Qr_12: float or bool = None
			self.Evm_Qr_34: float or bool = None
			self.Evm_16_Qam_14: float or bool = None
			self.Evm_16_Qam_38: float or bool = None
			self.Evm_16_Qam_12: float or bool = None
			self.Evm_16_Qam_34: float or bool = None
			self.Evm_64_Qam_23: float or bool = None
			self.Evm_64_Qam_34: float or bool = None
			self.Evm_64_Qam_56: float or bool = None
			self.Evm_256_Qam_34: float or bool = None
			self.Evm_256_Qam_56: float or bool = None
			self.Evm_1024_Qam_34: float or bool = None
			self.Evm_1024_Qam_56: float or bool = None

	def get_value(self) -> ValueStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMall \n
		Snippet: value: ValueStruct = driver.configure.multiEval.limit.modulation.heOfdm.evmAll.get_value() \n
		Defines and activates upper limits for the error vector magnitude (EVM) of 802.11ax data carriers. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMall?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMall \n
		Snippet with structure: \n
		structure = driver.configure.multiEval.limit.modulation.heOfdm.evmAll.ValueStruct() \n
		structure.Evm_Br_14: float or bool = 1.0 \n
		structure.Evm_Br_12: float or bool = 1.0 \n
		structure.Evm_Qr_14: float or bool = 1.0 \n
		structure.Evm_Qr_12: float or bool = 1.0 \n
		structure.Evm_Qr_34: float or bool = 1.0 \n
		structure.Evm_16_Qam_14: float or bool = 1.0 \n
		structure.Evm_16_Qam_38: float or bool = 1.0 \n
		structure.Evm_16_Qam_12: float or bool = 1.0 \n
		structure.Evm_16_Qam_34: float or bool = 1.0 \n
		structure.Evm_64_Qam_23: float or bool = 1.0 \n
		structure.Evm_64_Qam_34: float or bool = 1.0 \n
		structure.Evm_64_Qam_56: float or bool = 1.0 \n
		structure.Evm_256_Qam_34: float or bool = 1.0 \n
		structure.Evm_256_Qam_56: float or bool = 1.0 \n
		structure.Evm_1024_Qam_34: float or bool = 1.0 \n
		structure.Evm_1024_Qam_56: float or bool = 1.0 \n
		driver.configure.multiEval.limit.modulation.heOfdm.evmAll.set_value(value = structure) \n
		Defines and activates upper limits for the error vector magnitude (EVM) of 802.11ax data carriers. \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMall', value)
