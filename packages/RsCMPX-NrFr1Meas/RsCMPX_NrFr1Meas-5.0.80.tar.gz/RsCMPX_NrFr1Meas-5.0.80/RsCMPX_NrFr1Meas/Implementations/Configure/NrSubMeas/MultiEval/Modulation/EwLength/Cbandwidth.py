from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


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

	def set(self, cyc_prefix_norm_15: int, cyc_prefix_norm_30: int, cyc_prefix_norm_60: int, cyc_prefix_extend: int, channelBw=repcap.ChannelBw.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:MODulation:EWLength:CBANdwidth<bw> \n
		Snippet: driver.configure.nrSubMeas.multiEval.modulation.ewLength.cbandwidth.set(cyc_prefix_norm_15 = 1, cyc_prefix_norm_30 = 1, cyc_prefix_norm_60 = 1, cyc_prefix_extend = 1, channelBw = repcap.ChannelBw.Default) \n
		Specifies the EVM window length in samples for a selected channel bandwidth, depending on the cyclic prefix (CP) type and
		the SC spacing. \n
			:param cyc_prefix_norm_15: Samples for normal CP, 15-kHz SC spacing
			:param cyc_prefix_norm_30: Samples for normal CP, 60-kHz SC spacing
			:param cyc_prefix_norm_60: Samples for extended CP, 60-kHz SC spacing
			:param cyc_prefix_extend: No help available
			:param channelBw: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Cbandwidth')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cyc_prefix_norm_15', cyc_prefix_norm_15, DataType.Integer), ArgSingle('cyc_prefix_norm_30', cyc_prefix_norm_30, DataType.Integer), ArgSingle('cyc_prefix_norm_60', cyc_prefix_norm_60, DataType.Integer), ArgSingle('cyc_prefix_extend', cyc_prefix_extend, DataType.Integer))
		channelBw_cmd_val = self._cmd_group.get_repcap_cmd_value(channelBw, repcap.ChannelBw)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:MODulation:EWLength:CBANdwidth{channelBw_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class CbandwidthStruct(StructBase):
		"""Response structure. Fields: \n
			- Cyc_Prefix_Norm_15: int: Samples for normal CP, 15-kHz SC spacing
			- Cyc_Prefix_Norm_30: int: Samples for normal CP, 60-kHz SC spacing
			- Cyc_Prefix_Norm_60: int: Samples for extended CP, 60-kHz SC spacing
			- Cyc_Prefix_Extend: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Cyc_Prefix_Norm_15'),
			ArgStruct.scalar_int('Cyc_Prefix_Norm_30'),
			ArgStruct.scalar_int('Cyc_Prefix_Norm_60'),
			ArgStruct.scalar_int('Cyc_Prefix_Extend')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cyc_Prefix_Norm_15: int = None
			self.Cyc_Prefix_Norm_30: int = None
			self.Cyc_Prefix_Norm_60: int = None
			self.Cyc_Prefix_Extend: int = None

	def get(self, channelBw=repcap.ChannelBw.Default) -> CbandwidthStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:MODulation:EWLength:CBANdwidth<bw> \n
		Snippet: value: CbandwidthStruct = driver.configure.nrSubMeas.multiEval.modulation.ewLength.cbandwidth.get(channelBw = repcap.ChannelBw.Default) \n
		Specifies the EVM window length in samples for a selected channel bandwidth, depending on the cyclic prefix (CP) type and
		the SC spacing. \n
			:param channelBw: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Cbandwidth')
			:return: structure: for return value, see the help for CbandwidthStruct structure arguments."""
		channelBw_cmd_val = self._cmd_group.get_repcap_cmd_value(channelBw, repcap.ChannelBw)
		return self._core.io.query_struct(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:MODulation:EWLength:CBANdwidth{channelBw_cmd_val}?', self.__class__.CbandwidthStruct())

	def clone(self) -> 'CbandwidthCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CbandwidthCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
