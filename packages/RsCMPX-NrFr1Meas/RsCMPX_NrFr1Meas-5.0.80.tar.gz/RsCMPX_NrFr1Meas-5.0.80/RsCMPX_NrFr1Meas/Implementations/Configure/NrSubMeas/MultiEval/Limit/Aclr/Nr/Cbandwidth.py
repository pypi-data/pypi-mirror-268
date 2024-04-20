from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CbandwidthCls:
	"""Cbandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: ChannelBw, default value after init: ChannelBw.Bw5"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cbandwidth", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_channelBw_get', 'repcap_channelBw_set', repcap.ChannelBw.Bw5)

	def repcap_channelBw_set(self, channelBw: repcap.ChannelBw) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ChannelBw.Default
		Default value after init: ChannelBw.Bw5"""
		self._cmd_group.set_repcap_enum_value(channelBw)

	def repcap_channelBw_get(self) -> repcap.ChannelBw:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, relative_level: float or bool, absolute_level: float or bool, channelBw=repcap.ChannelBw.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:ACLR:NR:CBANdwidth<bw> \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.aclr.nr.cbandwidth.set(relative_level = 1.0, absolute_level = 1.0, channelBw = repcap.ChannelBw.Default) \n
		Defines relative and absolute limits for the ACLR measured in an adjacent NR channel (for NR SA without CA) .
		The settings are defined separately for each channel bandwidth. \n
			:param relative_level: (float or boolean) Relative lower ACLR limit without test tolerance
			:param absolute_level: (float or boolean) No help available
			:param channelBw: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Cbandwidth')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('relative_level', relative_level, DataType.FloatExt), ArgSingle('absolute_level', absolute_level, DataType.FloatExt))
		channelBw_cmd_val = self._cmd_group.get_repcap_cmd_value(channelBw, repcap.ChannelBw)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:ACLR:NR:CBANdwidth{channelBw_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class CbandwidthStruct(StructBase):
		"""Response structure. Fields: \n
			- Relative_Level: float or bool: Relative lower ACLR limit without test tolerance
			- Absolute_Level: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Relative_Level'),
			ArgStruct.scalar_float_ext('Absolute_Level')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Relative_Level: float or bool = None
			self.Absolute_Level: float or bool = None

	def get(self, channelBw=repcap.ChannelBw.Default) -> CbandwidthStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:ACLR:NR:CBANdwidth<bw> \n
		Snippet: value: CbandwidthStruct = driver.configure.nrSubMeas.multiEval.limit.aclr.nr.cbandwidth.get(channelBw = repcap.ChannelBw.Default) \n
		Defines relative and absolute limits for the ACLR measured in an adjacent NR channel (for NR SA without CA) .
		The settings are defined separately for each channel bandwidth. \n
			:param channelBw: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Cbandwidth')
			:return: structure: for return value, see the help for CbandwidthStruct structure arguments."""
		channelBw_cmd_val = self._cmd_group.get_repcap_cmd_value(channelBw, repcap.ChannelBw)
		return self._core.io.query_struct(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:ACLR:NR:CBANdwidth{channelBw_cmd_val}?', self.__class__.CbandwidthStruct())

	def clone(self) -> 'CbandwidthCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CbandwidthCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
