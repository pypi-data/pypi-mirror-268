from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PscchCls:
	"""Pscch commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pscch", core, parent)

	@property
	def nsymbols(self):
		"""nsymbols commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nsymbols'):
			from .Nsymbols import NsymbolsCls
			self._nsymbols = NsymbolsCls(self._core, self._cmd_group)
		return self._nsymbols

	@property
	def nrb(self):
		"""nrb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nrb'):
			from .Nrb import NrbCls
			self._nrb = NrbCls(self._core, self._cmd_group)
		return self._nrb

	@property
	def did(self):
		"""did commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_did'):
			from .Did import DidCls
			self._did = DidCls(self._core, self._cmd_group)
		return self._did

	def clone(self) -> 'PscchCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PscchCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
