"""
MIT License

Copyright (c) 2024 Rashid Al Abri

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import argparse
import logging
import json
from Bio import Align, Seq
import pysam
from tqdm import tqdm

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def find_repeat_indices(seq, motif, aligner):
    max_num_repeats = len(seq) // len(motif)
    target_seq = motif * max_num_repeats

    alignment = aligner.align(target_seq, seq)[0]
    _, indices = alignment.aligned

    if len(indices) == 0:
        raise Exception("No alignment found")
    elif alignment.score < 0:
        raise Exception("Alignment score is less than 0")

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


def format_locus_json(locus, exact_start, exact_end):
    contig, ehdn_start, ehdn_end, motif = locus
    locus_id = f"{contig}_{ehdn_start}_{ehdn_end}"
    entry = {
        "LocusId": locus_id,
        "LocusStructure": f"({motif})*",
        "ReferenceRegion": f"{contig}:{exact_start}-{exact_end}",
        "VariantType": "Repeat",
    }
    formatted = json.dumps(entry, indent=4)
    formatted = "\n".join(["    " + line for line in formatted.split("\n")])
    return formatted


def process_all_loci(
    loci,
    reference,
    aligner,
    output_tsv,
    output_json=None,
    error_margin=1000,
    ref_seq=False,
    min_repeats=2,
):
    tsv_header = "contig\tstart\tend\tmotif\texact_start\texact_end\tmotif"
    if ref_seq:
        tsv_header += "\tref_seq"
    output_tsv.write(tsv_header)

    if output_json:
        json_header = "["
        output_json.write(json_header)

    for locus in tqdm(loci):
        contig, ehdn_start, ehdn_end, motif = locus

        try:
            exact_start, exact_end, ref_seq = process_single_locus(
                locus, reference, aligner, error_margin
            )
            exact_len = exact_end - exact_start
        except Exception as e:
            exact_len = -1

        try:
            exact_start_rc, exact_end_rc, ref_seq_rc = process_single_locus(
                locus, reference, aligner, error_margin, revcomp=True
            )
            exact_len_rc = exact_end_rc - exact_start_rc
        except Exception as e:
            exact_len_rc = -1

        if exact_len == -1 and exact_len_rc == -1:
            continue

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
            # Write to TSV
            to_write = f"\n{contig}\t{ehdn_start}\t{ehdn_end}\t{longer_exact_start}\t{longer_exact_end}\t{motif}"
            if ref_seq:
                to_write += f"\t{longer_ref_seq}"
            output_tsv.write(to_write)

            # Write to JSON
            if output_json:
                formatted = format_locus_json(
                    locus, longer_exact_start, longer_exact_end
                )
                output_json.write("\n" + formatted + ",")

    if output_json:
        output_json.seek(output_json.tell() - 1)
        output_json.write("\n]")


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
    parser.add_argument(
        "output_prefix", help="Output prefix for results in TSV format."
    )
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
    parser.add_argument(
        "-c",
        "--eh-variant-catalog",
        action="store_true",
        help="Also output an ExpansionHunter variant catalog with exact regions.",
    )
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    logging.info("Loading reference...")
    reference = pysam.FastaFile(args.reference)

    logging.info("Loading loci...")
    loci = load_loci(args.loci)

    logging.info(f"Processing {len(loci)} loci...")
    aligner = Align.PairwiseAligner()
    aligner.mode = "local"
    aligner.open_gap_score = -99999
    aligner.extend_gap_score = -99999
    aligner.target_end_gap_score = 0
    aligner.query_end_gap_score = 0
    aligner.match_score = 1
    aligner.mismatch_score = -19

    output_tsv_path = args.output_prefix + ".tsv"
    output_json_path = args.output_prefix + ".json" if args.eh_variant_catalog else None

    output_tsv = open(output_tsv_path, "w")
    output_json = open(output_json_path, "w") if output_json_path else None

    process_all_loci(
        loci,
        reference,
        aligner,
        output_tsv,
        output_json,
        error_margin=args.error_margin,
        ref_seq=args.ref_seq,
        min_repeats=args.min_repeats,
    )

    output_tsv.close()
    if output_json:
        output_json.close()


if __name__ == "__main__":
    main()
