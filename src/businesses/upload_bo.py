import base64
import mimetypes
import os
import tempfile

from werkzeug.datastructures import FileStorage

from src.utils.exceptions import BadRequestException
from src.utils.settings import get_upload_image_allowed_extensions

IMAGE_ALLOWED_EXTENSIONS = get_upload_image_allowed_extensions()


class UploadBo:
    def get_image_base64(self, file: FileStorage) -> str:
        self._validate_extension(file, IMAGE_ALLOWED_EXTENSIONS)
        return self._parser_file_to_base64(file)

    def _validate_extension(self, file, allowed_extensions):
        extension = mimetypes.guess_extension(file.mimetype)
        extension = extension.lower().replace(".", "")

        if extension not in allowed_extensions:
            raise BadRequestException(
                message="Extension not allowed",
                errors={
                    "sent": extension,
                    "allowed": ", ".join(allowed_extensions),
                }
            )

    def _parser_file_to_base64(self, file: FileStorage) -> str:
        file.seek(0)

        """
        Creates the temporary file
        """
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(file.stream.read())
        temp_file.flush()
        temp_file.close()

        base64_file: str
        with open(temp_file.name, 'rb') as binary_file:
            binary_file_data = binary_file.read()
            base64_encoded = base64.b64encode(binary_file_data)
            base64_message = base64_encoded.decode('utf-8')
            base64_file = base64_message

        """
        Delete the temporary file
        """
        if temp_file and os.path.exists(temp_file.name):
            temp_file.close()
            os.remove(temp_file.name)

        return base64_file
