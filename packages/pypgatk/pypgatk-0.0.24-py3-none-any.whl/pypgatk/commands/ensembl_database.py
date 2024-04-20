import logging

import click

from pypgatk.commands.utils import print_help
from pypgatk.ensembl.ensembl import EnsemblDataService
from pypgatk.toolbox.general import read_yaml_from_file

log = logging.getLogger(__name__)


@click.command('ensembl-check', short_help="Command to check ensembl database for stop codons, gaps")
@click.option('-c', '--config_file',
              help='Configuration to perform Ensembl database check')
@click.option('-in', '--input_fasta', help='input_fasta file to perform the translation')
@click.option('-out', '--output', help='Output File', default="peptide-database.fa")
@click.option('-adds', '--add_stop_codons',
              help='If a stop codons is found, add a new protein with suffix (_Codon_{num})', is_flag=True)
@click.option('-aa', '--num_aa', help='Minimun number of aminoacids for a protein to be included in the database',
              default=6)
@click.pass_context
def ensembl_check(ctx, config_file, input_fasta, output, add_stop_codons, num_aa):

    config_data = None
    if config_file is not None:
        config_data = read_yaml_from_file(config_file)

    if input_fasta is None:
        print_help()

    pipeline_arguments = {EnsemblDataService.PROTEIN_DB_OUTPUT: output}

    ensembl_data_service = EnsemblDataService(config_data, pipeline_arguments)
    ensembl_data_service.check_proteindb(input_fasta, add_stop_codons, num_aa)
