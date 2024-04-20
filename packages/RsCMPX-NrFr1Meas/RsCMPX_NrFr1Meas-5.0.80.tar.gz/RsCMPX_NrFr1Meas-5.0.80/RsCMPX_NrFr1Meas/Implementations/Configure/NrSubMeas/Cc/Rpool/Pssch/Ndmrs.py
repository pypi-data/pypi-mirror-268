from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NdmrsCls:
	"""Ndmrs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ndmrs", core, parent)

	def set(self, no_dmrs: int, carrierComponentOne=repcap.CarrierComponentOne.Nr1) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:RPOol:PSSCh:NDMRs \n
		Snippet: driver.configure.nrSubMeas.cc.rpool.pssch.ndmrs.set(no_dmrs = 1, carrierComponentOne = repcap.CarrierComponentOne.Nr1) \n
		No command help available \n
			:param no_dmrs: No help available
			:param carrierComponentOne: optional repeated capability selector. Default value: Nr1
		"""
		param = Conversions.decimal_value_to_str(no_dmrs)
		carrierComponentOne_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentOne, repcap.CarrierComponentOne)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponentOne_cmd_val}:RPOol:PSSCh:NDMRs {param}')

	def get(self, carrierComponentOne=repcap.CarrierComponentOne.Nr1) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:RPOol:PSSCh:NDMRs \n
		Snippet: value: int = driver.configure.nrSubMeas.cc.rpool.pssch.ndmrs.get(carrierComponentOne = repcap.CarrierComponentOne.Nr1) \n
		No command help available \n
			:param carrierComponentOne: optional repeated capability selector. Default value: Nr1
			:return: no_dmrs: No help available"""
		carrierComponentOne_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentOne, repcap.CarrierComponentOne)
		response = self._core.io.query_str(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponentOne_cmd_val}:RPOol:PSSCh:NDMRs?')
		return Conversions.str_to_int(response)
