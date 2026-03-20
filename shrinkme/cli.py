"""
Command-line interface for the shrinkme image compression tool.

Provides CLI access to image compression with SVD, including options for
resizing, visualization, and metrics reporting.
"""

import argparse
import sys
from pathlib import Path
from typing import Optional

from . import core, utils


def create_parser() -> argparse.ArgumentParser:
    """
    Create and configure the argument parser for shrinkme CLI.

    Returns:
        argparse.ArgumentParser: Configured parser.
    """
    parser = argparse.ArgumentParser(
        prog="shrinkme",
        description="Compress images using Singular Value Decomposition (SVD)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  shrinkme compress --input image.jpg --k 50
  shrinkme compress --input image.jpg --k 50 --resize 800x600
  shrinkme compress --input image.jpg --k 50 --output result.jpg --visualize
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Compress command
    compress_parser = subparsers.add_parser(
        "compress", help="Compress an image using SVD"
    )
    compress_parser.add_argument(
        "--input",
        "-i",
        required=True,
        type=str,
        help="Path to input image file",
    )
    compress_parser.add_argument(
        "--k",
        "-k",
        required=True,
        type=int,
        help="Number of singular values to keep (compression level)",
    )
    compress_parser.add_argument(
        "--output",
        "-o",
        type=str,
        default="compressed_output.jpg",
        help="Path to save compressed image (default: compressed_output.jpg)",
    )
    compress_parser.add_argument(
        "--resize",
        "-r",
        type=str,
        default=None,
        help='Resize input image before compression to WIDTHxHEIGHT (e.g., "800x600")',
    )
    compress_parser.add_argument(
        "--resize-output",
        type=str,
        default=None,
        help='Resize output image after compression to WIDTHxHEIGHT (e.g., "800x600")',
    )
    compress_parser.add_argument(
        "--visualize",
        "-v",
        action="store_true",
        help="Display original and compressed images side by side",
    )
    compress_parser.add_argument(
        "--metrics",
        "-m",
        action="store_true",
        default=True,
        help="Show compression metrics (default: True)",
    )
    compress_parser.set_defaults(func=compress_command)

    return parser


def compress_command(args: argparse.Namespace) -> int:
    """
    Execute the compress command.

    Args:
        args (argparse.Namespace): Parsed command-line arguments.

    Returns:
        int: Exit code (0 for success, 1 for error).
    """
    try:
        # Validate input file
        if not Path(args.input).exists():
            print(f"Error: Input file not found: {args.input}", file=sys.stderr)
            return 1

        # Load and optionally resize input
        if args.resize:
            try:
                width, height = utils.parse_dimension_string(args.resize)
                print(f"Resizing input image to {width}x{height}...")
                img = utils.resize_image(args.input, width, height)
            except ValueError as e:
                print(f"Error: {e}", file=sys.stderr)
                return 1
        else:
            img = core.load_image(args.input)

        # Validate k parameter
        max_k = min(img.shape)
        if args.k <= 0 or args.k > max_k:
            print(
                f"Error: k must be between 1 and {max_k} for this image",
                file=sys.stderr,
            )
            return 1

        # Compress image
        print(f"Compressing image with k={args.k}...")
        compressed = core.compress_image(img, args.k)

        # Optionally resize output
        if args.resize_output:
            try:
                width, height = utils.parse_dimension_string(args.resize_output)
                print(f"Resizing output image to {width}x{height}...")
                compressed = utils.resize_output(compressed, width, height)
            except ValueError as e:
                print(f"Error: {e}", file=sys.stderr)
                return 1

        # Save compressed image
        core.save_compressed_image(compressed, args.output)

        # Show metrics
        if args.metrics:
            metrics = core.calculate_compression_metrics(args.input, img, args.k)
            core.print_metrics(metrics, args.k)

        # Visualize if requested
        if args.visualize:
            print("Launching visualization...")
            core.show_images(img, compressed)

        return 0

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def main(argv: Optional[list] = None) -> int:
    """
    Main entry point for the CLI.

    Args:
        argv (list, optional): Command-line arguments (default: sys.argv[1:]).

    Returns:
        int: Exit code.
    """
    parser = create_parser()
    args = parser.parse_args(argv)

    if not hasattr(args, "func"):
        parser.print_help()
        return 0

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
