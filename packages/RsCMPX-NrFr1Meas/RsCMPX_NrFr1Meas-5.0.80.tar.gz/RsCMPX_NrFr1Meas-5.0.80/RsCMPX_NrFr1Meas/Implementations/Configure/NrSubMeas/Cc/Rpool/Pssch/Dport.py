from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DportCls:
	"""Dport commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dport", core, parent)

	def set(self, dmrs_port: enums.DmrsPort, carrierComponentOne=repcap.CarrierComponentOne.Nr1) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:RPOol:PSSCh:DPORt \n
		Snippet: driver.configure.nrSubMeas.cc.rpool.pssch.dport.set(dmrs_port = enums.DmrsPort.ALL, carrierComponentOne = repcap.CarrierComponentOne.Nr1) \n
		No command help available \n
			:param dmrs_port: No help available
			:param carrierComponentOne: optional repeated capability selector. Default value: Nr1
		"""
		param = Conversions.enum_scalar_to_str(dmrs_port, enums.DmrsPort)
		carrierComponentOne_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentOne, repcap.CarrierComponentOne)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponentOne_cmd_val}:RPOol:PSSCh:DPORt {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponentOne=repcap.CarrierComponentOne.Nr1) -> enums.DmrsPort:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:RPOol:PSSCh:DPORt \n
		Snippet: value: enums.DmrsPort = driver.configure.nrSubMeas.cc.rpool.pssch.dport.get(carrierComponentOne = repcap.CarrierComponentOne.Nr1) \n
		No command help available \n
			:param carrierComponentOne: optional repeated capability selector. Default value: Nr1
			:return: dmrs_port: No help available"""
		carrierComponentOne_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentOne, repcap.CarrierComponentOne)
		response = self._core.io.query_str(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponentOne_cmd_val}:RPOol:PSSCh:DPORt?')
		return Conversions.str_to_scalar_enum(response, enums.DmrsPort)
