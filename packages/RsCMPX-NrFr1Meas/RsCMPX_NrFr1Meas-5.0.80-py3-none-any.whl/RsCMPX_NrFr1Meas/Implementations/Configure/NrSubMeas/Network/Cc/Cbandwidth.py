from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CbandwidthCls:
	"""Cbandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cbandwidth", core, parent)

	def set(self, channel_bw: enums.ChannelBwidth, carrierComponentOne=repcap.CarrierComponentOne.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NETWork[:CC<no>]:CBANdwidth \n
		Snippet: driver.configure.nrSubMeas.network.cc.cbandwidth.set(channel_bw = enums.ChannelBwidth.B005, carrierComponentOne = repcap.CarrierComponentOne.Default) \n
		No command help available \n
			:param channel_bw: No help available
			:param carrierComponentOne: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(channel_bw, enums.ChannelBwidth)
		carrierComponentOne_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentOne, repcap.CarrierComponentOne)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:NETWork:CC{carrierComponentOne_cmd_val}:CBANdwidth {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponentOne=repcap.CarrierComponentOne.Default) -> enums.ChannelBwidth:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NETWork[:CC<no>]:CBANdwidth \n
		Snippet: value: enums.ChannelBwidth = driver.configure.nrSubMeas.network.cc.cbandwidth.get(carrierComponentOne = repcap.CarrierComponentOne.Default) \n
		No command help available \n
			:param carrierComponentOne: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: channel_bw: No help available"""
		carrierComponentOne_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentOne, repcap.CarrierComponentOne)
		response = self._core.io.query_str(f'CONFigure:NRSub:MEASurement<Instance>:NETWork:CC{carrierComponentOne_cmd_val}:CBANdwidth?')
		return Conversions.str_to_scalar_enum(response, enums.ChannelBwidth)
