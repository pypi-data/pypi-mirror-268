from badbyte.utils.functions import analyze, generate_characters
import os
import badbyte

with open(os.path.join(badbyte.__path__[0], 'VERSION')) as version_file:
    version = version_file.read().strip()
analyze = analyze
generate_characters = generate_characters
__version__ = version
__all__ = ['analyze', 'generate_characters']

