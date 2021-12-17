# cover-trimmer

cover-trimmer is a python library for trimming PDF cover artworks and outputting JPEG representations of their front covers.

## Usage

```python
from cover_trimmer import Trimmer

# init Trimmer object
trimmer = Trimmer(pdf_path, output_folder=out_folder)

# set cropbox to front cover coordinates
trimmer.set_cropbox([748, 9, 1190, 672])

# trim PDF and output a JPEG 1200 pixels wide
trimmer.convert(1200)
```

The front page coordinates element is a python list with the [PyMuPDF Rect() set of references](https://pymupdf.readthedocs.io/en/latest/rect.html) you require (units are expressed in points).

### Thoth Wrapper (Optional)

The [Thoth](https://thoth.pub/) wrapper stored at `./src/thoth_wrapper.py` queries the metadata repository to apply the correct cropbox to the PDF cover artworks.

Built the docker container with: $`docker build . -t openbookpublishers/cover-trimmer`

Run the container with:

```bash
docker run --rm \
    -v /path/to/cover.pdf:/cover/cover.pdf \
    -v /path/to/out/:/cover/out \
    openbookpublishers/cover-trimmer \
    thoth_wrapper.py --doi obp.0231 --output_width 1875
```
where:

 - `/path/to/cover.pdf` is the path of the input PDF cover artwork;
 - `/path/to/out/` is the path to the output directory;


### Tests

```bash
docker build . -f Dockerfile.test -t openbookpublishers/cover-trimmer:test && \
docker run openbookpublishers/cover-trimmer:test
```

## Contributing

Pull requests are welcome.

## License

[GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)
