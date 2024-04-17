from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EattenuationCls:
	"""Eattenuation commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Connector, default value after init: Connector.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eattenuation", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_connector_get', 'repcap_connector_set', repcap.Connector.Nr1)

	def repcap_connector_set(self, connector: repcap.Connector) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Connector.Default
		Default value after init: Connector.Nr1"""
		self._cmd_group.set_repcap_enum_value(connector)

	def repcap_connector_get(self) -> repcap.Connector:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, ext_attenuation: float, connector=repcap.Connector.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:RFSettings:EATTenuation<antenna> \n
		Snippet: driver.configure.rfSettings.eattenuation.set(ext_attenuation = 1.0, connector = repcap.Connector.Default) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to RF input connectors for SISO and
		MIMO connections.
		For the combined signal path scenario, use CONFigure:WLAN:SIGN<i>:RFSettings:ANTenna<n>:EATTenuation:INPut . \n
			:param ext_attenuation: numeric Range: -50 dB to 90 dB
			:param connector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Eattenuation')
		"""
		param = Conversions.decimal_value_to_str(ext_attenuation)
		connector_cmd_val = self._cmd_group.get_repcap_cmd_value(connector, repcap.Connector)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:RFSettings:EATTenuation{connector_cmd_val} {param}')

	def get(self, connector=repcap.Connector.Default) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:RFSettings:EATTenuation<antenna> \n
		Snippet: value: float = driver.configure.rfSettings.eattenuation.get(connector = repcap.Connector.Default) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to RF input connectors for SISO and
		MIMO connections.
		For the combined signal path scenario, use CONFigure:WLAN:SIGN<i>:RFSettings:ANTenna<n>:EATTenuation:INPut . \n
			:param connector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Eattenuation')
			:return: ext_attenuation: numeric Range: -50 dB to 90 dB"""
		connector_cmd_val = self._cmd_group.get_repcap_cmd_value(connector, repcap.Connector)
		response = self._core.io.query_str(f'CONFigure:WLAN:MEASurement<Instance>:RFSettings:EATTenuation{connector_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'EattenuationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EattenuationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
