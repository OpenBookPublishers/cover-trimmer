# Description

cover-trimmer is a tool to trim book cover artworks (PDF) and output front cover images (JPEG). The tool is made up of a single module: `./src/cover_trimmer.py`. This can be used as you please.

The repository offers a thoth wrapper in `./src/tun_thoth.py`, which is able to retrieve info about cover size from thoth and use this data to trim cover to the right size.

# Run in docker
This tool runs in docker. Images can be built with this command:

```
docker build . -t openbookpublishers/cover-trimmer
```
and containers run with:

```
docker run --rm \
    -v /path/to/cover.pdf:/cover/cover.pdf \
    -v /path/to/out/:/cover/out \
    openbookpublishers/cover-trimmer \
    thoth_wrapper.py --doi obp.0231 --output_width 1875
```
where:

 - `/path/to/cover.pdf` is the path of the input cover;
 - `/path/to/out/` is the path to the output directory;


# Tests
Run tests as:
```
docker build . -f Dockerfile.test -t openbookpublishers/cover-trimmer:test && \
docker run openbookpublishers/cover-trimmer:test
```

# Personalization
## Cover size
The PDF cover artwork might come at different size. A geometry must be specified for the tool to work properly.

```
geometry = [748, 9, 1190, 672]

trimmer = Trimmer(pdf_path, output_folder=out_folder)
trimmer.set_cropbox(geometry)
trimmer.convert(args.output_width)
```
The page geometry is a python list with the [PyMuPDF Rect() coordinates](https://pymupdf.readthedocs.io/en/latest/rect.html) you require (units are expressed in points).
