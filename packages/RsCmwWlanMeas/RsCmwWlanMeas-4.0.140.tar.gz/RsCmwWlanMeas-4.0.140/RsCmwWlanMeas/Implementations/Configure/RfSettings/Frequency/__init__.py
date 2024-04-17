from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 4 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	@property
	def channels(self):
		"""channels commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channels'):
			from .Channels import ChannelsCls
			self._channels = ChannelsCls(self._core, self._cmd_group)
		return self._channels

	# noinspection PyTypeChecker
	def get_schannel(self) -> enums.SlopeType:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:RFSettings:FREQuency:SCHannel \n
		Snippet: value: enums.SlopeType = driver.configure.rfSettings.frequency.get_schannel() \n
		Sets the position of the secondary channel relative to the primary channel for 40 MHz 802.11n signals. \n
			:return: second_channel: POSitive | NEGative POSitive: Secondary channel right above the primary channel NEGative: Secondary channel right below the primary channel
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:RFSettings:FREQuency:SCHannel?')
		return Conversions.str_to_scalar_enum(response, enums.SlopeType)

	def set_schannel(self, second_channel: enums.SlopeType) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:RFSettings:FREQuency:SCHannel \n
		Snippet: driver.configure.rfSettings.frequency.set_schannel(second_channel = enums.SlopeType.NEGative) \n
		Sets the position of the secondary channel relative to the primary channel for 40 MHz 802.11n signals. \n
			:param second_channel: POSitive | NEGative POSitive: Secondary channel right above the primary channel NEGative: Secondary channel right below the primary channel
		"""
		param = Conversions.enum_scalar_to_str(second_channel, enums.SlopeType)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:RFSettings:FREQuency:SCHannel {param}')

	# noinspection PyTypeChecker
	def get_band(self) -> enums.FrequencyBand:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:RFSettings:FREQuency:BAND \n
		Snippet: value: enums.FrequencyBand = driver.configure.rfSettings.frequency.get_band() \n
		Selects the frequency band. \n
			:return: freq_band: B24Ghz | B5GHz | B4GHz B24Ghz: 2.4 GHz band B4GHz: 4 GHz band B5GHz: 5 GHz band
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:RFSettings:FREQuency:BAND?')
		return Conversions.str_to_scalar_enum(response, enums.FrequencyBand)

	def set_band(self, freq_band: enums.FrequencyBand) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:RFSettings:FREQuency:BAND \n
		Snippet: driver.configure.rfSettings.frequency.set_band(freq_band = enums.FrequencyBand.B24Ghz) \n
		Selects the frequency band. \n
			:param freq_band: B24Ghz | B5GHz | B4GHz B24Ghz: 2.4 GHz band B4GHz: 4 GHz band B5GHz: 5 GHz band
		"""
		param = Conversions.enum_scalar_to_str(freq_band, enums.FrequencyBand)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:RFSettings:FREQuency:BAND {param}')

	def get_value(self) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:RFSettings:FREQuency \n
		Snippet: value: float = driver.configure.rfSettings.frequency.get_value() \n
		Configures the center frequency of the RF analyzer. Set it to the center frequency of the received 20-MHz, 40-MHz, 80-MHz,
		or 160-MHz WLAN channel. For 80+80 MHz signals, set the center frequency of the left segment. The frequency of the right
		segment is calculated using channel distance, see method RsCmwWlanMeas.Configure.Isignal.cdistance.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:WLAN:SIGN<i>:RFSettings:FREQuency
			- CONFigure:WLAN:SIGN<i>:RFSettings:CHANnel
		For the supported frequency range, see 'Frequency ranges'. \n
			:return: frequency: numeric Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:RFSettings:FREQuency?')
		return Conversions.str_to_float(response)

	def set_value(self, frequency: float) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:RFSettings:FREQuency \n
		Snippet: driver.configure.rfSettings.frequency.set_value(frequency = 1.0) \n
		Configures the center frequency of the RF analyzer. Set it to the center frequency of the received 20-MHz, 40-MHz, 80-MHz,
		or 160-MHz WLAN channel. For 80+80 MHz signals, set the center frequency of the left segment. The frequency of the right
		segment is calculated using channel distance, see method RsCmwWlanMeas.Configure.Isignal.cdistance.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:WLAN:SIGN<i>:RFSettings:FREQuency
			- CONFigure:WLAN:SIGN<i>:RFSettings:CHANnel
		For the supported frequency range, see 'Frequency ranges'. \n
			:param frequency: numeric Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:RFSettings:FREQuency {param}')

	def clone(self) -> 'FrequencyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FrequencyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
