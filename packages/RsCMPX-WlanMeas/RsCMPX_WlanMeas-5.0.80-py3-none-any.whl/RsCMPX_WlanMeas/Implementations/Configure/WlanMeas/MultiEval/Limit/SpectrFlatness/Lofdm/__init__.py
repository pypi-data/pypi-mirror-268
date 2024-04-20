from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LofdmCls:
	"""Lofdm commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lofdm", core, parent)

	@property
	def lower(self):
		"""lower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lower'):
			from .Lower import LowerCls
			self._lower = LowerCls(self._core, self._cmd_group)
		return self._lower

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:LOFDm:ENABle \n
		Snippet: value: bool = driver.configure.wlanMeas.multiEval.limit.spectrFlatness.lofdm.get_enable() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:LOFDm:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:LOFDm:ENABle \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.spectrFlatness.lofdm.set_enable(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:LOFDm:ENABle {param}')

	def get_upper(self) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:LOFDm:UPPer \n
		Snippet: value: float = driver.configure.wlanMeas.multiEval.limit.spectrFlatness.lofdm.get_upper() \n
		No command help available \n
			:return: upper: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:LOFDm:UPPer?')
		return Conversions.str_to_float(response)

	def set_upper(self, upper: float) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:LOFDm:UPPer \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.spectrFlatness.lofdm.set_upper(upper = 1.0) \n
		No command help available \n
			:param upper: No help available
		"""
		param = Conversions.decimal_value_to_str(upper)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:LOFDm:UPPer {param}')

	def clone(self) -> 'LofdmCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LofdmCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
