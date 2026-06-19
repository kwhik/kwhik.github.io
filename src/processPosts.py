#!/usr/bin/env python
"""\
Process the topics.md file to find citations and hook them to the known sources.

Directly modifies the 'docs/topics.md' file although it creates a backup.  Could change this
to using a '.local' version of those files when working with the script, or to take them in as a parameter.
But given the directory is under 'git' management, wiping the file isn't particularly problematic.

Also regenerates and rewrites the 'docs/_data/citations.yml' file, but that is a derived file and all content
is sourced from the 'topics.md' file.

It expects the file paths to be from the 'home' directory.  Also the 'sources' array is manually synchronized
with the '_sources' directory.

Usage: python src/processTopicCitations.py
"""

import fileinput
import re
import sys
from urllib.parse import urlsplit
import frontmatter
import os
import json

# Current collection of sources: derived from '_sources' directory metadata information
sources = {}

# Filepaths relative to the 'home' directory of the project
# Expecting the script to be called from there.
topics_filepath = "./docs/topics.md"
citation_filepath = "./docs/_data/citations.yml"
sources_filepath = "./docs/_posts"
includes_filepath = "./docs/_includes/posts"


# Identify citation lines by the pattern:
# * [#] … <url>
pattern1 = r"\*\s+\[(\d+)\]([^\<]+)<([^\>]+)>"

# Break apart the '…' if it matches
# … «citation-description» …
pattern1b = r"([^«]*)«([^»]+)»(.*)"

# Identify Topic lines by the pattern:
# ### Topic-Name
pattern2 = r"\#\#\# (.*)"

# Break apart Topic-Name if it matches
# [Topic-Name](link)
pattern2b = r"\[([^\[]*)\]\(([^\)]*)\)"

# Identify Topic lines by the pattern:
# ## Topic-Name
pattern3 = r"\#\# (.*)"

# Break apart Topic-Name if it matches
# [Topic-Name](link)
pattern3b = r"\[([^\[]*)\]\(([^\)]*)\)"


# Sources found for documentation
found_sources = {}


def make_anchor_name(name: str) -> str:
    # 1. Convert to lowercase and strip leading/trailing whitespace
    slug = name.lower().strip()

    # 2. Replace all spaces with hyphens
    slug = slug.replace(' ', '-')

    # 3. Remove any non-alphanumeric characters (excluding hyphens)
    slug = ''.join(c for c in slug if c.isalnum() or c == '-')

    # 4. Remove consecutive hyphens
    while '--' in slug:
        slug = slug.replace('--', '-')

    return slug


extracted_data = []
files = []

file_ext_map = {".md": 1, ".markdown": 1}

for root, _, filenames in os.walk(sources_filepath):
    for filename in filenames:
        # Combine the folder path and file name
        file_name, file_ext = os.path.splitext(filename)
        infile = f"{root}/{filename}"
        outfile = f"{includes_filepath}/{file_name}_toc.txt"
        files.append(infile);
        files.append(outfile);
        if (file_ext not in file_ext_map):
            print("Ignore:", filename, file_ext, file_ext_map, file=sys.stderr)
            continue

        with fileinput.input(files=infile, inplace=True) as infile_file:
            with open(outfile, "w", encoding="utf-8") as outfile_file:
                # Loop over all the lines in the file
                for line in infile_file:
                    # Check for subsection match
                    match2 = re.match(pattern2, line)
                    if match2:
                        subsection3 = match2.group(1)
                        subsection3_url = ""
                        match2b = re.match(pattern2b, subsection3)
                        if match2b:
                            subsection3, subsection3_url = match2b.groups()

                        subsection3_slug = make_anchor_name(subsection3)
                        if not subsection3_url:
                            subsection3_url = "#"+subsection3_slug

                        print(f"### [{subsection3}]({subsection3_url})")
                        print("Found:", subsection3_slug, subsection3_url, file=sys.stderr)
                        print(f"  * [{subsection3}]({subsection3_url})", file=outfile_file)

                        continue

                    match3 = re.match(pattern3, line)
                    if match3:
                        subsection3 = match3.group(1)
                        subsection3_url = ""
                        match2b = re.match(pattern2b, subsection3)
                        if match2b:
                            subsection3, subsection3_url = match2b.groups()

                        subsection3_slug = make_anchor_name(subsection3)
                        if not subsection3_url:
                            subsection3_url = "#"+subsection3_slug

                        print(f"## [{subsection3}]({subsection3_url})")
                        print("Found:", subsection3_slug, subsection3_url, file=sys.stderr)
                        print(f"* [{subsection3}]({subsection3_url})", file=outfile_file)

                        continue


                    print(line, end="")

print(files)

