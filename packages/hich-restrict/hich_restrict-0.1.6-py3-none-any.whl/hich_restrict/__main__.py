import click
import time
import sys
from .restrict_manager import *

@click.command()
@click.option("--frag-file-format",
    type=click.Choice(RestrictManager.frag_file_format_options()),
    show_default=True,
    default=RestrictManager.frag_file_format_options()[0],
    help="Whether lines of fragments file are in .bed format (chrom start end) "
         "or 'chromlines' format (chrom end1 end2 end3...). Autodetect is "
         "based on first line of file, not filename.")
@click.option("--output-pairs",
    type=str,
    help="Filename for output .pairs file")
@click.argument("frag-file")
@click.argument("input-pairs")
def cli(frag_file_format, output_pairs, frag_file, input_pairs):
    """
    hich-restrict v 0.1.6
    
    frag-file: a non-compressed plaintext file containing fragments. All
    fragments from a particular chromosome must be in one contiguous block,
    with ascending coordinates. All fragments in a chromosome must be
    adjacent (frag_n start = frag_n-1 end + 1).

    input-pairs: a text file containing pairs in .pairs format. Can be
    plaintext or compressed with gzip (.gz, .gzip) or lz4 (.lz4).
    """
    cmd = ' '.join(sys.argv)
    rm = RestrictManager()
    rm.setup(cmd, frag_file_format, output_pairs, frag_file, input_pairs)
    start = time.time()
    rm.tag()
    end = time.time()
    duration = end - start
    print(f"Tag duration (s): {duration}")

    # My current speed is about 4k reads/s which means a 400M read .pairs file
    # takes over a day to tag, roughly fitting what we get on exacloud.
    # The main issue is that loading the restriction fragments into memory
    # takes 5 Gb, but the runtime is bottlenecked by the search, so
    # to parallelize that it would require multiprocessing where each process
    # utilizes 5 Gb of memory, and currently we are achieving that by just
    # tagging all the files at the same time.
    # 
    # Improving performance would require splitting restriction fragments over
    # multiple processes. One way we could do that is by splitting up the
    # restriction fragments by chromosomes (or by position within chroms)
    # and assigning one process per interval. Pairs would be fed into the
    # appropriate process in batches, multiprocessed, and then rejoined
    #
    # However, it is probably not hard for people to just request more memory
    # and accept an extra day of processing time. So I'm not convinced this
    # is high-priority yet.

if __name__ == "__main__":
    cli()