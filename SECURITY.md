# Security Policy

## Reporting a Vulnerability

We take the security of Shrinkme very seriously. If you discover a security vulnerability, please email us privately at [your-security-email@example.com] instead of using the public issue tracker.

Please include the following information in your report:

- Description of the vulnerability
- Affected version(s)
- Steps to reproduce (if applicable)
- Potential impact
- Suggested fix (if you have one)

We will acknowledge your report within 48 hours and provide a more detailed response within 7 days indicating the next steps in handling your report.

## Security Best Practices

### For Users

When using Shrinkme:

1. **Keep dependencies updated**: Regularly update NumPy, Pillow, and other dependencies
   ```bash
   pip install --upgrade shrinkme
   pip install --upgrade -r requirements.txt
   ```

2. **Validate inputs**: When processing user-supplied images, validate file types and sizes
   ```python
   from pathlib import Path
   allowed_types = {'.jpg', '.jpeg', '.png', '.bmp', '.gif'}
   if Path(filename).suffix.lower() not in allowed_types:
       raise ValueError("Invalid file type")
   ```

3. **Limit resource usage**: Set reasonable limits on image size and k values
   ```python
   MAX_IMAGE_SIZE = 10_000_000  # 10MP
   MAX_K = 500
   
   img = load_image(path)
   if img.size > MAX_IMAGE_SIZE:
       raise ValueError("Image too large")
   if k > MAX_K:
       raise ValueError("k value too large")
   ```

4. **Secure file handling**: Use temporary directories for intermediate files
   ```python
   import tempfile
   with tempfile.TemporaryDirectory() as tmpdir:
       # Process files in tmpdir
       pass
   ```

### For Developers

When contributing to Shrinkme:

1. **Validate all inputs** - Check data types, ranges, and formats
2. **Use safe file operations** - Validate paths, use context managers
3. **Avoid user input in system commands** - Never use subprocess with untrusted input
4. **Keep dependencies updated** - Monitor for security updates in dependencies
5. **Test edge cases** - Include tests for malformed inputs, boundary conditions
6. **Use type hints** - Help catch type-related bugs early

## Dependency Security

We use the following key dependencies:

- **NumPy**: Used for matrix operations. Monitor https://numpy.org/security/
- **Pillow**: Used for image I/O. Monitor https://pillow.readthedocs.io/
- **Matplotlib**: Used for visualization. Monitor https://matplotlib.org/

To check for known vulnerabilities:

```bash
pip install safety
safety check
```

Or use your preferred vulnerability scanner:

```bash
pip install bandit
bandit -r shrinkme/
```

## CVE Tracking

Any security vulnerabilities in Shrinkme will be tracked with CVE identifiers when applicable.

## Security Updates

- Security patches will be released as soon as possible
- Critical vulnerabilities will trigger emergency releases
- All security updates will be announced on the GitHub releases page
- Users are encouraged to subscribe to release notifications

## Scope of Coverage

This security policy applies to:
- The main Shrinkme package
- All released versions on PyPI
- The GitHub repository main branch

This policy does NOT cover:
- Third-party code or plugins
- Versions older than 2 major versions
- Code in development branches

## Supported Versions

| Version | Status         | End of Support |
|---------|----------------|----------------|
| 1.x     | Current        | TBD            |
| 0.2.x   | Maintenance    | 6 months       |
| 0.1.x   | Unsupported    | 2024-09-20     |

We recommend always using the latest version for security updates.

## Responsible Disclosure

We follow responsible disclosure practices:

1. Security issues are NOT public until patched and released
2. Reporters will be credited in release notes (if desired)
3. Fix will be released within 30 days unless extenuating circumstances
4. Critical issues may result in immediate minor version release

## Questions or Suggestions?

If you have suggestions for improving this security policy, please open an issue or contact the maintainers.

Thank you for helping keep Shrinkme secure! 🔒
