import click

@click.command()
@click.option('--features', default='audio', help='the kind of features to be extracted from the file')
@click.option('--format', default='csv', help='the format in which the extracted features will be put out (by default, "csv")')
@click.argument('inputfile', type=click.File('rb'), default='-')
@click.argument('outputfile', type=click.File('wb'), default='-', required=False)

#def cli(features, format, inputfile):
def cli(inputfile, outputfile, features, format):
    """This tool takes a video, picture or audio file as an input, extracts a number of features from it, and outputs the features in a structured way (e.g., csv).

    \b
    Analyze audio.wav and print the features extracted to features.csv:
    
		mmfe audio.wav features.csv
    """
    click.echo('Extracting %s features' % features)
    while True:
        chunk = inputfile.read(1024)
        if not chunk:
            break
        outputfile.write(chunk)
        outputfile.flush()

