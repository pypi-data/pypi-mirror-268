from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EvMagnitudeCls:
	"""EvMagnitude commands group definition. 84 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("evMagnitude", core, parent)

	@property
	def dsss(self):
		"""dsss commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_dsss'):
			from .Dsss import DsssCls
			self._dsss = DsssCls(self._core, self._cmd_group)
		return self._dsss

	@property
	def carrier(self):
		"""carrier commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .Carrier import CarrierCls
			self._carrier = CarrierCls(self._core, self._cmd_group)
		return self._carrier

	@property
	def symbol(self):
		"""symbol commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_symbol'):
			from .Symbol import SymbolCls
			self._symbol = SymbolCls(self._core, self._cmd_group)
		return self._symbol

	@property
	def ofdm(self):
		"""ofdm commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ofdm'):
			from .Ofdm import OfdmCls
			self._ofdm = OfdmCls(self._core, self._cmd_group)
		return self._ofdm

	@property
	def nsiso(self):
		"""nsiso commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_nsiso'):
			from .Nsiso import NsisoCls
			self._nsiso = NsisoCls(self._core, self._cmd_group)
		return self._nsiso

	@property
	def acsiso(self):
		"""acsiso commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_acsiso'):
			from .Acsiso import AcsisoCls
			self._acsiso = AcsisoCls(self._core, self._cmd_group)
		return self._acsiso

	def clone(self) -> 'EvMagnitudeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EvMagnitudeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
