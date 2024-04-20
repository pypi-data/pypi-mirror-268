from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DsssCls:
	"""Dsss commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dsss", core, parent)

	@property
	def y(self):
		"""y commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_y'):
			from .Y import YCls
			self._y = YCls(self._core, self._cmd_group)
		return self._y

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:DSSS:ENABle \n
		Snippet: value: bool = driver.configure.wlanMeas.multiEval.limit.tsMask.dsss.get_enable() \n
		Activates or deactivates the transmit spectrum mask (transmission scheme DSSS) , i.e. the limit check. \n
			:return: spe_lim_enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:DSSS:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, spe_lim_enable: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:DSSS:ENABle \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.tsMask.dsss.set_enable(spe_lim_enable = False) \n
		Activates or deactivates the transmit spectrum mask (transmission scheme DSSS) , i.e. the limit check. \n
			:param spe_lim_enable: No help available
		"""
		param = Conversions.bool_to_str(spe_lim_enable)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:DSSS:ENABle {param}')

	def clone(self) -> 'DsssCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DsssCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
