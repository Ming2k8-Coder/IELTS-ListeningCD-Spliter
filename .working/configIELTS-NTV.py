
# config['ffmpeg_path']        = 'ffmpeg', # On Windows, you will probably need this to be \path\to\ffmpeg.exe

config['source_path']        = './.working/';

config['source_frame_start'] = 0;    # (x * sample_rate) / hop_length)
config['source_frame_end']   = None; # (x * sample_rate) / hop_length)

config['matching_samples']   = './.working/event'; # Could also be a path to a single file.
config['matching_min_score'] = 0.15;
config['matching_skip']      = 0;    # Jump forward X seconds after a match.
config['matching_ignore']    = 0;    # Ignore additional matches X seconds after the last one.

config['output_title']       = 'CD1'; # Set a title, which creates the files: "X.meta", "X.results", and "X-chapters.mp3"
config['output_split']       = True; #If True, spiting chapters to individual files, name according output_title
config['debug']              = 0;