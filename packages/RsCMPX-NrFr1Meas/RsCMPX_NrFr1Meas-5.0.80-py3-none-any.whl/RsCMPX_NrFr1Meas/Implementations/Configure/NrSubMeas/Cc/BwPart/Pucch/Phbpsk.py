from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PhbpskCls:
	"""Phbpsk commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phbpsk", core, parent)

	def set(self, bwp: enums.BandwidthPart, pi_half_pbsk: bool, carrierComponent=repcap.CarrierComponent.Nr1) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:BWPart:PUCCh:PHBPsk \n
		Snippet: driver.configure.nrSubMeas.cc.bwPart.pucch.phbpsk.set(bwp = enums.BandwidthPart.BWP0, pi_half_pbsk = False, carrierComponent = repcap.CarrierComponent.Nr1) \n
		Specifies whether the PUCCH in the <BWP> on carrier <no> uses π/2-BPSK modulation. \n
			:param bwp: No help available
			:param pi_half_pbsk: No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('bwp', bwp, DataType.Enum, enums.BandwidthPart), ArgSingle('pi_half_pbsk', pi_half_pbsk, DataType.Boolean))
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponent_cmd_val}:BWPart:PUCCh:PHBPsk {param}'.rstrip())

	def get(self, bwp: enums.BandwidthPart, carrierComponent=repcap.CarrierComponent.Nr1) -> bool:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:BWPart:PUCCh:PHBPsk \n
		Snippet: value: bool = driver.configure.nrSubMeas.cc.bwPart.pucch.phbpsk.get(bwp = enums.BandwidthPart.BWP0, carrierComponent = repcap.CarrierComponent.Nr1) \n
		Specifies whether the PUCCH in the <BWP> on carrier <no> uses π/2-BPSK modulation. \n
			:param bwp: No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1
			:return: pi_half_pbsk: No help available"""
		param = Conversions.enum_scalar_to_str(bwp, enums.BandwidthPart)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponent_cmd_val}:BWPart:PUCCh:PHBPsk? {param}')
		return Conversions.str_to_bool(response)
