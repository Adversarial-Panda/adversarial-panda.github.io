"""Redact identifying terminal text in the website GIFs and regenerate posters.

Run against the original GIFs. Requires Pillow, NumPy, and SciPy.
Original MP4s are local source recordings and are not published.
"""
from pathlib import Path
import argparse
import numpy as np
from PIL import Image, ImageFilter
from scipy.signal import fftconvolve
from scipy.ndimage import maximum_filter

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--source-dir', type=Path, required=True, help='Directory containing benign-original.gif and adversarial-original.gif')
args = parser.parse_args()
source = Image.open(args.source_dir / 'benign-original.gif').convert('RGB')
# Username in a traceback, result directory, and shell prompt, respectively.
boxes = [(48, 263, 79, 270), (185, 143, 216, 150), (29, 53, 60, 60)]
templates = []
for box in boxes:
    a = np.asarray(source.crop(box).convert('L'), dtype=float)
    a -= a.mean()
    templates.append(a)

def redact(frame):
    frame = frame.convert('RGB')
    gray = np.asarray(frame.convert('L'), dtype=float)
    regions = []
    for t in templates:
        h, w = t.shape
        ones = np.ones((h, w))
        sums = fftconvolve(gray, ones, mode='valid')
        squares = fftconvolve(gray ** 2, ones, mode='valid')
        denom = np.sqrt(np.maximum(squares - sums ** 2 / t.size, 0) * (t ** 2).sum())
        scores = fftconvolve(gray, t[::-1, ::-1], mode='valid') / np.maximum(denom, 1e-8)
        peaks = (scores > .80) & (scores == maximum_filter(scores, size=(5, 21)))
        for y, x in zip(*np.where(peaks)):
            if y >= 48 and any(abs(int(x)-column) <= 3 for column in (29, 48, 185)):
                regions.append((max(0, x-3), max(0, y-2), (98 if abs(int(x)-29) <= 3 else x+w+3), y+h+2))
    # Window title and terminal tabs contain the account name too.
    regions.append((0, 14, 800, 49))
    for box in regions:
        patch = frame.crop(box)
        frame.paste(patch.filter(ImageFilter.GaussianBlur(9)), box)
    return frame, len(regions)-1

if __name__ == '__main__':
    for name in ['benign', 'adversarial']:
        path = ROOT / f'assets/{name}-2x.gif'
        original = Image.open(args.source_dir / f'{name}-original.gif')
        frames, durations, counts = [], [], []
        for i in range(original.n_frames):
            original.seek(i)
            frame, count = redact(original)
            frames.append(frame.quantize(palette=Image.open(args.source_dir / f'{name}-original.gif'), dither=Image.Dither.NONE))
            counts.append(count)
            durations.append(original.info.get('duration', 100))
        frames[0].save(ROOT / f'assets/{name}-poster.webp', quality=90)
        frames[0].save(path, save_all=True, append_images=frames[1:], duration=durations, loop=0, optimize=True, disposal=1)
        print(name, 'frames:', len(frames), 'redactions:', sum(counts), 'first:', counts[:15])
