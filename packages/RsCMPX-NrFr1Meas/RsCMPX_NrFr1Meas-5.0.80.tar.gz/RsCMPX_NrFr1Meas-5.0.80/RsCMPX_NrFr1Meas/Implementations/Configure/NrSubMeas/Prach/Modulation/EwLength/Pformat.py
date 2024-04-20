from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PformatCls:
	"""Pformat commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: PFormat, default value after init: PFormat.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pformat", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_pFormat_get', 'repcap_pFormat_set', repcap.PFormat.Nr1)

	def repcap_pFormat_set(self, pFormat: repcap.PFormat) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to PFormat.Default
		Default value after init: PFormat.Nr1"""
		self._cmd_group.set_repcap_enum_value(pFormat)

	def repcap_pFormat_get(self) -> repcap.PFormat:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, evm_window_length: int, pFormat=repcap.PFormat.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:PRACh:MODulation:EWLength:PFORmat<no> \n
		Snippet: driver.configure.nrSubMeas.prach.modulation.ewLength.pformat.set(evm_window_length = 1, pFormat = repcap.PFormat.Default) \n
		No command help available \n
			:param evm_window_length: No help available
			:param pFormat: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pformat')
		"""
		param = Conversions.decimal_value_to_str(evm_window_length)
		pFormat_cmd_val = self._cmd_group.get_repcap_cmd_value(pFormat, repcap.PFormat)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:PRACh:MODulation:EWLength:PFORmat{pFormat_cmd_val} {param}')

	def get(self, pFormat=repcap.PFormat.Default) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:PRACh:MODulation:EWLength:PFORmat<no> \n
		Snippet: value: int = driver.configure.nrSubMeas.prach.modulation.ewLength.pformat.get(pFormat = repcap.PFormat.Default) \n
		No command help available \n
			:param pFormat: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pformat')
			:return: evm_window_length: No help available"""
		pFormat_cmd_val = self._cmd_group.get_repcap_cmd_value(pFormat, repcap.PFormat)
		response = self._core.io.query_str(f'CONFigure:NRSub:MEASurement<Instance>:PRACh:MODulation:EWLength:PFORmat{pFormat_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'PformatCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PformatCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
