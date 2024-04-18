"""
File: mkdocs_glossary/plugin.py
Desc: This file contain the plugin used by mkdocs to reference entries of the glossary
Author: Thibaud Briard - BRT, <thibaud.brrd@eduge.ch>
Version: 0.1.2 - 2024-04-18
"""
# Imports...
import os, shutil # used to create folder and file in documentation
import re # used to recognize markdown figure pattern
import logging # used to log warning and errors for MkDocs among other things

from mkdocs.config.base import Config as base_config # used to create an MkDocs config class derived from MkDocs config base
from mkdocs.plugins import BasePlugin as base_plugin # used to create an MkDocs plugin class derived from MkDocs plugin base
from mkdocs.config import config_options as c # used for config schema type safety
from mkdocs.structure.files import File # used to create File in documentation

# The plugin config options
class GlossaryConfig(base_config):
    file = c.Type(str, default='glossary.md')
    exclude = c.ListOfItems(c.Type(str), default=[])
    unknown_warning = c.Type(bool, default=False)

# The plugin itself
class Glossary(base_plugin[GlossaryConfig]):

    def __init__(self):
        self._logger = logging.getLogger('mkdocs.glossary')
        self._logger.setLevel(logging.INFO)

        self.enabled = True
        self.total_time = 0

        self.terms = []
        self.unknowns = []
        self.counter = 1
        self.page = None

    def on_config(self, config):
        self.exclude_list = [item.lower() for item in self.config.exclude]

        self._logger.info(f'The following list of terms will be ignored by the glossary as specified in the exclude option : {self.exclude_list}')

        return config

    def on_files(self, files, config):
        self.page = files.get_file_from_path(self.config.file)

        glossary = os.path.join(config.docs_dir, self.config.file)
        with open(glossary, 'r') as file:
            markdown = file.read()

        # Regular expression pattern to match the glossary terms
        pattern_glossary_entry = r'^[1-9][0-9]*\. \*\*(?![\s])([^*]+)(?<![\s])\*\* : (.+)$'
        # Find all matches of the pattern in the markdown text
        matches = re.findall(pattern_glossary_entry, markdown, flags=re.MULTILINE)
        
        for match in matches:
            variantes = [v.strip().lower() for v in match[0].split(', ')]
            self.terms.append(variantes)

        return files
    
    def on_page_markdown(self, markdown, page, config, files):
        if self.page == page.file:
            pattern_list_num = r'^([1-9][0-9]*\. \*\*(?![\s]))([^*]+)((?<![\s])\*\* : (?:.+))$'
            matches = []
            matches.extend(re.finditer(pattern_list_num, markdown, flags=re.MULTILINE))
            matches = sorted(matches, key=lambda x: x.start())

            position_offset = 0
            for match in matches:
                replacement = f'{match.group(1)}<span id="term-{self.counter}" markdown="span">{match.group(2)}</span>{match.group(3)}'
                self.counter += 1

                markdown = markdown[:match.start() + position_offset] + replacement + markdown[match.end() + position_offset:]
                position_offset += len(replacement) - len(match.group(0))
        else:
            original = markdown
            lines = markdown.split('\n')

            file_directories_count = page.file.src_uri.count('/')
            file_relative_path = '../' * file_directories_count

            try:
                pattern_term = r'((?<!\*)\*|\*{3})(?![\s])([^*]+)(?<![\s])(\*(?!\*)|\*{3})'
                matches = []
                matches.extend(re.finditer(pattern_term, markdown, flags=re.MULTILINE))
                matches = sorted(matches, key=lambda x: x.start())
                position_offset = 0

                for match in matches:
                    # Retrieve term, prefix and suffix
                    prefix =  match.group(1)
                    term = match.group(2)
                    suffix =  match.group(3)
                    # Initialize variables to track line number and relative start/end positions
                    line_num = 0
                    relative_start = match.start()
                    relative_end = match.end()

                    # Iterate through lines to find the line number containing the match
                    for line in lines:
                        line_length = len(line)
                        
                        # Check if the match is within the current line
                        if relative_start < line_length:
                            break  # Found the line containing the match
                        else:
                            # Move to the next line
                            relative_start -= line_length + 1  # Add 1 for the newline character
                            relative_end -= line_length + 1
                            line_num += 1
                    checkpoint = markdown
                    try:
                        replacement = match.group(0)
                        flag = False
                        number = 0
                        for index, sublist in enumerate(self.terms):
                            if term.lower() in sublist:
                                flag = True
                                number = index + 1
                                break
                        if term.lower() in self.exclude_list:
                            self._logger.debug(f'Glossary ignore term "{term}" --> because in exclude list')
                        elif lines[line_num].startswith('#'):
                            self._logger.debug(f'Glossary ignore term "{term}" --> because in markdown header')
                        elif '[' in line[:relative_start] and '](' in line[relative_end:]:
                           self._logger.debug(f'Glossary ignore term "{term}" --> because in markdown link')
                        elif line[:relative_start].count('`') % 2 and line[relative_end:].count('`') % 2:
                           self._logger.debug(f'Glossary ignore term "{term}" --> because in markdown code')
                        elif markdown[:match.start() + position_offset].count('```') % 2 and markdown[match.end() + position_offset:].count('```') % 2:
                           self._logger.debug(f'Glossary ignore term "{term}" --> because in markdown code block')
                        elif flag :
                            replacement = f'{prefix}{term}{suffix}^[{number}]({file_relative_path}{self.config.file}#term-{number})^'
                            markdown = markdown[:match.start() + position_offset] + replacement + markdown[match.end() + position_offset:]
                            position_offset += len(replacement) - len(match.group(0))
                        else:
                            flag = False
                            number = 0
                            for index, item in enumerate(self.unknowns):
                                if term.lower() == item['term']:
                                    flag = True
                                    number = index
                                    break
                            if flag:
                                self.unknowns[index]['count'] += 1
                            else:
                                self.unknowns.append({'term': term.lower(), 'count': 1, 'first_found': page.file.src_uri})
                    except:
                        markdown = checkpoint
            except:
                markdown = original

        return markdown
    
    def on_post_build(self, config):
        total_count = 0
        if self.config.unknown_warning:
            for item in self.unknowns:
                self._logger.warning(f'Glossary ignored {item["count"]} appearance{"" if item["count"] == 1 else "s"} of term "{item["term"]}" --> not in Glossary list (found first appearance at "{item["first_found"]})"')
                total_count += item["count"]
            self._logger.warning(f'Glossary ignored {total_count} eappearance{"" if total_count == 1 else "s"} of {len(self.unknowns)} term{"" if len(self.unknowns) == 1 else "s"} that {"is" if len(self.unknowns) == 1 else "are"} not in glossary list')
        else:
            for item in self.unknowns:
                self._logger.debug(f'Glossary ignored {item["count"]} appearance{"" if item["count"] == 1 else "s"} of term "{item["term"]}" --> not in Glossary list (found first appearance at "{item["first_found"]})"')
                total_count += item["count"]
            self._logger.info(f'Glossary ignored {total_count} eappearance{"" if total_count == 1 else "s"} of {len(self.unknowns)} term{"" if len(self.unknowns) == 1 else "s"} that {"is" if len(self.unknowns) == 1 else "are"} not in glossary list')