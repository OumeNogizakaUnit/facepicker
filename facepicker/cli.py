import click
import face_recognition
from pathlib import Path
from PIL import Image

from facepicker.utils import save_face


@click.command()
@click.option('-s',
              '--savedir',
              default='./cut_img',
              show_default=True,
              type=click.Path())
@click.argument('imgdir', type=click.Path(exists=True))
def cli(savedir, imgdir):
    click.echo(imgdir)
    imgdirpath = Path(imgdir)
    dirnames = [d for d in imgdirpath.iterdir() if d.is_dir()]
    for dirname in dirnames:
        dirpath = Path(dirname)
        name = dirpath.name
        filepaths = [p for p in dirpath.iterdir()]
        for filepath in filepaths:
            save_face(filepath, savedir, name)
