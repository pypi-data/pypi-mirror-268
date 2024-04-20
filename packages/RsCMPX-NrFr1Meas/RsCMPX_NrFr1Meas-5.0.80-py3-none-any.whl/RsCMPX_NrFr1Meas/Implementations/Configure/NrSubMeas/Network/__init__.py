from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NetworkCls:
	"""Network commands group definition. 12 total commands, 4 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("network", core, parent)

	@property
	def cc(self):
		"""cc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cc'):
			from .Cc import CcCls
			self._cc = CcCls(self._core, self._cmd_group)
		return self._cc

	@property
	def ccall(self):
		"""ccall commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccall'):
			from .Ccall import CcallCls
			self._ccall = CcallCls(self._core, self._cmd_group)
		return self._ccall

	@property
	def ulDl(self):
		"""ulDl commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ulDl'):
			from .UlDl import UlDlCls
			self._ulDl = UlDlCls(self._core, self._cmd_group)
		return self._ulDl

	@property
	def prach(self):
		"""prach commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prach'):
			from .Prach import PrachCls
			self._prach = PrachCls(self._core, self._cmd_group)
		return self._prach

	def get_frequency(self) -> float:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NETWork:FREQuency \n
		Snippet: value: float = driver.configure.nrSubMeas.network.get_frequency() \n
		No command help available \n
			:return: analyzer_freq: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:NETWork:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, analyzer_freq: float) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NETWork:FREQuency \n
		Snippet: driver.configure.nrSubMeas.network.set_frequency(analyzer_freq = 1.0) \n
		No command help available \n
			:param analyzer_freq: No help available
		"""
		param = Conversions.decimal_value_to_str(analyzer_freq)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:NETWork:FREQuency {param}')

	# noinspection PyTypeChecker
	def get_band(self) -> enums.Band:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NETWork:BAND \n
		Snippet: value: enums.Band = driver.configure.nrSubMeas.network.get_band() \n
		No command help available \n
			:return: band: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:NETWork:BAND?')
		return Conversions.str_to_scalar_enum(response, enums.Band)

	def set_band(self, band: enums.Band) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NETWork:BAND \n
		Snippet: driver.configure.nrSubMeas.network.set_band(band = enums.Band.OB1) \n
		No command help available \n
			:param band: No help available
		"""
		param = Conversions.enum_scalar_to_str(band, enums.Band)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:NETWork:BAND {param}')

	# noinspection PyTypeChecker
	def get_dmode(self) -> enums.DuplexModeB:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NETWork:DMODe \n
		Snippet: value: enums.DuplexModeB = driver.configure.nrSubMeas.network.get_dmode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str_with_opc('CONFigure:NRSub:MEASurement<Instance>:NETWork:DMODe?')
		return Conversions.str_to_scalar_enum(response, enums.DuplexModeB)

	def set_dmode(self, mode: enums.DuplexModeB) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NETWork:DMODe \n
		Snippet: driver.configure.nrSubMeas.network.set_dmode(mode = enums.DuplexModeB.FDD) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.DuplexModeB)
		self._core.io.write_with_opc(f'CONFigure:NRSub:MEASurement<Instance>:NETWork:DMODe {param}')

	# noinspection PyTypeChecker
	def get_ns_value(self) -> enums.NetworkSigVal:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NETWork:NSValue \n
		Snippet: value: enums.NetworkSigVal = driver.configure.nrSubMeas.network.get_ns_value() \n
		No command help available \n
			:return: value: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:NETWork:NSValue?')
		return Conversions.str_to_scalar_enum(response, enums.NetworkSigVal)

	def set_ns_value(self, value: enums.NetworkSigVal) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NETWork:NSValue \n
		Snippet: driver.configure.nrSubMeas.network.set_ns_value(value = enums.NetworkSigVal.NS01) \n
		No command help available \n
			:param value: No help available
		"""
		param = Conversions.enum_scalar_to_str(value, enums.NetworkSigVal)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:NETWork:NSValue {param}')

	def get_nantenna(self) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NETWork:NANTenna \n
		Snippet: value: int = driver.configure.nrSubMeas.network.get_nantenna() \n
		No command help available \n
			:return: number: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:NETWork:NANTenna?')
		return Conversions.str_to_int(response)

	def set_nantenna(self, number: int) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NETWork:NANTenna \n
		Snippet: driver.configure.nrSubMeas.network.set_nantenna(number = 1) \n
		No command help available \n
			:param number: No help available
		"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:NETWork:NANTenna {param}')

	# noinspection PyTypeChecker
	def get_rfp_sharing(self) -> enums.Sharing:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NETWork:RFPSharing \n
		Snippet: value: enums.Sharing = driver.configure.nrSubMeas.network.get_rfp_sharing() \n
		No command help available \n
			:return: sharing: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:NETWork:RFPSharing?')
		return Conversions.str_to_scalar_enum(response, enums.Sharing)

	def set_rfp_sharing(self, sharing: enums.Sharing) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NETWork:RFPSharing \n
		Snippet: driver.configure.nrSubMeas.network.set_rfp_sharing(sharing = enums.Sharing.FSHared) \n
		No command help available \n
			:param sharing: No help available
		"""
		param = Conversions.enum_scalar_to_str(sharing, enums.Sharing)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:NETWork:RFPSharing {param}')

	def clone(self) -> 'NetworkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NetworkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
