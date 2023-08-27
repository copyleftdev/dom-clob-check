# DOM Clobbering Detector

A simple CLI tool to detect potential DOM clobbering vulnerabilities in web pages.

## What is DOM Clobbering?

DOM Clobbering is a technique where global JavaScript variables can be overwritten or "clobbered" by naming HTML elements with certain IDs or names. This can cause unexpected behavior in scripts and potentially lead to security vulnerabilities.

For example, if a web page has a script that references a global variable `x`, and an attacker can inject an HTML element with `id="x"`, the reference to `x` in the script will now point to the injected HTML element instead of the original variable. This behavior can lead to various issues including cross-site scripting (XSS) vulnerabilities.

## Features

- Detect potential DOM clobbering patterns in the HTML content.
- Identify script sinks that could be affected by DOM clobbering.
- Lightweight and simple to use.

## Installation

Ensure you have Python and the necessary libraries installed:

```bash
pip install requests beautifulsoup4
```

## Usage

Run the script:

```bash
python dom_clobbering_detector.py
```

When prompted, enter the URL of the web page you'd like to check.

## Contributing

Contributions are welcome! Please fork this repository and open a pull request with your changes.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [PortSwigger](https://portswigger.net/web-security/dom-based/dom-clobbering) for their detailed explanations on DOM clobbering.

---

**Note**: Remember, this tool provides basic detection capabilities and may produce both false positives and false negatives. Always verify the results and consider incorporating additional features for a more comprehensive analysis.
