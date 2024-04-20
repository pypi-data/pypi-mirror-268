from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HeOfdmCls:
	"""HeOfdm commands group definition. 11 total commands, 4 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("heOfdm", core, parent)

	@property
	def evmAll(self):
		"""evmAll commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_evmAll'):
			from .EvmAll import EvmAllCls
			self._evmAll = EvmAllCls(self._core, self._cmd_group)
		return self._evmAll

	@property
	def evmPilot(self):
		"""evmPilot commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_evmPilot'):
			from .EvmPilot import EvmPilotCls
			self._evmPilot = EvmPilotCls(self._core, self._cmd_group)
		return self._evmPilot

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

	def get_cf_error(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:CFERror \n
		Snippet: value: float or bool = driver.configure.wlanMeas.multiEval.limit.modulation.heOfdm.get_cf_error() \n
		Defines and activates an upper limit for the center frequency error in 802.11ax signals. \n
			:return: center_freq_error: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:CFERror?')
		return Conversions.str_to_float_or_bool(response)

	def set_cf_error(self, center_freq_error: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:CFERror \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.modulation.heOfdm.set_cf_error(center_freq_error = 1.0) \n
		Defines and activates an upper limit for the center frequency error in 802.11ax signals. \n
			:param center_freq_error: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(center_freq_error)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:CFERror {param}')

	def get_sc_error(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:SCERror \n
		Snippet: value: float or bool = driver.configure.wlanMeas.multiEval.limit.modulation.heOfdm.get_sc_error() \n
		Defines and activates an upper limit for the symbol clock error in 802.11ax signals. \n
			:return: clock_error: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:SCERror?')
		return Conversions.str_to_float_or_bool(response)

	def set_sc_error(self, clock_error: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:SCERror \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.modulation.heOfdm.set_sc_error(clock_error = 1.0) \n
		Defines and activates an upper limit for the symbol clock error in 802.11ax signals. \n
			:param clock_error: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(clock_error)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:SCERror {param}')

	def clone(self) -> 'HeOfdmCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HeOfdmCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
