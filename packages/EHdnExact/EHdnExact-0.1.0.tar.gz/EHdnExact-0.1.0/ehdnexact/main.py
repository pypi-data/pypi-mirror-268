import argparse
import logging
from Bio import Align, Seq
import pysam
from tqdm import tqdm

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def find_repeat_indices(seq, motif, aligner):
    max_num_repeats = len(seq) // len(motif) + 1
    target_seq = motif * max_num_repeats

    alignment = aligner.align(target_seq, seq)[0]
    _, indices = alignment.aligned

    if len(indices) == 0:
        raise Exception("No alignment found")

    return indices[0]


def process_single_locus(locus, reference, aligner, error_margin=1000, revcomp=False):
    contig, ehdn_start, ehdn_end, motif = locus

    if revcomp:
        motif = str(Seq.Seq(motif).reverse_complement())

    search_start = max(0, ehdn_start - error_margin)
    search_end = ehdn_end + error_margin

    search_seq = reference.fetch(contig, search_start, search_end)
    seq_start, seq_end = find_repeat_indices(search_seq, motif, aligner)
    ref_seq = search_seq[seq_start:seq_end]
    exact_start, exact_end = seq_start + search_start, seq_end + search_start

    return exact_start, exact_end, ref_seq


def process_all_loci(
    loci,
    reference,
    aligner,
    output_path,
    error_margin=1000,
    ref_seq=False,
    min_repeats=2,
):
    with open(output_path, "w") as output:
        header = "contig\tstart\tend\tmotif\texact_start\texact_end\tmotif"
        if ref_seq:
            header += "\tref_seq"
        output.write(header)

        for locus in tqdm(loci):
            contig, ehdn_start, ehdn_end, motif = locus

            try:
                exact_start, exact_end, ref_seq = process_single_locus(
                    locus, reference, aligner, error_margin
                )
            except Exception as e:
                logging.error(f"Error: {e}")
                exact_len = -1

            try:
                exact_start_rc, exact_end_rc, ref_seq_rc = process_single_locus(
                    locus, reference, aligner, error_margin, revcomp=True
                )
            except Exception as e:
                logging.error(f"Error: {e}")
                exact_len_rc = -1

            exact_len = exact_end - exact_start
            exact_len_rc = exact_end_rc - exact_start_rc

            if exact_len >= exact_len_rc:
                longer_exact_start = exact_start
                longer_exact_end = exact_end
                longer_ref_seq = ref_seq
                longer_exact_len = exact_len
            else:
                longer_exact_start = exact_start_rc
                longer_exact_end = exact_end_rc
                longer_ref_seq = ref_seq_rc
                longer_exact_len = exact_len_rc

            min_len_to_pass = min_repeats * len(motif)
            if longer_exact_len > 0 and longer_exact_len >= min_len_to_pass:
                to_write = f"\n{contig}\t{ehdn_start}\t{ehdn_end}\t{longer_exact_start}\t{longer_exact_end}\t{motif}"
                if ref_seq:
                    to_write += f"\t{longer_ref_seq}"
                output.write(to_write)


def load_loci(loci_path):
    loci = []
    with open(loci_path, "r") as file:
        next(file)  # Skip the header
        for line in file:
            line = line.strip()
            if len(line) == 0:
                continue
            row = line.split("\t")
            contig, start, end, motif = row[:4]
            loci.append((contig, int(start), int(end), motif))
    return loci


def parse_args():
    parser = argparse.ArgumentParser(
        description="Refines approximate repeat regions identified by EHdn to exact genomic coordinates using local sequence alignment."
    )
    parser.add_argument("loci", help="Path to the EHdn locus TSV file.")
    parser.add_argument("reference", help="Path to the reference FASTA file.")
    parser.add_argument("output", help="Output path for results in TSV format.")
    parser.add_argument(
        "-e",
        "--error-margin",
        default=1000,
        type=int,
        help="The error margin of regions given by EHdn. Defaults to 1000 bp.",
    )
    parser.add_argument(
        "-m",
        "--min-repeats",
        default=2,
        type=float,
        help="Minimum number of repeats units found in the reference for a region to be reported. Defaults to 2 units.",
    )
    parser.add_argument(
        "-r",
        "--ref-seq",
        action="store_true",
        help="Include the reference sequence in the output file.",
    )
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    logging.info("Loading reference...")
    reference = pysam.FastaFile(args.reference)

    logging.info("Loading loci...")
    loci = load_loci(args.loci)

    logging.info("Processing loci...")
    aligner = Align.PairwiseAligner()
    aligner.mode = "local"
    aligner.open_gap_score = -99999
    aligner.target_end_gap_score = -99999
    aligner.query_end_gap_score = 0
    aligner.match_score = 1
    aligner.mismatch_score = -19

    process_all_loci(
        loci,
        reference,
        aligner,
        args.output,
        error_margin=args.error_margin,
        ref_seq=args.ref_seq,
        min_repeats=args.min_repeats,
    )


if __name__ == "__main__":
    main()
