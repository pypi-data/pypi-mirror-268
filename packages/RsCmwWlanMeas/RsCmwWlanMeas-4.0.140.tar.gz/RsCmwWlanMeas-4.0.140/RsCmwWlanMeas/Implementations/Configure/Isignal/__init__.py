from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IsignalCls:
	"""Isignal commands group definition. 13 total commands, 3 Subgroups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("isignal", core, parent)

	@property
	def tdata(self):
		"""tdata commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdata'):
			from .Tdata import TdataCls
			self._tdata = TdataCls(self._core, self._cmd_group)
		return self._tdata

	@property
	def dsss(self):
		"""dsss commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dsss'):
			from .Dsss import DsssCls
			self._dsss = DsssCls(self._core, self._cmd_group)
		return self._dsss

	@property
	def ofdm(self):
		"""ofdm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ofdm'):
			from .Ofdm import OfdmCls
			self._ofdm = OfdmCls(self._core, self._cmd_group)
		return self._ofdm

	# noinspection PyTypeChecker
	def get_standard(self) -> enums.IeeeStandard:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:ISIGnal:STANdard \n
		Snippet: value: enums.IeeeStandard = driver.configure.isignal.get_standard() \n
		Selects the IEEE 802.11 standard. Several WLAN signal properties depend on the selected standard, see 'Physical layer'.
		In the combined signal path (CSP) , consider the dependency between this parameter and the burst type, set for the RX
		frame trigger in the signaling application. See TRIGger:WLAN:SIGN<i>:RX:MACFrame:BTYPe Selecting a standard that is not
		compatible with the current scenario restores the 'Standalone' scenario. \n
			:return: standard: DSSS | LOFDm | HTOFdm | VHTofdm | HEOFdm | POFDm DSSS: 802.11b/g (DSSS) LOFDm: 802.11a/g (OFDM) HTOFdm: 802.11n VHTofdm: 802.11ac HEOFdm: 802.11ax POFDm: 802.11p
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:ISIGnal:STANdard?')
		return Conversions.str_to_scalar_enum(response, enums.IeeeStandard)

	def set_standard(self, standard: enums.IeeeStandard) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:ISIGnal:STANdard \n
		Snippet: driver.configure.isignal.set_standard(standard = enums.IeeeStandard.DSSS) \n
		Selects the IEEE 802.11 standard. Several WLAN signal properties depend on the selected standard, see 'Physical layer'.
		In the combined signal path (CSP) , consider the dependency between this parameter and the burst type, set for the RX
		frame trigger in the signaling application. See TRIGger:WLAN:SIGN<i>:RX:MACFrame:BTYPe Selecting a standard that is not
		compatible with the current scenario restores the 'Standalone' scenario. \n
			:param standard: DSSS | LOFDm | HTOFdm | VHTofdm | HEOFdm | POFDm DSSS: 802.11b/g (DSSS) LOFDm: 802.11a/g (OFDM) HTOFdm: 802.11n VHTofdm: 802.11ac HEOFdm: 802.11ax POFDm: 802.11p
		"""
		param = Conversions.enum_scalar_to_str(standard, enums.IeeeStandard)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:ISIGnal:STANdard {param}')

	# noinspection PyTypeChecker
	def get_rmode(self) -> enums.ReceiveMode:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:ISIGnal:RMODe \n
		Snippet: value: enums.ReceiveMode = driver.configure.isignal.get_rmode() \n
		Sets the receive mode. Not all standards support MIMO. If you set a standard that is incompatible with the current
		receive mode, the receive mode automatically reverts to SISO. \n
			:return: receive_mode: SISO | TMIMo | CMIMo SISO: SISO signal CMIMo: Composite MIMO TMIMo: True MIMO
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:ISIGnal:RMODe?')
		return Conversions.str_to_scalar_enum(response, enums.ReceiveMode)

	def set_rmode(self, receive_mode: enums.ReceiveMode) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:ISIGnal:RMODe \n
		Snippet: driver.configure.isignal.set_rmode(receive_mode = enums.ReceiveMode.CMIMo) \n
		Sets the receive mode. Not all standards support MIMO. If you set a standard that is incompatible with the current
		receive mode, the receive mode automatically reverts to SISO. \n
			:param receive_mode: SISO | TMIMo | CMIMo SISO: SISO signal CMIMo: Composite MIMO TMIMo: True MIMO
		"""
		param = Conversions.enum_scalar_to_str(receive_mode, enums.ReceiveMode)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:ISIGnal:RMODe {param}')

	# noinspection PyTypeChecker
	def get_elength(self) -> enums.BurstEvalLength:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:ISIGnal:ELENgth \n
		Snippet: value: enums.BurstEvalLength = driver.configure.isignal.get_elength() \n
		No command help available \n
			:return: evaluation_length: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:ISIGnal:ELENgth?')
		return Conversions.str_to_scalar_enum(response, enums.BurstEvalLength)

	def set_elength(self, evaluation_length: enums.BurstEvalLength) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:ISIGnal:ELENgth \n
		Snippet: driver.configure.isignal.set_elength(evaluation_length = enums.BurstEvalLength.REDucedburst) \n
		No command help available \n
			:param evaluation_length: No help available
		"""
		param = Conversions.enum_scalar_to_str(evaluation_length, enums.BurstEvalLength)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:ISIGnal:ELENgth {param}')

	# noinspection PyTypeChecker
	def get_btype(self) -> enums.BurstType:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:ISIGnal:BTYPe \n
		Snippet: value: enums.BurstType = driver.configure.isignal.get_btype() \n
		Sets the burst type for standard 802.11n. Do not use the command for other standards. \n
			:return: burst_type: MIXed | GREenfield MIXed: Compatibility mode, for coexistence with older standards GREenfield: Greenfield mode, incompatible with older standards
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:ISIGnal:BTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.BurstType)

	def set_btype(self, burst_type: enums.BurstType) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:ISIGnal:BTYPe \n
		Snippet: driver.configure.isignal.set_btype(burst_type = enums.BurstType.AUTO) \n
		Sets the burst type for standard 802.11n. Do not use the command for other standards. \n
			:param burst_type: MIXed | GREenfield MIXed: Compatibility mode, for coexistence with older standards GREenfield: Greenfield mode, incompatible with older standards
		"""
		param = Conversions.enum_scalar_to_str(burst_type, enums.BurstType)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:ISIGnal:BTYPe {param}')

	# noinspection PyTypeChecker
	def get_bandwidth(self) -> enums.Bandwidth:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:ISIGnal:BWIDth \n
		Snippet: value: enums.Bandwidth = driver.configure.isignal.get_bandwidth() \n
		Selects the channel bandwidth. In the combined signal path (CSP) , consider the dependency between this parameter and the
		trigger bandwidth, set for the RX frame trigger in the signaling application. See TRIGger:WLAN:SIGN<i>:RX:MACFrame:BW For
		802.11ax and trigger source set to 'HE_TB Trigger', the setting depends on the trigger configuration:
		CONFigure:WLAN:SIGN<i>:CONNection:HETF:CHBW \n
			:return: bandwidth: BW05mhz | BW10mhz | BW20mhz | BW40mhz | BW80mhz | BW16mhz | BW88mhz BW05mhz: 5 MHz BW10mhz: 10 MHz BW20mhz: 20 MHz BW40mhz: 40 MHz BW80mhz: 80 MHz BW88mhz: 80+80 MHz BW16mhz: 160 MHz
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:ISIGnal:BWIDth?')
		return Conversions.str_to_scalar_enum(response, enums.Bandwidth)

	def set_bandwidth(self, bandwidth: enums.Bandwidth) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:ISIGnal:BWIDth \n
		Snippet: driver.configure.isignal.set_bandwidth(bandwidth = enums.Bandwidth.BW05mhz) \n
		Selects the channel bandwidth. In the combined signal path (CSP) , consider the dependency between this parameter and the
		trigger bandwidth, set for the RX frame trigger in the signaling application. See TRIGger:WLAN:SIGN<i>:RX:MACFrame:BW For
		802.11ax and trigger source set to 'HE_TB Trigger', the setting depends on the trigger configuration:
		CONFigure:WLAN:SIGN<i>:CONNection:HETF:CHBW \n
			:param bandwidth: BW05mhz | BW10mhz | BW20mhz | BW40mhz | BW80mhz | BW16mhz | BW88mhz BW05mhz: 5 MHz BW10mhz: 10 MHz BW20mhz: 20 MHz BW40mhz: 40 MHz BW80mhz: 80 MHz BW88mhz: 80+80 MHz BW16mhz: 160 MHz
		"""
		param = Conversions.enum_scalar_to_str(bandwidth, enums.Bandwidth)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:ISIGnal:BWIDth {param}')

	def get_cdistance(self) -> int:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:ISIGnal:CDIStance \n
		Snippet: value: int = driver.configure.isignal.get_cdistance() \n
		Configures the distance between the center frequencies of the two 80-MHz segments for the bandwidth of 80+80 MHz. \n
			:return: channel_distance: numeric Range: 80 MHz to 940 MHz, Unit: MHz
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:ISIGnal:CDIStance?')
		return Conversions.str_to_int(response)

	def set_cdistance(self, channel_distance: int) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:ISIGnal:CDIStance \n
		Snippet: driver.configure.isignal.set_cdistance(channel_distance = 1) \n
		Configures the distance between the center frequencies of the two 80-MHz segments for the bandwidth of 80+80 MHz. \n
			:param channel_distance: numeric Range: 80 MHz to 940 MHz, Unit: MHz
		"""
		param = Conversions.decimal_value_to_str(channel_distance)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:ISIGnal:CDIStance {param}')

	# noinspection PyTypeChecker
	def get_pclass(self) -> enums.PowerClass:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:ISIGnal:PCLass \n
		Snippet: value: enums.PowerClass = driver.configure.isignal.get_pclass() \n
		Sets the STA transmit power class for 802.11p and selects the transmit spectrum mask to be applied. \n
			:return: power_class: CLA | CLB | CLCD | USERdefined CLA: class A transmit spectrum mask CLB: class B transmit spectrum mask CLCD: class C or D, no transmit spectrum limit check USERdefined: user-defined transmit spectrum mask
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:ISIGnal:PCLass?')
		return Conversions.str_to_scalar_enum(response, enums.PowerClass)

	def set_pclass(self, power_class: enums.PowerClass) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:ISIGnal:PCLass \n
		Snippet: driver.configure.isignal.set_pclass(power_class = enums.PowerClass.CLA) \n
		Sets the STA transmit power class for 802.11p and selects the transmit spectrum mask to be applied. \n
			:param power_class: CLA | CLB | CLCD | USERdefined CLA: class A transmit spectrum mask CLB: class B transmit spectrum mask CLCD: class C or D, no transmit spectrum limit check USERdefined: user-defined transmit spectrum mask
		"""
		param = Conversions.enum_scalar_to_str(power_class, enums.PowerClass)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:ISIGnal:PCLass {param}')

	def get_iqswap(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:ISIGnal:IQSWap \n
		Snippet: value: bool = driver.configure.isignal.get_iqswap() \n
		Swaps the role of the I and Q axes in the baseband. \n
			:return: iqswap: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:ISIGnal:IQSWap?')
		return Conversions.str_to_bool(response)

	def set_iqswap(self, iqswap: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:ISIGnal:IQSWap \n
		Snippet: driver.configure.isignal.set_iqswap(iqswap = False) \n
		Swaps the role of the I and Q axes in the baseband. \n
			:param iqswap: OFF | ON
		"""
		param = Conversions.bool_to_str(iqswap)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:ISIGnal:IQSWap {param}')

	# noinspection PyTypeChecker
	def get_modfilter(self) -> enums.ModulationFilter:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:ISIGnal:MODFilter \n
		Snippet: value: enums.ModulationFilter = driver.configure.isignal.get_modfilter() \n
		This command allows you to limit the evaluation to bursts of a particular modulation type. If the received burst has a
		different modulation, the reliability 'Wrong Modulation' is displayed. In the combined signal path (CSP) , consider the
		dependency between this parameter and the data rate, set for the RX frame trigger in the signaling application.
		See TRIGger:WLAN:SIGN<i>:RX:MACFrame:RATE For 802.11ax and trigger source set to 'HE_TB Trigger', the setting depends on
		the trigger configuration: CONFigure:WLAN:SIGN<i>:STA<s>:CONNection:HETF:MCS \n
			:return: modulation_filter: ALL | BPSK | QPSK | QAM16 | QAM64 | QAM256 | QAM1024 | DBPSk | DQPSk | CCK5_5 | CCK11 For OFDM: ALL | BPSK | QPSK | QAM16 | QAM64 | QAM256 | QAM1024 For DSSS: ALL | DBPSk | DQPSk | CCK5_5 | CCK11
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:ISIGnal:MODFilter?')
		return Conversions.str_to_scalar_enum(response, enums.ModulationFilter)

	def set_modfilter(self, modulation_filter: enums.ModulationFilter) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:ISIGnal:MODFilter \n
		Snippet: driver.configure.isignal.set_modfilter(modulation_filter = enums.ModulationFilter.ALL) \n
		This command allows you to limit the evaluation to bursts of a particular modulation type. If the received burst has a
		different modulation, the reliability 'Wrong Modulation' is displayed. In the combined signal path (CSP) , consider the
		dependency between this parameter and the data rate, set for the RX frame trigger in the signaling application.
		See TRIGger:WLAN:SIGN<i>:RX:MACFrame:RATE For 802.11ax and trigger source set to 'HE_TB Trigger', the setting depends on
		the trigger configuration: CONFigure:WLAN:SIGN<i>:STA<s>:CONNection:HETF:MCS \n
			:param modulation_filter: ALL | BPSK | QPSK | QAM16 | QAM64 | QAM256 | QAM1024 | DBPSk | DQPSk | CCK5_5 | CCK11 For OFDM: ALL | BPSK | QPSK | QAM16 | QAM64 | QAM256 | QAM1024 For DSSS: ALL | DBPSk | DQPSk | CCK5_5 | CCK11
		"""
		param = Conversions.enum_scalar_to_str(modulation_filter, enums.ModulationFilter)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:ISIGnal:MODFilter {param}')

	def clone(self) -> 'IsignalCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IsignalCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
