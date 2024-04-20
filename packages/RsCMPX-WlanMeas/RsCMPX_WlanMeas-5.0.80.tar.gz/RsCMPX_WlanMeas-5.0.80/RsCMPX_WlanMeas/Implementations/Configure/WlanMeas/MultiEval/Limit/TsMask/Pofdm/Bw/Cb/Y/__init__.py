from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class YCls:
	"""Y commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("y", core, parent)

	@property
	def a(self):
		"""a commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_a'):
			from .A import ACls
			self._a = ACls(self._core, self._cmd_group)
		return self._a

	@property
	def b(self):
		"""b commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_b'):
			from .B import BCls
			self._b = BCls(self._core, self._cmd_group)
		return self._b

	@property
	def c(self):
		"""c commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_c'):
			from .C import CCls
			self._c = CCls(self._core, self._cmd_group)
		return self._c

	@property
	def d(self):
		"""d commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_d'):
			from .D import DCls
			self._d = DCls(self._core, self._cmd_group)
		return self._d

	@property
	def e(self):
		"""e commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_e'):
			from .E import ECls
			self._e = ECls(self._core, self._cmd_group)
		return self._e

	def clone(self) -> 'YCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = YCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
