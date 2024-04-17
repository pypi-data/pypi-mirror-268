from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RxAntennaCls:
	"""RxAntenna commands group definition. 48 total commands, 1 Subgroups, 0 group commands
	Repeated Capability: RxAntenna, default value after init: RxAntenna.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rxAntenna", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_rxAntenna_get', 'repcap_rxAntenna_set', repcap.RxAntenna.Nr1)

	def repcap_rxAntenna_set(self, rxAntenna: repcap.RxAntenna) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to RxAntenna.Default
		Default value after init: RxAntenna.Nr1"""
		self._cmd_group.set_repcap_enum_value(rxAntenna)

	def repcap_rxAntenna_get(self) -> repcap.RxAntenna:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def stream(self):
		"""stream commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_stream'):
			from .Stream import StreamCls
			self._stream = StreamCls(self._core, self._cmd_group)
		return self._stream

	def clone(self) -> 'RxAntennaCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RxAntennaCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
