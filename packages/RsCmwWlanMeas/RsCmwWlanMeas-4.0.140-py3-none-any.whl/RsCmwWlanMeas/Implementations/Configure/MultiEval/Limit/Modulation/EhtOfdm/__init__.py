from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EhtOfdmCls:
	"""EhtOfdm commands group definition. 6 total commands, 2 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ehtOfdm", core, parent)

	@property
	def iqOffset(self):
		"""iqOffset commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOffset'):
			from .IqOffset import IqOffsetCls
			self._iqOffset = IqOffsetCls(self._core, self._cmd_group)
		return self._iqOffset

	@property
	def cfoDistribution(self):
		"""cfoDistribution commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cfoDistribution'):
			from .CfoDistribution import CfoDistributionCls
			self._cfoDistribution = CfoDistributionCls(self._core, self._cmd_group)
		return self._cfoDistribution

	# noinspection PyTypeChecker
	class EvmAllStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Evm_Br_12: float or bool: No parameter help available
			- Evm_Qr_12: float or bool: No parameter help available
			- Evm_Qr_34: float or bool: No parameter help available
			- Evm_16_Qam_12: float or bool: No parameter help available
			- Evm_16_Qam_34: float or bool: No parameter help available
			- Evm_64_Qam_23: float or bool: No parameter help available
			- Evm_64_Qam_34: float or bool: No parameter help available
			- Evm_64_Qam_56: float or bool: No parameter help available
			- Evm_256_Qam_34: float or bool: No parameter help available
			- Evm_256_Qam_56: float or bool: No parameter help available
			- Evm_1024_Qam_34: float or bool: No parameter help available
			- Evm_1024_Qam_56: float or bool: No parameter help available
			- Evm_4096_Qam_34: float or bool: No parameter help available
			- Evm_4096_Qam_56: float or bool: No parameter help available
			- Evm_Bdcm: float or bool: No parameter help available
			- Evm_Bdcmd_Up: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Evm_Br_12'),
			ArgStruct.scalar_float_ext('Evm_Qr_12'),
			ArgStruct.scalar_float_ext('Evm_Qr_34'),
			ArgStruct.scalar_float_ext('Evm_16_Qam_12'),
			ArgStruct.scalar_float_ext('Evm_16_Qam_34'),
			ArgStruct.scalar_float_ext('Evm_64_Qam_23'),
			ArgStruct.scalar_float_ext('Evm_64_Qam_34'),
			ArgStruct.scalar_float_ext('Evm_64_Qam_56'),
			ArgStruct.scalar_float_ext('Evm_256_Qam_34'),
			ArgStruct.scalar_float_ext('Evm_256_Qam_56'),
			ArgStruct.scalar_float_ext('Evm_1024_Qam_34'),
			ArgStruct.scalar_float_ext('Evm_1024_Qam_56'),
			ArgStruct.scalar_float_ext('Evm_4096_Qam_34'),
			ArgStruct.scalar_float_ext('Evm_4096_Qam_56'),
			ArgStruct.scalar_float_ext('Evm_Bdcm'),
			ArgStruct.scalar_float_ext('Evm_Bdcmd_Up')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Evm_Br_12: float or bool = None
			self.Evm_Qr_12: float or bool = None
			self.Evm_Qr_34: float or bool = None
			self.Evm_16_Qam_12: float or bool = None
			self.Evm_16_Qam_34: float or bool = None
			self.Evm_64_Qam_23: float or bool = None
			self.Evm_64_Qam_34: float or bool = None
			self.Evm_64_Qam_56: float or bool = None
			self.Evm_256_Qam_34: float or bool = None
			self.Evm_256_Qam_56: float or bool = None
			self.Evm_1024_Qam_34: float or bool = None
			self.Evm_1024_Qam_56: float or bool = None
			self.Evm_4096_Qam_34: float or bool = None
			self.Evm_4096_Qam_56: float or bool = None
			self.Evm_Bdcm: float or bool = None
			self.Evm_Bdcmd_Up: float or bool = None

	def get_evm_all(self) -> EvmAllStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:MODulation:EHTofdm:EVMall \n
		Snippet: value: EvmAllStruct = driver.configure.multiEval.limit.modulation.ehtOfdm.get_evm_all() \n
		No command help available \n
			:return: structure: for return value, see the help for EvmAllStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:EHTofdm:EVMall?', self.__class__.EvmAllStruct())

	def set_evm_all(self, value: EvmAllStruct) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:MODulation:EHTofdm:EVMall \n
		Snippet with structure: \n
		structure = driver.configure.multiEval.limit.modulation.ehtOfdm.EvmAllStruct() \n
		structure.Evm_Br_12: float or bool = 1.0 \n
		structure.Evm_Qr_12: float or bool = 1.0 \n
		structure.Evm_Qr_34: float or bool = 1.0 \n
		structure.Evm_16_Qam_12: float or bool = 1.0 \n
		structure.Evm_16_Qam_34: float or bool = 1.0 \n
		structure.Evm_64_Qam_23: float or bool = 1.0 \n
		structure.Evm_64_Qam_34: float or bool = 1.0 \n
		structure.Evm_64_Qam_56: float or bool = 1.0 \n
		structure.Evm_256_Qam_34: float or bool = 1.0 \n
		structure.Evm_256_Qam_56: float or bool = 1.0 \n
		structure.Evm_1024_Qam_34: float or bool = 1.0 \n
		structure.Evm_1024_Qam_56: float or bool = 1.0 \n
		structure.Evm_4096_Qam_34: float or bool = 1.0 \n
		structure.Evm_4096_Qam_56: float or bool = 1.0 \n
		structure.Evm_Bdcm: float or bool = 1.0 \n
		structure.Evm_Bdcmd_Up: float or bool = 1.0 \n
		driver.configure.multiEval.limit.modulation.ehtOfdm.set_evm_all(value = structure) \n
		No command help available \n
			:param value: see the help for EvmAllStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:EHTofdm:EVMall', value)

	def get_evm_pilot(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:MODulation:EHTofdm:EVMPilot \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.modulation.ehtOfdm.get_evm_pilot() \n
		No command help available \n
			:return: evm_pilot: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:EHTofdm:EVMPilot?')
		return Conversions.str_to_float_or_bool(response)

	def set_evm_pilot(self, evm_pilot: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:MODulation:EHTofdm:EVMPilot \n
		Snippet: driver.configure.multiEval.limit.modulation.ehtOfdm.set_evm_pilot(evm_pilot = 1.0) \n
		No command help available \n
			:param evm_pilot: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(evm_pilot)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:EHTofdm:EVMPilot {param}')

	def get_cf_error(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:EHTofdm:CFERror \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.modulation.ehtOfdm.get_cf_error() \n
		No command help available \n
			:return: center_freq_error: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:EHTofdm:CFERror?')
		return Conversions.str_to_float_or_bool(response)

	def set_cf_error(self, center_freq_error: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:EHTofdm:CFERror \n
		Snippet: driver.configure.multiEval.limit.modulation.ehtOfdm.set_cf_error(center_freq_error = 1.0) \n
		No command help available \n
			:param center_freq_error: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(center_freq_error)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:EHTofdm:CFERror {param}')

	def get_sc_error(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:EHTofdm:SCERror \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.modulation.ehtOfdm.get_sc_error() \n
		No command help available \n
			:return: clock_error: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:EHTofdm:SCERror?')
		return Conversions.str_to_float_or_bool(response)

	def set_sc_error(self, clock_error: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:EHTofdm:SCERror \n
		Snippet: driver.configure.multiEval.limit.modulation.ehtOfdm.set_sc_error(clock_error = 1.0) \n
		No command help available \n
			:param clock_error: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(clock_error)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:EHTofdm:SCERror {param}')

	def clone(self) -> 'EhtOfdmCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EhtOfdmCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
