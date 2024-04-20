from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DmrsCls:
	"""Dmrs commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dmrs", core, parent)

	@property
	def init(self):
		"""init commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_init'):
			from .Init import InitCls
			self._init = InitCls(self._core, self._cmd_group)
		return self._init

	@property
	def did(self):
		"""did commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_did'):
			from .Did import DidCls
			self._did = DidCls(self._core, self._cmd_group)
		return self._did

	def clone(self) -> 'DmrsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DmrsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
