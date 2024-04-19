"""Contains the core business logic of the OpenAI CLI."""

import asyncio
import logging
import pathlib
import tempfile
from typing import Literal

import aiofiles
import ffmpeg

from cloai import openai_api
from cloai.cli import prompts
from cloai.core import config, exceptions, utils

settings = config.get_settings()
logger = logging.getLogger(settings.LOGGER_NAME)
MAX_FILE_SIZE = 24_500_000  # Max size is 25MB, but we leave some room for error.


class ChatCompletion:
    """A class for running the Chat Completion model.

    Attributes:
        user_prompt: The prompt to use.
        system_prompt: The system prompt to use.
        model: The model to use for chat completion.
    """

    def __init__(  # noqa: PLR0913
        self,
        model: Literal["gpt-4", "gpt-3.5-turbo", "gpt-4-1106-preview"],
        *,
        user_prompt: str | None = None,
        user_prompt_file: pathlib.Path | None = None,
        system_prompt: str | None = None,
        system_prompt_file: pathlib.Path | None = None,
        system_preset: str | None = None,
    ) -> None:
        """Initializes a ChatCompletion object.

        Args:
            user_prompt: The prompt to use.
            user_prompt_file: The file containing the prompt to use.
            system_prompt: The system prompt to use.
            system_prompt_file: The file containing the system prompt to use.
            system_preset: The preset system prompt to use.
            model: The model to use for chat completion.

        """
        logger.debug("Initializing ChatCompletion.")
        self._validate_initialization(
            user_prompt,
            user_prompt_file,
            system_prompt,
            system_prompt_file,
            system_preset,
        )
        self.user_prompt: str = (
            self._read_file(user_prompt_file) if user_prompt_file else user_prompt  # type: ignore[assignment]
        )
        self.system_prompt = self._determine_system_prompt(
            system_prompt,
            system_prompt_file,
            system_preset,
        )
        self.model = model

    async def run(self) -> str:
        """Runs the chat completion.

        Returns:
            The completed chat response as a string.
        """
        logger.debug("Running chat completion.")
        return await openai_api.ChatCompletion().run(
            model=self.model,
            user_prompt=self.user_prompt,
            system_prompt=self.system_prompt,
        )

    @staticmethod
    def _validate_initialization(
        user_prompt: str | None = None,
        user_prompt_file: pathlib.Path | None = None,
        system_prompt: str | None = None,
        system_prompt_file: pathlib.Path | None = None,
        system_preset: str | None = None,
    ) -> None:
        """Validates the arguments passed to the constructor.

        Args:
            user_prompt: The prompt to use.
            user_prompt_file: The file containing the prompt to use.
            system_prompt: The system prompt to use.
            system_prompt_file: The file containing the system prompt to use.
            system_preset: The preset system prompt to use.

        Raises:
            ValueError: If prompt and prompt_file are both None.
            ValueError: If not just one of system_prompt, system_prompt_file,
                and system_preset are provided.
        """
        user_args = (user_prompt, user_prompt_file)
        if sum(arg is not None for arg in user_args) != 1:
            msg = "Either prompt or prompt_file must be provided."
            raise exceptions.LoggedValueError(msg)

        system_args = (system_prompt, system_prompt_file, system_preset)
        if sum(arg is not None for arg in system_args) != 1:
            msg = (
                "Exactly one of system_prompt, system_prompt_file,"
                "or system_preset must be provided."
            )
            raise exceptions.LoggedValueError(msg)

    @staticmethod
    def _read_file(file_path: pathlib.Path) -> str:
        """Reads the contents of a file.

        Args:
            file_path: The path to the file.

        Returns:
            The contents of the file as a string.
        """
        if file_path.suffix == ".pdf":
            return utils.pdf_to_str(file_path)
        if file_path.suffix == ".docx":
            return utils.docx_to_str(file_path)
        if file_path.suffix != ".txt":
            logger.warning(
                "File %s has an unsupported extension, treating it as a .txt file.",
                file_path,
            )
        return utils.txt_to_str(file_path)

    def _determine_system_prompt(
        self,
        system_prompt: str | None = None,
        system_prompt_file: pathlib.Path | None = None,
        system_preset: str | None = None,
    ) -> str:
        """Determines the system prompt to use.

        Args:
            system_prompt: The system prompt to use.
            system_prompt_file: The file containing the system prompt to use.
            system_preset: The preset system prompt to use.

        Returns:
            The determined system prompt as a string.
        """
        if system_prompt_file:
            return self._read_file(system_prompt_file)
        if system_preset:
            return getattr(prompts.Prompts, system_preset)
        if system_prompt:
            return system_prompt
        msg = "No system prompt provided."
        raise exceptions.LoggedValueError(msg)


async def speech_to_text(
    filename: pathlib.Path,
    model: str,
    *,
    clip: bool = False,
    language: config.WhisperLanguages = config.WhisperLanguages.ENGLISH,
) -> str:
    """Transcribes audio files with OpenAI's TTS models.

    Args:
        filename: The file to transcribe. Can be any format that ffmpeg supports.
        model: The transcription model to use.
        clip: Whether to clip the file if it is too large, defaults to False.
        language: The language used in the audio file.
    """
    logger.debug("Transcribing audio.")
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file = pathlib.Path(temp_dir) / "temp.mp3"
        ffmpeg.input(filename).output(str(temp_file)).overwrite_output().run()

        if clip:
            files = list(utils.clip_audio(temp_file, temp_dir, MAX_FILE_SIZE))
        else:
            files = [temp_file]

        stt = openai_api.SpeechToText()
        transcription_promises = [
            stt.run(filename, model=model, language=language) for filename in files
        ]
        transcriptions = await asyncio.gather(*transcription_promises)

        return " ".join(transcriptions)


async def text_to_speech(
    text: str,
    output_file: str,
    model: Literal["tts-1", "tts-1-hd"],
    voice: Literal["alloy", "echo", "fable", "onyx", "nova", "shimmer"],
) -> None:
    """Converts text to speech with OpenAI's TTS models.

    Args:
        text: The text to convert to speech.
        output_file: The name of the output file.
        model: The model to use.
        voice: The voice to use.
    """
    logger.debug("Converting text to speech.")
    tts = openai_api.TextToSpeech()
    audio_bytes = await tts.run(text, model=model, voice=voice)
    await utils.save_file(output_file, audio_bytes)


async def image_generation(  # noqa: PLR0913
    prompt: str,
    output_base_name: str,
    model: str,
    size: Literal["256x256", "512x512", "1024x1024", "1792x1024", "1024x1792"] | None,
    quality: Literal["standard", "hd"],
    n: int,
) -> None:
    """Generates an image from text with OpenAI's Image Generation models.

    Args:
        prompt: The text to generate an image from.
        output_base_name: The base name of the output file.
        model: The model to use.
        size: The size of the generated image.
        quality: The quality of the generated
        image. Defaults to "standard".
        n: The number of images to generate.

    Returns:
        bytes: The generated image as bytes.

    Notes:
        At present, the image generation API of dalle-3 only supports generating
        one image at a time. Instead, we call the API once for each image we want
        to generate.
    """
    logger.debug("Generating %s images.", n)
    image_generation = openai_api.ImageGeneration()
    url_promises = [
        image_generation.run(
            prompt,
            model=model,
            size=size,
            quality=quality,
            n=1,
        )
        for _ in range(n)
    ]
    urls = [url[0] for url in await asyncio.gather(*url_promises)]
    if all(url is None for url in urls):
        msg = "No images were generated."
        raise exceptions.OpenAIError(msg)
    urls_not_none = [url for url in urls if url is not None]

    await asyncio.gather(
        *[
            utils.download_file(f"{output_base_name}_{index}.png", url)
            for index, url in enumerate(urls_not_none)
        ],
    )


async def get_embedding(
    text_file: pathlib.Path,
    output_file: pathlib.Path,
    model: Literal[
        "text-embedding-3-small",
        "text-embedding-3-large",
    ] = "text-embedding-3-large",
    *,
    keep_new_lines: bool = False,
) -> None:
    """Get the embedding using OpenAI's Embedding models.

    Args:
        text_file: the text file to embed.
        model: the name of the Embedding model to use,
        defaults to text-embedding-3-large.
        output_file: the name of the CSV output file.
        keep_new_lines: Whether to keep or remove line breaks,
        defaults to False.
    """
    async with aiofiles.open(text_file, mode="r") as file:
        text = await file.read()

    get_embedding = openai_api.Embedding()

    embedding = await get_embedding.run(
        text=text,
        model=model,
        keep_new_lines=keep_new_lines,
    )
    await utils.save_csv(output_file, embedding)
