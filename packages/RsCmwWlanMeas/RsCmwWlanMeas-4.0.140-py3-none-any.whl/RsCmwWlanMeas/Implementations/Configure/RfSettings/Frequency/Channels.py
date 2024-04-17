from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChannelsCls:
	"""Channels commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Channels, default value after init: Channels.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("channels", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_channels_get', 'repcap_channels_set', repcap.Channels.Nr1)

	def repcap_channels_set(self, channels: repcap.Channels) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Channels.Default
		Default value after init: Channels.Nr1"""
		self._cmd_group.set_repcap_enum_value(channels)

	def repcap_channels_get(self) -> repcap.Channels:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, channel: float, channels=repcap.Channels.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:RFSettings:FREQuency:CHANnels<Ch> \n
		Snippet: driver.configure.rfSettings.frequency.channels.set(channel = 1.0, channels = repcap.Channels.Default) \n
		The command logic depends on the standard. This description applies to the standards 802.11ac and ax. For other standards,
		see method RsCmwWlanMeas.Configure.RfSettings.Frequency.Channels.set. A setting command sets channel number <Ch> to the
		channel index <Channel>. The other 20-MHz channels of the bandwidth are configured automatically, resulting in a sequence
		of channel indices with the increment 4, see examples. A query returns the channel indices of all 20-MHz channels as
		comma-separated list.
			INTRO_CMD_HELP: Before using this command, configure the standard, the bandwidth and the band, see: \n
			- method RsCmwWlanMeas.Configure.Isignal.standard
			- method RsCmwWlanMeas.Configure.Isignal.bandwidth
			- method RsCmwWlanMeas.Configure.RfSettings.Frequency.band \n
			:param channel: numeric Channel index for the 20-MHz channel number Ch For a valid configuration, all 20-MHz channels must fit into the band. So the effective ranges depend on Ch, see table below. Range: 0 to 200
			:param channels: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Channels')
		"""
		param = Conversions.decimal_value_to_str(channel)
		channels_cmd_val = self._cmd_group.get_repcap_cmd_value(channels, repcap.Channels)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:RFSettings:FREQuency:CHANnels{channels_cmd_val} {param}')

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Channel_Other: int: No parameter help available
			- Channels: List[int]: decimal Comma-separated list of channel indices 1, 2, 4, or 8 values, see table below Range: 0 to 200"""
		__meta_args_list = [
			ArgStruct.scalar_int('Channel_Other'),
			ArgStruct('Channels', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Channel_Other: int = None
			self.Channels: List[int] = None

	def get(self, channels=repcap.Channels.Default) -> GetStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:RFSettings:FREQuency:CHANnels<Ch> \n
		Snippet: value: GetStruct = driver.configure.rfSettings.frequency.channels.get(channels = repcap.Channels.Default) \n
		The command logic depends on the standard. This description applies to the standards 802.11ac and ax. For other standards,
		see method RsCmwWlanMeas.Configure.RfSettings.Frequency.Channels.set. A setting command sets channel number <Ch> to the
		channel index <Channel>. The other 20-MHz channels of the bandwidth are configured automatically, resulting in a sequence
		of channel indices with the increment 4, see examples. A query returns the channel indices of all 20-MHz channels as
		comma-separated list.
			INTRO_CMD_HELP: Before using this command, configure the standard, the bandwidth and the band, see: \n
			- method RsCmwWlanMeas.Configure.Isignal.standard
			- method RsCmwWlanMeas.Configure.Isignal.bandwidth
			- method RsCmwWlanMeas.Configure.RfSettings.Frequency.band \n
			:param channels: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Channels')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		channels_cmd_val = self._cmd_group.get_repcap_cmd_value(channels, repcap.Channels)
		return self._core.io.query_struct(f'CONFigure:WLAN:MEASurement<Instance>:RFSettings:FREQuency:CHANnels{channels_cmd_val}?', self.__class__.GetStruct())

	def clone(self) -> 'ChannelsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ChannelsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
