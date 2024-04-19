# QWrapper

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/ddybing/qwrapper/pypi-publish.yml)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/qwrapper)

![PyPI - Downloads](https://img.shields.io/pypi/dm/qwrapper)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



QWrapper is a Python module meant to make automated interactions with QEMU (Quick EMUlator) easier. By the use of the existing Python modules `pygdbmi` and `qemu.qmp`, this modules communicates with a QEMU virtual machine instance and provides a simple interface for the developer to control the VM and extract useful information. 

This module was specifically developed for our bachelor project, where needed to automate the use of QEMU and to extract specific values such as registers. Much of this data is provided through the aforementioned modules, but their output is unstructured.

The purpose of this module is thus to simplify the interaction with these modules and provide structured output that can be more easily used.
