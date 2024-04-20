# Parendum Library

**Parendum OÜ**  
Creation Date: December 2023  
Copyright © 2023 Parendum OÜ. All rights reserved.

## Description

The Parendum library provides a Python client for interacting with the Parendum services. This library facilitates secure communication with the API, including HMAC signature generation and request header creation.

## Installation

To use this library in your project, simply install it with the next command.

```bash
pip install git+https://gitlab.com/parendumteam/parendum-lib/
```

## Usage

Initialize a new Logger:

```python
from parendumlib import Logger

logger = Logger(domain="logger.parendum.com", api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET")
```

Send logs:

```python
logger.debug("Arrives here :)")
logger.info("Hello world!")
logger.warning("Deprecated function :S")
logger.exception("Division by zero exception")
logger.error("Unauthorized access detected")
```


## Contact

For any inquiries, feedback, or issues, please contact:

- Email: info@parendum.com
- Website: https://parendum.com


## License

Unauthorized use, reproduction, modification, or distribution without the express consent of Parendum OÜ is strictly prohibited.
