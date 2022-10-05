from pathlib import Path


p = Path.cwd() / "pathlib_exercices" / "image.png"

parent_dir = p.parent
file_name = p.stem
extension_file = p.suffix

new_file = parent_dir / (file_name + "-lowers" + extension_file)

new_file.touch(exist_ok=True)