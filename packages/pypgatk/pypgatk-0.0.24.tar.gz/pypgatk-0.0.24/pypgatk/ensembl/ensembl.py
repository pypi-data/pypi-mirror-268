import os
import gffutils
from Bio import SeqIO
from Bio.Seq import Seq
from pybedtools import BedTool
import pandas as pd
from pypgatk.toolbox.general import ParameterConfiguration


class EnsemblDataService(ParameterConfiguration):
    CONFIG_KEY_VCF = "ensembl_translation"
    INPUT_FASTA = "input_fasta"
    TRANSLATION_TABLE = "translation_table"
    MITO_TRANSLATION_TABLE = "mito_translation_table"
    HEADER_VAR_PREFIX = "protein_prefix"
    REPORT_REFERENCE_SEQ = "report_ref_seq"
    PROTEIN_DB_OUTPUT = "proteindb_output_file"
    ANNOTATION_FIELD_NAME = "annotation_field_name"
    AF_FIELD = "af_field"
    AF_THRESHOLD = "af_threshold"
    TRANSCRIPT_STR = 'transcript_str'
    CONSEQUENCE_STR = "consequence_str"
    EXCLUDE_BIOTYPES = "exclude_biotypes"
    EXCLUDE_CONSEQUENCES = "exclude_consequences"
    SKIP_INCLUDING_ALL_CDS = "skip_including_all_cds"
    INCLUDE_BIOTYPES = "include_biotypes"
    INCLUDE_CONSEQUENCES = "include_consequences"
    BIOTYPE_STR = "biotype_str"
    TRANSCRIPT_DESCRIPTION_SEP = "transcript_description_sep"
    SKIP_INCLUDING_ALL_CDSS = "skip_including_all_CDSs"
    CONFIG_KEY_DATA = "ensembl_translation"
    NUM_ORFS = "num_orfs"
    NUM_ORFS_COMPLEMENT = "num_orfs_complement"
    EXPRESSION_STR = "expression_str"
    EXPRESSION_THRESH = "expression_thresh"
    IGNORE_FILTERS = "ignore_filters"
    ACCEPTED_FILTERS = "accepted_filters"

    def __init__(self, config_file, pipeline_arguments):
        """
    Init the class with the specific parameters.
    :param config_file configuration file
    :param pipeline_arguments pipelines arguments
    """
        super(EnsemblDataService, self).__init__(self.CONFIG_KEY_DATA, config_file,
                                                 pipeline_arguments)

        self._proteindb_output = 'peptide-database.fa'
        if self.PROTEIN_DB_OUTPUT in self.get_pipeline_parameters():
            self._proteindb_output = self.get_pipeline_parameters()[self.PROTEIN_DB_OUTPUT]
        elif self.CONFIG_KEY_DATA in self.get_default_parameters() and self.PROTEIN_DB_OUTPUT in \
                self.get_default_parameters()[self.CONFIG_KEY_DATA]:
            self._proteindb_output = self.get_default_parameters()[self.CONFIG_KEY_DATA][self.PROTEIN_DB_OUTPUT]

        self._translation_table = 1
        if self.TRANSLATION_TABLE in self.get_pipeline_parameters():
            self._translation_table = self.get_pipeline_parameters()[self.TRANSLATION_TABLE]
        elif self.CONFIG_KEY_DATA in self.get_default_parameters() and self.TRANSLATION_TABLE in \
                self.get_default_parameters()[self.CONFIG_KEY_DATA]:
            self._translation_table = self.get_default_parameters()[self.CONFIG_KEY_DATA][self.TRANSLATION_TABLE]

        self._mito_translation_table = self.get_translation_properties(variable=self.MITO_TRANSLATION_TABLE,
                                                                       default_value=2)
        self._header_protein_prefix = self.get_translation_properties(variable=self.HEADER_VAR_PREFIX, default_value="var_")
        self._report_reference_seq = self.get_translation_properties(variable=self.REPORT_REFERENCE_SEQ,
                                                                     default_value=False)
        self._annotation_field_name = self.get_translation_properties(variable=self.ANNOTATION_FIELD_NAME,
                                                                      default_value='CSQ')
        self._transcript_str = self.get_translation_properties(variable=self.TRANSCRIPT_STR, default_value='FEATURE')
        self._consequence_str = self.get_translation_properties(variable=self.CONSEQUENCE_STR,
                                                                default_value='CONSEQUENCE')
        self._af_field = self.get_translation_properties(variable=self.AF_FIELD, default_value='')

        self._af_threshold = self.get_translation_properties(variable=self.AF_THRESHOLD, default_value=0.01)
        self._af_threshold = float(self._af_threshold)

        self._exclude_biotypes = self.get_multiple_options(
            self.get_translation_properties(variable=self.EXCLUDE_BIOTYPES, default_value=''))
        self._exclude_consequences = self.get_multiple_options(
            self.get_translation_properties(variable=self.EXCLUDE_CONSEQUENCES,
                                            default_value='downstream_gene_variant, upstream_gene_variant, intergenic_variant, intron_variant, synonymous_variant, regulatory_region_variant'))

        self._skip_including_all_cds = self.get_translation_properties(variable=self.SKIP_INCLUDING_ALL_CDS,
                                                                       default_value=False)
        self._include_biotypes = self.get_multiple_options(
            self.get_translation_properties(variable=self.INCLUDE_BIOTYPES,
                                            default_value='protein_coding,polymorphic_pseudogene,non_stop_decay,nonsense_mediated_decay,IG_C_gene,IG_D_gene,IG_J_gene,IG_V_gene,TR_C_gene,TR_D_gene,TR_J_gene,TR_V_gene,TEC,mRNA'))

        self._include_consequences = self.get_multiple_options(
            self.get_translation_properties(variable=self.INCLUDE_CONSEQUENCES, default_value='all'))
        self._biotype_str = self.get_translation_properties(variable=self.BIOTYPE_STR, default_value='transcript_biotype')

        self._transcript_description_sep = self.get_translation_properties(variable=self.TRANSCRIPT_DESCRIPTION_SEP,
                                                                           default_value=';')
        self._num_orfs = self.get_translation_properties(variable=self.NUM_ORFS, default_value=3)
        self._num_orfs_complement = self.get_translation_properties(variable=self.NUM_ORFS_COMPLEMENT, default_value=0)
        self._expression_str = self.get_translation_properties(variable=self.EXPRESSION_STR, default_value="")
        self._expression_thresh = self.get_translation_properties(variable=self.EXPRESSION_THRESH, default_value=5.0)

        self._ignore_filters = self.get_translation_properties(variable=self.IGNORE_FILTERS, default_value=False)

        self._accepted_filters = self.get_multiple_options(
            self.get_translation_properties(variable=self.ACCEPTED_FILTERS, default_value='PASS'))

    def get_translation_properties(self, variable, default_value):
        value_return = default_value
        if variable in self.get_pipeline_parameters():
            value_return = self.get_pipeline_parameters()[variable]
        elif self.CONFIG_KEY_DATA in self.get_default_parameters() and \
                self.CONFIG_KEY_VCF in self.get_default_parameters()[self.CONFIG_KEY_DATA] and \
                variable in self.get_default_parameters()[self.CONFIG_KEY_DATA][self.CONFIG_KEY_VCF]:
            value_return = self.get_default_parameters()[self.CONFIG_KEY_DATA][self.CONFIG_KEY_VCF][variable]
        return value_return

    def three_frame_translation(self, input_fasta):
        """
    This function translate a transcriptome into a 3'frame translation protein sequence database
    :param input_fasta: fasta input file
    :return:
    """

        input_handle = open(input_fasta, 'r')
        output_handle = open(self._proteindb_output, 'w')

        for record in SeqIO.parse(input_handle, 'fasta'):
            seq = record.seq
            RF1 = seq.translate(table=self._translation_table)
            RF2 = seq[1::].translate(table=self._translation_table)
            RF3 = seq[2::].translate(table=self._translation_table)

            if record.id == "":
                print("skip entries without id", record.description)
                continue
            output_handle.write("%s\n%s\n" % ('>' + record.id + '_RF1', RF1))
            output_handle.write("%s\n%s\n" % ('>' + record.id + '_RF2', RF2))
            output_handle.write("%s\n%s\n" % ('>' + record.id + '_RF3', RF3))

    @staticmethod
    def get_multiple_options(options_str: str):
        """
        This method takes an String like option1, option2, ... and produce and array [option1, option2,... ]
        :param options_str:
        :return: Array
        """
        return list(map(lambda x: x.strip(), options_str.split(",")))

    @staticmethod
    def check_overlap(var_start, var_end, features_info=None):
        """
    This function returns true when the variant overlaps any of the features
    :param var_start: Start location
    :param var_end: End location
    :param features_info: Feature information (default = [[0, 1, 'type']])
    :return:
    """

        if features_info is None:
            features_info = [[0, 1, 'type']]
        if var_start == -1:
            return True
        # check if the var overlaps any of the features
        for feature_pos in features_info:
            pep_start = feature_pos[0]
            pep_end = feature_pos[1]
            if var_start <= pep_start <= var_end:  # fully contained or partial overlap from the end
                return True
            elif var_start <= pep_end <= var_end:  # partial overlap in the begining
                return True
            elif pep_start <= var_start and pep_end >= var_end:  # fully covered
                return True
        return False

    @staticmethod
    def get_altseq(ref_seq, ref_allele, var_allele, var_pos, strand, features_info, cds_info=None):
        """
    The given sequence in the fasta file represents all exons of the transcript combined.
    for protein coding genes, the CDS is specified therefore the sequence position has to be
    calculated based on the CDS's positions
    However, for non-protein coding genes, the whole sequence is used
    :param ref_seq:
    :param ref_allele:
    :param var_allele:
    :param var_pos:
    :param strand:
    :param features_info:
    :param cds_info:
    :return:
    """
        if cds_info is None:
            cds_info = []
        alt_seq = ""
        if len(cds_info) == 2:
            start_coding_index = cds_info[0] - 1  # it should be index not pos
            stop_coding_index = cds_info[1]  # get end position of the  last cds
        else:
            start_coding_index = 0
            total_len = 0
            for x in features_info:
                total_len += x[1] - x[0] + 1
            stop_coding_index = total_len  # the features are sorted by end therefroe the end pos of the last item is the last coding nc

        if strand == '-':  # ge the correct orientation, because exons are oredered based on their position
            ref_seq = ref_seq[
                      ::-1]  # in order to calculate from the first base of the first feature (sorted by genomic coordinates)
            ref_allele = ref_allele.complement()  # the reverse will be done on return
            var_allele = var_allele.complement()  # the reverse will be done on return

        ref_seq = ref_seq[
                  start_coding_index:stop_coding_index]  # just keep the coding regions (mostly effective in case of protein-coding genes)
        nc_index = 0
        if len(ref_allele) == len(var_allele) or ref_allele[0] == var_allele[0]:
            for feature in features_info:  # for every exon, cds or stop codon
                if var_pos in range(feature[0], feature[
                                                    1] + 1):  # get index of the var relative to the position of the overlapping feature in the coding region
                    var_index_in_cds = nc_index + (var_pos - feature[0])
                    # modify the coding reference sequence accoding to the var_allele
                    c = len(ref_allele)
                    alt_seq = ref_seq[0:var_index_in_cds] + var_allele + ref_seq[
                                                                         var_index_in_cds + c::]  # variant and ref strand??
                    if strand == '-':
                        return ref_seq[::-1], alt_seq[::-1]
                    else:
                        return ref_seq, alt_seq

                nc_index += (feature[1] - feature[0] + 1)

        return ref_seq, alt_seq

    @staticmethod
    def parse_gtf(gene_annotations_gtf, gtf_db_file):
        """
    Convert GTF file into a FeatureDB
    :param gene_annotations_gtf:
    :param gtf_db_file:
    :return:
    """
        try:
            gffutils.create_db(gene_annotations_gtf, gtf_db_file, merge_strategy="create_unique",
                               keep_order=True, disable_infer_transcripts=True, disable_infer_genes=True,
                               verbose=True,
                               force=False)
        except Exception as e:  # already exists
            print("Database already exists: " + str(e), gtf_db_file)

        db = gffutils.FeatureDB(gtf_db_file)
        return db

    @staticmethod
    def get_features(db, feature_id, feature_types=None):
        """
    Get chr, genomic positions, strand and biotype for feature_id
    also genomic positions for all its elements (exons/cds&start_codon)
    :param db:
    :param feature_id:
    :param feature_types:
    :return:
    """

        if feature_types is None:
            feature_types = ['exon']
        try:
            feature = db[feature_id]
        except gffutils.exceptions.FeatureNotFoundError:  # remove version number from the ID
            try:
                feature = db[feature_id.split('.')[0]]
            except gffutils.exceptions.FeatureNotFoundError:
                print("""Feature {} found in fasta file but not in gtf file. Check that the fasta file and the gtf files match.
                          A common issue is when the fasta file have chromosome patches but not the gtf""".format(
                    feature_id))
                return None, None, None
        coding_features = []
        features = db.children(feature, featuretype=feature_types, order_by='end')
        for f in features:
            f_type = f.featuretype
            coding_features.append([f.start, f.end, f_type])
        return feature.chrom, feature.strand, coding_features

    @staticmethod
    def get_orfs_vcf(ref_seq: str, alt_seq: str, translation_table: int, num_orfs=1):
        """
    Translate the coding_ref and the coding_alt into ORFs
    :param ref_seq:
    :param alt_seq:
    :param translation_table:
    :param num_orfs:
    :return:
    """

        ref_orfs = []
        alt_orfs = []
        for n in range(0, num_orfs):
            ref_orfs.append(ref_seq[n::].translate(translation_table))
            alt_orfs.append(alt_seq[n::].translate(translation_table))

        return ref_orfs, alt_orfs

    @staticmethod
    def get_orfs_dna(ref_seq: str, translation_table: int, num_orfs: int, num_orfs_complement: int, to_stop: bool):
        """
    translate the coding_ref into ORFs
    """

        ref_orfs = []
        for n in range(0, num_orfs):
            ref_orfs.append(ref_seq[n::].translate(translation_table, to_stop=to_stop))

        rev_ref_seq = ref_seq.reverse_complement()
        for n in range(0, num_orfs_complement):
            ref_orfs.append(rev_ref_seq[n::].translate(translation_table, to_stop=to_stop))

        return ref_orfs

    def dnaseq_to_proteindb(self, input_fasta):
        """
    translates DNA sequences to protein sequences
    :param input_fasta: input fasta file
    :return:
    """

        seq_dict = SeqIO.index(input_fasta, "fasta")

        with open(self._proteindb_output, 'w') as prots_fn:
            for record_id in seq_dict.keys():

                ref_seq = seq_dict[record_id].seq  # get the seq and desc for the record from the fasta of the gtf
                desc = str(seq_dict[record_id].description)

                key_values = {}  # extract key=value in the desc into a dict
                sep = self._transcript_description_sep
                desc = desc.replace(' ', sep)
                for value in desc.split(sep):
                    if value.split('=')[0] == 'cds' or value.split(':')[0] == 'cds':
                        value.replace('cds', 'CDS')
                    if '=' in value:
                        key_values[value.split('=')[0]] = value.split('=')[1]
                    elif ':' in value:
                        key_values[value.split(':')[0]] = value.split(':')[1]
                    elif value.split('=')[
                        0] == 'CDS':  # when only it is specified to be a CDS, it means the whole sequence to be used
                        key_values[value.split('=')[0]] = '{}-{}'.format(1, len(ref_seq))

                feature_biotype = ""
                if self._biotype_str:
                    try:
                        feature_biotype = key_values[self._biotype_str]
                    except KeyError:
                        msg = "Biotype info was not found in the header using {} for record {} {}".format(
                            self._biotype_str,
                            record_id, desc)
                        self.get_logger().debug(msg)

                # only include features that have the specified biotypes or they have CDSs info
                if 'CDS' in key_values.keys() and (
                        not self._skip_including_all_cds or 'altORFs' in self._include_biotypes):
                    pass
                elif self._biotype_str and (feature_biotype == "" or (feature_biotype in self._exclude_biotypes or
                                                                      (feature_biotype not in self._include_biotypes and self._include_biotypes != [
                                                                          'all']))):
                    continue

                # check wether to filter on expression and if it passes
                if self._expression_str:
                    try:
                        if float(key_values[self._expression_str]) < self._expression_thresh:
                            continue
                    except KeyError:
                        msg = "Expression information not found in the fasta header with expression_str: {} for record {} {}".format(
                            self._expression_str, record_id, desc)
                        self.get_logger().debug(msg)
                        continue
                    except TypeError:
                        msg = "Expression value is not of valid type (float) at record: {} {}".format(record_id,
                                                                                                      key_values[
                                                                                                          self._expression_str])
                        self.get_logger().debug(msg)
                        continue

                # translate the whole sequences (3 ORFs) for non CDS sequences and not take alt_ORFs for CDSs
                if 'CDS' not in key_values.keys() or ('CDS' in key_values.keys() and
                                                      ('altORFs' in self._include_biotypes or
                                                       self._include_biotypes == ['all'])):
                    ref_orfs = self.get_orfs_dna(ref_seq, self._translation_table, self._num_orfs,
                                                 self._num_orfs_complement, to_stop=False)
                    self.write_output(seq_id=self._header_protein_prefix + record_id, desc=desc, seqs=ref_orfs,
                                      prots_fn=prots_fn)

                # also allow for direct translation of the CDS, when the cds info exists in the fasta header skip_including_all_cds is false
                if 'CDS' in key_values.keys() and not self._skip_including_all_cds:
                    try:
                        cds_info = [int(x) for x in key_values['CDS'].split('-')]
                        ref_seq = ref_seq[cds_info[0] - 1:cds_info[1]]
                        ref_orfs = self.get_orfs_dna(ref_seq, self._translation_table, 1, 0, to_stop=True)
                        self.write_output(seq_id=record_id, desc=desc, seqs=ref_orfs, prots_fn=prots_fn)
                    except (ValueError, IndexError, KeyError):
                        print("Could not extra cds position from fasta header for: ", record_id, desc)

        return self._proteindb_output

    @staticmethod
    def get_key(fasta_header):
        return fasta_header.split('|')[0].split(' ')[0]

    @staticmethod
    def annoate_vcf(vcf_file, gtf_file,
                    vcf_info_field_index=7, record_type_index=2,
                    gene_info_index=8, gene_info_sep=';',
                    transcript_str='transcript_id', transcript_info_sep=' ',
                    annotation_str='transcriptOverlaps'):
        """
    intersect vcf and a gtf, add ID of the overlapping transcript to the vcf INFO field
    """
        annotated_vcf = os.path.abspath(vcf_file.split('/')[-1].replace('.vcf', ''))

        BedTool(gtf_file).intersect(BedTool(vcf_file), wo=True).saveas(annotated_vcf + '_all.bed')

        muts_dict = {}
        with open(annotated_vcf + '_all.bed', 'r') as an:
            for line in an.readlines():
                sl = line.strip().split('\t')
                if sl[record_type_index].strip() != 'CDS':
                    continue
                transcript_id = 'NO_OVERLAP'

                gene_info = sl[gene_info_index].split(gene_info_sep)
                for info in gene_info:  # extract transcript id from the gtf info column
                    if info.strip().startswith(transcript_str):
                        transcript_id = info.strip().split(transcript_info_sep)[1].strip('"')
                        continue

                if transcript_id == 'NO_OVERLAP':
                    continue

                # write the mutation line as a key and set the overlapping transcriptID as its value(s)
                try:
                    muts_dict['\t'.join(sl[gene_info_index + 1:-1])].append(transcript_id)
                except KeyError:
                    muts_dict['\t'.join(sl[gene_info_index + 1:-1])] = [transcript_id]

        with open(annotated_vcf + '_annotated.vcf', 'w') as ann, open(vcf_file, 'r') as v:
            # write vcf headers to the output file
            for line in v.readlines():
                if line.startswith('#'):
                    ann.write(line)
                else:
                    # write the mutations and their overlapping transcript to output file
                    try:
                        sl = line.strip().split('\t')
                        sl[vcf_info_field_index] = '{};{}={}'.format(
                            sl[vcf_info_field_index].strip(), annotation_str,
                            ','.join(set(muts_dict[line.strip()])))
                        ann.write('\t'.join(sl) + '\n')
                    except KeyError:
                        ann.write(line)

        return annotated_vcf + '_annotated.vcf'

    @staticmethod
    def vcf_from_file(vcf_file):
        """
    Read a VCF file and return a dataframe for the records
    as well as a list for the metadata
    """

        HEADERS = {
            'CHROM': str,
            'POS': int,
            'ID': str,
            'REF': str,
            'ALT': str,
            'QUAL': str,
            'FILTER': str,
            'INFO': str,
        }

        metadata = []
        data = []
        with open(vcf_file, 'r') as vcf:
            line = vcf.readline().strip()
            while line:
                if line.startswith('#'):
                    metadata.append(line)
                else:
                    data.append(line.split('\t')[0:8])
                line = vcf.readline().strip()

        vcf_df = pd.DataFrame(data, columns=HEADERS)

        return metadata, vcf_df

    def vcf_to_proteindb(self, vcf_file, input_fasta, gene_annotations_gtf):
        """
    Generate proteins for variants by modifying sequences of affected transcripts.
    In case of already annotated variants it only considers variants within
    potential coding regions of the transcript (CDSs & stop codons for protein-coding genes,
    exons for non-protein coding genes)
    In case of not annotated variants, it considers all variants overlapping
    transcripts from the selected biotypes.
    :param vcf_file:
    :param input_fasta:
    :param gene_annotations_gtf:
    :return:
    """
        db = self.parse_gtf(gene_annotations_gtf, gene_annotations_gtf.replace('.gtf', '.db'))

        transcripts_dict = SeqIO.index(input_fasta, "fasta", key_function=self.get_key)
        # handle cases where the transcript has version in the GTF but not in the VCF
        transcript_id_mapping = {k.split('.')[0]: k for k in transcripts_dict.keys()}

        transcript_index, consequence_index, biotype_index = None, None, None
        if self._annotation_field_name:
            metadata, vcf_reader = self.vcf_from_file(vcf_file)
            annotation_cols = []
            try:
                annotation_cols = \
                    [x for x in metadata if x.startswith('##INFO=<ID={}'.format(self._annotation_field_name))][
                        0].upper().split(
                        'FORMAT')[1].strip(' ').split(':')[-1].split('=')[-1].strip(' ').split('|')
            except IndexError:
                pass

            'try to extract index of transcript ID and consequence from the VCF metadata in the header'
            try:
                transcript_index = annotation_cols.index(self._transcript_str.upper())
            except ValueError:
                msg = "Error: Unable to find {} or {} in metadata header {} of VCF file: {} ".format(
                    self._transcript_str,
                    self._consequence_str,
                    annotation_cols, vcf_file)
                self.get_logger().debug(msg)

            try:
                consequence_index = annotation_cols.index(self._consequence_str.upper())
                biotype_index = annotation_cols.index(self._biotype_str.upper())
            except ValueError:
                msg = "Error: Unable to find {} or {} in metadata header {} of VCF file: {} ".format(
                    self._transcript_str,
                    self._consequence_str,
                    annotation_cols, vcf_file)
                self.get_logger().debug(msg)

        else:
            'in case the given VCF is not annotated, annotate it by identifying the overlapping transcripts'
            vcf_file = self.annoate_vcf(vcf_file, gene_annotations_gtf)
            metadata, vcf_reader = self.vcf_from_file(vcf_file)
            self._annotation_field_name = 'transcriptOverlaps'
            transcript_index = 0

        invalid_records = {'# variants with invalid record': 0,
                           '# variants not passing Filter': 0,
                           '# variants not passing AF threshold': 0,
                           '# feature IDs from VCF that are not found in the given FASTA file': 0,
                           '# variants successfully translated': 0}

        with open(self._proteindb_output, 'w') as prots_fn:
            for idx, record in vcf_reader.iterrows():
                trans = False
                if [x for x in str(record.REF) if x not in 'ACGT']:
                    msg = "Invalid VCF record, skipping: {}".format(record)
                    invalid_records['# variants with invalid record'] += 1
                    self.get_logger().debug(msg)
                    continue

                alts = []
                for alt in record.ALT.split(','):
                    if alt is None:
                        continue
                    elif [x for x in str(alt) if x not in 'ACGT']:
                        'check if all alt alleles are nucleotides'
                        continue
                    alts.append(alt)
                if not alts:
                    msg = "Invalid VCF record, skipping: {}".format(record)
                    invalid_records['# variants with invalid record'] += 1
                    self.get_logger().debug(msg)
                    continue

                self._accepted_filters = [x.upper() for x in self._accepted_filters]
                if not self._ignore_filters and self._accepted_filters != ['ALL']:
                    if record.FILTER and record.FILTER != '.' and record.FILTER != 'NA' and record.FILTER != '':  # if not PASS: None and empty means PASS
                        filters = set(record.FILTER.upper().split(','))
                        if ';' in record.FILTER and len(filters) <= 1:
                            filters = set(record.FILTER.upper().split(';'))
                        if not filters <= set(self._accepted_filters):
                            invalid_records['# variants not passing Filter'] += 1
                            continue
                # only process variants above a given allele frequency threshold if the AF string is not empty
                if self._af_field:
                    # get AF from the INFO field
                    try:
                        af = float([x.split('=')[1] for x in record.INFO.split(';') if x.startswith(self._af_field)][0])
                    except (ValueError, IndexError):
                        invalid_records['# variants with invalid record'] += 1
                        continue

                    # check if the AF passed the threshold
                    if af < self._af_threshold:
                        invalid_records['# variants not passing AF threshold'] += 1
                        continue

                trans_table = self._translation_table
                if str(record.CHROM).lstrip('chr').upper() in ['M', 'MT']:
                    trans_table = self._mito_translation_table

                processed_transcript_allele = []
                transcript_records = []
                try:
                    transcript_records = \
                        [x.split('=')[1] for x in record.INFO.split(';') if x.startswith(self._annotation_field_name)][
                            0]
                except IndexError:  # no overlapping feature was found
                    invalid_records['# variants with invalid record'] += 1
                    msg = "skipped record {}, no annotation feature was found".format(record)
                    self.get_logger().debug(msg)
                    continue

                for transcript_record in transcript_records.split(','):
                    transcript_info = transcript_record.split('|')
                    if consequence_index:
                        try:
                            consequence = transcript_info[consequence_index]
                        except IndexError:
                            invalid_records['# variants with invalid record'] += 1
                            msg = "Give a valid index for the consequence in the INFO field for: {}".format(
                                transcript_record)
                            self.get_logger().debug(msg)
                            continue
                        except TypeError:
                            pass
                    if biotype_index:
                        try:
                            biotype = transcript_info[biotype_index]
                        except IndexError:
                            invalid_records['# variants with invalid record'] += 1
                            msg = "Give a valid index for the biotype in the INFO field for: {}".format(
                                transcript_record)
                            self.get_logger().debug(msg)
                            continue
                        except TypeError:
                            pass

                    try:
                        transcript_id = transcript_info[transcript_index]
                    except IndexError:
                        invalid_records['# variants with invalid record'] += 1
                        msg = "Give a valid index for the Transcript IDs in the INFO field for: {}".format(
                            transcript_record)
                        self.get_logger().debug(msg)
                        continue
                    if transcript_id == "":
                        continue

                    try:
                        transcript_id_v = transcript_id_mapping[transcript_id]
                    except KeyError:
                        transcript_id_v = transcript_id

                    try:
                        row = transcripts_dict[transcript_id_v]
                        ref_seq = row.seq  # get the seq and desc for the transcript from the fasta of the gtf
                        desc = str(row.description)
                    except KeyError:
                        invalid_records['# feature IDs from VCF that are not found in the given FASTA file'] += 1
                        msg = "Feature {} not found in fasta of the GTF file {}".format(transcript_id_v, record)
                        self.get_logger().debug(msg)
                        continue

                    feature_types = ['exon']
                    # check if cds info exists in the fasta header otherwise translate all exons
                    cds_info = []
                    num_orfs = 3
                    if 'CDS=' in desc:
                        try:
                            cds_info = [int(x) for x in desc.split(' ')[1].split('=')[1].split('-')]
                            feature_types = ['CDS', 'stop_codon']
                            num_orfs = 1
                        except (ValueError, IndexError):
                            msg = "Could not extra cds position from fasta header for: {}".format(desc)
                            self.get_logger().debug(msg)

                    chrom, strand, features_info = self.get_features(db,
                                                                     transcript_id_v,
                                                                     feature_types)
                    if chrom is None:  # the record info was not found
                        continue
                    # skip transcripts with unwanted consequences
                    if consequence_index:
                        if (consequence in self._exclude_consequences or
                                (consequence not in self._include_consequences and
                                 self._include_consequences != ['all'])):
                            continue

                    # skip transcripts with unwanted biotypes
                    if biotype_index:
                        if (biotype in self._exclude_biotypes or
                                (biotype not in self._include_biotypes and
                                 self._include_biotypes != ['all'])):
                            continue

                    for alt in alts:
                        if transcript_id + str(record.REF) + str(
                                alt) in processed_transcript_allele:  # because VEP reports affected transcripts per alt allele
                            continue
                        processed_transcript_allele.append(transcript_id + str(record.REF) + str(alt))

                        # for non-CDSs, only consider the exon that actually overlaps the variant
                        try:
                            overlap_flag = self.check_overlap(int(record.POS), int(record.POS) + len(alt),
                                                              features_info)
                        except TypeError:
                            invalid_records['# variants with invalid record'] += 1
                            msg = "Wrong VCF record in {}".format(record)
                            self.get_logger().debug(msg)
                            continue

                        if (chrom.lstrip("chr") == str(record.CHROM).lstrip("chr") and
                                overlap_flag):
                            coding_ref_seq, coding_alt_seq = self.get_altseq(ref_seq, Seq(str(record.REF)),
                                                                             Seq(str(alt)), int(record.POS), strand,
                                                                             features_info, cds_info)
                            if coding_alt_seq != "":
                                ref_orfs, alt_orfs = self.get_orfs_vcf(coding_ref_seq, coding_alt_seq, trans_table,
                                                                       num_orfs)
                                record_id = ""
                                if record.ID:
                                    record_id = '_' + str(record.ID)
                                self.write_output(seq_id='_'.join([self._header_protein_prefix + str(record_id),
                                                                   '.'.join([str(record.CHROM), str(record.POS),
                                                                             str(record.REF), str(alt)]),
                                                                   transcript_id_v]),
                                                  desc='',
                                                  seqs=alt_orfs,
                                                  prots_fn=prots_fn,
                                                  seqs_filter=ref_orfs)
                                trans = True

                                if self._report_reference_seq:
                                    self.write_output(seq_id=transcript_id_v,
                                                      desc='',
                                                      seqs=ref_orfs,
                                                      prots_fn=prots_fn)
                if trans:
                    invalid_records['# variants successfully translated'] += 1

        msg = "Translation summary:\n {}".format(
            '\n'.join([x + ":" + str(invalid_records[x]) for x in invalid_records.keys()]))
        self.get_logger().debug(msg)

        print(msg)
        return self._proteindb_output

    @staticmethod
    def add_protein_to_map(seq: str, new_desc_string: str, protein_id: str, proteins, output_handle):
        protein = {'description': new_desc_string, 'sequence': seq, 'accession': protein_id}
        proteins.append(protein)
        output_handle.write(">{}\t{}\n{}\n".format(protein_id, new_desc_string, seq))
        return proteins

    def check_proteindb(self, input_fasta: str = None, add_stop_codon: bool = False, num_aa: int = 6):

        input_handle = open(input_fasta, 'r')
        output_handle = open(self._proteindb_output, 'w')
        proteins = []
        pcount = 0
        stop_count = 0
        gap_count = 0
        no_met = 0
        less = 0

        for record in SeqIO.parse(input_handle, 'fasta'):

            seq = str(record.seq)
            pcount += 1

            # parse the description string into a dictionary
            new_desc_string = record.description
            new_desc_string = new_desc_string[new_desc_string.find(' ') + 1:]
            # test for odd amino acids, stop codons, gaps
            if not seq.startswith('M'):
                no_met += 1
            if seq.endswith('*'):
                seq = seq[:-1]
            if '-' in seq:
                gap_count += 1
                new_desc_string = new_desc_string + ' (Contains gaps)'
            if '*' in seq:
                stop_count += 1
                if add_stop_codon:
                    seq_list = seq.split("*")
                    codon_index = 1
                    for codon in seq_list:
                        codon_description = new_desc_string + ' codon ' + str(codon_index)
                        protein_id = record.id + '_codon_' + str(codon_index)
                        seq = codon
                        if len(seq) > num_aa:
                            proteins = self.add_protein_to_map(seq, codon_description, protein_id, proteins,
                                                               output_handle)
                        codon_index = codon_index + 1
                else:
                    cut = seq.index('*')
                    string = ' (Premature stop %s/%s)' % (cut, len(seq))
                    new_desc_string = new_desc_string + string
                    seq = seq[:cut]
                    # save the protein in list
                    if len(seq) > num_aa:
                        protein_id = record.id
                        proteins = self.add_protein_to_map(seq, new_desc_string, protein_id, proteins, output_handle)
                    else:
                        less += 1
            else:
                if len(seq) > num_aa:
                    protein_id = record.id
                    proteins = self.add_protein_to_map(seq, new_desc_string, protein_id, proteins, output_handle)
                else:
                    less += 1

        print("   translations that do not start with Met:", no_met)
        print("   translations that have premature stop codons:", stop_count)
        print("   translations that contain gaps:", gap_count)
        print("   total number of input sequences was:", pcount)
        print("   total number of sequences written was:", len(proteins))
        print("   total number of proteins less than {} aminoacids: {}".format(num_aa, less))

    @staticmethod
    def write_output(seq_id, desc, seqs, prots_fn, seqs_filter=None):
        """
    write the orfs to the output file
    :param seq_id: Sequence Accession
    :param desc: Sequence Description
    :param seqs: Sequence
    :param prots_fn:
    :param seqs_filter: filter orfs/seqs found in this list, used for alt_orfs
    :return:
    """
        if seqs_filter is None:
            seqs_filter = []
        write_i = False
        if len(seqs) > 1:  # only add _num when multiple ORFs are generated (e.g in 3 ORF)
            write_i = True

        for i, orf in enumerate(seqs):
            if orf in seqs_filter:
                continue
            if desc:
                desc = " " + desc
            if write_i:  # only add _num when multiple ORFs are generated (e.g in 3 ORF)
                prots_fn.write('>{}{}\n{}\n'.format(seq_id + "_" + str(i + 1), desc, orf))
            else:
                prots_fn.write('>{}{}\n{}\n'.format(seq_id, desc, orf))


if __name__ == '__main__':
    print("ERROR: This script is part of a pipeline collection and it is not meant to be run in stand alone mode")
