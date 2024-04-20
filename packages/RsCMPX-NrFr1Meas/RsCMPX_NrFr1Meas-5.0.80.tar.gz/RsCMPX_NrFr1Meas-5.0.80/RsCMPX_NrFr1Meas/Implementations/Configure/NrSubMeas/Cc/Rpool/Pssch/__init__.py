from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PsschCls:
	"""Pssch commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pssch", core, parent)

	@property
	def nsymbols(self):
		"""nsymbols commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nsymbols'):
			from .Nsymbols import NsymbolsCls
			self._nsymbols = NsymbolsCls(self._core, self._cmd_group)
		return self._nsymbols

	@property
	def nsubChannels(self):
		"""nsubChannels commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nsubChannels'):
			from .NsubChannels import NsubChannelsCls
			self._nsubChannels = NsubChannelsCls(self._core, self._cmd_group)
		return self._nsubChannels

	@property
	def mscheme(self):
		"""mscheme commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mscheme'):
			from .Mscheme import MschemeCls
			self._mscheme = MschemeCls(self._core, self._cmd_group)
		return self._mscheme

	@property
	def ndmrs(self):
		"""ndmrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ndmrs'):
			from .Ndmrs import NdmrsCls
			self._ndmrs = NdmrsCls(self._core, self._cmd_group)
		return self._ndmrs

	@property
	def nlayers(self):
		"""nlayers commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nlayers'):
			from .Nlayers import NlayersCls
			self._nlayers = NlayersCls(self._core, self._cmd_group)
		return self._nlayers

	@property
	def dport(self):
		"""dport commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dport'):
			from .Dport import DportCls
			self._dport = DportCls(self._core, self._cmd_group)
		return self._dport

	def clone(self) -> 'PsschCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PsschCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
