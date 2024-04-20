from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerCls:
	"""Power commands group definition. 12 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def rxAntenna(self):
		"""rxAntenna commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_rxAntenna'):
			from .RxAntenna import RxAntennaCls
			self._rxAntenna = RxAntennaCls(self._core, self._cmd_group)
		return self._rxAntenna

	@property
	def runit(self):
		"""runit commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_runit'):
			from .Runit import RunitCls
			self._runit = RunitCls(self._core, self._cmd_group)
		return self._runit

	def clone(self) -> 'PowerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PowerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
