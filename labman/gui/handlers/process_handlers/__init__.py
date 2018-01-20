# ----------------------------------------------------------------------------
# Copyright (c) 2017-, labman development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from .sample_plating_process import (
    SamplePlatingProcessListHandler, SamplePlatingProcessHandler)
from .gdna_extraction_process import GDNAExtractionProcessHandler
from .gdna_compression_process import GDNAPlateCompressionProcessHandler
from .library_prep_16s_process import LibraryPrep16SProcessHandler
from .library_prep_shotgun_process import (
    LibraryPrepShotgunProcessHandler, DownloadLibraryPrepShotgunProcessHandler)
from .quantification_process import (
    QuantificationProcessParseHandler, QuantificationProcessHandler)
from .pooling_process import PoolProcessHandler
from .sequencing_process import (
    SequencingProcessHandler, DownloadSampleSheetHandler)
from .normalization_process import (
    NormalizationProcessHandler, DownloadNormalizationProcessHandler)
from .primer_working_plate_creation_process import (
    PrimerWorkingPlateCreationProcessHandler)

__all__ = ['SamplePlatingProcessListHandler', 'SamplePlatingProcessHandler',
           'GDNAExtractionProcessHandler', 'LibraryPrep16SProcessHandler',
           'QuantificationProcessParseHandler', 'QuantificationProcessHandler',
           'PoolProcessHandler', 'SequencingProcessHandler',
           'DownloadSampleSheetHandler', 'GDNAPlateCompressionProcessHandler',
           'PrimerWorkingPlateCreationProcessHandler']

PROCESS_ENDPOINTS = [
    (r"/process/sample_plating/([0-9]+)$", SamplePlatingProcessHandler),
    (r"/process/sample_plating$", SamplePlatingProcessListHandler),
    (r"/process/gdna_extraction$", GDNAExtractionProcessHandler),
    (r"/process/gdna_compression$", GDNAPlateCompressionProcessHandler),
    (r"/process/library_prep_16S$", LibraryPrep16SProcessHandler),
    (r"/process/parse_quantify$", QuantificationProcessParseHandler),
    (r"/process/quantify$", QuantificationProcessHandler),
    (r"/process/pool$", PoolProcessHandler),
    (r"/process/sequencing$", SequencingProcessHandler),
    (r"/process/library_prep_shotgun$", LibraryPrepShotgunProcessHandler),
    (r"/process/library_prep_shotgun/([0-9]+)/echo_pick_list$",
     DownloadLibraryPrepShotgunProcessHandler),
    (r"/process/sequencing/([0-9]+)/sample_sheet$",
     DownloadSampleSheetHandler),
    (r"/process/normalize$", NormalizationProcessHandler),
    (r"/process/normalize/([0-9]+)/echo_pick_list$",
     DownloadNormalizationProcessHandler),
    (r"/process/working_primers$", PrimerWorkingPlateCreationProcessHandler),
]
