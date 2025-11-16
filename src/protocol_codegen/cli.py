#!/usr/bin/env python3
"""
Protocol CodeGen - CLI Interface

Command-line interface for generating protocol code from message definitions.
"""

import sys
from pathlib import Path
from typing import Optional

import click


@click.group()
@click.version_option(version="1.0.0", prog_name="protocol-codegen")
def cli():
    """
    Protocol CodeGen - Generate type-safe protocol code from message definitions.

    Supports multiple protocol methods (SysEx, OSC, etc.) and code generators (C++, Java, Rust, etc.).
    """
    pass


@cli.command()
@click.option(
    '--method',
    type=click.Choice(['sysex'], case_sensitive=False),
    required=True,
    help='Protocol method to use (sysex, osc, etc.)'
)
@click.option(
    '--messages',
    type=click.Path(exists=True, path_type=Path),
    required=True,
    help='Path to messages.py file containing message definitions'
)
@click.option(
    '--config',
    type=click.Path(exists=True, path_type=Path),
    default=None,
    help='Path to protocol configuration file (optional)'
)
@click.option(
    '--output-cpp',
    type=click.Path(path_type=Path),
    default=None,
    help='Output directory for C++ code'
)
@click.option(
    '--output-java',
    type=click.Path(path_type=Path),
    default=None,
    help='Output directory for Java code'
)
@click.option(
    '--verbose',
    is_flag=True,
    help='Enable verbose output'
)
def generate(
    method: str,
    messages: Path,
    config: Optional[Path],
    output_cpp: Optional[Path],
    output_java: Optional[Path],
    verbose: bool
):
    """
    Generate protocol code from message definitions.

    Examples:

        # Generate C++ and Java code using SysEx
        protocol-codegen generate --method sysex --messages ./messages.py \\
            --output-cpp ./src/protocol --output-java ./src/main/java/protocol

        # Generate with custom config
        protocol-codegen generate --method sysex --messages ./messages.py \\
            --config ./protocol_config.py --output-cpp ./protocol
    """
    click.echo(f"🚀 Protocol CodeGen v1.0.0")
    click.echo(f"Method: {method}")
    click.echo(f"Messages: {messages}")

    if not output_cpp and not output_java:
        click.echo("❌ Error: At least one output directory (--output-cpp or --output-java) must be specified", err=True)
        sys.exit(1)

    # Import generator based on method
    if method.lower() == 'sysex':
        from protocol_codegen.methods.sysex.generator import generate_sysex_protocol

        try:
            generate_sysex_protocol(
                messages_path=messages,
                config_path=config,
                output_cpp=output_cpp,
                output_java=output_java,
                verbose=verbose
            )
            click.echo("✅ Code generation completed successfully!")
        except Exception as e:
            click.echo(f"❌ Error during generation: {e}", err=True)
            if verbose:
                import traceback
                traceback.print_exc()
            sys.exit(1)
    else:
        click.echo(f"❌ Method '{method}' not yet implemented", err=True)
        sys.exit(1)


@cli.command()
@click.option(
    '--method',
    type=click.Choice(['sysex'], case_sensitive=False),
    required=True,
    help='Protocol method to validate for'
)
@click.option(
    '--messages',
    type=click.Path(exists=True, path_type=Path),
    required=True,
    help='Path to messages.py file'
)
def validate(method: str, messages: Path):
    """
    Validate message definitions without generating code.

    Examples:

        protocol-codegen validate --method sysex --messages ./messages.py
    """
    click.echo(f"🔍 Validating messages: {messages}")
    click.echo(f"Method: {method}")

    # TODO: Implement validation
    click.echo("⚠️  Validation not yet implemented")
    sys.exit(1)


@cli.command(name='list-methods')
def list_methods():
    """List available protocol methods."""
    click.echo("📋 Available Protocol Methods:")
    click.echo()
    click.echo("  ✅ sysex    - MIDI System Exclusive protocol")
    click.echo("  🔮 osc      - Open Sound Control (planned)")
    click.echo("  🔮 custom   - Custom binary protocol (planned)")
    click.echo()


@cli.command(name='list-generators')
def list_generators():
    """List available code generators."""
    click.echo("📋 Available Code Generators:")
    click.echo()
    click.echo("  ✅ C++         - For embedded systems, audio plugins, native apps")
    click.echo("  ✅ Java        - For desktop apps, Android, host extensions")
    click.echo("  🔮 Rust        - (planned)")
    click.echo("  🔮 Python      - (planned)")
    click.echo("  🔮 TypeScript  - (planned)")
    click.echo()


@cli.command()
@click.option(
    '--method',
    type=click.Choice(['sysex'], case_sensitive=False),
    default='sysex',
    help='Protocol method for scaffolding'
)
@click.option(
    '--generators',
    default='cpp,java',
    help='Comma-separated list of generators (e.g., cpp,java)'
)
@click.option(
    '--output',
    type=click.Path(path_type=Path),
    default=Path('./my-protocol'),
    help='Output directory for scaffolding'
)
def init(method: str, generators: str, output: Path):
    """
    Initialize a new protocol project with scaffolding.

    Examples:

        # Create new SysEx project with C++ and Java
        protocol-codegen init --method sysex --generators cpp,java --output ./my-protocol
    """
    click.echo(f"🏗️  Initializing new protocol project")
    click.echo(f"Method: {method}")
    click.echo(f"Generators: {generators}")
    click.echo(f"Output: {output}")

    # TODO: Implement scaffolding
    click.echo("⚠️  Scaffolding not yet implemented")
    sys.exit(1)


def main():
    """Main entry point for CLI."""
    cli()


if __name__ == '__main__':
    main()
