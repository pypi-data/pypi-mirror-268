from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NlayersCls:
	"""Nlayers commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nlayers", core, parent)

	def set(self, number: int, carrierComponentFour=repcap.CarrierComponentFour.Nr1, allocation=repcap.Allocation.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUSCh:NLAYers \n
		Snippet: driver.configure.nrSubMeas.cc.allocation.pusch.nlayers.set(number = 1, carrierComponentFour = repcap.CarrierComponentFour.Nr1, allocation = repcap.Allocation.Default) \n
		Selects the number of layers transmitted by the UE, for carrier <no>, allocation <a>. \n
			:param number: Number of layers
			:param carrierComponentFour: optional repeated capability selector. Default value: Nr1
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
		"""
		param = Conversions.decimal_value_to_str(number)
		carrierComponentFour_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentFour, repcap.CarrierComponentFour)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponentFour_cmd_val}:ALLocation{allocation_cmd_val}:PUSCh:NLAYers {param}')

	def get(self, carrierComponentFour=repcap.CarrierComponentFour.Nr1, allocation=repcap.Allocation.Default) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUSCh:NLAYers \n
		Snippet: value: int = driver.configure.nrSubMeas.cc.allocation.pusch.nlayers.get(carrierComponentFour = repcap.CarrierComponentFour.Nr1, allocation = repcap.Allocation.Default) \n
		Selects the number of layers transmitted by the UE, for carrier <no>, allocation <a>. \n
			:param carrierComponentFour: optional repeated capability selector. Default value: Nr1
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
			:return: number: Number of layers"""
		carrierComponentFour_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentFour, repcap.CarrierComponentFour)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		response = self._core.io.query_str(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponentFour_cmd_val}:ALLocation{allocation_cmd_val}:PUSCh:NLAYers?')
		return Conversions.str_to_int(response)
