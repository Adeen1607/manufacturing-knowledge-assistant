# Security and privacy boundaries

## Supported use

This project is a localhost portfolio demonstration using synthetic data. It has no enterprise authentication, production hardening or published service-level commitment. Keep it bound to `127.0.0.1`. Do not place it behind a public tunnel or load confidential company records into it.

## Current controls

The application caps POST request bodies at 16 KiB, uses parameterized SQLite writes and escapes displayed dynamic content in the interface. These controls reduce particular risks; they do not constitute a comprehensive security review. Neither application implements authenticated users, authorization over API routes, rate limiting or a full production error-handling layer.

## Reporting a concern

For non-sensitive reproducible defects, open a GitHub issue describing the affected path, expected behavior, observed behavior and a synthetic reproduction. Do not put passwords, tokens, private documents or identifiable telemetry in issues. If the evidence is sensitive, first contact the maintainer using an available private channel; no private reporting channel or response timetable is promised by this repository.

## Data handling

Local databases contain prototype records and are ignored by Git. SQLite files are not encrypted by the application, have no automatic retention policy and are readable by someone with filesystem access. Stop the application before making a simple file backup. A real deployment needs identity-based permissions, approved retention, protected logs and managed infrastructure.

See the project-specific risk register in the [documentation index](docs/README.md) for controls, residual risks and proposed ownership.
