# TeToS

A unified interface for multiple Text-to-Speech (TTS) providers.


## Supported TTS providers

- [Edge-TTS](https://github.com/rany2/edge-tts)
- [OpenAI TTS](https://platform.openai.com/docs/guides/text-to-speech)

  Required parameters:

  - `api_key`: OpenAI API key

- [Azure TTS](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/text-to-speech)

  Required parameters(Please refer to the documentation to get the secrets):

  - `speech_key`: Azure Speech service key
  - `service_region`: Azure Speech service region

- [Volcengine TTS(火山引擎)](https://console.volcengine.com/sami)

  Required parameters:

  - `access_key`: Volcengine access key ID. ([Get it here](https://console.volcengine.com/iam/keymanage/))
  - `secret_key`: Volcengine access secret key. ([Get it here](https://console.volcengine.com/iam/keymanage/))
  - `app_key`: Volcengine app key


## Installation

Requires Python 3.8 or higher.

```bash
pip install tetos
```

## CLI Usage

```
tetos PROVIDER [PROVIDER_OPTIONS] TEXT [--output FILE]
```

Please run `tetos --help` for available providers and options.

## API Usage

Use Azure TTS as an example:

```python
from tetos.azure import AzureSpeaker
import asyncio

async def main():
    speaker = AzureSpeaker(speech_key='...', service_region='...')
    await speaker.synthesize('Hello, world!', 'output.mp3')

if __name__ == '__main__':
    asyncio.run(main())
```

The initialization parameters may be different for other providers.

## License

[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
