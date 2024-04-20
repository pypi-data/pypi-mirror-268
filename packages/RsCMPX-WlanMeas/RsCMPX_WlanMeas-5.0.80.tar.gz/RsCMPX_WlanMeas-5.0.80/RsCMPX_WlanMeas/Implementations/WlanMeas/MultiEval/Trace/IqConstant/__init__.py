from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqConstantCls:
	"""IqConstant commands group definition. 4 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqConstant", core, parent)

	@property
	def inphase(self):
		"""inphase commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_inphase'):
			from .Inphase import InphaseCls
			self._inphase = InphaseCls(self._core, self._cmd_group)
		return self._inphase

	@property
	def quadrature(self):
		"""quadrature commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_quadrature'):
			from .Quadrature import QuadratureCls
			self._quadrature = QuadratureCls(self._core, self._cmd_group)
		return self._quadrature

	def clone(self) -> 'IqConstantCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IqConstantCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
