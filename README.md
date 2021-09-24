# Description

cover-trimmer is a tool to trim book cover artworks and output front cover images.

The tool takes PDF cover artworks as input and outputs jpeg images scaled at different width sizes. These output sizes are specified in a config file, making this tool easy to customise.

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
    -e cover_type=royaloctavo \
    -e OUTPUT_WIDTH=1200 \
    openbookpublishers/cover-trimmer
```
where:

 - `/path/to/cover.pdf` is the path of the input cover;
 - `/path/to/out/` is the path to the output directory;
 - `cover_type` environment variable is the name of the trimming preset you require, picking from the ones reported in the `config.json` config file;
 - `OUTPUT_WITH` environment variable defines the width of the output image.

# Personalization
## Cover size
You can personalise the config file to trim covers at the size you require. The config file looks like this:

```
{
    "cover_geometry" : {
	    "royaloctavo" : [748, 9, 1190, 672],
        [...]
```
You can add a new entry to the `cover_geometry` key, specifying a new name for your preset and the [PyMuPDF Rect() coordinates](https://pymupdf.readthedocs.io/en/latest/rect.html) you require (units are expressed in points).

Finally, you can run the container with your personalised config file like so:

```
docker run --rm \
    -v /path/to/cover.pdf:/cover/cover.pdf \
    -v /path/to/out/:/cover/out \
    -v /path/to/config.json:/cover/config.json \
    -e cover_type=your_new_preset_name \
    -e OUTPUT_WIDTH=1200 \
    openbookpublishers/cover-trimmer
```